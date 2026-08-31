import json, sys, os, collections
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import site_nav, esc

SCRATCH = os.path.dirname(__file__)
DATA_PATH = f"{SCRATCH}/whatsapp_entries.json"
TEMPLATE = f"{SCRATCH}/oa_insights_template.html"
OUT = "/Users/pushpakumar/quant-hft-interview-prep/docs/company-oa-insights.html"
URL_MAP_LOCAL = f"{SCRATCH}/url_map_local.json"

TOPIC_ORDER = [
    "Algorithms & Data Structures (Coding/OA)",
    "Quantitative & Probability Puzzles",
    "General Technical / Company-Specific",
    "System Design (Trading/Low-Latency)",
    "Concurrency, Atomics & Lock-Free",
    "STL, Memory Management & Pointers",
    "C++ Core & Modern C++",
    "OS, Linux, Networking & CPU/Cache/Performance",
    "HFT & Trading Domain Concepts",
    "Interview Process, Format & Behavioral",
]

TOPIC_SHORT = {
    "Algorithms & Data Structures (Coding/OA)": "DSA",
    "Quantitative & Probability Puzzles": "Quant/Aptitude",
    "General Technical / Company-Specific": "General/MCQ/SQL",
}

DSA_SLUG_ORDER = [
    "arrays-strings", "string-algorithms", "trees", "dynamic-programming",
    "bit-manipulation", "number-theory", "data-structures", "graphs",
    "recursion-backtracking", "sorting-searching", "computational-geometry",
    "game-theory", "greedy", "network-flow", "fft-ntt", "unclassified",
]
DSA_SLUG_LABEL = {
    "arrays-strings": "Arrays & Strings", "string-algorithms": "String Algorithms",
    "trees": "Trees", "dynamic-programming": "Dynamic Programming",
    "bit-manipulation": "Bit Manipulation", "number-theory": "Number Theory & Combinatorics",
    "data-structures": "Data Structures (stack/heap/trie/etc.)", "graphs": "Graph Algorithms",
    "recursion-backtracking": "Recursion & Backtracking", "sorting-searching": "Sorting & Binary Search",
    "computational-geometry": "Computational Geometry", "game-theory": "Game Theory",
    "greedy": "Greedy Algorithms", "network-flow": "Network Flow & Matching", "fft-ntt": "FFT / NTT",
    "unclassified": "Unclassified (contest-only reference, e.g. a bare Codeforces/AtCoder problem number with no description)",
}

# Named problems referenced only by title+link (no descriptive text to keyword-match) —
# classified from known knowledge of the actual problem, not guessed.
DSA_OVERRIDES = [
    ("Basic Calculator (https", "data-structures"),
    ("Number of Perfect Pairs (https", "arrays-strings"),
    ("Maximize Distance to Closest Person", "arrays-strings"),
    ("Delete edge to minimize subtree sum", "trees"),
    ("Find Servers That Handled Most Number of Requests", "data-structures"),
    ("Find the Length of the Longest Common Prefix", "string-algorithms"),
    ("Next Greater Element I", "data-structures"),
    ("Maximum of minimum difference of all pairs from subsequences", "sorting-searching"),
    ("N segments are given, each defined by", "data-structures"),
    ("Two arrays arr1 and arr2 of the same length are given. You may independently rearrange", "greedy"),
    ("Ugly Number II", "dynamic-programming"),
    ("Arithmetic Slices", "dynamic-programming"),
    ("generating ascending sequence of 2", "number-theory"),
    ("Zuma Game", "recursion-backtracking"),
    ("A 'hard trees' question", "trees"),
    ("LeetCode 233", "dynamic-programming"),
    ("dynamic-programming-on-a-grid", "dynamic-programming"),
    ("Find Minimum Diameter After Merging Two Trees", "trees"),
]

