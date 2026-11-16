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
- [ ] Title for Re-Born 2 no. 35 (Miki is asking Yoko; Stephen to prompt her)
- [x] Title typos fixed; titles in title case (parenthetical glosses left lower case); British spelling ("Vapour")
- [x] Photo credit for the tapestries: "Photography by: Hideto Ichige" (Miki: no need to ask him)
- [x] Confirmed by Miki: catalogue numbers as captions; the sketch's BIO block left out (about me has it); the page wider than the old 977 px frame
- [x] Yoko approved the shortened introduction (`plans/catalog-introduction.md`)
- [x] Page named Tapestries / タペストリー; new biography moved to about me
- [x] Spelling: British throughout (Miki)

Decided (2026-11-15): the old home page was obsolete and is removed; the Tapestries page is the landing page (`index.html`). The header email address is a mailto link.
Decided (2026-11-15): contact is by `yoko@yokofukada.com`, shown in plain text on every page and as a mailto button on Tapestries; no form, no obfuscation (20 years of exposure have caused no trouble).

Decided (2026-11-15): Miki's full-resolution originals (`src/art/`) go in the public repo.

## Stage 3: Deploy to `lambent.net`

Decided: no CI/CD and no GitHub Actions. A publish script in this repo rebuilds the site and copies it to the droplet with `rsync`. Drafts are staged under `/var/www/lambenttechnology.com/wireframes/` on the droplet (`wireframes/yokofukada/`). No password protection. Stephen has SSH access and runs the script.

- [x] Generator writes relative links only, so the same build works under `wireframes/yokofukada/` and at the domain root
- [x] Publish script `lib/publish` (dry run by default; `--go` to publish; logs in as `stephen@lambent.net`; `staging` or `production`; a production publish tags the commit `published-YYYY-MM-DD`)
- [x] First publish to staging (2026-11-15): https://lambenttechnology.com/wireframes/yokofukada/
Decided (2026-11-16): production is on the droplet at `/var/www/yokofukada.com`, not on Fasthosts (its SSL certificate costs £37.45 a year; Let's Encrypt is free). Email stays at Fasthosts. Step by step: `plans/launch.md`.

- [x] Production path `/var/www/yokofukada.com`; `lib/publish production` targets it
- [x] 2026-11-16: staging published (`a25ad43`): works grid, Salad Garden, new menu order
- [x] A-record TTLs: Fasthosts fixes them at 3600 s and has no setting for them; nothing to do
- [x] 2026-11-16: site folder and Nginx conf on the droplet; first production publish (`1372166`, tag `published-2026-11-16`, pushed); tested with `curl --resolve`
- [x] 2026-11-16: HTTPS with `certbot --nginx` (certificate for apex and `www`, to 2027-02-14; renewal `installer = nginx`); HTTP → HTTPS; `www` → apex

## Stage 4: Revise with Yoko

- [ ] Loop on style and content until Yoko is satisfied
- [x] 2026-11-16, Yoko: jewellery before works in the navigation; former home-page image added to works as "Salad Garden with Pointy Hats" (とんがり帽子のサラダガーデン); works page now a thumbnail grid (the collage could not take a ninth work)
- [x] 2026-11-16: works page reworked: one page, full-width grid, pop-ups; staging `5b532db`

Decided (2026-11-16): the works are one page, a grid of thumbnails (3, 2, then 1 column as the window narrows) opening pop-ups; no page per work. Camden is one tile, its pop-up showing both pictures. Miki's credit is in the pop-ups of works 1–4. Works and jewellery pop-ups close on any click or Esc; arrow keys step. CSS and JS URLs carry a content hash (`?v=…`) so browsers never mix old and new files.

- [ ] Open questions sent to Miki (`Yoko site/for Miki/open-questions-2026.11.16.md`): no. 35 title; Salad Garden's Japanese title (とんがり帽子のサラダガーデン, or the old サラダ帽), capitals in works titles, position in the grid, photo credit (the old home page had none)

## Stage 5: DNS

- [x] 2026-11-16: redirect `jewellery.php` and `jw.php` to the new jewellery page, `works01.html`–`works08.html` to `works.html`, `ifproject/` to the home page (in the Nginx conf, `plans/launch.md`; all other page names are kept)
- [x] 2026-11-16: `yokofukada.com` and `www.yokofukada.com` A records point at the droplet (134.122.97.96). **Live.**
- [ ] Watch the Nginx 404 log for a couple of weeks for old addresses we missed (`plans/launch.md` step 13)
- [ ] Optional: set the `webmail` A record to 213.171.216.231, Fasthosts' current default, to restore its automatic updates (both addresses serve the same webmail login)
- [ ] Never use Fasthosts' *Restore Default DNS Records*: it would point the site back at Fasthosts
- [x] Keep the MX, `mail` and `webmail` records at Fasthosts: Yoko keeps `yoko@yokofukada.com` (decided 2026-11-16)

## Collaboration

Decided (2026-11-15): the working copy moved from the `mackenzie-shared` share to `~/Projects/webhands` (the share kept losing access to folders); Miki supplies material through the Dropbox folder `Yoko site/`.

- [x] Shared the Dropbox folder `Yoko site` with Miki; she is using it
- [x] Questions for Miki (`Yoko site/for Miki/`): answered 2026-11-15 and 2026-11-16 and folded in. No. 18 "square fawn spot check designs" stays as it is; credit reads "mikiy.com" (apex domain)
- [ ] Later: let Miki replace images and edit Markdown pages herself (e.g. GitHub's web editor on a branch, or a sync from her Dropbox folder)
- [ ] Put the `webhands/` planning files (`plans/`, `progress/`, `CLAUDE.md`) under version control too?
- [ ] Once the local copy has been in use for a while, archive or delete the copy on the share

## Open questions

- [x] Typos in `plans/inventory.md` fixed (Miki approved; "Yamanouchi", "Camden Recycling Centre (London)")
Decided (2026-11-15): the copyright line reads "© Yoko Fukada 2006–{year}", the year being when the site is built.

- [x] Extra pages: none for now (2026-11-16)
- [ ] Higher-resolution originals: Miki may have some in her archive; searching will take time. Use the recovered images meanwhile (2026-11-16)
- [x] `yoko@yokofukada.com` stays in use, and with it the Fasthosts hosting package (decided 2026-11-16)
