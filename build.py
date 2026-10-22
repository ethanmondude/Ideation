#!/usr/bin/env python3
"""Build the Startup Theses static site (GitHub Pages "docs" folder).

Reads (never writes) idea bot's theses, Project Bot's reviews and tests, and
the shared JSONL feeds, then regenerates everything under ./docs/.
Safe to re-run: output is wiped and rebuilt deterministically each time.
"""
import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("The 'markdown' package is needed: pip install --user markdown")

HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"
WS = Path("/workspace")
THESES_DIR = WS / "idea-bot" / "theses"
REVIEWS_DIR = WS / "project-bot" / "reviews"
TESTS_DIR = WS / "project-bot" / "tests"
THESES_JSONL = WS / "shared-data" / "idea-bot" / "theses.jsonl"
REVIEWS_JSONL = WS / "shared-data" / "project-bot" / "reviews.jsonl"
REVIEW_INDEX = REVIEWS_DIR / "index.md"

FNAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})-(.+)\.md$")
SITE_TITLE = "Startup theses"


# ---------- helpers ----------
def esc(s):
    return html.escape(s or "", quote=True)


LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")


def fix_lists(text):
    """Python-Markdown needs a blank line before a list; GitHub-style sources often omit it."""
    out, prev = [], ""
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
        if (not in_code and LIST_RE.match(line) and prev.strip()
                and not LIST_RE.match(prev) and not prev.startswith((" ", "\t"))):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def md(text):
    text = fix_lists(text)
    return markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])


def md_inline(text):
    out = md(text).strip()
    if out.startswith("<p>") and out.endswith("</p>") and out.count("<p>") == 1:
        out = out[3:-4]
    return out


def awst(d):
    hour = d.strftime("%I").lstrip("0")
    return f"{d.day} {d.strftime('%b %Y')}, {hour}:{d.strftime('%M')}{d.strftime('%p').lower()} AWST"


def parse_fname(p):
    m = FNAME_RE.match(p.name)
    if not m:
        return None, None
    y, mo, d, h, mi, slug = m.groups()
    return dt.datetime(int(y), int(mo), int(d), int(h), int(mi)), slug


def split_sections(text):
    """Return (h1, preamble, [(heading, body), ...]) for '## ' sections."""
    lines = text.splitlines()
    h1, pre, sections, cur = "", [], [], None
    for line in lines:
        if line.startswith("# ") and not h1:
            h1 = line[2:].strip()
        elif line.startswith("## "):
            cur = [line[3:].strip(), []]
            sections.append(cur)
        elif cur is None:
            pre.append(line)
        else:
            cur[1].append(line)
    return h1, "\n".join(pre).strip(), [(h, "\n".join(b).strip()) for h, b in sections]


def find_section(sections, *keys):
    for h, b in sections:
        hl = h.lower()
        if any(k in hl for k in keys):
            return h, b
    return None, None


def read_jsonl(path):
    out = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out


def score_class(score):
    if score is None:
        return "pending"
    if score >= 7:
        return "high"
    if score >= 5:
        return "mid"
    return "low"


def badge(score):
    if score is None:
        return '<span class="badge pending">Review pending</span>'
    return f'<span class="badge {score_class(score)}">{score:g}/10</span>'


# ---------- load sources ----------
def load_theses():
    meta = {}
    for rec in read_jsonl(THESES_JSONL):
        f = (rec.get("extra") or {}).get("file")
        if f:
            meta[Path(f).name] = rec
    theses = []
    for p in sorted(THESES_DIR.glob("*.md")):
        when, slug = parse_fname(p)
        if not when:
            print(f"skip (unexpected file name): {p}")
            continue
        text = p.read_text(encoding="utf-8")
        h1, pre, sections = split_sections(text)
        name, _, tagline = h1.partition(":")
        _, exec_body = find_section(sections, "executive summary")
        rec = meta.get(p.name, {})
        summary = rec.get("summary") or tagline.strip() or name
        theses.append({
            "path": p, "slug": slug, "when": when, "h1": h1,
            "name": name.strip() or slug, "tagline": tagline.strip(),
            "byline": pre, "sections": sections, "exec": exec_body,
            "summary": summary, "status": (rec.get("extra") or {}).get("status", ""),
            "tags": rec.get("tags") or [], "review": None, "tests": [],
        })
    return theses


def load_review_index():
    """Map review file name -> short verdict from reviews/index.md table."""
    out = {}
    if not REVIEW_INDEX.exists():
        return out
    for line in REVIEW_INDEX.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[-1].endswith(".md"):
            out[cells[-1]] = {"overall": cells[2], "verdict": cells[3], "thesis": cells[1]}
    return out


