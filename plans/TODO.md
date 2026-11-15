# TODO

Agenda for yokofukada.com. See `README.md` for the goal and stages.

## Stage 1: Recover content from the current site

- [x] Download the current site over FTP into `prev/ftp/` (branch `recover-prev`)
- [x] Compare it with the live site (HTTP only; no HTTPS): the live site is a subset of the FTP copy and identical to it
- [x] Commit `prev/ftp/private/webcd/` (an older version of the site)
- [x] List the pages, navigation, bilingual pattern and images: see `plans/inventory.md`
- [ ] Merge `recover-prev`
- [ ] Remove `phpinfo.php` and `jw.php` from Fasthosts now (security holes)

Decided: the IF project is over; `ifproject/` is archived in `prev/` and not rebuilt.

## Stage 2: Regenerate the site

- [ ] Convert Shift_JIS and ISO-8859-1 text to UTF-8
- [ ] Python generator in `lib/`, run in a virtual environment (add `.venv/` to `.gitignore`)
- [ ] Source format: Markdown or similar, holding English and Japanese side by side in one page (the site is bilingual within each page, not two monolingual versions)
- [ ] Keep the existing minimalist look; make the layout responsive, the navigation consistent and the images larger
- [x] `html/` (generated) is git-ignored; deploy from a fresh build

## Stage 3: Deploy to `lambent.net`

Decided: no CI/CD and no GitHub Actions. A publish script in this repo rebuilds the site and copies it to the droplet with `rsync`. Drafts are staged under `/var/www/lambenttechnology.com/wireframes/` on the droplet (proposed: `wireframes/yokofukada/`). No password protection. Stephen has SSH access and runs the script.

- [ ] Generator writes relative links only, so the same build works under `wireframe/` and at the domain root
- [ ] Publish script in `lib/`: build, then `rsync` to either staging (`wireframe`) or production
- [ ] Confirm the production path for `yokofukada.com`
- [ ] Production site configuration and HTTPS for `yokofukada.com` (Jack, once)

## Stage 4: Revise with Yoko

- [ ] Loop on style and content until Yoko is satisfied

## Stage 5: DNS

- [ ] Point the `yokofukada.com` and `www.yokofukada.com` A records at the droplet
- [ ] Keep the MX records at Fasthosts while `yoko@yokofukada.com` may be in use

## Open questions

- [ ] Which extra pages does Yoko want, and with what content? (Not yet known.)
- [ ] Do higher-resolution originals of the images exist? If not, use what we recover from the old site.
- [ ] Does Yoko use `yoko@yokofukada.com`? This decides whether the Fasthosts hosting package can be removed.
