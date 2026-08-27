# CP Guide — Extra Hard Problems: Trees & Data Structures Subtopics

Scope: 6 new subtopics not already covered by the existing Trees page (traversals/Euler tour, LCA/binary lifting, diameter, HLD, centroid decomposition) or Data Structures page (segment tree incl. persistent, Fenwick, sparse table, DSU, trie, monotonic stack/queue). All problems below were verified for existence and rating via the Codeforces public API (`problemset.problems`), direct CSES task pages, or the LeetCode public problem-list API — none invented.

## Small-to-Large Merging (DSU on Tree / Sack technique)

### Lomsat gelral
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/600/E
- Difficulty: CF rating 2300
- Subtopic: Small-to-Large Merging
- One-line description: Rooted tree with a color per vertex; for every vertex output the sum of all colors that are "dominant" (most frequent) in its subtree.
- Why it's a good hard problem: The canonical introductory problem for the technique — naive per-vertex counting is O(n^2), and small-to-large merging of child color-count maps gets it to O(n log n).

### Dominant Indices
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1009/F
- Difficulty: CF rating 2300
- Subtopic: Small-to-Large Merging
- One-line description: For each vertex of a rooted tree, find the depth (relative to that vertex) that contains the most vertices in its subtree, breaking ties by smallest depth.
- Why it's a good hard problem: Requires merging depth-count arrays across children — the classic setting where "small-to-large" beats naive array merging, since arrays being merged can be swapped/pointer-merged instead of copied.

### GCD Counting
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1101/D
- Difficulty: CF rating 2000
- Subtopic: Small-to-Large Merging
- One-line description: Given a tree with a number on each vertex, find the length of the longest path whose vertices share a GCD greater than 1, for every prime factor.
- Why it's a good hard problem: Combines small-to-large merging of per-prime depth information with tree DP; a good example of merging non-trivial per-vertex maps rather than simple counters. (Mirrored at CF 990G, rating 2400.)

### Graph and Queries
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1416/D
- Difficulty: CF rating 2600
- Subtopic: Small-to-Large Merging
- One-line description: Process edge-deletion and "find-and-zero-out-max-in-component" queries offline by reversing time (edge additions) and merging component data with a DSU where the smaller structure (e.g. an ordered set) is always merged into the larger.
- Why it's a good hard problem: Shows small-to-large merging generalized beyond trees — merging balanced BSTs/sets across DSU components in reverse-time processing, a step up from the standard subtree-only setting.

## Virtual Trees (Auxiliary Tree Technique)

### Kingdom and its Cities
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/613/D
- Difficulty: CF rating 2800
- Subtopic: Virtual Trees (Auxiliary Tree)
- One-line description: Given a tree and repeated small subsets of "capital" vertices, find the minimum number of vertices to block so that no capital can reach any other capital, using only vertices near the given subset.
- Why it's a good hard problem: The textbook auxiliary-tree problem — building the virtual tree (via LCA-closure) of only the queried vertices each time is what makes the total work near-linear in the sum of query sizes instead of O(n) per query.

### Tourism
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1220/E
- Difficulty: CF rating 2200
- Subtopic: Virtual Trees (Auxiliary Tree)
- One-line description: On a graph built from a tree with extra "back" edges forming simple cycles, compute for every vertex the maximum total vertex weight reachable via a walk that never repeats a road consecutively.
- Why it's a good hard problem: Requires condensing cycles and building auxiliary/virtual-tree-style structures over a reduced vertex set to make an otherwise quadratic DP tractable.

### Partial Virtual Trees
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1707/D
- Difficulty: CF rating 3000
- Subtopic: Virtual Trees (Auxiliary Tree)
- One-line description: Count, for every k, the number of ways to repeatedly shrink a vertex set to a proper "partial virtual tree" (an LCA-closed subset) exactly k times until only the root remains.
- Why it's a good hard problem: The problem statement literally defines the auxiliary/virtual tree closure property (LCA-closed subsets) and turns counting over that structure into a combinatorics + tree-DP exercise, making it an unusually direct test of understanding the technique's core definition.

## Tree Isomorphism / Canonical Form

