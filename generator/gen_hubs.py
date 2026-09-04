import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import gen_lib
from gen_lib import esc, inline_code, progress_script_tag, HEAD_CSS, site_nav, FOOTER
from gen_cpguide_page import TOPIC_PAGES
from gen_concept_page import GROUP_FILES
from gen_atcoder_ladders import ladder_counts

SCRATCH = os.path.dirname(__file__)

CPGUIDE_DESCRIPTIONS = {
    "arrays-strings": "Two pointers, sliding window, prefix sums, Kadane's algorithm.",
    "sorting-searching": "Sorting tradeoffs, binary search, and binary search on the answer.",
    "recursion-backtracking": "Permutation/subset generation, pruning, meet-in-the-middle.",
    "dynamic-programming": "The full DP toolkit: linear, grid, knapsack, interval, bitmask, tree, digit, game-theory, probability, string DP, and optimization techniques.",
    "greedy": "Exchange-argument correctness proofs, interval scheduling, greedy + data structures.",
    "graphs": "Shortest paths, MST, topological sort, SCC, bridges/articulation points, bipartite check.",
    "trees": "Traversals, Euler tour, LCA/binary lifting, diameter, HLD, centroid decomposition.",
    "data-structures": "Segment tree (incl. persistent), Fenwick tree, sparse table, DSU, trie, monotonic stack/queue.",
    "number-theory": "GCD/extended Euclid, modular arithmetic, sieves, primality at scale, combinatorics.",
    "string-algorithms": "KMP, Z-function, string hashing, Manacher's, tries, suffix arrays.",
    "bit-manipulation": "Subset enumeration, SOS DP, XOR properties, linear basis.",
    "game-theory": "Nim, the XOR winning condition, and the Sprague-Grundy theorem.",
    "network-flow": "Max flow (Edmonds-Karp), min cut, bipartite matching (Kuhn's algorithm).",
    "fft-ntt": "Polynomial multiplication via FFT, exact convolution via NTT.",
    "computational-geometry": "Convex hull, sweep-line rectangle union area, closest pair of points, polygon area & point-in-polygon.",
}

ROADMAP = [
    {
        "stage": 0, "title": "C++ Foundations",
        "goal": "Skim these alongside everything else below — you'll lean on value categories/move semantics and RAII constantly once you start writing real solutions, and OOP mechanics comes up in interviews even outside CP.",
        "items": [
            ("concept", "value-categories", "Value Categories & Move Semantics"),
            ("concept", "raii-resources", "RAII & Resource Management"),
            ("concept", "oop-mechanics", "OOP Mechanics & Polymorphism"),
        ],
    },
    {
        "stage": 1, "title": "Core Patterns",
        "goal": "Build fluency with the basic \"vocabulary\" of CP before layering on DP or graphs. Don't rush this stage — most harder topics are built directly on top of it.",
        "items": [
            ("topic", "arrays-strings", "Arrays & Strings"),
            ("topic", "sorting-searching", "Sorting & Binary Search"),
            ("topic", "recursion-backtracking", "Recursion & Backtracking"),
        ],
    },
    {
        "stage": 2, "title": "Foundational DP & Greedy",
        "goal": "Start with Dynamic Programming's core subtopics (Fundamentals, Linear/1D, 2D Grid, Knapsack, Interval, String DP) — save Bitmask/Tree/Digit DP and DP optimization for Stage 5. DP is the single highest-leverage topic on this whole site; expect to revisit its page many times.",
        "items": [
            ("topic", "dynamic-programming", "Dynamic Programming (core subtopics)"),
            ("topic", "greedy", "Greedy Algorithms"),
        ],
    },
    {
        "stage": 3, "title": "Graphs & Trees",
        "goal": "Graph and tree code leans heavily on pointers/references and generic adjacency representations — the Templates and Compile-Time Concepts pages are handy references if anything there feels shaky.",
        "items": [
            ("topic", "graphs", "Graph Algorithms"),
            ("topic", "trees", "Trees (traversals, LCA, diameter — skip HLD/centroid decomposition for now)"),
        ],
    },
    {
        "stage": 4, "title": "Data Structures for CP",
        "goal": "This unlocks the harder Graph/Tree/DP problems you may have skipped earlier — once done, go back and retry a few Stage 2-3 problems using segment trees / BIT / DSU where relevant.",
        "items": [
            ("topic", "data-structures", "Data Structures for CP"),
        ],
    },
    {
        "stage": 5, "title": "Advanced DP & Math",
        "goal": "This is where CP gets genuinely hard — budget the most time here. Return to the Dynamic Programming page for its Bitmask, Tree DP, Digit DP, DP on DAGs, Game-theory DP, Probability/EV DP, and DP-optimization subtopics.",
        "items": [
            ("topic", "dynamic-programming", "Dynamic Programming (advanced subtopics)"),
            ("topic", "number-theory", "Number Theory & Combinatorics"),
            ("topic", "bit-manipulation", "Bit Manipulation"),
        ],
    },
    {
        "stage": 6, "title": "Strings & Game Theory",
        "goal": "Reasonably self-contained — you could pull this stage earlier if you prefer, but it builds cleanly on Stage 4's trie/DSU work and Stage 5's bitmask-adjacent DP thinking.",
        "items": [
            ("topic", "string-algorithms", "String Algorithms"),
            ("topic", "game-theory", "Game Theory"),
        ],
    },
    {
        "stage": 7, "title": "Computational Geometry",
        "goal": "A self-contained topic you can slot in anytime after Stage 1 (it only needs sorting and basic arithmetic) — added because convex hull and sweep-line rectangle-area problems showed up independently across several real company OAs in the Company OA Bank.",
        "items": [
            ("topic", "computational-geometry", "Computational Geometry"),
        ],
    },
    {
        "stage": 8, "title": "Optional / Advanced",
        "goal": "Rarely needed for placement-level OAs — treat these as a CF-rating-climbing / ICPC-style extension once the rest is solid, not a prerequisite for interviews.",
        "items": [
            ("topic", "network-flow", "Network Flow & Matching"),
            ("topic", "fft-ntt", "FFT / NTT"),
            ("topic", "trees", "Trees — HLD & Centroid Decomposition sections"),
        ],
    },
]

