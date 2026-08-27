import json, sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import esc, inline_code, HEAD_CSS, site_nav, FOOTER
from gen_cpguide_page import TOPIC_PAGES

SCRATCH = os.path.dirname(__file__)
RAW_DIR = os.path.expanduser("~/quant-hft-interview-prep/raw-notes")

BLOG_FILES = [
    "cp-blogs-arrays-sorting-recursion.md",
    "cp-blogs-dp-greedy.md",
    "cp-blogs-graphs-trees-ds.md",
    "cp-blogs-numbertheory-bitmanip-game.md",
    "cp-blogs-strings-flow-fft.md",
    "cp-blogs-arrays-sorting-extra.md",
    "cp-blogs-graphs-extra.md",
    "cp-blogs-numbertheory-flow-fft-extra.md",
    "cp-blogs-recursion-greedy-bit-game-extra.md",
    "cp-blogs-strings-extra.md",
    "cp-blogs-trees-ds-extra.md",
]

# Subtopic-keyword override: some cluster research files loosely mislabel the
# "Topic:" field (e.g. an FFT/NTT blog filed under Number Theory because it was
# researched in the same cluster). This corrects by subtopic keyword, which is
# ground truth since we dictated the exact new-subtopic names.
SUBTOPIC_OVERRIDE = [
    ("Difference Arrays", "Arrays & Strings"),
    ("Merge Intervals", "Arrays & Strings"),
    ("Monotonic Deque", "Arrays & Strings"),
    ("Two-Pointer Partitioning", "Arrays & Strings"),
    ("Custom Comparators", "Sorting & Binary Search"),
    ("Order Statistics", "Sorting & Binary Search"),
    ("Ternary Search", "Sorting & Binary Search"),
    ("Linear Recurrences via Polynomials", "FFT / NTT"),
    ("Min-Cost Max-Flow", "Network Flow & Matching"),
    ("Hungarian Algorithm", "Network Flow & Matching"),
    ("Chinese Remainder", "Number Theory & Combinatorics"),
    ("Matrix Exponentiation", "Number Theory & Combinatorics"),
    ("Lucas", "Number Theory & Combinatorics"),
    ("Möbius", "Number Theory & Combinatorics"),
    ("Divide and Conquer", "Recursion & Backtracking"),
    ("Minimax", "Recursion & Backtracking"),
    ("Huffman", "Greedy Algorithms"),
    ("Fractional vs", "Greedy Algorithms"),
    ("Bit Tricks", "Bit Manipulation"),
    ("Bitset Optimization", "Bit Manipulation"),
    ("Combinatorial Game Sums", "Game Theory"),
    ("Suffix Automaton", "String Algorithms"),
    ("Aho-Corasick", "String Algorithms"),
    ("Palindromic Tree", "String Algorithms"),
    ("Small-to-Large", "Trees"),
    ("Virtual Trees", "Trees"),
    ("Tree Isomorphism", "Trees"),
    ("Sqrt Decomposition", "Data Structures for CP"),
    ("Mo's Algorithm", "Data Structures for CP"),
    ("2D Fenwick", "Data Structures for CP"),
]

def apply_subtopic_override(topic, subtopic):
    for keyword, override_topic in SUBTOPIC_OVERRIDE:
        if keyword.lower() in (subtopic or "").lower():
            return override_topic
    return topic

FIELD_RE = re.compile(r'^-\s*(Author|URL|Topic|Subtopic|Takeaway)\s*:\s*(.*)$')

# Map free-text "Topic:" values from research files to our canonical topic titles/slugs
TOPIC_ALIASES = {
    "arrays & strings": "Arrays & Strings",
    "sorting & binary search": "Sorting & Binary Search",
    "recursion & backtracking": "Recursion & Backtracking",
    "dynamic programming": "Dynamic Programming",
    "greedy algorithms": "Greedy Algorithms",
    "greedy": "Greedy Algorithms",
    "graph algorithms": "Graph Algorithms",
    "trees": "Trees",
    "data structures for cp": "Data Structures for CP",
    "number theory & combinatorics": "Number Theory & Combinatorics",
    "bit manipulation": "Bit Manipulation",
    "game theory": "Game Theory",
    "string algorithms": "String Algorithms",
    "network flow & matching": "Network Flow & Matching",
    "fft / ntt": "FFT / NTT",
}