DSA_RULES = [
    ("computational-geometry", [r"convex hull", r"polygon", r"rectangle area", r"\bfence\b", r"points on a (2d )?plane", r"line segment"]),
    ("network-flow", [r"max(imum)? flow", r"min(imum)? cut", r"bipartite matching", r"\bmatching\b"]),
    ("fft-ntt", [r"\bconvolution\b", r"\bfft\b", r"\bntt\b", r"polynomial multiplication"]),
    ("game-theory", [r"alice and bob", r"two players", r"optimal play", r"\bnim\b", r"first player", r"winning strategy", r"who wins"]),
    ("bit-manipulation", [r"\bxor\b", r"bitwise", r"bit manipulation", r"base -2", r"binary representation of the number"]),
    ("number-theory", [r"\bgcd\b", r"\bprime\b", r"modulo", r"divisib", r"\bnCr\b", r"\bcombinatoric", r"factorial"]),
    ("string-algorithms", [r"palindrom", r"\bkmp\b", r"z-function", r"edit distance", r"\banagram\b", r"lexicograph", r"subsequence of x that is also a substring"]),
    ("data-structures", [r"\bheap\b", r"priority queue", r"\btrie\b", r"segment tree", r"fenwick", r"lru cache", r"\bstack\b", r"\bqueue\b", r"union.?find", r"\bdsu\b"]),
    ("trees", [r"\bbst\b", r"binary search tree", r"\blca\b", r"binary tree", r"\btrees?\b(?!.*\bgraph)"]),
    ("graphs", [r"\bgraphs?\b", r"\bnodes?\b.*\bedges?\b", r"shortest path", r"spanning tree", r"\bmst\b", r"connected component", r"\bbfs\b", r"\bdfs\b", r"\bvertices\b"]),
    ("dynamic-programming", [r"dynamic[- ]programming", r"\bdp\b", r"number of ways", r"no\.?\s*of\s*arrangements", r"minimum cost", r"maximum sum of subsequence", r"knapsack"]),
    ("recursion-backtracking", [r"backtrack", r"\bpermutations? of\b", r"\bsubsets?\b", r"all combinations"]),
    ("greedy", [r"\bgreedy\b", r"minimum number of operations", r"minimize the number of"]),
    ("sorting-searching", [r"binary search", r"\bsort(ed|ing)?\b"]),
    ("arrays-strings", [r"\barray\b", r"subarray", r"\bstring\b", r"substring", r"sliding window", r"two pointers", r"prefix sum"]),
]


def classify_dsa(q):
    import re as _re
    for sub, slug in DSA_OVERRIDES:
        if sub.lower() in q.lower():
            return slug
    ql = q.lower()
    for slug, pats in DSA_RULES:
        for p in pats:
            if _re.search(p, ql):
                return slug
    return "unclassified"


def build_topic_bars(data):
    total = len(data)
    counts = collections.Counter(e["topic"] for e in data)
    rows = []
    for t in TOPIC_ORDER:
        n = counts.get(t, 0)
        if not n:
            continue
        pct = round(100 * n / total)
        rows.append(
            f'<div class="bar-row"><span class="bar-label">{esc(t)}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{pct}%"></span></span>'
            f'<span class="bar-n">{n} ({pct}%)</span></div>'
        )
    return "".join(rows)


def build_company_rows(data):
    by_company = collections.defaultdict(list)
    for e in data:
        for c in e["companies"]:
            if c == "Unknown":
                continue
            by_company[c].append(e)

    rows = []
    for c, items in by_company.items():
        n = len(items)
        if n < 2:
            continue
        topic_counts = collections.Counter(e["topic"] for e in items)
        pct_dsa = round(100 * topic_counts.get("Algorithms & Data Structures (Coding/OA)", 0) / n)
        pct_quant = round(100 * topic_counts.get("Quantitative & Probability Puzzles", 0) / n)
        pct_general = round(100 * topic_counts.get("General Technical / Company-Specific", 0) / n)
        with_link = round(100 * sum(1 for e in items if e.get("url")) / n)
        rows.append((c, n, pct_dsa, pct_quant, pct_general, with_link))

    rows.sort(key=lambda r: -r[1])
    html_rows = []
    for c, n, dsa, quant, general, link in rows:
        html_rows.append(
            f"<tr><td class='company'>{esc(c)}</td><td>{n}</td>"
            f"<td class='pct-dsa'>{dsa}%</td><td>{quant}%</td><td>{general}%</td><td>{link}%</td></tr>"
        )
    return "".join(html_rows)