def load_reviews():
    idx = load_review_index()
    jl = {Path((r.get("data") or {}).get("file", "")).name: r
          for r in read_jsonl(REVIEWS_JSONL) if r.get("kind") == "review"}
    reviews = []
    for p in sorted(REVIEWS_DIR.glob("*.md")):
        if p.name == "index.md" or p.name.startswith("inputs-"):
            continue
        when, slug = parse_fname(p)
        text = p.read_text(encoding="utf-8")
        h1, pre, sections = split_sections(text)
        m = re.search(r"/idea-bot/theses/([\w.-]+\.md)", pre)
        thesis_file = m.group(1) if m else None
        if not thesis_file and (jl.get(p.name) or {}).get("data", {}).get("thesis"):
            thesis_file = Path(jl[p.name]["data"]["thesis"]).name
        score = None
        sm = re.search(r"Score:\s*([\d.]+)\s*/\s*10", text)
        if sm:
            score = float(sm.group(1))
        elif p.name in jl and (jl[p.name].get("metrics") or {}).get("score") is not None:
            score = float(jl[p.name]["metrics"]["score"])
        short = (idx.get(p.name) or {}).get("verdict") or (jl.get(p.name) or {}).get("summary", "")
        reviews.append({
            "path": p, "slug": slug, "when": when, "h1": h1, "byline": pre,
            "sections": sections, "thesis_file": thesis_file, "score": score,
            "short_verdict": short, "matched": False,
        })
    return reviews


def load_tests():
    tests = []
    for p in sorted(TESTS_DIR.glob("*.md")) if TESTS_DIR.exists() else []:
        text = p.read_text(encoding="utf-8")
        h1, pre, sections = split_sections(text)
        m = re.search(r"/idea-bot/theses/([\w.-]+\.md)", pre)
        tests.append({"path": p, "slug": p.stem, "h1": h1 or p.stem, "byline": pre,
                      "text": text, "thesis_file": m.group(1) if m else None, "matched": False})
    return tests


def dedupe_slugs(theses):
    seen = {}
    for t in theses:
        seen.setdefault(t["slug"], []).append(t)
    for slug, ts in seen.items():
        if len(ts) > 1:  # same idea name on different dates: keep pages separate
            for t in ts:
                t["page"] = f"{t['when'].strftime('%Y-%m-%d-%H%M')}-{slug}"
    for t in theses:
        t.setdefault("page", t["slug"])


def match(theses, reviews, tests):
    by_file = {t["path"].name: t for t in theses}
    for r in sorted(reviews, key=lambda r: r["when"] or dt.datetime.min):
        t = by_file.get(r["thesis_file"]) if r["thesis_file"] else None
        if not t:  # fallback: same slug, review after thesis
            cands = [t for t in theses if t["slug"] == r["slug"]
                     and (not r["when"] or t["when"] <= r["when"])]
            t = cands[-1] if cands else None
        if t:
            t["review"] = r  # latest review wins
            r["matched"] = True
    for x in tests:
        t = by_file.get(x["thesis_file"]) if x["thesis_file"] else None
        if not t:
            cands = [t for t in theses if x["slug"].startswith(t["slug"])]
            t = cands[-1] if cands else None
        if t:
            t["tests"].append(x)
            x["matched"] = True


# ---------- rendering ----------
def page(title, body, depth=0):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<header class="site"><a href="{up}index.html">{SITE_TITLE}</a></header>
<main>
{body}
</main>
<footer class="site">Theses by idea bot, reviews by Project Bot. Times are AWST (Perth time).</footer>
</body>
</html>
"""


def copy_source(src, sub):
    dest = DOCS / "sources" / sub / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return f"sources/{sub}/{src.name}"


def render_test(x):
    _, _, sections = split_sections(x["text"])
    body = md(re.sub(r"^# .*\n", "", x["text"], count=1))
    src = copy_source(x["path"], "tests")
    html_body = f"""<p class="back"><a href="../index.html">&larr; All theses</a></p>