def roadmap_html():
    def item_link(kind, slug, label):
        return f'<li><a href="__PAGE__:{slug}"><span>{esc(label)}</span></a></li>'
    stages_html = []
    for s in ROADMAP:
        items = "".join(item_link(*it) for it in s["items"])
        stages_html.append(f'''<div class="roadmap-stage">
  <div class="roadmap-num">{s["stage"]}</div>
  <div class="roadmap-body">
    <h3>{esc(s["title"])}</h3>
    <p class="roadmap-goal">{esc(s["goal"])}</p>
    <ul class="nav-list roadmap-items">{items}</ul>
  </div>
</div>''')
    return f'''<section class="topic-section" id="roadmap">
  <div class="topic-head"><h2>Suggested Study Order</h2></div>
  <p class="topic-desc">A prerequisite-aware path through all 15 topics (and the most relevant C++ Concepts pages) if you're not sure where to start. At every stage, once you've worked through a topic's solved examples and a few practice problems, dip into the <a href="__PAGE__:index">Interview Q&amp;A + MCQ Bank</a> for that area to consolidate it for actual interview settings.</p>
  <div class="roadmap-grid">{"".join(stages_html)}</div>
</section>'''

def build_cpguide_hub(nav_urls, topic_urls):
    total_examples = 0
    total_problems = 0
    cards = []
    for jfs, slug, title in TOPIC_PAGES:
        n_examples = 0
        for jf in jfs:
            d = json.load(open(f"{SCRATCH}/{jf}"))
            n_examples += sum(len(s["examples"]) for s in d["subtopics"])
        try:
            n_problems = len(json.load(open(f"{SCRATCH}/problems/{slug}.json")))
        except FileNotFoundError:
            n_problems = 0
        total_examples += n_examples
        total_problems += n_problems
        url = topic_urls.get(slug, "#")
        cards.append(f'''<a class="hub-card" href="{esc(url)}">
  <h3>{esc(title)}</h3>
  <p>{esc(CPGUIDE_DESCRIPTIONS.get(slug, ""))}</p>
  <div class="meta">{n_examples} solved examples &middot; {n_problems} practice problems</div>
</a>''')

    # Ladder rungs are individually markable too, so they count toward the total.
    n_ladders, n_ladder_problems = ladder_counts()
    total_problems += n_ladder_problems

    progress_section = ""
    if gen_lib.PROGRESS_ENABLED:
        progress_section = f'''<section class="topic-section" id="my-progress">
  <div class="topic-head"><h2>My Progress</h2></div>
  <p class="progress-signin-hint" data-progress-signin-hint>Sign in (top right) to mark problems, examples, and concepts as done and have it follow you across devices.</p>
  <div class="progress-summary" data-progress-signed-in style="display:none;">
    <div class="stat-tile"><div class="n" data-progress-summary="problem" data-progress-total="{total_problems}">0 / {total_problems}</div><div class="l">Problems Done</div></div>
    <div class="stat-tile"><div class="n" data-progress-summary="example" data-progress-total="{total_examples}">0 / {total_examples}</div><div class="l">Examples Done</div></div>
  </div>
</section>'''

    html = f'''<title>CP / DSA Guide</title>
{HEAD_CSS}
{progress_script_tag()}
<div>
{site_nav(nav_urls, "cpguide")}
<div class="app">
  <header class="topbar">
    <p class="eyebrow">Competitive Programming &amp; DSA</p>
    <h1>CP / DSA Guide</h1>
    <p class="tagline">A comprehensive, placement-exam-oriented guide across 15 major CP/DSA topics &mdash; theory, hand-verified solved examples (every one compiled and run), and curated hard practice problems from Codeforces, CSES, and LeetCode.</p>
    <div class="stats-strip">
      <div class="stat-tile"><div class="n">{len(TOPIC_PAGES)}</div><div class="l">Topics</div></div>
      <div class="stat-tile"><div class="n">{total_examples}</div><div class="l">Solved Examples</div></div>
      <div class="stat-tile"><div class="n">{total_problems}</div><div class="l">Practice Problems</div></div>
    </div>
  </header>
  <div class="app" style="padding-top:28px;">
    {progress_section}
    {roadmap_html()}
    <div class="topic-head" style="margin-top:8px;"><h2>All Topics</h2></div>
    <div class="hub-grid">{"".join(cards)}</div>
    <div class="topic-head" style="margin-top:40px;"><h2>Practice Ladders</h2></div>
    <p class="topic-desc">Ordered problem ladders built from the AtCoder Categories tags &mdash; one technique per ladder, climbing from its easiest AtCoder appearance to its hardest, with each rung chosen to add a model the earlier rungs did not cover.</p>
    <div class="hub-grid">
      <a class="hub-card" href="__PAGE__:atcoder-ladders"><h3>AtCoder Ladders</h3><p>Technique ladders in increasing difficulty, each rung tagged with the model it teaches and a one-line nudge for when you get stuck.</p><div class="meta">{n_ladders} ladder{"s" if n_ladders != 1 else ""} &middot; {n_ladder_problems} problems</div></a>
    </div>
    <div class="topic-head" style="margin-top:40px;"><h2>Further Reading</h2></div>
    <p class="topic-desc">Curated, verified Codeforces blog posts per topic &mdash; tutorials, uncommon tricks, and paths to more problems, straight from the CP community.</p>
    <div class="hub-grid">
      <a class="hub-card" href="__PAGE__:further-reading"><h3>Further Reading: Codeforces Blogs</h3><p>Real, verified blog posts organized by topic, with a one-line takeaway for each.</p></a>
    </div>
  </div>
  {FOOTER}
</div>
</div>
'''
    return html