### Tree Isomorphism I
- Judge: CSES
- Link: https://cses.fi/problemset/task/1700
- Difficulty: CSES (Tree Algorithms section)
- Subtopic: Tree Isomorphism / Canonical Form
- One-line description: Given several pairs of rooted trees, determine for each pair whether the two rooted trees are isomorphic.
- Why it's a good hard problem: The direct introduction to canonical-form hashing (AHU algorithm) — recursively computing a sorted-children canonical label per subtree and comparing root labels.

### Tree Isomorphism II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1701
- Difficulty: CSES (Tree Algorithms section)
- Subtopic: Tree Isomorphism / Canonical Form
- One-line description: Same as Tree Isomorphism I, but the input trees are unrooted, so a canonical root (e.g. centroid) must be chosen before canonical-form hashing applies.
- Why it's a good hard problem: Forces the extra insight that unrooted-tree isomorphism needs a canonical rooting (via centroid, since a tree has at most 2 centroids) before AHU-style hashing is even well-defined.

### Symmetree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1800/G
- Difficulty: CF rating 2200
- Subtopic: Tree Isomorphism / Canonical Form
- One-line description: Determine whether a rooted tree can have its children reordered at every vertex so that it becomes a mirror-symmetric tree.
- Why it's a good hard problem: A disguised isomorphism check — a subtree is "symmetric" iff it is isomorphic to its own mirror image, so it directly tests canonical-form hashing plus matching canonical forms in pairs among siblings.

### Regular Forestation
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1252/F
- Difficulty: CF rating 2400
- Subtopic: Tree Isomorphism / Canonical Form
- One-line description: Find a vertex whose removal splits a tree into two or more pairwise-isomorphic ("identical") subtrees, and report the maximum possible number of pieces.
- Why it's a good hard problem: The problem statement explicitly defines tree isomorphism via a bijection preserving adjacency, then requires efficiently comparing many candidate subtrees for isomorphism using canonical hashing rather than brute-force bijection search.

## Sqrt Decomposition

### Anton and Permutation
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/785/E
- Difficulty: CF rating 2200
- Subtopic: Sqrt Decomposition
- One-line description: Maintain a permutation under repeated element swaps, reporting the number of inversions after each swap.
- Why it's a good hard problem: The classic sqrt-decomposition-of-a-permutation problem — split the array into O(sqrt n) blocks and maintain per-block sortedness so each swap/query costs O(sqrt n).

### Serega and Fun
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/455/D
- Difficulty: CF rating 2700
- Subtopic: Sqrt Decomposition
- One-line description: Support cyclic-shift updates on a subarray and count occurrences of a value in a subarray, on an array of up to 10^5 elements with up to 10^5 queries.
- Why it's a good hard problem: A canonical block-decomposition-with-deques problem — each block holds its elements in a deque plus a frequency map so shifts and counts are both handled in O(sqrt n).

### Holes
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/13/E
- Difficulty: CF rating 2700
- Subtopic: Sqrt Decomposition
- One-line description: Each position on a line has a "power" that launches a ball forward by that amount; support updating a position's power and querying how many jumps and how far a ball launched from a position travels before leaving the row.
- Why it's a good hard problem: The original teaching example for sqrt decomposition with block "jump pointers" that are lazily recomputed only for the block containing an update, making updates and queries both O(sqrt n).

### Yet Another Array Queries Problem
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/863/D
- Difficulty: CF rating 1800
- Subtopic: Sqrt Decomposition
- One-line description: Apply a mix of cyclic-shift and reversal operations to subarray segments, then report the final value at several queried indices.
- Why it's a good hard problem: Solved offline by sqrt-decomposing time into blocks of sqrt(q) operations and simulating within each block, a less common but instructive "decompose the query sequence" variant of the technique.

### Falling Squares
- Judge: LeetCode
- Link: https://leetcode.com/problems/falling-squares/
- Difficulty: LeetCode Hard
- Subtopic: Sqrt Decomposition
- One-line description: Drop axis-aligned squares one at a time onto the x-axis (they stack on whatever is beneath them) and report the tallest stack height after each drop.
- Why it's a good hard problem: With coordinates compressed, maintaining per-block maximum height over an array of O(n) compressed positions with range-max-query/range-update is a natural sqrt-decomposition exercise as an alternative to a segment tree.

## Mo's Algorithm

