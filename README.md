# WiNet — Wireless Networking Research Group

Source for **https://scespedesu.github.io/winet/**, the site for the WiNet Research Group led by Prof. Sandra Céspedes, Concordia University.

The site is a [Jekyll](https://jekyllrb.com/) site using the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, pulled in automatically via `remote_theme` — GitHub Pages builds and publishes it on every push to `main`. You do **not** need to install anything to edit content; everything below can be done by editing plain text files in the GitHub web UI if you prefer.

The site's previous life at Universidad de Chile (2014–2022) is preserved, unchanged, in [`legacy-uchile/`](legacy-uchile/index.html) and linked from the new site's navigation and footer.

## One-time setup after you push this

1. In the repo's **Settings → Pages**, set "Source" to **Deploy from a branch**, branch `main`, folder `/ (root)`.
2. Wait a minute or two for the first build, then visit `https://scespedesu.github.io/winet/`.
3. Optional but recommended: enable the "Enforce HTTPS" checkbox on the same Settings → Pages screen (usually on by default).

## Adding a publication

Each publication is one file in [`_publications/`](_publications/). Copy an existing one and edit the front matter:

```yaml
---
title: "Full paper title"
authors: "S. Céspedes, A. Coauthor, B. Coauthor"
venue: "Name of journal or conference"
year: 2026
type: journal   # journal | conference | preprint | chapter | standard
verified: true  # set to true once you've checked the author list — removes the [verify] flag
links:
  doi: "https://doi.org/..."
  pdf: "https://..."
---
```

The filename doesn't matter (it just needs to be unique and end in `.md`) — the publications page sorts everything automatically by year.

**Note:** the ~60 publications currently in `_publications/` were auto-drafted from ResearchGate as a starting point. Titles/venues/years should be right, but author order was not verified — please check each one and set `verified: true` as you go (see `scripts/generate_publications.py` for how they were generated, purely for reference — you won't need to run it again for single additions).

## Adding a news item

Add a file to [`_news/`](_news/) named `YYYY-MM-DD-short-title.md`:

```yaml
---
title: "Short headline"
date: 2026-09-10
---
Optional longer description.
```

Delete the `TEMPLATE-*` files in `_news/` once you've added real content, or just leave them as a reference — they won't look out of place, but they're clearly marked.

## Adding a person

Add a file to [`_people/`](_people/):

```yaml
---
name: "Full Name"
role: "PhD Student"          # or MASc Student, Postdoc, Undergraduate Researcher, etc.
status: current              # current | alumni
thesis: "Working thesis title"   # optional
now: "Current position"          # optional, alumni only
---
```

Delete the `TEMPLATE-*.md` placeholder files once real people are added.

## Editing other pages

General pages (Home, Research, Join Us) are plain Markdown in [`_pages/`](_pages/) and [`index.md`](index.md) — edit them directly.

## Local preview (optional)

```bash
bundle install
bundle exec jekyll serve
```
then open http://localhost:4000/winet/

## Structure

```
_config.yml       site settings, theme, navigation collections
_data/navigation.yml   top navigation menu
index.md          home page
_pages/            Research, Publications, People, News, Join Us
_publications/     one file per paper (collection)
_news/             one file per news item (collection)
_people/           one file per person (collection)
assets/            images, logo, custom CSS tweaks
legacy-uchile/     archived 2014–2022 Universidad de Chile site, untouched
```
