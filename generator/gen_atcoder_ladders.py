import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import esc, inline_code, done_checkbox_html, progress_script_tag, HEAD_CSS, site_nav, FOOTER

SCRATCH = os.path.dirname(__file__)
LADDERS_JSON = f"{SCRATCH}/atcoder_ladders.json"

TASK_URL = "https://atcoder.jp/contests/{contest}/tasks/{task}"

# AtCoder's own rating bands, so a difficulty number reads the same here as it
# does on the contest site.
BANDS = [(400, "gray"), (800, "brown"), (1200, "green"), (1600, "cyan"),
         (2000, "blue"), (2400, "yellow"), (2800, "orange")]

EXTRA_CSS = """
<style>
  :root{
    --ac-gray:#7a7f8c; --ac-brown:#8a5a2b; --ac-green:#2f7d32; --ac-cyan:#0f7f86;
    --ac-blue:#2f52c8; --ac-yellow:#8a7500; --ac-orange:#b85c00; --ac-red:#b3302b;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --ac-gray:#9098ac; --ac-brown:#c08a4e; --ac-green:#6fbf8b; --ac-cyan:#4fd1d9;
      --ac-blue:#7aa8e0; --ac-yellow:#d3a256; --ac-orange:#e8a15c; --ac-red:#e08a72;
    }
  }
  :root[data-theme="dark"]{
    --ac-gray:#9098ac; --ac-brown:#c08a4e; --ac-green:#6fbf8b; --ac-cyan:#4fd1d9;
    --ac-blue:#7aa8e0; --ac-yellow:#d3a256; --ac-orange:#e8a15c; --ac-red:#e08a72;
  }

  .ladder-tier{ margin:0 0 22px; }
  .ladder-tier .tier-head{
    display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; margin:0 0 4px;
  }
  .ladder-tier .tier-head h3{ font-size:.95rem; }
  .ladder-tier .tier-band{
    font-family:var(--mono); font-variant-numeric:tabular-nums;
    font-size:.75rem; color:var(--text-faint);
  }
  .ladder-tier .tier-meta{
    padding-bottom:10px; border-bottom:1px solid var(--border); margin-bottom:12px;
  }
  .ladder-tier .tier-note{
    margin:0; font-size:.85rem; color:var(--text-muted); max-width:80ch;
  }

  .rung{
    display:grid; grid-template-columns:34px 1fr; gap:12px;
    padding:12px 0; border-bottom:1px solid var(--border);
  }
  .rung:last-child{ border-bottom:none; }
  .rung-n{
    font-family:var(--mono); font-variant-numeric:tabular-nums;
    font-size:.9rem; font-weight:600; color:var(--text-faint); padding-top:1px;
  }
  .rung-title{ display:flex; align-items:baseline; gap:9px; flex-wrap:wrap; }
  .rung-title a{ font-family:var(--mono); font-size:.88rem; font-weight:600; }
  .rung-id{ font-family:var(--mono); font-size:.74rem; color:var(--text-muted); }
  .ac-diff{
    font-family:var(--mono); font-variant-numeric:tabular-nums;
    font-size:.72rem; font-weight:600; padding:1px 7px;
    border:1px solid currentColor; border-radius:5px;
  }
  .ac-gray{ color:var(--ac-gray); }      .ac-brown{ color:var(--ac-brown); }
  .ac-green{ color:var(--ac-green); }    .ac-cyan{ color:var(--ac-cyan); }
  .ac-blue{ color:var(--ac-blue); }      .ac-yellow{ color:var(--ac-yellow); }
  .ac-orange{ color:var(--ac-orange); }  .ac-red{ color:var(--ac-red); }
  .rung-model{
    font-family:var(--mono); font-size:.7rem; text-transform:uppercase;
    letter-spacing:.06em; color:var(--accent-strong); margin-top:5px;
  }
  .rung-teaches{ font-size:.87rem; color:var(--text-muted); margin:4px 0 0; max-width:80ch; }
  .rung details{ margin-top:6px; }
  .rung summary{
    font-family:var(--mono); font-size:.7rem; text-transform:uppercase;
    letter-spacing:.06em; color:var(--text-faint); cursor:pointer;
    list-style:none; width:fit-content;
  }
  .rung summary::-webkit-details-marker{ display:none; }
  .rung summary::before{ content:"\\25b8  "; }
  .rung details[open] summary::before{ content:"\\25be  "; }
  .rung summary:hover{ color:var(--text); }
  .rung details .nudge{
    margin:6px 0 0; padding-left:11px; border-left:2px solid var(--accent);
    font-size:.87rem; color:var(--text-muted); max-width:78ch;
  }
  .rung .done-checkbox{ margin-left:2px; }
  .nav-list a.sub{ padding-left:20px; font-size:.8rem; }
</style>
"""


def band_class(d):
    for hi, name in BANDS:
        if d < hi:
            return f"ac-{name}"
    return "ac-red"


