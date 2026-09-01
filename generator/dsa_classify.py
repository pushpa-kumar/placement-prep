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


# ---------------------------------------------------------------------------
# Second, finer layer: within each coarse DSA topic, identify the specific
# technique a question actually uses (e.g. "Monotonic Stack" rather than just
# "Data Structures"). Applied only to DSA-tagged questions.
# ---------------------------------------------------------------------------

TECHNIQUE_OVERRIDES = [
    ("Basic Calculator (https", "Stack-Based Expression Parsing"),
    ("Number of Perfect Pairs (https", "Sorting + Two-Pointer Pair Counting"),
    ("Maximize Distance to Closest Person", "Greedy Array Scan (Gap Analysis)"),
    ("Delete edge to minimize subtree sum", "Tree DP / Subtree Aggregation"),
    ("Find Servers That Handled Most Number of Requests", "Heap / Ordered-Set Simulation"),
    ("Find the Length of the Longest Common Prefix", "Trie / Longest Common Prefix"),
    ("Next Greater Element I", "Monotonic Stack"),
    ("Maximum of minimum difference of all pairs from subsequences", "Binary Search on the Answer"),
    ("N segments are given, each defined by", "Sweep Line + Interval Counting"),
    ("Ugly Number II", "Multi-Pointer Merge DP"),
    ("Arithmetic Slices", "Linear-Scan Counting DP"),
    ("Zuma Game", "Backtracking Search (Interval Removal)"),
    ("Find Minimum Diameter After Merging Two Trees", "Tree Diameter / Distance Queries"),
]

