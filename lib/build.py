"""Build the yokofukada.com site from src/ into html/.

Usage: .venv/bin/python lib/build.py

Every link the generator writes is relative, so the same build works at
the domain root and in a staging subfolder.
"""

from datetime import date
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "html"
TEMPLATES = Path(__file__).resolve().parent / "templates"


def load_yaml(name):
    return yaml.safe_load((SRC / name).read_text(encoding="utf-8"))


def md(text):
    return markdown.markdown(text, extensions=["nl2br", "md_in_html"])


def read_page(path):
    """Split a Markdown file into front matter (dict) and body (HTML)."""
    text = path.read_text(encoding="utf-8")
    meta = {}
    if text.startswith("---\n"):
        head, text = text[4:].split("\n---\n", 1)
        meta = yaml.safe_load(head) or {}
    return meta, md(text)


_sizes = {}


def size(file):
    """Pixel size (width, height) of an image in src/img/."""
    if file not in _sizes:
        with Image.open(SRC / "img" / file) as im:
            _sizes[file] = im.size
    return _sizes[file]


def image(spec):
    """Add width and height to an image spec: {file, en, ja?}."""
    spec = dict(spec)
    if spec.get("file"):
        spec["width"], spec["height"] = size(spec["file"])
    return spec


def works_grid(works):
    """One entry per work for the thumbnail grid: its page and first image."""
    return [{"page": w["page"], "title": w["title"], "image": image(w["images"][0])}
            for w in works["works"]]


def build(out):
    site = load_yaml("site.yaml")
    site["copyright"] = site["copyright"].format(year=date.today().year)
    works = load_yaml("works.yaml")
    jewellery = load_yaml("jewellery.yaml")
    tapestries = load_yaml("tapestries.yaml")

    env = Environment(loader=FileSystemLoader(TEMPLATES),
                      undefined=StrictUndefined, autoescape=True,
                      trim_blocks=True, lstrip_blocks=True)

    written = set()

    def write(path, data):
        """Write bytes to out/path, only if they differ from what's there."""
        target = out / path
        written.add(target)
        if target.exists() and target.read_bytes() == data:
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    for src_dir, dest in (("css", "css"), ("js", "js"), ("img", "images")):
        for f in sorted((SRC / src_dir).iterdir()):
            if f.is_file() and not f.name.startswith("."):
                write(Path(dest) / f.name, f.read_bytes())

    def render(template, page, section, **context):
        html = env.get_template(template).render(
            site=site, current=page, section=section, **context)
        write(f"{page}.html", html.encode("utf-8"))
        print(f"  {page}.html")

    # Markdown pages
    for path in sorted((SRC / "pages").glob("*.md")):
        meta, body = read_page(path)
        if meta.get("image"):
            meta["image"] = image(meta["image"])
        render("page.html", path.stem, path.stem, title=meta["title"], meta=meta, body=body)

    # Works
    grid = works_grid(works)
    render("works.html", "works", "works", title="works", grid=grid)
    for w in works["works"]:
        w = dict(w, images=[image(i) for i in w["images"]])
        render("work.html", w["page"], "work", title="works",
               work=w, grid=grid)

    # Jewellery
    render("jewellery.html", "jewellery", "jewellery",
           title=jewellery["title"], gallery=jewellery,
           images=[image({"file": f}) for f in jewellery["images"]])

    # Tapestries. A piece's `file` may be one image or a list (strips of
    # one piece); either way the template gets a list of images.
    def strips(p):
        files = p.get("file")
        if not files:
            return []
        if isinstance(files, str):
            files = [files]
        return [image({"file": f}) for f in files]

    sections = []
    for s in tapestries["sections"]:
        s = dict(s)
        if s.get("text"):
            s["text"] = md((SRC / "text" / s["text"]).read_text(encoding="utf-8"))
        s["pieces"] = [dict(p, images=strips(p)) for p in s["pieces"]]
        sections.append(s)
    # The landing page, so it is index.html; `section` keeps its styling.
    render("tapestries.html", "index", "tapestries",
           title=tapestries["title"], spec=tapestries,
           covers=[image(c) for c in tapestries["covers"]],
           sections=sections)

    # Remove files left over from earlier builds. Directories are never
    # removed: on the network share a removed directory can linger,
    # unreadable, until every handle on it is closed.
    for f in out.rglob("*"):
        if (f.is_file() and f not in written and not f.name.startswith(".")
                and f.name != "version.txt"):   # written by lib/publish
            f.unlink()
            print(f"  removed {f.relative_to(out)}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Build the site.")
    parser.add_argument("--out", type=Path, default=OUT,
                        help="output directory (default: html/)")
    out = parser.parse_args().out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    build(out)
    print(f"Built {out}")
