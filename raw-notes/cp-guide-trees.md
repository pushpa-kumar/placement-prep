# CP Guide — Tree Algorithms (hard practice problems, CF 1700+/LC Hard/CSES harder variants)

## LCA/Binary Lifting

### Kth Ancestor of a Tree Node
- Judge: LeetCode
- Link: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
- Difficulty: LeetCode Hard
- Subtopic: LCA/Binary Lifting
- One-line description: Preprocess a rooted tree so that many "what is the kth ancestor of node u" queries can each be answered quickly.
- Why it's a good hard problem: Climbing ancestor-by-ancestor per query is too slow at the given constraints, forcing the binary lifting sparse-ancestor-table technique (O(n log n) preprocessing, O(log n) per query).

### Fools and Roads
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/191/C
- Difficulty: CF 1900
- Subtopic: LCA/Binary Lifting
- One-line description: Given many simple paths marked on a tree, compute how many times each edge of the tree is used across all the marked paths.
- Why it's a good hard problem: Each path must be split at its LCA into two upward paths, applied as point updates that are only resolved into per-edge counts via a subsequent subtree-sum (difference-array) DFS — a two-step technique built on top of LCA.

## Euler Tour

### Distinct Colors
- Judge: CSES
- Link: https://cses.fi/problemset/task/1139
- Difficulty: CSES (Tree Algorithms section)
- Subtopic: Euler Tour
- One-line description: Each node of a tree has a color; for every node, count the number of distinct colors among the nodes in its subtree.
- Why it's a good hard problem: A naive per-node subtree scan is O(n^2); an efficient solution needs either small-to-large merging of subtree sets or an Euler-tour-based offline reduction (e.g., Mo's algorithm on the tour), both nontrivial.

### Vasya and a Tree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1076/E
- Difficulty: CF 1900
- Subtopic: Euler Tour
- One-line description: Process offline update queries that each add a value to every vertex within a bounded depth inside the subtree of a given vertex, then report the final value at every vertex.
- Why it's a good hard problem: "Subtree AND bounded depth" must be encoded via Euler tour entry/exit times combined with a per-depth difference-array trick, a step beyond the standard single-dimension Euler tour + Fenwick tree pattern.

## Tree Diameter

### Minimal Diameter Forest
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1092/E
- Difficulty: CF 2000
- Subtopic: Tree Diameter
- One-line description: Given a forest consisting of exactly two trees, add a single edge connecting them so that the diameter of the resulting combined tree is minimized.
- Why it's a good hard problem: Requires knowing that the optimal connection point in each tree is its center (not an arbitrary node) and deriving the resulting diameter from both trees' original diameters — well beyond a plain double-BFS diameter computation.

## HLD

### Path Queries II
- Judge: CSES
- Link: https://cses.fi/problemset/task/2134
- Difficulty: CSES (Tree Algorithms section, hard version)
- Subtopic: HLD (Heavy-Light Decomposition)
- One-line description: Support point-update and maximum-value-on-path queries between two arbitrary nodes of a tree.
- Why it's a good hard problem: Arbitrary node-to-node path queries (not just root-to-node or subtree queries) on a general tree require heavy-light decomposition to break each path into O(log n) contiguous segment-tree ranges.

## Centroid Decomposition

### Fixed-Length Paths II
- Judge: CSES
- Link: https://cses.fi/problemset/task/2081
- Difficulty: CSES (Tree Algorithms section, hard version)
- Subtopic: Centroid Decomposition
- One-line description: Count the number of paths in a tree whose length lies within a given range [a, b].
- Why it's a good hard problem: Requires full centroid decomposition to enumerate, for every centroid, all paths passing through it in aggregate O(n log n) time, plus careful inclusion-exclusion to avoid double-counting paths through the same centroid.

### Xenia and Tree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/342/E
- Difficulty: CF 2400
- Subtopic: Centroid Decomposition
- One-line description: Support two online operations on a tree: repaint a given vertex blue, and query the minimum distance from a given vertex to the nearest currently-blue vertex.
- Why it's a good hard problem: It is the canonical online centroid-decomposition problem — nearest-marked-vertex queries must be answered by maintaining auxiliary minimum-distance data at every level of the centroid decomposition tree, updated online after every repaint.