TECHNIQUE_RULES = {
    "arrays-strings": [
        ("Prefix Sum / Range-Sum Queries", [r"prefix sum", r"sum of the subarray", r"average exactly", r"subarray.*average", r"sum.*of.*subarray"]),
        ("Sliding Window / Two Pointers", [r"sliding window", r"two pointers?", r"window size", r"contiguous block"]),
        ("Interval / Overlap Processing", [r"overlapping", r"startsat", r"endsat", r"\bintervals?\b"]),
        ("Greedy Rearrangement / Sorting for Optimum", [r"rearrange", r"swap any two elements", r"maximi[sz]e.*index", r"partition of an array"]),
        ("Binary-String / Char-Frequency Manipulation", [r"binary string", r"string containing only", r"'0' or '1'", r"change (any )?'?a'? to '?b'?"]),
        ("Simulation", [r"simulat", r"collisions?", r"\brobots?\b", r"stack of food"]),
        ("Minimum-Operations String/Array Transformation", [r"minimum (number of )?(changes|operations)", r"\bconvert\b", r"operation \(?x,? y\)?"]),
        ("Heap / Selection Algorithm (Quickselect)", [r"kth largest", r"kth smallest"]),
        ("Greedy + Heap (repeated element reduction)", [r"\bhalve\b", r"\bceil\b.*add it back"]),
        ("Bipartite/Greedy Matching Between Two Arrays", [r"two arrays.*login", r"initiallogin", r"standardlogin"]),
        ("Subarray / Subsequence Counting", [r"count of subarrays", r"number of subarrays", r"number of ways to (choose|split)", r"how many ways", r"count how many", r"\bsubsequences?\b", r"\bsubarrays?\b"]),
    ],
    "string-algorithms": [
        ("Palindrome Construction (Greedy)", [r"palindrom"]),
        ("Edit Distance / LCS DP", [r"edit distance", r"longest common subsequence", r"\blcs\b"]),
        ("Trie / Longest Common Prefix", [r"longest common prefix", r"\btrie\b"]),
        ("Anagram / Character-Rearrangement Counting", [r"anagram", r"rearranged.*characters", r"concatenation"]),
        ("Substring Matching / Lexicographic Queries", [r"substring", r"lexicograph", r"differs from s in at most one position", r"closest word"]),
        ("Minimum-Operations String Transformation", [r"minimum (number of )?(changes|operations)", r"convert any character"]),
    ],
    "trees": [
        ("Tree DP / Subtree Aggregation", [r"subtree", r"friend group", r"differential sum", r"sum all nodes", r"sum.*descendant"]),
        ("BST Property / Inorder Traversal", [r"\bbst\b", r"binary search tree"]),
        ("Tree Diameter / Distance Queries", [r"distance", r"diameter", r"propagat", r"farthest node"]),
        ("Minimum Spanning Tree (Kruskal/Prim variant)", [r"spanning tree"]),
        ("Tree Edge-Removal / Component Partition", [r"remove.*edges?", r"k-tree", r"delete edge"]),
    ],
    "dynamic-programming": [
        ("Digit DP", [r"number of digit one", r"digit dp", r"count.*digits?.*number"]),
        ("Grid DP", [r"\bgrid\b", r"movement across a grid", r"paint n x 3 grid"]),
        ("Counting Permutations / Arrangements DP", [r"number of permutations", r"arrangements"]),
        ("Interval / Partition DP", [r"partition", r"combine.*adjacent", r"minimum cost.*combin"]),
        ("String-Matching DP (min prefixes to build target)", [r"minimum number of (pre)?strings", r"used as prefixes"]),
        ("Layered/Multi-Track Path DP", [r"bus lines?", r"red line", r"blue line"]),
    ],
    "bit-manipulation": [
        ("Negative/Custom Base Representation", [r"base -2", r"base minus two", r"negative base"]),
        ("Bitwise Matrix/Submatrix Operations", [r"submatrix", r"binary matri"]),
        ("Bitwise Recurrence / Sequence Generation", [r"recurrence", r"f\[i\]", r"sequence with f\[0\]"]),
        ("XOR Properties", [r"\bxor\b"]),
    ],
    "number-theory": [
        ("GCD / Divisibility", [r"\bgcd\b", r"prime number", r"divisib"]),
        ("Modular Arithmetic / Combinatorics Counting", [r"modulo", r"number of ways to split", r"\bncr\b"]),
        ("Digit-Sum / Number Generation", [r"ascending sequence", r"digit sum"]),
    ],
    "data-structures": [
        ("Monotonic Stack", [r"next greater element", r"\bstack\b"]),
        ("Stack-Based Expression Parsing", [r"calculator", r"expression"]),
        ("Heap / Ordered-Set Simulation", [r"servers that handled", r"priority queue", r"\bheap\b"]),
        ("Sweep Line + Interval Counting (BIT/Segment Tree)", [r"segments? are given", r"intersects?/overlaps?"]),
        ("Binary Search on the Answer (feasibility check)", [r"binary.search.*throughput", r"binary search question"]),
    ],
    "graphs": [
        ("Connected Components", [r"connected component"]),
        ("Graph Degree-Based Elimination Simulation", [r"degree 0 or 1", r"vertex.*disappear"]),
        ("Shortest Path / Reachability", [r"shortest path", r"reachab"]),
        ("Graph Spread/Containment Simulation", [r"virus", r"containment", r"spread"]),
    ],
    "recursion-backtracking": [("Backtracking Search", [r".*"])],
    "sorting-searching": [
        ("Binary Search on the Answer", [r"binary search"]),
        ("Sorting for Greedy Optimum", [r"sort"]),
    ],
    "computational-geometry": [
        ("Convex Hull", [r"convex hull", r"fence"]),
        ("Sweep-Line Rectangle Area", [r"rectangle area"]),
    ],
    "game-theory": [("Optimal-Play / Nim-Style Game", [r".*"])],
    "greedy": [("Greedy Pairing / Rearrangement Inequality", [r".*"])],
    "network-flow": [("Max Flow / Min Cut", [r".*"])],
    "fft-ntt": [("Polynomial Convolution", [r".*"])],
}


def classify_technique(q):
    for sub, label in TECHNIQUE_OVERRIDES:
        if sub.lower() in q.lower():
            return label
    coarse = classify_dsa(q)
    if coarse == "unclassified":
        return "Unclassified (contest problem — see linked judge for exact technique)"
    ql = q.lower()
    for label, pats in TECHNIQUE_RULES.get(coarse, []):
        for p in pats:
            if re.search(p, ql):
                return label
    return f"General {DSA_SLUG_LABEL[coarse].split(' (')[0]} Problem"


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


UNCLASSIFIED_TECHNIQUE_LABEL = "Unclassified (contest problem — see linked judge for exact technique)"


def dsa_technique_counts(dsa_entries):
    return collections.Counter(classify_technique(e["q"]) for e in dsa_entries)


def dsa_company_top_techniques(dsa_entries, min_count=3, top_n=3):
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
        counts = collections.Counter(classify_technique(e["q"]) for e in items)
        top = [(s, k) for s, k in counts.most_common() if s != UNCLASSIFIED_TECHNIQUE_LABEL][:top_n]
        rows.append((c, n, top))
    rows.sort(key=lambda r: -r[1])
    return rows
