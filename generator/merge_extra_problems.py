import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from parse_cp_problems import parse_file

RAW_DIR = os.path.expanduser("~/quant-hft-interview-prep/raw-notes")
PROBLEMS_DIR = os.path.join(os.path.dirname(__file__), "problems")

# (subtopic keyword to match, case-insensitive substring) -> target topic slug
SUBTOPIC_TO_SLUG = [
    ("Difference Arrays", "arrays-strings"),
    ("Merge Intervals", "arrays-strings"),
    ("Monotonic Deque", "arrays-strings"),
    ("Two-Pointer Partitioning", "arrays-strings"),
    ("Custom Comparators", "sorting-searching"),
    ("Order Statistics", "sorting-searching"),
    ("Ternary Search", "sorting-searching"),
    ("2-SAT", "graphs"),
    ("0/1 BFS", "graphs"),
    ("Multi-Source BFS", "graphs"),
    ("Euler Path", "graphs"),
    ("Euler Circuit", "graphs"),
    ("Functional Graphs", "graphs"),
    ("Chinese Remainder", "number-theory"),
    ("Matrix Exponentiation", "number-theory"),
    ("Lucas", "number-theory"),
    ("Möbius", "number-theory"),
    ("Mobius", "number-theory"),
    ("Min-Cost Max-Flow", "network-flow"),
    ("Hungarian", "network-flow"),
    ("Linear Recurrences via Polynomials", "fft-ntt"),
    ("Divide and Conquer", "recursion-backtracking"),
    ("Minimax", "recursion-backtracking"),
    ("Huffman", "greedy"),
    ("Fractional vs", "greedy"),
    ("Bit Tricks", "bit-manipulation"),
    ("Bitset Optimization", "bit-manipulation"),
    ("Combinatorial Game Sums", "game-theory"),
    ("Suffix Automaton", "string-algorithms"),
    ("Aho-Corasick", "string-algorithms"),
    ("Palindromic Tree", "string-algorithms"),
    ("Small-to-Large", "trees"),
    ("Virtual Trees", "trees"),
    ("Tree Isomorphism", "trees"),
    ("Sqrt Decomposition", "data-structures"),
    ("Mo's Algorithm", "data-structures"),
    ("2D Fenwick", "data-structures"),
]

def classify(subtopic_text):
    for keyword, slug in SUBTOPIC_TO_SLUG:
        if keyword.lower() in subtopic_text.lower():
            return slug
    return None

EXTRA_FILES = [
    "cp-guide-arrays-sorting-extra.md",
    "cp-guide-graphs-extra.md",
    "cp-guide-numbertheory-flow-fft-extra.md",
    "cp-guide-recursion-greedy-bit-game-extra.md",
    "cp-guide-strings-extra.md",
    "cp-guide-trees-ds-extra.md",
]

by_slug = {}
unclassified = []
for fname in EXTRA_FILES:
    path = os.path.join(RAW_DIR, fname)
    entries = parse_file(path)
    for e in entries:
        slug = classify(e["subtopic"])
        if not slug:
            unclassified.append((fname, e["subtopic"], e["name"]))
            continue
        by_slug.setdefault(slug, []).append(e)

print("Entries per topic (new):")
total = 0
for slug, entries in sorted(by_slug.items()):
    print(f"  {slug:25s} {len(entries)}")
    total += len(entries)
print(f"TOTAL NEW: {total}")

if unclassified:
    print(f"\nUNCLASSIFIED ({len(unclassified)}):")
    for fname, sub, name in unclassified:
        print(f"  {fname} | subtopic={sub!r} | {name}")

# merge into existing per-topic problems/<slug>.json
for slug, new_entries in by_slug.items():
    path = os.path.join(PROBLEMS_DIR, f"{slug}.json")
    existing = json.load(open(path)) if os.path.exists(path) else []
    seen_names = {e["name"] for e in existing}
    added = 0
    for e in new_entries:
        if e["name"] in seen_names:
            continue
        existing.append(e)
        seen_names.add(e["name"])
        added += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=1)
    print(f"merged {added} new problems into {slug}.json (total now {len(existing)})")
