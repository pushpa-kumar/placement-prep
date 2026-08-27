import json, sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import esc, inline_code, HEAD_CSS, site_nav, FOOTER, problems_table_html

SCRATCH = os.path.dirname(__file__)
PROBLEMS_DIR = f"{SCRATCH}/problems"

TOPIC_PAGES = [
    # (page_json_files, slug, title)
    (["page_arrays_strings.json", "page_arrays_strings_extra.json"], "arrays-strings", "Arrays & Strings"),
    (["page_sorting_searching.json", "page_sorting_searching_extra.json"], "sorting-searching", "Sorting & Binary Search"),
    (["page_recursion_backtracking.json", "page_recursion_backtracking_extra.json"], "recursion-backtracking", "Recursion & Backtracking"),
    (["page_dp_core.json", "page_dp_advanced.json"], "dynamic-programming", "Dynamic Programming"),
    (["page_greedy.json", "page_greedy_extra.json"], "greedy", "Greedy Algorithms"),
    (["page_graphs.json", "page_graphs_extra.json"], "graphs", "Graph Algorithms"),
    (["page_trees.json", "page_trees_extra.json"], "trees", "Trees"),
    (["page_data_structures.json", "page_data_structures_extra.json"], "data-structures", "Data Structures for CP"),
    (["page_number_theory.json", "page_number_theory_extra.json"], "number-theory", "Number Theory & Combinatorics"),
    (["page_string_algorithms.json", "page_string_algorithms_extra.json"], "string-algorithms", "String Algorithms"),
    (["page_bit_manipulation.json", "page_bit_manipulation_extra.json"], "bit-manipulation", "Bit Manipulation"),
    (["page_game_theory.json", "page_game_theory_extra.json"], "game-theory", "Game Theory"),
    (["page_network_flow.json", "page_network_flow_extra.json"], "network-flow", "Network Flow & Matching"),
    (["page_fft.json", "page_fft_extra.json"], "fft-ntt", "FFT / NTT"),
]

def slugify(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

def example_card_html(ex, idx, sub_anchor):
    anchor = f"{sub_anchor}-ex{idx}"
    return f'''<article class="example-card" id="{anchor}">
  <h4>{esc(ex["title"])}</h4>
  <div class="section-label">Problem</div>
  <div class="prose">{inline_code(ex["problem"])}</div>
  <div class="section-label">Approach</div>
  <div class="prose">{inline_code(ex["approach"])}</div>
  <div class="section-label">Solution</div>
  <pre><code>{esc(ex["code"])}</code></pre>
  <div class="section-label">Sample I/O</div>
  <div class="io-row">
    <pre><code>{esc(ex["sample_input"])}</code></pre>
    <pre><code>{esc(ex["expected_output"])}</code></pre>
  </div>
</article>'''

def subtopic_html(sub, topic_slug, idx):
    anchor = f"{topic_slug}-{slugify(sub['name'])}"
    examples = "".join(example_card_html(ex, i, anchor) for i, ex in enumerate(sub["examples"]))
    return f'''<section class="topic-section" id="{anchor}">
  <div class="topic-head"><h2>{esc(sub["name"])}</h2><span class="cnt">{len(sub["examples"])} worked example{"s" if len(sub["examples"])!=1 else ""}</span></div>
  <div class="theory-block">{inline_code(sub["theory"])}</div>
  <div class="callout-row">
    <div class="callout"><span class="c-label">Recognize it by</span>{inline_code(sub["recognition"])}</div>
    <div class="callout"><span class="c-label">Complexity</span>{inline_code(sub["complexity"])}</div>
  </div>
  {examples}
</section>'''

def build_page(json_files, slug, title, nav_urls):
    subtopics = []
    intro_parts = []
    for jf in json_files:
        d = json.load(open(f"{SCRATCH}/{jf}"))
        subtopics.extend(d["subtopics"])
        intro_parts.append(d["intro"])
    intro = " ".join(intro_parts)

    problems = []
    try:
        problems = json.load(open(f"{PROBLEMS_DIR}/{slug}.json"))
    except FileNotFoundError:
        pass

    total_examples = sum(len(s["examples"]) for s in subtopics)

    nav_items = "".join(
        f'<li><a href="#{slug}-{slugify(s["name"])}"><span>{esc(s["name"])}</span><span class="cnt">{len(s["examples"])}</span></a></li>'
        for s in subtopics
    )
    other_topics = "".join(
        f'<li><a href="__PAGE__:{tslug}">{esc(ttitle)}</a></li>'
        for _, tslug, ttitle in TOPIC_PAGES if tslug != slug
    )

    sections = "".join(subtopic_html(s, slug, i) for i, s in enumerate(subtopics))
    problems_html = problems_table_html(problems, table_id="probs")

    html = f'''<title>{esc(title)} — CP / DSA Guide</title>
{HEAD_CSS}
<div>
{site_nav(nav_urls, "cpguide")}
<div class="app">
  <header class="topbar">
    <p class="eyebrow">CP / DSA Guide</p>
    <h1>{esc(title)}</h1>
    <p class="tagline">{inline_code(intro)}</p>
    <div class="stats-strip">
      <div class="stat-tile"><div class="n">{len(subtopics)}</div><div class="l">Subtopics</div></div>
      <div class="stat-tile"><div class="n">{total_examples}</div><div class="l">Solved Examples</div></div>
      <div class="stat-tile"><div class="n">{len(problems)}</div><div class="l">Practice Problems</div></div>
    </div>
  </header>

  <div class="layout">
    <aside class="sidebar">
      <h2>On this page</h2>
      <ul class="nav-list">{nav_items}<li><a href="#practice-problems"><span>Practice Problems</span><span class="cnt">{len(problems)}</span></a></li></ul>
      <h2>Other topics</h2>
      <ul class="nav-list">{other_topics}</ul>
      <h2>Back to</h2>
      <ul class="nav-list">
        <li><a href="__PAGE__:cpguide-hub">CP / DSA Guide Hub</a></li>
        <li><a href="__PAGE__:index">Interview Q&amp;A Bank</a></li>
        <li><a href="__PAGE__:further-reading#{slug}">Further Reading (CF Blogs)</a></li>
      </ul>
      <h2>About this page</h2>
      <div class="sidebar-note">
        <p>Every solved example's code was <strong>compiled and run</strong> against its stated sample input, with output verified to match exactly before publishing &mdash; many were additionally stress-tested against independent brute-force references.</p>
        <p>Practice problems are pulled from real Codeforces (verified via the public API), CSES, and LeetCode problem sets &mdash; filtered to non-trivial/hard difficulty.</p>
      </div>
    </aside>
    <main>
      {sections}
      <section class="topic-section" id="practice-problems">
        <div class="topic-head"><h2>Practice Problems</h2><span class="cnt">{len(problems)}</span></div>
        <p class="topic-desc">Curated hard/medium-hard problems from Codeforces, CSES, and LeetCode for this topic &mdash; verified real, not generated.</p>
        {problems_html}
      </section>
    </main>
  </div>
  {FOOTER}
</div>
</div>
'''
    return html