def build_concepts_hub(nav_urls, concept_urls):
    cards = []
    total_concepts = 0
    total_examples = 0
    for fname, title in GROUP_FILES:
        d = json.load(open(f"{SCRATCH}/{fname}"))
        n = len(d["concepts"])
        ne = sum(len(c["examples"]) for c in d["concepts"])
        total_concepts += n
        total_examples += ne
        url = concept_urls.get(d["slug"], "#")
        cards.append(f'''<a class="hub-card" href="{esc(url)}">
  <h3>{esc(title)}</h3>
  <p>{esc(d["intro"][:180])}{"…" if len(d["intro"])>180 else ""}</p>
  <div class="meta">{n} concepts &middot; {ne} worked examples</div>
</a>''')

    html = f'''<title>C++ Concepts Reference</title>
{HEAD_CSS}
{progress_script_tag()}
<div>
{site_nav(nav_urls, "concepts")}
<div class="app">
  <header class="topbar">
    <p class="eyebrow">Quick-Refresher Glossary</p>
    <h1>C++ Concepts Reference</h1>
    <p class="tagline">40 core C++ concepts, grouped into 7 in-depth pages &mdash; each with a thorough explanation, worked code examples, common pitfalls, and why it matters for low-latency/HFT interviews. Every code example here was compile-verified.</p>
    <div class="stats-strip">
      <div class="stat-tile"><div class="n">{len(GROUP_FILES)}</div><div class="l">Groups</div></div>
      <div class="stat-tile"><div class="n">{total_concepts}</div><div class="l">Concepts</div></div>
      <div class="stat-tile"><div class="n">{total_examples}</div><div class="l">Worked Examples</div></div>
    </div>
  </header>
  <div class="app" style="padding-top:28px;">
    <div class="hub-grid">{"".join(cards)}</div>
  </div>
  {FOOTER}
</div>
</div>
'''
    return html