### Powerful array
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/86/D
- Difficulty: CF rating 2200
- Subtopic: Mo's Algorithm
- One-line description: For repeated subarray range queries, compute the sum over all distinct values v of (count of v in the range)^2 * v.
- Why it's a good hard problem: The single most-cited introductory Mo's algorithm problem — add/remove-element transitions are O(1) with a frequency array, so sqrt-block query reordering is exactly what makes it feasible.

### XOR and Favorite Number
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/617/E
- Difficulty: CF rating 2200
- Subtopic: Mo's Algorithm
- One-line description: For repeated range queries, count the number of subarray pairs (i, j) within the range whose XOR of elements equals a fixed favorite number k.
- Why it's a good hard problem: Requires transforming the condition into a prefix-XOR frequency count first, then applying Mo's algorithm on top — a good test of recognizing when a problem reduces to a Mo's-friendly form.

### Machine Learning
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/940/F
- Difficulty: CF rating 2600
- Subtopic: Mo's Algorithm
- One-line description: Support point updates to an array along with range queries asking for the Mex of the multiset of frequencies of values appearing in the range.
- Why it's a good hard problem: A classic "Mo's algorithm with updates" (3D Mo's) problem — queries are sorted by block of l, block of r, and time, adding a third dimension to the usual technique.

### Tree and Queries
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/375/D
- Difficulty: CF rating 2400
- Subtopic: Mo's Algorithm
- One-line description: Given a rooted, vertex-colored tree, answer queries asking how many colors occur at least k times in the subtree of a given vertex.
- Why it's a good hard problem: Shows Mo's algorithm applied to a tree by flattening a subtree into a contiguous Euler-tour range, then running standard Mo's over that range — a nice bridge between the trees and Mo's-algorithm subtopics.

### Distinct Values Queries
- Judge: CSES
- Link: https://cses.fi/problemset/task/1734
- Difficulty: CSES (Range Queries section)
- Subtopic: Mo's Algorithm
- One-line description: Answer offline queries asking for the number of distinct values in a given subarray range.
- Why it's a good hard problem: The most standard possible Mo's-algorithm target (distinct-count with O(1) add/remove) and a good baseline before tackling the harder XOR/Mex variants above.

## 2D Fenwick Tree / 2D Range Queries

### Forest Queries II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1739
- Difficulty: CSES (Advanced Techniques section)
- Subtopic: 2D Fenwick Tree / 2D Range Queries
- One-line description: On an n x n grid of trees, support toggling whether a cell has a tree and querying the number of trees inside an axis-aligned rectangle.
- Why it's a good hard problem: The direct CSES introduction to a 2D Fenwick (Binary Indexed) Tree, requiring the nested-BIT-of-BITs structure for point update / rectangle sum.

### The Untended Antiquity
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/869/E
- Difficulty: CF rating 2400
- Subtopic: 2D Fenwick Tree / 2D Range Queries
- One-line description: On a grid, support adding/removing rectangular barriers and querying whether one point can be enclosed and thus separated from another by the currently placed barriers.
- Why it's a good hard problem: Reduces rectangle-containment queries to 2D range updates/point queries handled via a 2D Fenwick tree (using the standard 2D difference trick), combined with a segment tree over one dimension — a strong test of composing 2D BIT ideas with other structures.

### Iahub and Xors
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/341/D
- Difficulty: CF rating 2500
- Subtopic: 2D Fenwick Tree / 2D Range Queries
- One-line description: Support 2D rectangle-XOR updates and 2D rectangle-XOR queries on an n x n matrix, both online.
- Why it's a good hard problem: Requires generalizing the 1D difference-array-plus-Fenwick-tree trick to two dimensions using four 2D BITs (analogous to the 1D range-update range-query trick), a genuinely non-obvious extension.

### Ball
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/12/D
- Difficulty: CF rating 2400
- Subtopic: 2D Fenwick Tree / 2D Range Queries
- One-line description: Given n people each with three attributes, count how many people are dominated (strictly worse) in all three attributes by at least one other person.
- Why it's a good hard problem: The classic "3D dominance counting" problem — sort by one dimension, sweep, and use a 2D Fenwick tree (or Fenwick tree over compressed second coordinate) to answer 2D dominance counts online, a staple pattern for offline dominance/partial-order problems.
