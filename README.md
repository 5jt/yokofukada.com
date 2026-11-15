yokofukada.com
==============

This is the personal website of Yoko Fukada, an artist in Japan.

The site was originally built two decades ago using a tool like FrontPage, then adapted by a Japanese web designer with whom we have no contact.

The website is badly out of date, with inconsistent navigation controls and no adaptation to mobile devices. Its images are too small to adapt to the current range of display devices.

The domain is registered in our Fasthosts account and also currently hosted there: see `Fasthosts Control Panel.pdf`.



Goal
----
Our brief is to add one or a few extra pages to the website.

Our client is not 'literate' with websites. We have little confidence in settling questions verbally: neither in speech nor in writing. Show rather than tell.

Yoko has declined offers to redesign the existing pages. She values its minimalist aesthetic.


Plan
----

The original plan for `../../sites` was to use the same platform for all three sites. The requirements for this site are much simpler than for `fionacunninghamreid.com` and `mikiy.com`. It makes no sense to encumber the project with a large framework; even `hugo` might be eschewed for custom code to generate the HTML.

Stages:

1.  Recover content from the current site
2.  Regenerate the site as static, responsive HTML5 and CSS from human-editable source such as Markdown. A generator such as `hugo` could be used; alternatively, the site is so simple that a custom generator could be written.
3.  Post to the DigitalOcean droplet we use to host static sites: the host known to this machine as `lambent.net`. Switch HTTP requests to HTTPS.
4.  Loop on style and content until Yoko is satisfied.
5.  Repoint `*yokofukada.com` requests to the `lambent.net` IP.

We foresee each year a few requests to add new content.

If Yoko does not use her `yoko@yokofukada.com` email address, the Fasthosts hosting package can be removed and only the DNS registration left there.


Project structure
-----------------

	html/			generated site content
	lib/			code for generating `html`
	plans/			planning documents
	plans/TODO.md 	agenda
	prev/			previous site content
	progress/		records of progress
	reviews/		reviews and responses
	src/
		art/		original images
		css/		style sheet/s
		img/		images ready for use


Building and publishing
-----------------------

One-time setup (Python version in `.python-version`; dependencies pinned in `requirements.txt`):

	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

Content lives in `src/`: `site.yaml` (navigation), `works.yaml`, `jewellery.yaml`, `tapestries.yaml`, Markdown pages in `src/pages/` and longer texts in `src/text/`. Images go in `src/img/`.

	.venv/bin/python lib/prepare_images.py  # make web copies of new originals in src/art/
	.venv/bin/python lib/build.py        # build into html/
	lib/publish                          # build, then show what rsync would change
	lib/publish --go                     # build and publish to staging (needs a clean working tree)
	lib/shot URL out.png [WIDTH HEIGHT]  # screenshot a page with headless Firefox

Staging: https://lambenttechnology.com/wireframes/yokofukada/


Reviews and responses
---------------------

All reviews and responses are appended to the current day's review file, named `reviews/{YYYY-MM-DD}.md`.

Each review begins with an H1 followed by a timestamp, e.g.:

	# Review: {topic}

	10:34

When asked to respond to a review, begin your response with an H2 and a timestamp, e.g.

	## Response to review of {topic}

	10:37

Before writing a review or a response, always check any existing section timestamps are in chronological order. Complain loudly and abort if that is not so.

**Always** append your review or response to the tail of the current review file; **never** insert it anywhere else.

**Always** read dates and times from the system clock; **never** estimate them.


End of day
----------
When I tell you to wrap up, record the current state ready to resume the conversation in an empty context.

-   Propose committing any uncommitted work in the worktree
-   Update `plans/TODO.md`
-   Append to `progress/{YYYY-MM-DD}.md` a summary of what was decided or achieved in the session.
-   Commit changes to planning documents


Commits
-------
I (Stephen) am the sole developer in this project.

Commits to planning documents only **may** be made to the `main` branch.

Changes to any other documents must be made in a branch for merging into `main`.