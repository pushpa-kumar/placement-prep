# Arrays & Strings — hard practice problems (two pointers, sliding window, prefix sums, Kadane variants, 2D prefix sums)

### Petya and Array
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1042/D
- Difficulty: 1800
- Subtopic: prefix sums + counting (Fenwick tree)
- One-line description: Count the number of subarrays of an array (which may contain negative numbers) whose sum is strictly less than a given t.
- Why it's a good hard problem: Negative elements break plain two-pointer/sliding-window counting, forcing the prefix-sum-plus-Fenwick-tree trick (count pairs of prefix sums within a range) — the standard escape hatch when two pointers fail.

### Close Tuples (hard version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1462/E2
- Difficulty: 1700
- Subtopic: two pointers + combinatorial counting
- One-line description: Count the number of size-m subsequences of an array such that the difference between the maximum and minimum element in the subsequence is at most k.
- Why it's a good hard problem: Requires sorting, then a two-pointer sliding window to bound each candidate "maximum" element's valid range, combined with nCr combinatorics to count subsequences per window — a clean fusion of two pointers with counting rather than plain search.

### OpenStreetMap
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1195/E
- Difficulty: 2100
- Subtopic: 2D sliding window minimum (monotonic deque)
- One-line description: Given an n×m grid, compute the minimum element of every k×k submatrix and sum all these minima.
- Why it's a good hard problem: Naive per-submatrix scanning is too slow; it requires chaining a 1D sliding-window-minimum (monotonic deque) pass over rows and then over columns — a genuinely hard monotonic-structure sliding-window problem in 2D.

### Subarray Sums II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1661
- Difficulty: CSES
- Subtopic: prefix sums + hashmap counting
- One-line description: Count the number of subarrays (of an array that may contain negative or zero values) with sum exactly equal to a given x.
- Why it's a good hard problem: Unlike the "easy" version restricted to non-negative values (solvable with a simple two-pointer window), negative values invalidate the sliding-window monotonicity, forcing a prefix-sum + hashmap-of-counts approach.

### Maximum Subarray Sum II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1644
- Difficulty: CSES
- Subtopic: Kadane variant with length constraint (prefix sums + segment tree/deque)
- One-line description: Find the maximum possible sum of a subarray whose length is between two given bounds a and b.
- Why it's a good hard problem: Plain Kadane's algorithm doesn't enforce a length window, so this needs prefix sums combined with a sliding-window-of-minimums structure (segment tree or monotonic deque) over the valid range of earlier prefix indices — a substantially harder Kadane variant.

### Sliding Window Maximum
- Judge: LeetCode
- Link: https://leetcode.com/problems/sliding-window-maximum/
- Difficulty: Hard
- Subtopic: sliding window with monotonic deque
- One-line description: Given an array and a window size k, return the maximum value in every contiguous window of size k as it slides across the array.
- Why it's a good hard problem: The naive approach is O(nk); achieving O(n) requires maintaining a monotonic decreasing deque of indices, the canonical hard-sliding-window-with-monotonic-structure technique.

### Shortest Subarray with Sum at Least K
- Judge: LeetCode
- Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
- Difficulty: Hard
- Subtopic: prefix sums + monotonic deque
- One-line description: Given an integer array (possibly containing negative numbers) and integer K, find the length of the shortest contiguous subarray with sum at least K, or -1 if none exists.
- Why it's a good hard problem: Negative numbers break simple two-pointer/Kadane approaches, so the intended solution keeps a monotonic increasing deque of prefix-sum indices and pops/pushes carefully — a non-obvious combination of prefix sums with a monotonic-deque sliding window.

### Number of Submatrices That Sum to Target
- Judge: LeetCode
- Link: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
- Difficulty: Hard
- Subtopic: 2D prefix sums + hashmap
- One-line description: Given a 2D matrix and an integer target, count the number of non-empty submatrices whose element sum equals target.
- Why it's a good hard problem: Requires reducing the 2D problem to repeated 1D "subarray sum equals k" counting (via row-pair compression using 2D prefix sums) combined with hashmap counting — a genuine 2D-prefix-sum-and-difference-array-style trick, not a toy application.