SLUG_BY_TITLE = {title: slug for _, slug, title in TOPIC_PAGES}
TITLE_ORDER = [title for _, _, title in TOPIC_PAGES]

def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    blocks = re.split(r'(?m)^###\s+', text)
    entries = []
    for block in blocks[1:]:
        lines = block.split("\n")
        title = lines[0].strip()
        fields = {}
        current = None
        for line in lines[1:]:
            if line.startswith("## ") or line.startswith("# "):
                continue
            m = FIELD_RE.match(line)
            if m:
                current = m.group(1)
                fields[current] = m.group(2).strip()
            elif current and line.strip():
                fields[current] += " " + line.strip()
        if not title or "URL" not in fields:
            continue
        raw_topic = fields.get("Topic", "").strip().lower()
        canon_topic = TOPIC_ALIASES.get(raw_topic, fields.get("Topic", "Unknown"))
        canon_topic = apply_subtopic_override(canon_topic, fields.get("Subtopic", ""))
        entries.append({
            "title": title,
            "author": fields.get("Author", ""),
            "url": fields.get("URL", ""),
            "topic": canon_topic,
            "subtopic": fields.get("Subtopic", ""),
            "takeaway": fields.get("Takeaway", ""),
        })
    return entries

def load_all_blogs():
    all_entries = []
    for fname in BLOG_FILES:
        path = os.path.join(RAW_DIR, fname)
        if os.path.exists(path):
            all_entries.extend(parse_file(path))
    return all_entries

def blog_card_html(b):
    sub = f'<span class="judge-badge">{esc(b["subtopic"])}</span>' if b.get("subtopic") else ""
    return f'''<div class="example-box">
  <div class="ex-title"><a href="{esc(b['url'])}" target="_blank" rel="noopener noreferrer">{esc(b['title'])}</a></div>
  <div class="meta-row" style="margin-bottom:8px;"><span class="src">by {esc(b['author'])}</span> {sub}</div>
  <div class="ex-explain">{inline_code(b['takeaway'])}</div>
</div>'''

def build_page(nav_urls):
    entries = load_all_blogs()
    by_topic = {}
    for b in entries:
        by_topic.setdefault(b["topic"], []).append(b)

    nav_items = "".join(
        f'<li><a href="#{slug}"><span>{esc(title)}</span><span class="cnt">{len(by_topic.get(title, []))}</span></a></li>'
        for _, slug, title in TOPIC_PAGES
    )

    sections = []
    for _, slug, title in TOPIC_PAGES:
        blogs = by_topic.get(title, [])
        if not blogs:
            continue
        cards = "".join(blog_card_html(b) for b in blogs)
        sections.append(f'''<section class="topic-section" id="{slug}">
  <div class="topic-head"><h2>{esc(title)}</h2><span class="cnt">{len(blogs)} blogs</span></div>
  <p class="topic-desc">Real, verified Codeforces blog posts for {esc(title)} &mdash; jump to the <a href="__PAGE__:{slug}">{esc(title)} guide page</a> for theory and solved examples.</p>
  {cards}
</section>''')

    total = len(entries)
    html = f'''<title>Further Reading: Codeforces Blogs</title>
{HEAD_CSS}
<div>
{site_nav(nav_urls, "cpguide")}
<div class="app">
  <header class="topbar">
    <p class="eyebrow">CP / DSA Guide &mdash; Further Reading</p>
    <h1>Further Reading: Codeforces Blogs</h1>
    <p class="tagline">Real, verified Codeforces blog posts organized by topic &mdash; tutorials, uncommon tricks, and paths to more problems, straight from the competitive-programming community. Every entry was fetched and confirmed real before inclusion, not invented.</p>
    <div class="stats-strip">
      <div class="stat-tile"><div class="n">{total}</div><div class="l">Blog Posts</div></div>
      <div class="stat-tile"><div class="n">{len(by_topic)}</div><div class="l">Topics Covered</div></div>
    </div>
  </header>

  <div class="layout">
    <aside class="sidebar">
      <h2>On this page</h2>
      <ul class="nav-list">{nav_items}</ul>
      <h2>Back to</h2>
      <ul class="nav-list">
        <li><a href="__PAGE__:cpguide-hub">CP / DSA Guide Hub</a></li>
        <li><a href="__PAGE__:index">Interview Q&amp;A Bank</a></li>
      </ul>
    </aside>
    <main>{"".join(sections)}</main>
  </div>
  {FOOTER}
</div>
</div>
'''
    return html
