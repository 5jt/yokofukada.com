# Inventory of the current site

Recovered over FTP into `prev/ftp/` on 2026-11-15 (branch `recover-prev`). Paths below are relative to `prev/ftp/htdocs/`.

## Pages

| Page | Content |
|---|---|
| `index.html` | Home: one photograph (`image_top.jpg`, 450×300) with a caption, and a paragraph of English biography |
| `works.html` | Collage of eight thumbnails (`works_big.jpg`, 444×492) used as an image map linking to the eight works pages |
| `works01.html`–`works08.html` | One work each (`works07` has two images): photograph, English title, Japanese title, photographer credit (Miki Yamanouchi, on 01–04 only). A smaller copy of the collage (`works_small.jpg`) serves as the navigation |
| `jewellery.php` | Grid of 12 thumbnails (`Untitled-1.jpg`–`Untitled-12.jpg`, up to 600 px) opening `jw.php?pic=N` in a popup window. Photographer credit: Sadanori Nomura. Uses a different page template (`templates/*.inc`) and a different navigation from the other pages |
| `aboutme.html` | English CV paragraph |

## Navigation

A left-hand column on every page except the jewellery page: the logo `yf2.gif` ("Yoko Fukada", as an image), then five links drawn from the sprite `nav.gif`, each with the English label over a small katakana label (home ホーム, works アート作品, jewellery ジュエリー, about me プロフィール, if project イフプロジェクト), black, and green when current or on hover. Below them, the email address as an image (`address.gif`) and "© yoko fukada -2008".

The jewellery page replaces this with a vertical logogram (`yf.gif`) and a single "« Home" link.

## Bilingual pattern

English is primary. Japanese appears in two places only: work titles, as a smaller second line under the English title (e.g. "from the gap" / ほころび), and the katakana labels in the navigation (which are part of the images). The biography and CV are in English only. So the source format needs an optional Japanese title for each work and image, not parallel texts.

## Look

White page, a background stripe image (`back.gif`), fixed 977 px layout positioned absolutely, Gill Sans for English, Hiragino or MS P Gothic for Japanese, small type, lots of white space.

## Images

The typical longest side is about 340 px; the largest artwork image is 450 px on the main pages and 600 px for the jewellery. Larger originals are needed for a responsive site.

## Archived (not to be rebuilt)

- `ifproject/`: the IF project, now over. Mostly reachable only through Flash menus, so it has been invisible since 2020.
- `prev/ftp/private/webcd/`: an older version of the site (sculpture, Jerwood, jewellery pages).

## Problems on the live server

- `phpinfo.php` is publicly reachable and shows the server configuration.
- `jw.php` echoes the `pic` query parameter into the page without escaping it (a cross-site scripting hole).
- `ifproject/images/living_s.jpg` is missing (broken image).
- Typos: "Yamanouch" (for Yamanouchi), "Collage" (for College), "Royal british Sculpture Association", "Cener", `target="_balnk"`.
