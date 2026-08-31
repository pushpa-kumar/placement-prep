import re, collections

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
    for sub, slug in DSA_OVERRIDES:
        if sub.lower() in q.lower():
            return slug
    ql = q.lower()
    for slug, pats in DSA_RULES:
        for p in pats:
            if re.search(p, ql):
                return slug
    return "unclassified"


def dsa_topic_counts(dsa_entries):
    return collections.Counter(classify_dsa(e["q"]) for e in dsa_entries)


def dsa_company_top_subtopics(dsa_entries, min_count=3, top_n=3):
    by_company = collections.defaultdict(list)
    for e in dsa_entries:
        for c in e["companies"]:
            if c == "Unknown":
                continue
            by_company[c].append(e)

    rows = []
    for c, items in by_company.items():
        n = len(items)
        if n < min_count:
            continue
        counts = collections.Counter(classify_dsa(e["q"]) for e in items)
        top = [(s, k) for s, k in counts.most_common() if s != "unclassified"][:top_n]
        rows.append((c, n, top))
    rows.sort(key=lambda r: -r[1])
    return rows
