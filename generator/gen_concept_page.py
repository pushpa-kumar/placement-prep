import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import esc, inline_code, highlight_cpp, HEAD_CSS, site_nav, FOOTER

GROUP_FILES = [
    ("concepts_group1_value_categories.json", "Value Categories & Move Semantics"),
    ("concepts_group2_oop.json", "Object-Oriented Mechanics & Polymorphism"),
    ("concepts_group3_raii.json", "RAII & Resource Management"),
    ("concepts_group4_templates.json", "Templates & Generic Programming"),
    ("concepts_group5_compile_time.json", "Compile-Time Constructs & Program Structure"),
    ("concepts_group6_concurrency_memory.json", "Concurrency, Memory Model & Low-Level Layout"),
    ("concepts_group7_modern.json", "Modern C++ (17/20) & STL Utilities"),
]

SCRATCH = os.path.dirname(__file__)

def slugify(t):
    import re
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

def build_term_map():
    """term -> (group_slug, group_title, anchor_id)"""
    m = {}
    for fname, _ in GROUP_FILES:
        d = json.load(open(f"{SCRATCH}/{fname}"))
        for c in d["concepts"]:
            m[c["term"]] = (d["slug"], d["group"], slugify(c["term"]))
    return m

TERM_MAP = build_term_map()

def concept_card_html(c, group_slug):
    anchor = slugify(c["term"])
    examples_html = "".join(f'''<div class="example-box">
  <div class="ex-title">{esc(ex["title"])}</div>
  <pre><code>{highlight_cpp(ex["code"])}</code></pre>
  <div class="ex-explain">{inline_code(ex["explanation"])}</div>
</div>''' for ex in c["examples"])
    pitfalls_html = ""
    if c.get("pitfalls"):
        items = "".join(f"<li>{inline_code(p)}</li>" for p in c["pitfalls"])
        pitfalls_html = f'<div class="pitfalls"><div class="p-label">Pitfalls</div><ul>{items}</ul></div>'
    why_html = f'<p class="why-box">{inline_code(c["why"])}</p>' if c.get("why") else ""
    related_html = ""
    if c.get("related"):
        tags = []
        for r in c["related"]:
            if r in TERM_MAP and r != c["term"]:
                gslug, gtitle, ganchor = TERM_MAP[r]
                if gslug == group_slug:
                    href = f"#{ganchor}"
                else:
                    href = f"__PAGE__:{gslug}#{ganchor}"
                tags.append((r, href))
            else:
                tags.append((r, None))
        tag_html = "".join(
            f'<a class="related-tag" href="{esc(href)}" data-related-href="{esc(href)}">{esc(r)}</a>' if href
            else f'<span class="related-tag">{esc(r)}</span>'
            for r, href in tags
        )
        related_html = f'<div class="related-row"><span class="r-label">Related</span>{tag_html}</div>'
    return f'''<article class="concept-card" id="{anchor}">
  <h3>{esc(c["term"])}</h3>
  <div class="intro">{inline_code(c["intro"])}</div>
  {examples_html}
  {pitfalls_html}
  {why_html}
  {related_html}
</article>'''

def build_page(fname, group_title, nav_urls):
    d = json.load(open(f"{SCRATCH}/{fname}"))
    group_slug = d["slug"]
    nav_items = "".join(
        f'<li><a href="#{slugify(c["term"])}"><span>{esc(c["term"])}</span></a></li>'
        for c in d["concepts"]
    )
    other_groups = "".join(
        f'<li><a href="__PAGE__:{gd_slug}">{esc(gd_title)}</a></li>'
        for gfname, gd_title in GROUP_FILES
        for gd_slug in [json.load(open(f"{SCRATCH}/{gfname}"))["slug"]]
        if gd_slug != group_slug
    )
    cards = "".join(concept_card_html(c, group_slug) for c in d["concepts"])

    html = f'''<title>{esc(group_title)} — C++ Concepts</title>
{HEAD_CSS}
<div>
{site_nav(nav_urls, "concepts")}
<div class="app">
  <header class="topbar">
    <p class="eyebrow">C++ Concepts Reference</p>
    <h1>{esc(group_title)}</h1>
    <p class="tagline">{inline_code(d["intro"])}</p>
    <div class="stats-strip">
      <div class="stat-tile"><div class="n">{len(d["concepts"])}</div><div class="l">Concepts</div></div>
      <div class="stat-tile"><div class="n">{sum(len(c["examples"]) for c in d["concepts"])}</div><div class="l">Worked Examples</div></div>
    </div>
  </header>

  <div class="layout">
    <aside class="sidebar">
      <h2>On this page</h2>
      <ul class="nav-list">{nav_items}</ul>
      <h2>Other concept groups</h2>
      <ul class="nav-list">{other_groups}</ul>
      <h2>Back to</h2>
      <ul class="nav-list">
        <li><a href="__PAGE__:concepts-hub">All C++ Concepts</a></li>
        <li><a href="__PAGE__:index">Interview Q&amp;A Bank</a></li>
      </ul>
    </aside>
    <main>{cards}</main>
  </div>
  {FOOTER}
</div>
</div>
'''
    return html

if __name__ == "__main__":
    print("term map size:", len(TERM_MAP))
    for t, v in list(TERM_MAP.items())[:5]:
        print(t, "->", v)
