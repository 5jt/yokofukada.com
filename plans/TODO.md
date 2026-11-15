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
- [ ] Decide whether `html/` (generated) is committed or git-ignored

## Stage 3: Deploy to `lambent.net`

- [ ] Publish a staging URL on `lambent.net` for Yoko to review before the DNS switch (show, don't tell)
- [ ] HTTPS (Jack runs server commands on `lambent-static`)

## Stage 4: Revise with Yoko

- [ ] Loop on style and content until Yoko is satisfied

## Stage 5: DNS

- [ ] Point the `yokofukada.com` and `www.yokofukada.com` A records at the droplet
- [ ] Keep the MX records at Fasthosts while `yoko@yokofukada.com` may be in use

## Open questions

- [ ] Which extra pages does Yoko want, and with what content? (Not yet known.)
- [ ] Do higher-resolution originals of the images exist? If not, use what we recover from the old site.
- [ ] Does Yoko use `yoko@yokofukada.com`? This decides whether the Fasthosts hosting package can be removed.
