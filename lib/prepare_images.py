"""Make web-sized copies of original images.

Usage: .venv/bin/python lib/prepare_images.py

Reads src/tapestries.yaml. For every cover and piece with an `art:` path
(relative to src/art/), writes the web copy named by `file:` (or each
entry of `files:`/`art:` lists) into src/img/: converted to sRGB, fitted
within 1600 × 1600 px, saved as progressive JPEG without metadata.
Copies newer than their original are left alone.
"""

import io
from pathlib import Path

import yaml
from PIL import Image, ImageCms

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "src" / "art"
IMG = ROOT / "src" / "img"
BOX = (1600, 1600)
SRGB = ImageCms.createProfile("sRGB")


def prepare(art, file):
    src, dest = ART / art, IMG / file
    if dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
        return
    with Image.open(src) as im:
        icc = im.info.get("icc_profile")
        if icc:
            im = ImageCms.profileToProfile(
                im, ImageCms.ImageCmsProfile(io.BytesIO(icc)), SRGB,
                outputMode="RGB")
        im = im.convert("RGB")
        im.thumbnail(BOX, Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"  {file}  {im.width}×{im.height}  from {art}")


def pairs(entry):
    arts, files = entry.get("art"), entry.get("file")
    if arts is None:
        return []
    if isinstance(arts, str):
        return [(arts, files)]
    return list(zip(arts, files))


def main():
    spec = yaml.safe_load((ROOT / "src" / "tapestries.yaml").read_text(encoding="utf-8"))
    entries = list(spec["covers"])
    for s in spec["sections"]:
        entries += s["pieces"]
    for e in entries:
        for art, file in pairs(e):
            prepare(art, file)


if __name__ == "__main__":
    main()
