# TODO

Agenda for yokofukada.com. See `README.md` for the goal and stages.

## Stage 1: Recover content from the current site

- [x] Download the current site over FTP into `prev/ftp/` (branch `recover-prev`)
- [x] Compare it with the live site (HTTP only; no HTTPS): the live site is a subset of the FTP copy and identical to it
- [x] Commit `prev/ftp/private/webcd/` (an older version of the site)
- [x] List the pages, navigation, bilingual pattern and images: see `plans/inventory.md`
- [x] Merge `recover-prev`
- [x] 2026-11-15: deleted `phpinfo.php` and `jw.php` from Fasthosts; patched the live `jewellery.php` so its popups open the image directly. `prev/ftp/htdocs/` is the snapshot from before these changes.

Decided: the IF project is over; `ifproject/` is archived in `prev/` and not rebuilt.

## Stage 2: Regenerate the site

- [ ] Convert Shift_JIS and ISO-8859-1 text to UTF-8
- [x] Python generator in `lib/` (branch `generator`), run in a virtual environment (add `.venv/` to `.gitignore`)
- [ ] Source format: Markdown or similar, holding English and Japanese side by side in one page (the site is bilingual within each page, not two monolingual versions)
- [x] Keep the existing minimalist look; make the layout responsive, the navigation consistent and the images larger
- [x] `html/` (generated) is git-ignored; deploy from a fresh build

## New page: Re-Born obi tapestries

Decided: Miki's sketch (`plans/Yoko Fukada.png`, made in Canva, approved by Yoko) is one new page added to the existing site and reached from its navigation (option b). English only. Typography is negotiable. On phones, sections stack in one column with tapestries in a two-column grid.

- [x] Photographs and titles from Miki (in `src/art/`, titles from file names)
- [ ] Title for Re-Born 2 no. 35; check title typos ("incence", "fawn spot check", spacing around brackets and commas)
- [ ] Photo credit for the tapestries (the catalogue credits Hideto Ichige)
- [ ] Confirm: catalogue numbers as captions; the sketch's BIO block left out (about me has it); the page wider than the old 977 px frame
- [ ] Get Miki's and Yoko's approval of the shortened introduction (`plans/catalog-introduction.md`)
- [x] Page named Tapestries / タペストリー; new biography moved to about me
- [ ] Spelling: British throughout? ("jewelry" in the new biography vs "jewellery" elsewhere); home page still says "temporarily based in Sydney"
Decided (2026-11-15): contact is by `yoko@yokofukada.com`, shown in plain text on every page and as a mailto button on Tapestries; no form, no obfuscation (20 years of exposure have caused no trouble).

Decided (2026-11-15): Miki's full-resolution originals (`src/art/`) go in the public repo.

## Stage 3: Deploy to `lambent.net`

Decided: no CI/CD and no GitHub Actions. A publish script in this repo rebuilds the site and copies it to the droplet with `rsync`. Drafts are staged under `/var/www/lambenttechnology.com/wireframes/` on the droplet (`wireframes/yokofukada/`). No password protection. Stephen has SSH access and runs the script.

- [x] Generator writes relative links only, so the same build works under `wireframes/yokofukada/` and at the domain root
- [x] Publish script `lib/publish` (dry run by default; `--go` to publish; logs in as `stephen@lambent.net`; staging only so far)
- [x] First publish to staging (2026-11-15): https://lambenttechnology.com/wireframes/yokofukada/
- [ ] Confirm the production path for `yokofukada.com`
- [ ] Production site configuration and HTTPS for `yokofukada.com` (Jack, once)

## Stage 4: Revise with Yoko

- [ ] Loop on style and content until Yoko is satisfied

## Stage 5: DNS

- [ ] Redirect `jewellery.php` to the new jewellery page (all other page names are kept)
- [ ] Point the `yokofukada.com` and `www.yokofukada.com` A records at the droplet
- [ ] Keep the MX records at Fasthosts while `yoko@yokofukada.com` may be in use

## Collaboration

Decided (2026-11-15): the working copy moved from the `mackenzie-shared` share to `~/Projects/webhands` (the share kept losing access to folders); Miki supplies material through the Dropbox folder `Yoko site/`.

- [ ] Share the Dropbox folder `Yoko site` with Miki (Stephen, in Dropbox)
- [ ] Tell Miki about the new arrangement
- [ ] Questions for Miki are in `Yoko site/for Miki/Questions for Miki 2026-11-15.md` (Tapestries titles, credit, introduction, spelling, typos, copyright line); fold her answers into the items above
- [ ] Later: let Miki replace images and edit Markdown pages herself (e.g. GitHub's web editor on a branch, or a sync from her Dropbox folder)
- [ ] Put the `webhands/` planning files (`plans/`, `progress/`, `CLAUDE.md`) under version control too?
- [ ] Once the local copy has been in use for a while, archive or delete the copy on the share

## Open questions

- [ ] Content fixes awaiting approval: typos (see `plans/inventory.md`), the "© yoko fukada -2008" line

- [ ] Which extra pages does Yoko want, and with what content? (Not yet known.)
- [ ] Do higher-resolution originals of the images exist? If not, use what we recover from the old site.
- [ ] `yoko@yokofukada.com` stays in use (decided 2026-11-15). Is the mailbox part of the Fasthosts hosting package? If so, the package stays, or the mailbox moves elsewhere before it is cancelled.
