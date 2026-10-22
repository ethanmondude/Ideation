# Startup theses site

A static website with one page per startup thesis from idea bot, each with Project Bot's review. It's ready for GitHub Pages (serve the `docs/` folder) but isn't published yet.

## Rebuild

```bash
pip install --user markdown   # once (add --break-system-packages if pip refuses)
python3 /workspace/project-bot/site/build.py
```

Re-run it after every new thesis, review or test. It wipes and regenerates `docs/` each time, so the output always matches the sources and running it twice gives identical files.

## What it reads (read-only)

| Source | Used for |
|---|---|
| `/workspace/idea-bot/theses/YYYY-MM-DD-HHMM-<slug>.md` | One page per thesis. The date and time come from the file name (AWST). The `## Executive summary` section goes at the top of the page |
| `/workspace/shared-data/idea-bot/theses.jsonl` | One-line summary and status for the index (falls back to the thesis subtitle) |
| `/workspace/project-bot/reviews/*.md` | The "Project Bot review" section: Verdict, Scores (score breakdown), Competitor check and Build plan. The rest goes in a collapsible block. The score comes from `Score: X/10` |
| `/workspace/project-bot/reviews/index.md` | Short verdict for the index |
| `/workspace/shared-data/project-bot/reviews.jsonl` | Fallback thesis link and score |
| `/workspace/project-bot/tests/*.md` | Test pages, linked from the matching thesis |

**Matching:** a review or test is matched to a thesis by the thesis path in its italic byline (`/workspace/idea-bot/theses/<file>.md`). If there's no path, it's matched by slug, using the latest thesis with that name dated before the review. A thesis without a review shows "Review pending". The build prints any review or test it couldn't match.

## Output (`docs/`)

- `index.html`: every thesis, newest first, with its date (AWST), one-line summary, score and verdict. Buttons sort the list by newest or by highest score.
- `theses/<slug>.html`: one page per thesis. If two theses share a name, the date is added to the slug.
- `tests/<name>.html`: rendered test results.
- `sources/`: copies of the source Markdown, so the "Sources" links work once the site is online.
- `style.css` (one file, no external CDNs) and `.nojekyll`.

## Publishing later

Push this `site/` folder to a GitHub repo and set Pages to deploy from the `main` branch, `/docs` folder. Everything in `docs/` becomes public, including the copied source files, so check them first.


Published: https://github.com/ethanmondude/Ideation (main, /docs) -> https://ethanmondude.github.io/Ideation/
