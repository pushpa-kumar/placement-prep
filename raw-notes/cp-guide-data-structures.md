# CP Guide: Data Structures (segment tree family, Fenwick, sparse table, DSU, trie, monotonic stack/queue, sqrt decomposition) — hard practice problems, CF rating 1700+ / LC Hard / CSES harder set

## Segment Tree

### New Year Tree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/620/E
- Difficulty: 2100
- Subtopic: Segment Tree (lazy propagation with bitmask trick)
- One-line description: On a rooted tree, repaint an entire subtree with a color or answer how many distinct colors appear in a subtree.
- Why it's a good hard problem: Requires flattening the tree with an Euler tour and running a segment tree whose lazy tag and node value are both bitmasks (colors packed into bits of a 64-bit int), a non-obvious lazy-propagation trick beyond plain range add/assign.

### Hotel Queries
- Judge: CSES
- Link: https://cses.fi/problemset/task/1143
- Difficulty: CSES (Range Queries, harder set)
- Subtopic: Segment Tree (descent / binary search on tree)
- One-line description: Given hotel room capacities, greedily assign each incoming group to the leftmost hotel that still has enough free rooms, and update capacity.
- Why it's a good hard problem: The query is not a plain range max/sum — it requires walking down a segment-tree-of-maxima to find the leftmost leaf satisfying a threshold, an important segment-tree pattern distinct from simple range queries.

## Persistent Segment Tree

### One Occurrence
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1000/F
- Difficulty: 2400
- Subtopic: Persistent Segment Tree
- One-line description: For each query range [l, r], report any element that appears in the range an odd number of times, guaranteed to be exactly once.
- Why it's a good hard problem: The standard solution builds a persistent segment tree (one version per array index) storing, at each position, the index of the previous occurrence of that value, then does a min-query descent per version to find a position in [l, r] whose previous occurrence lies before l — a canonical, non-trivial persistent-segment-tree application.

## Merge-sort Tree

### Count of Smaller Numbers After Self
- Judge: LeetCode
- Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/
- Difficulty: Hard
- Subtopic: Merge-sort Tree / offline order-statistics counting
- One-line description: For every index i, count how many elements to its right are strictly smaller than nums[i].
- Why it's a good hard problem: The textbook solution augments merge sort to count cross-inversions while merging (a "merge-sort tree" counting technique), an alternative to a coordinate-compressed Fenwick tree — good for contrasting the two approaches to the same order-statistics problem.

## Fenwick Tree / BIT

### Salary Queries
- Judge: CSES
- Link: https://cses.fi/problemset/task/1144
- Difficulty: CSES (Range Queries, harder set)
- Subtopic: Fenwick Tree / BIT (point update, range count with coordinate compression)
- One-line description: Support raising/lowering an employee's salary and counting how many employees currently have a salary within a given range.
- Why it's a good hard problem: Salaries must be coordinate-compressed first (values up to 1e9), then maintained in a Fenwick tree with point updates and prefix-count queries — a step up from a static range-sum BIT.

### Mishka and Interesting Sum
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/703/D
- Difficulty: 2100
- Subtopic: Fenwick Tree / BIT (offline queries)
- One-line description: For each range [l, r], compute the XOR of all values that occur an even number of times within that range.
- Why it's a good hard problem: Needs the identity (XOR of all elements in range) XOR (XOR of distinct elements in range) = XOR of even-occurrence elements, where the distinct-XOR part is computed offline with a Fenwick tree using a last-occurrence trick — a clever, non-obvious offline BIT pattern.

## Sparse Table

### Friends and Subsequences
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/689/D
- Difficulty: 2100
- Subtopic: Sparse Table (RMQ)
- One-line description: Given two arrays a and b, for each query [l, r] count the number of subsegments of [l, r] where the maximum of a equals the minimum of b.
- Why it's a good hard problem: Relies on O(1) range max/min via sparse tables plus the monotonicity of max(a) and min(b) as the window grows, exploited with a two-pointer/binary-search sweep — a real fusion of sparse-table RMQ with a non-trivial counting argument.

## DSU / Union-Find

### Envy
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/891/C
- Difficulty: 2300
- Subtopic: DSU / Union-Find (offline, grouped by weight)
- One-line description: Given a weighted graph, answer multiple queries each asking whether a specified subset of edges can simultaneously belong to some minimum spanning tree.
- Why it's a good hard problem: Requires the cycle property of MSTs plus an offline DSU that resets/rebuilds per distinct edge weight across queries sorted appropriately — a genuinely tricky, non-standard use of union-find beyond basic connectivity.

## Trie

### Word Search II
- Judge: LeetCode
- Link: https://leetcode.com/problems/word-search-ii/
- Difficulty: Hard
- Subtopic: Trie + backtracking
- One-line description: Given a 2D board of letters and a dictionary of words, find all dictionary words that can be formed by a path of adjacent cells.
- Why it's a good hard problem: Naive per-word DFS is too slow; the intended solution merges all dictionary words into a single trie and prunes the board DFS using trie nodes, requiring careful backtracking and duplicate-avoidance.

### Vasiliy's Multiset
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/706/D
- Difficulty: 1800
- Subtopic: Trie (binary/XOR trie)
- One-line description: Maintain a multiset of integers supporting insertion, deletion, and "find the maximum XOR of x with any element currently in the multiset."
- Why it's a good hard problem: Requires a bitwise (binary) trie over ~30-bit representations with per-node counts to support deletion, plus a greedy bit-by-bit descent to maximize XOR — the canonical binary-trie technique, distinct from string tries.

## Monotonic Stack / Queue

### Sliding Window Maximum
- Judge: LeetCode
- Link: https://leetcode.com/problems/sliding-window-maximum/
- Difficulty: Hard
- Subtopic: Monotonic Queue
- One-line description: Given an array and a sliding window of size k, output the maximum value in the window at every position as it slides.
- Why it's a good hard problem: The O(n) solution needs a monotonic deque that keeps candidate maxima in decreasing order and evicts indices that fall out of the window — the standard monotonic-queue pattern, easy to get wrong on eviction order and index bookkeeping.

## Sqrt Decomposition

### GukiZ and GukiZiana
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/551/E
- Difficulty: 2500
- Subtopic: Sqrt Decomposition
- One-line description: On an array, support "add a value to every element in a range" and "find the leftmost/rightmost index whose value equals v" queries.
- Why it's a good hard problem: Classic block decomposition where each block keeps a sorted copy of its elements plus a pending lazy add, so value-lookup queries binary-search within blocks while range updates touch full blocks in O(1) and partial blocks by rebuilding — a canonical, tightly-tuned sqrt-decomposition design.