def build_dsa_bars(dsa_entries):
    total = len(dsa_entries)
    counts = collections.Counter(classify_dsa(e["q"]) for e in dsa_entries)
    rows = []
    for slug in DSA_SLUG_ORDER:
        n = counts.get(slug, 0)
        if not n:
            continue
        pct = round(100 * n / total)
        rows.append(
            f'<div class="bar-row"><span class="bar-label">{esc(DSA_SLUG_LABEL[slug])}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{pct}%"></span></span>'
            f'<span class="bar-n">{n} ({pct}%)</span></div>'
        )
    return "".join(rows)


def build_dsa_company_rows(dsa_entries):
    by_company = collections.defaultdict(list)
    for e in dsa_entries:
        for c in e["companies"]:
            if c == "Unknown":
                continue
            by_company[c].append(e)

    rows = []
    for c, items in by_company.items():
        n = len(items)
        if n < 3:
            continue
        counts = collections.Counter(classify_dsa(e["q"]) for e in items)
        top = [(s, k) for s, k in counts.most_common() if s != "unclassified"][:3]
        top_str = ", ".join(f"{DSA_SLUG_LABEL[s]} ({k})" for s, k in top) if top else "mostly unclassified/contest references"
        rows.append((c, n, top_str))

    rows.sort(key=lambda r: -r[1])
    return "".join(
        f"<tr><td class='company'>{esc(c)}</td><td>{n}</td><td style='text-align:left;'>{esc(top_str)}</td></tr>"
        for c, n, top_str in rows
    )


def main():
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)
    dsa_entries = [e for e in data if e["topic"] == "Algorithms & Data Structures (Coding/OA)"]

    with open(URL_MAP_LOCAL, encoding="utf-8") as f:
        url_map_local = json.load(f)

    nav_urls = {
        "cpguide": url_map_local.get("cpguide-hub", "#"),
        "concepts": url_map_local.get("concepts-hub", "#"),
        "index": url_map_local.get("index", "#"),
        "companyoa": url_map_local.get("companyoa", "#"),
    }
    nav_html = site_nav(nav_urls, "companyoa")

    total = len(data)
    company_count = len(set(c for e in data for c in e["companies"] if c != "Unknown"))
    with_link_count = sum(1 for e in data if e.get("url"))
    stats_html = "".join(
        f'<div class="stat-tile"><div class="n">{n}</div><div class="l">{l}</div></div>'
        for l, n in [
            ("Questions analyzed", total),
            ("Named companies", company_count),
            ("With a practice link", with_link_count),
        ]
    )

    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()

    html = (
        tpl.replace("__SITE_NAV__", nav_html)
        .replace("__STATS_HTML__", stats_html)
        .replace("__TOPIC_BARS_HTML__", build_topic_bars(data))
        .replace("__COMPANY_ROWS_HTML__", build_company_rows(data))
        .replace("__DSA_COUNT__", str(len(dsa_entries)))
        .replace("__DSA_BARS_HTML__", build_dsa_bars(dsa_entries))
        .replace("__DSA_COMPANY_ROWS_HTML__", build_dsa_company_rows(dsa_entries))
        .replace("__BANK_URL__", url_map_local.get("companyoa", "#"))
        .replace("__CPGUIDE_URL__", url_map_local.get("cpguide-hub", "#"))
        .replace("__GEOMETRY_URL__", url_map_local.get("computational-geometry", "#"))
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {OUT}  ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
