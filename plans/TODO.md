# TODO

Agenda for yokofukada.com. See `README.md` for the goal and stages.

## Stage 1: Recover content from the current site

- [ ] Download the current site over FTP (credentials in `secrets/ftp-credentials.json`, git-ignored) into `prev/`
- [ ] Also mirror the live site (`wget --mirror`) to check for differences between what is on the server and what is served
- [ ] Find the character encodings (probably Shift_JIS for some or all pages) and convert to UTF-8
- [ ] List the pages, the navigation structure and the images, with the size of each image

## Stage 2: Regenerate the site

- [ ] Python generator in `lib/`, run in a virtual environment (add `.venv/` to `.gitignore`)
- [ ] Source format: Markdown or similar, holding English and Japanese side by side in one page (the site is bilingual within each page, not two monolingual versions)
- [ ] Keep the existing minimalist look; make the layout responsive, the navigation consistent and the images larger
- [x] `html/` (generated) is git-ignored; deploy from a fresh build

## Stage 3: Deploy to `lambent.net`

Decided: no CI/CD and no GitHub Actions. A publish script in this repo rebuilds the site and copies it to the droplet with `rsync`. Drafts are staged in the `wireframe` folder of `lambenttechnology.com` on the droplet.

- [ ] Generator writes relative links only, so the same build works under `wireframe/` and at the domain root
- [ ] Publish script in `lib/`: build, then `rsync` to either staging (`wireframe`) or production
- [ ] Confirm the server paths and the SSH user the script will use (Stephen runs it; Claude can't reach the server)
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