def rung_html(p):
    url = TASK_URL.format(contest=p["contest"], task=p["task"])
    return f'''<div class="rung">
  <div class="rung-n">{p["n"]:02d}</div>
  <div>
    <div class="rung-title">
      <a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(p["title"])}</a>
      <span class="rung-id">{esc(p["label"])}</span>
      <span class="ac-diff {band_class(p["difficulty"])}">{p["difficulty"]}</span>
      {done_checkbox_html(url, "problem")}
    </div>
    <div class="rung-model">{esc(p["model"])}</div>
    <p class="rung-teaches">{esc(p["teaches"])}</p>
    <details><summary>Nudge</summary><div class="nudge">{inline_code(p["nudge"])}</div></details>
  </div>
</div>'''


def tier_html(tier, ladder_slug):
    rungs = "".join(rung_html(p) for p in tier["problems"])
    anchor = f'{ladder_slug}-{tier["name"].lower().replace(" ", "-")}'
    return f'''<div class="ladder-tier" id="{esc(anchor)}">
  <div class="tier-meta">
    <div class="tier-head">
      <h3>{esc(tier["name"])}</h3>
      <span class="tier-band">{esc(tier["band"])}</span>
    </div>
    <p class="tier-note">{esc(tier["note"])}</p>
  </div>
  {rungs}
</div>'''


def ladder_html(ladder):
    n = sum(len(t["problems"]) for t in ladder["tiers"])
    tiers = "".join(tier_html(t, ladder["slug"]) for t in ladder["tiers"])
    guide_link = ""
    if ladder.get("guide_slug"):
        guide_link = (f' Theory and worked examples for this technique live on the '
                      f'<a href="__PAGE__:{ladder["guide_slug"]}{ladder.get("guide_anchor", "")}">'
                      f'{esc(ladder.get("guide_label", ladder["name"]))} section</a>.')
    return f'''<section class="topic-section" id="{esc(ladder["slug"])}">
  <div class="topic-head"><h2>{esc(ladder["name"])}</h2><span class="cnt">{n} problems</span></div>
  <p class="topic-desc">{esc(ladder["blurb"])} Picked from the {ladder["pool"]} problems tagged on
    <a href="{esc(ladder["source_url"])}" target="_blank" rel="noopener noreferrer">{esc(ladder["source_label"])}</a>.{guide_link}</p>
  {tiers}
</section>'''


def ladder_counts():
    """(number of ladders, total problems) — used by the hub for its stats."""
    d = json.load(open(LADDERS_JSON))
    total = sum(len(t["problems"]) for l in d["ladders"] for t in l["tiers"])
    return len(d["ladders"]), total


def build_page(nav_urls):
    d = json.load(open(LADDERS_JSON))
    ladders = d["ladders"]
    total = sum(len(t["problems"]) for l in ladders for t in l["tiers"])
    ratings = [p["difficulty"] for l in ladders for t in l["tiers"] for p in t["problems"]]

    nav_items = []
    index_cards = []
    for l in ladders:
        probs = [p for t in l["tiers"] for p in t["problems"]]
        n = len(probs)
        nav_items.append(f'<li><a href="#{esc(l["slug"])}"><span>{esc(l["name"])}</span>'
                         f'<span class="cnt">{n}</span></a></li>')
        index_cards.append(
            f'<a class="hub-card" href="#{esc(l["slug"])}"><h3>{esc(l["name"])}</h3>'
            f'<div class="meta">{n} problems &middot; {probs[0]["difficulty"]}&ndash;{probs[-1]["difficulty"]}</div></a>')

    index = (f'<section class="topic-section" id="all-ladders">'
             f'<div class="topic-head"><h2>All Ladders</h2><span class="cnt">{len(ladders)}</span></div>'
             f'<p class="topic-desc">Each ladder is independent &mdash; start with whichever technique you are working on. '
             f'Every guide page also links straight into the ladder for its own topic.</p>'
             f'<div class="hub-grid">{"".join(index_cards)}</div></section>')

    sections = index + "".join(ladder_html(l) for l in ladders)

    html = f'''<title>AtCoder Ladders</title>
{HEAD_CSS}
{EXTRA_CSS}
{progress_script_tag()}
<div>
{site_nav(nav_urls, "cpguide")}
<div class="app">
  <header class="topbar">
    <p class="eyebrow">CP / DSA Guide &mdash; AtCoder Ladders</p>
    <h1>AtCoder Ladders</h1>
    <p class="tagline">{esc(d["intro"])}</p>
    <div class="stats-strip">
      <div class="stat-tile"><div class="n">{len(ladders)}</div><div class="l">Ladders</div></div>
      <div class="stat-tile"><div class="n">{total}</div><div class="l">Problems</div></div>
      <div class="stat-tile"><div class="n">{min(ratings)}&ndash;{max(ratings)}</div><div class="l">Difficulty Range</div></div>
    </div>
  </header>

  <div class="layout">
    <aside class="sidebar">
      <h2>On this page</h2>
      <ul class="nav-list">{"".join(nav_items)}</ul>
      <h2>Back to</h2>
      <ul class="nav-list">
        <li><a href="__PAGE__:cpguide-hub">CP / DSA Guide Hub</a></li>
        <li><a href="__PAGE__:further-reading">Further Reading (CF Blogs)</a></li>
        <li><a href="__PAGE__:index">Interview Q&amp;A Bank</a></li>
      </ul>
      <h2>How to use this</h2>
      <div class="sidebar-note"><p>{esc(d["how_to_use"])}</p></div>
    </aside>
    <main>{sections}</main>
  </div>
  {FOOTER}
</div>
</div>
'''
    return html
