# Recursion & Backtracking — Curated Hard Practice Problems

### Maximum Subsequence
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/888/E
- Difficulty: CF 1800
- Subtopic: meet in the middle (subset sums)
- One-line description: Given an array (n ≤ 35) and modulus m, choose a subsequence maximizing the sum of its elements modulo m.
- Why it's a good hard problem: n rules out 2^n brute force, so you must recurse over two halves separately to generate all subset sums, sort one half, and combine the two sorted lists with a two-pointer/binary-search sweep to find the optimal pairing mod m.

### Anya and Cubes
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/525/E
- Difficulty: CF 2100
- Subtopic: meet in the middle (subset sum with a twist operation)
- One-line description: Given n numbers (n ≤ 25) and a target sum S, count subsets where you may additionally replace up to k of the chosen numbers with their factorial, such that the resulting sum equals S.
- Why it's a good hard problem: The extra "apply factorial to ≤k picks" dimension means each half's recursive enumeration must track (subset sum, count of factorials used) pairs, and the merge step needs a hashmap keyed on remaining factorial budget rather than a simple two-pointer join.

### Lizard Era: Beginning
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/585/D
- Difficulty: CF 2300
- Subtopic: meet in the middle (3-way partition)
- One-line description: Split n scientists (n ≤ 24) among 3 research groups to minimize a pairwise dissatisfaction cost that depends on which groups two scientists end up in.
- Why it's a good hard problem: Ternary (not binary) choices per element push brute force to 3^n; you must recursively enumerate all 3^(n/2) assignments on each half, precompute partial costs, and combine the two halves' best completions — a genuine step up in meet-in-the-middle bookkeeping.

### Chessboard and Queens
- Judge: CSES
- Link: https://cses.fi/problemset/task/1624
- Difficulty: CSES (Introductory Problems, high end)
- Subtopic: N-Queens style pruning
- One-line description: Count the ways to place 8 non-attacking queens on an 8×8 board where some squares are reserved and unusable.
- Why it's a good hard problem: The reserved-square constraint means you can't use a closed-form queens count — you need real row-by-row backtracking with column/diagonal attack-set pruning, making it the canonical first "write actual N-Queens backtracking" exercise.

### Creating Strings
- Judge: CSES
- Link: https://cses.fi/problemset/task/1622
- Difficulty: CSES (Introductory Problems, high end)
- Subtopic: permutation generation with duplicate pruning
- One-line description: Given a string of up to 8 letters (possibly with repeats), generate every distinct permutation of its characters exactly once, in sorted order.
- Why it's a good hard problem: Naively permuting and deduplicating with a set wastes time and memory; the real challenge is backtracking directly over sorted character counts and skipping repeated branches so duplicate permutations are never generated in the first place.

### Apple Division
- Judge: CSES
- Link: https://cses.fi/problemset/task/1623
- Difficulty: CSES (Introductory Problems, high end)
- Subtopic: recursive subset enumeration / meet in the middle
- One-line description: Divide n ≤ 20 apples (with large integer weights) into two groups minimizing the absolute difference of the groups' total weights.
- Why it's a good hard problem: With n up to 20 and weights up to 1e9, there's no DP-on-sum shortcut; you must recursively enumerate all 2^20 subset assignments (with pruning/early termination) rather than iterate, making it a clean introduction to exponential backtracking search with a real complexity ceiling.

### N-Queens
- Judge: LeetCode
- Link: https://leetcode.com/problems/n-queens/
- Difficulty: Hard
- Subtopic: N-Queens style pruning
- One-line description: Return all distinct board configurations for placing n non-attacking queens on an n×n chessboard.
- Why it's a good hard problem: The reference "canonical" backtracking problem — solving it efficiently (not just correctly) requires maintaining column/diagonal/anti-diagonal occupancy sets so each placement attempt is checked and pruned in O(1) rather than rescanning the board.

### Sudoku Solver
- Judge: LeetCode
- Link: https://leetcode.com/problems/sudoku-solver/
- Difficulty: Hard
- Subtopic: constraint-propagation backtracking
- One-line description: Fill a partially completed 9×9 Sudoku board so every row, column, and 3×3 box contains 1-9 exactly once.
- Why it's a good hard problem: A naive cell-by-cell backtracking search is technically correct but can blow up; a genuinely fast solution needs candidate-set pruning and picking the most-constrained empty cell first, which is where most incorrect/slow submissions fail.