<article>
<h1>{esc(x['h1'])}</h1>
<div class="prose">{body}</div>
<p class="sources">Source: <a href="../{src}">{esc(x['path'].name)}</a></p>
</article>"""
    (DOCS / "tests" / f"{x['slug']}.html").write_text(page(x["h1"], html_body, 1), encoding="utf-8")


def render_thesis(t):
    r = t["review"]
    score = r["score"] if r else None
    parts = [f'<p class="back"><a href="../index.html">&larr; All theses</a></p>', "<article>"]
    parts.append(f'<h1>{esc(t["name"])}</h1>')
    if t["tagline"]:
        parts.append(f'<p class="tagline">{esc(cap(t["tagline"]))}</p>')
    meta = [f'<span>{esc(awst(t["when"]))}</span>', badge(score)]
    if t["status"]:
        meta.append(f'<span class="status">Status: {esc(cap(t["status"].replace("-", " ")))}</span>')
    parts.append(f'<p class="meta">{" ".join(meta)}</p>')

    parts.append('<section class="exec"><h2>Executive summary</h2>')
    parts.append(md(t["exec"]) if t["exec"] else "<p><em>No executive summary found in the thesis file.</em></p>")
    parts.append("</section>")

    if t["tests"]:
        links = ", ".join(f'<a href="../tests/{esc(x["slug"])}.html">{esc(x["h1"])}</a>' for x in t["tests"])
        parts.append(f'<p class="callout">Test results: {links}</p>')

    parts.append('<section class="thesis"><h2>Full thesis</h2>')
    if t["byline"]:
        parts.append(f'<div class="byline">{md(t["byline"])}</div>')
    for h, b in t["sections"]:
        if "executive summary" in h.lower():
            continue
        parts.append(f"<h3>{esc(h)}</h3>{md(b)}")
    parts.append("</section>")

    parts.append('<section class="review"><h2>Project Bot review</h2>')
    if not r:
        parts.append('<p class="pending-note">Review pending.</p>')
    else:
        parts.append(f'<p class="meta">{badge(score)} <span>Reviewed {esc(awst(r["when"]))}</span></p>' if r["when"] else "")
        wanted = [("Verdict", ("verdict",)), ("Score breakdown", ("score",)),
                  ("Competitors", ("competitor",)), ("Build plan", ("build plan",))]
        used = set()
        for label, keys in wanted:
            h, b = find_section(r["sections"], *keys)
            if h:
                used.add(h)
                sub = "" if h.lower() == label.lower() else f'<div class="sub">From “{esc(h)}”</div>'
                parts.append(f'<h3>{esc(label)}</h3>{sub}{md(b)}')
            else:
                parts.append(f"<h3>{esc(label)}</h3><p><em>Not in this review.</em></p>")
        rest = [(h, b) for h, b in r["sections"] if h not in used]
        if rest:
            parts.append("<details><summary>Rest of the review (fact-check and notes)</summary>")
            for h, b in rest:
                parts.append(f"<h3>{esc(h)}</h3>{md(b)}")
            parts.append("</details>")
    parts.append("</section>")

    src = [f'<a href="../{copy_source(t["path"], "theses")}">Thesis ({esc(t["path"].name)})</a>']
    if r:
        src.append(f'<a href="../{copy_source(r["path"], "reviews")}">Review ({esc(r["path"].name)})</a>')
    for x in t["tests"]:
        src.append(f'<a href="../{copy_source(x["path"], "tests")}">Test ({esc(x["path"].name)})</a>')
    parts.append(f'<section class="sources"><h2>Sources</h2><ul>{"".join(f"<li>{s}</li>" for s in src)}</ul></section>')
    parts.append("</article>")
    (DOCS / "theses" / f"{t['page']}.html").write_text(page(t["name"], "\n".join(parts), 1), encoding="utf-8")


def render_index(theses):
    rows = []
    for t in sorted(theses, key=lambda t: t["when"], reverse=True):
        r = t["review"]
        score = r["score"] if r else None
        verdict = r["short_verdict"] if r else "Review pending"
        rows.append(f"""<li class="card" data-date="{t['when'].strftime('%Y%m%d%H%M')}" data-score="{'' if score is None else score}">
<div class="card-head"><a class="name" href="theses/{esc(t['page'])}.html">{esc(t['name'])}</a>{badge(score)}</div>
<div class="date">{esc(awst(t['when']))}</div>
<p class="summary">{esc(t['summary'])}</p>
<p class="verdict"><strong>Verdict:</strong> {md_inline(verdict) if r else '<em>Review pending</em>'}</p>
</li>""")
    body = f"""<h1>{SITE_TITLE}</h1>
<p class="lede">Every AI and tech startup thesis from idea bot, each with Project Bot's review. {len(theses)} theses so far.</p>
<div class="sort" role="group" aria-label="Sort theses">
<span>Sort:</span>
<button type="button" data-sort="date" aria-pressed="true">Newest first</button>
<button type="button" data-sort="score" aria-pressed="false">Highest score</button>
</div>
<ol id="list" class="cards">
{''.join(rows)}
</ol>
<script>
(function () {{
  var list = document.getElementById('list');
  var btns = document.querySelectorAll('.sort button');
  function sortBy(key) {{
    var items = Array.prototype.slice.call(list.children);
    items.sort(function (a, b) {{
      if (key === 'score') {{
        var sa = a.dataset.score === '' ? -1 : parseFloat(a.dataset.score);
        var sb = b.dataset.score === '' ? -1 : parseFloat(b.dataset.score);
        if (sb !== sa) return sb - sa;
      }}
      return b.dataset.date.localeCompare(a.dataset.date);
    }});
    items.forEach(function (el) {{ list.appendChild(el); }});
    btns.forEach(function (b) {{ b.setAttribute('aria-pressed', b.dataset.sort === key); }});
  }}
  btns.forEach(function (b) {{ b.addEventListener('click', function () {{ sortBy(b.dataset.sort); }}); }});
}})();
</script>"""
    (DOCS / "index.html").write_text(page(SITE_TITLE, body, 0), encoding="utf-8")


CSS = """:root{--fg:#1d232b;--muted:#5b6672;--bg:#fafbfc;--card:#fff;--line:#e3e7ec;--accent:#1f6feb;
--high:#1a7f37;--mid:#9a6700;--low:#cf222e;--pending:#6e7781}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--fg);background:var(--bg)}
header.site,footer.site{padding:.8rem 1rem;border-bottom:1px solid var(--line);background:var(--card)}
header.site a{font-weight:700;color:var(--fg);text-decoration:none}
footer.site{border-top:1px solid var(--line);border-bottom:0;color:var(--muted);font-size:.85rem;margin-top:3rem;text-align:center}
main{max-width:52rem;margin:0 auto;padding:1rem}
a{color:var(--accent)}
h1{font-size:1.9rem;line-height:1.25;margin:.6rem 0 .3rem}
h2{font-size:1.35rem;margin:2.2rem 0 .6rem;padding-bottom:.3rem;border-bottom:2px solid var(--line)}
h3{font-size:1.1rem;margin:1.6rem 0 .4rem}
.tagline,.lede{color:var(--muted);font-size:1.1rem;margin:.2rem 0 .8rem}
.meta{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;color:var(--muted);font-size:.92rem}
.badge{display:inline-block;padding:.1rem .55rem;border-radius:999px;font-weight:700;font-size:.85rem;color:#fff;white-space:nowrap}
.badge.high{background:var(--high)}.badge.mid{background:var(--mid)}.badge.low{background:var(--low)}.badge.pending{background:var(--pending)}
.exec{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:.2rem 1.1rem 1rem;margin-top:1rem}
.exec h2{border:0;margin-top:1rem}
.callout{background:#fff8c5;border:1px solid #eedc82;border-radius:8px;padding:.6rem .9rem}
.byline{color:var(--muted);font-size:.92rem}
.sub{color:var(--muted);font-size:.85rem;margin-top:-.3rem}
.pending-note{font-weight:600;color:var(--pending)}
.prose,.thesis,.review{overflow-wrap:anywhere}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:.92rem;margin:.6rem 0}
th,td{border:1px solid var(--line);padding:.4rem .55rem;text-align:left;vertical-align:top}
th{background:#f0f3f6}
code{background:#eef1f4;padding:.05rem .3rem;border-radius:4px;font-size:.88em}
pre{background:#eef1f4;padding:.8rem;border-radius:6px;overflow-x:auto}
pre code{background:none;padding:0}
details{margin-top:1.2rem;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:.6rem 1rem}
summary{cursor:pointer;font-weight:600}
.back{margin:.4rem 0 0;font-size:.92rem}
.sources ul{padding-left:1.2rem}
.sort{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;margin:1rem 0;color:var(--muted)}
.sort button{font:inherit;padding:.35rem .8rem;border:1px solid var(--line);border-radius:6px;background:var(--card);cursor:pointer}
.sort button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.cards{list-style:none;padding:0;margin:0;display:grid;gap:.9rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.9rem 1.1rem}
.card-head{display:flex;justify-content:space-between;gap:.8rem;align-items:baseline}
.card .name{font-size:1.2rem;font-weight:700;text-decoration:none}
.card .date{color:var(--muted);font-size:.88rem}
.card p{margin:.45rem 0}
.card .verdict{font-size:.93rem}
@media (max-width:600px){h1{font-size:1.5rem}main{padding:.8rem}.card-head{flex-direction:column;gap:.2rem}}
"""


def main():
    theses = load_theses()
    reviews = load_reviews()
    tests = load_tests()
    dedupe_slugs(theses)
    match(theses, reviews, tests)

    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "theses").mkdir(parents=True)
    (DOCS / "tests").mkdir()
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "style.css").write_text(CSS, encoding="utf-8")

    for x in tests:
        render_test(x)
    for t in theses:
        render_thesis(t)
    render_index(theses)

    print(f"Built {len(theses)} thesis pages, {len(tests)} test pages -> {DOCS}")
    for t in theses:
        r = t["review"]
        print(f"  {t['slug']}: review={'%s (%s/10)' % (r['path'].name, r['score']) if r else 'pending'}"
              f", tests={[x['path'].name for x in t['tests']]}")
    for r in reviews:
        if not r["matched"]:
            print(f"  UNMATCHED review: {r['path'].name}")
    for x in tests:
        if not x["matched"]:
            print(f"  UNMATCHED test: {x['path'].name}")


if __name__ == "__main__":
    main()
