# Core Dynamic Programming — Hard Practice Problems (CF 1700+/1900-2400 preferred, LeetCode Medium-Hard/Hard, CSES harder-section picks)

## Linear/1D DP

### A Simple Task
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/11/D
- Difficulty: CF 2200
- Subtopic: Linear/1D DP
- One-line description: Count the total number of simple cycles (no repeated vertices/edges) in an undirected graph with n <= 19 vertices.
- Why it's a good hard problem: Requires bitmask DP over (current vertex set, current endpoint) with careful overcounting correction to avoid double-counting each cycle in both directions and from every starting vertex.

### Elongated Matrix
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1102/F
- Difficulty: CF 2000
- Subtopic: Linear/1D DP
- One-line description: Reorder the n <= 16 rows of an n x m matrix (traversed column-by-column) to maximize the minimum absolute difference between consecutive visited values.
- Why it's a good hard problem: Combines binary search on the answer with bitmask DP over row permutations, a classic "clever state compression" pattern (TSP-style transition costs between rows).

### Increasing Subsequence II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1748
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: Linear/1D DP
- One-line description: Count the number of strictly increasing subsequences of an array, counting subsequences with equal values at different positions separately.
- Why it's a good hard problem: A genuine LIS-family generalization — moves from "find the longest" to "count all," requiring a Fenwick tree over compressed values to sum DP contributions in O(n log n).

### Russian Doll Envelopes
- Judge: LeetCode
- Link: https://leetcode.com/problems/russian-doll-envelopes/
- Difficulty: LeetCode Hard
- Subtopic: Linear/1D DP
- One-line description: Given (width, height) envelope pairs, find the maximum number that can be nested inside each other (both dimensions must strictly increase).
- Why it's a good hard problem: A 2D LIS in disguise — needs a sort-then-LIS reduction (with a subtlety in tie-breaking on the sort key) to hit O(n log n).

### Maximum Profit in Job Scheduling
- Judge: LeetCode
- Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
- Difficulty: LeetCode Hard
- Subtopic: Linear/1D DP
- One-line description: Given jobs with start time, end time, and profit, schedule a non-overlapping subset that maximizes total profit.
- Why it's a good hard problem: Classic weighted interval scheduling DP that requires sorting by end time plus binary search for the last compatible job to reach an efficient solution.

### Super Egg Drop
- Judge: LeetCode
- Link: https://leetcode.com/problems/super-egg-drop/
- Difficulty: LeetCode Hard
- Subtopic: Linear/1D DP
- One-line description: With k eggs and n floors, find the minimum number of egg-drop trials in the worst case to determine the critical floor.
- Why it's a good hard problem: The naive DP is O(kn^2); the intended solution flips the DP state to "moves needed to distinguish m floors with k eggs," an unintuitive reformulation that gets it to O(kn) or O(k log n).

## 2D Grid DP

### The least round way
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/2/B
- Difficulty: CF 2000
- Subtopic: 2D Grid DP
- One-line description: Find a top-left to bottom-right path (moving only right/down) through an n x n matrix that minimizes the number of trailing zeros in the product of visited cells, and output the path.
- Why it's a good hard problem: Trailing zeros depend on min(count of factor 2, count of factor 5) along the path, forcing a two-state grid DP plus special-case handling whenever the path is forced through a zero cell.

### Grid Paths I
- Judge: CSES
- Link: https://cses.fi/problemset/task/1638
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: 2D Grid DP
- One-line description: Count the number of paths (moving only right/down) from the top-left to bottom-right of an n x n grid (n up to 1000) that avoid trap cells, modulo 1e9+7.
- Why it's a good hard problem: Straightforward recurrence but at n=1000 requires an efficient O(n^2) implementation with careful obstacle handling, a step up from the introductory grid-path DP.

### Dungeon Game
- Judge: LeetCode
- Link: https://leetcode.com/problems/dungeon-game/
- Difficulty: LeetCode Hard
- Subtopic: 2D Grid DP
- One-line description: A knight must traverse a grid of damage/heal values from top-left to bottom-right; find the minimum starting health needed so health never drops to zero.
- Why it's a good hard problem: The DP must be computed backward from the destination because the natural forward state (max health so far) is not well-defined — a classic "reverse the direction of the DP" trick.

### Unique Paths III
- Judge: LeetCode
- Link: https://leetcode.com/problems/unique-paths-iii/
- Difficulty: LeetCode Hard
- Subtopic: 2D Grid DP
- One-line description: Count the number of paths from a start to an end square in a grid with obstacles that visit every non-obstacle square exactly once.
- Why it's a good hard problem: Requires Hamiltonian-path counting rather than simple monotone-path DP, typically solved with bitmask-augmented backtracking/DP over visited cells since paths can move in all four directions.

### Cherry Pickup
- Judge: LeetCode
- Link: https://leetcode.com/problems/cherry-pickup/
- Difficulty: LeetCode Hard
- Subtopic: 2D Grid DP
- One-line description: Starting from the top-left of a grid with cherries and obstacles, go to the bottom-right and back to the top-left, collecting the maximum cherries (each cell's cherry collected only once).
- Why it's a good hard problem: The round trip is modeled as two agents walking forward simultaneously, requiring a 3D state (two positions constrained to the same step count) instead of a naive two-pass DP.

### Cherry Pickup II
- Judge: LeetCode
- Link: https://leetcode.com/problems/cherry-pickup-ii/
- Difficulty: LeetCode Hard
- Subtopic: 2D Grid DP
- One-line description: Two robots start at the top corners of a grid and move downward simultaneously, collecting the maximum total cherries, sharing cells but each counted once.
- Why it's a good hard problem: A genuine multi-agent grid DP — state is (row, col1, col2), and transitions must handle the case where both robots land on the same cell.

## Knapsack family

### Round Subset
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/837/D
- Difficulty: CF 2100
- Subtopic: Knapsack family
- One-line description: Choose exactly k numbers from a list of n (n <= 200) to maximize the number of trailing zeros in their product.
- Why it's a good hard problem: A genuinely multi-dimensional knapsack — state is (items chosen, total factors of 5), tracking the best achievable count of factors of 2 for each state, since trailing zeros are min(#2s, #5s).

### Knapsack
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1132/E
- Difficulty: CF 2300
- Subtopic: Knapsack family
- One-line description: With 8 item weight-classes (1..8), each available in a huge bounded quantity, and a knapsack capacity up to 1e18, find the maximum total weight that fits.
- Why it's a good hard problem: Astronomical capacity and counts rule out a direct DP table; it forces recognizing that only a small residue/threshold region needs real DP while the rest is handled by bounded-copy reasoning.

### Two Sets II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1093
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: Knapsack family
- One-line description: Count the number of ways to partition {1, ..., n} into two sets with equal sum.
- Why it's a good hard problem: A subset-sum counting knapsack where the target sum and array size both scale with n, requiring care with the modulus and the sum/2 target derivation.

### Elevator Rides
- Judge: CSES
- Link: https://cses.fi/problemset/task/1653
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: Knapsack family
- One-line description: Given n people (n <= 20) with weights and an elevator weight limit, find the minimum number of elevator rides needed to move everyone up.
- Why it's a good hard problem: This is bin-packing dressed as knapsack — the standard solution is a bitmask DP over subsets tracking (rides used, current ride's remaining capacity), an NP-hard-flavored problem tamed only by the small n.

### Profitable Schemes
- Judge: LeetCode
- Link: https://leetcode.com/problems/profitable-schemes/
- Difficulty: LeetCode Hard
- Subtopic: Knapsack family
- One-line description: Choose a subset of crimes (each with a member cost and a profit) using at most n members total that yields profit at least minProfit; count the number of such schemes.
- Why it's a good hard problem: A 2D bounded knapsack (members used x profit achieved) where profit must be capped/clamped at minProfit to keep the state space polynomial.

### Tallest Billboard
- Judge: LeetCode
- Link: https://leetcode.com/problems/tallest-billboard/
- Difficulty: LeetCode Hard
- Subtopic: Knapsack family
- One-line description: Given steel rod lengths, split them into two groups (welded end-to-end) whose totals are equal, maximizing that common total.
- Why it's a good hard problem: The natural knapsack state isn't a target sum but the running difference between the two sides, requiring a hash-map-indexed DP keyed by signed height difference.

## Interval DP

### Coloring Brackets
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/149/D
- Difficulty: CF 1900
- Subtopic: Interval DP
- One-line description: Given a valid bracket sequence, count the ways to color each character red/blue/uncolored so that exactly one bracket of each matched pair is colored and no two adjacent characters share a color.
- Why it's a good hard problem: Classic interval DP over matched bracket ranges with an extra boundary-color dimension in the state to enforce the adjacency constraint across sub-interval joins.

### Zuma
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/607/B
- Difficulty: CF 1900
- Subtopic: Interval DP
- One-line description: Given a sequence of colored gems (n <= 500), remove contiguous palindromic substrings one at a time to clear the whole sequence in as few operations as possible.
- Why it's a good hard problem: The transition must consider merging a middle segment's removal with matching endpoints, an interval DP recurrence subtler than plain palindrome partitioning (dp[i][j] depends on dp over interior splits plus matched-endpoint cases).

### Removal Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/1097
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: Interval DP
- One-line description: Two players alternately remove the first or last number of a list, each maximizing their own score; compute the first player's optimal score.
- Why it's a good hard problem: A minimax interval game DP — dp[i][j] must reason about the opponent's optimal response, not just a single maximizer, which is a genuinely different flavor from standard interval optimization.

### Rectangle Cutting
- Judge: CSES
- Link: https://cses.fi/problemset/task/1744
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: Interval DP
- One-line description: Given an a x b rectangle, repeatedly cut a rectangle into two integer-sided rectangles until only squares remain; find the minimum number of cuts.
- Why it's a good hard problem: A 2D generalization of matrix-chain-style interval DP — dp[a][b] tries every horizontal and vertical cut position, mirroring the "try every split point" recurrence of classic interval DP but over a 2D dimension space.

### Burst Balloons
- Judge: LeetCode
- Link: https://leetcode.com/problems/burst-balloons/
- Difficulty: LeetCode Hard
- Subtopic: Interval DP
- One-line description: Given n balloons with values, burst them one at a time (gaining left*balloon*right coins) to maximize total coins collected.
- Why it's a good hard problem: The textbook example of "think about the last event in the interval, not the first" — dp[i][j] represents the best score for bursting everything strictly between i and j last, requiring padding with sentinel 1s.

### Minimum Cost to Merge Stones
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-cost-to-merge-stones/
- Difficulty: LeetCode Hard
- Subtopic: Interval DP
- One-line description: Given piles of stones in a row, merge exactly k consecutive piles into one at a time (cost = sum merged) until one pile remains; find the minimum total cost, or -1 if impossible.
- Why it's a good hard problem: A true generalization of matrix chain multiplication to groups of size k, needing an extra DP dimension for "number of piles currently merged into a group" and a feasibility check based on (n-1) % (k-1).

## String DP

### Regular Expression Matching
- Judge: LeetCode
- Link: https://leetcode.com/problems/regular-expression-matching/
- Difficulty: LeetCode Hard
- Subtopic: String DP
- One-line description: Implement regex matching with support for '.' (any character) and '*' (zero or more of the preceding element) to determine if a pattern matches an entire string.
- Why it's a good hard problem: The '*' operator creates non-local transitions (it can match zero occurrences, forcing a skip-back in the DP), making the 2D state transition genuinely tricky to get right.

### Wildcard Matching
- Judge: LeetCode
- Link: https://leetcode.com/problems/wildcard-matching/
- Difficulty: LeetCode Hard
- Subtopic: String DP
- One-line description: Implement wildcard pattern matching with support for '?' (any single character) and '*' (any sequence, including empty) against an entire input string.
- Why it's a good hard problem: Naive O(nm) memoized DP is correct but the interesting challenge is recognizing the greedy two-pointer O(1)-space alternative, making it a good "DP vs. greedy trade-off" problem.

### Distinct Subsequences
- Judge: LeetCode
- Link: https://leetcode.com/problems/distinct-subsequences/
- Difficulty: LeetCode Hard
- Subtopic: String DP
- One-line description: Count the number of distinct ways string t appears as a subsequence of string s.
- Why it's a good hard problem: The counting recurrence (sum over "use this match" and "skip it" branches) is easy to state but easy to get subtly wrong on the base cases and overflow of counts.

### Minimum Insertion Steps to Make a String Palindrome
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
- Difficulty: LeetCode Hard
- Subtopic: String DP
- One-line description: Find the minimum number of character insertions needed to turn a given string into a palindrome.
- Why it's a good hard problem: A hard palindrome-DP variant that reduces to n - LCS(s, reverse(s)), requiring the non-obvious insight to connect interval palindrome DP with a longest-common-subsequence reformulation.

### Edit Distance
- Judge: CSES
- Link: https://cses.fi/problemset/task/1639
- Difficulty: CSES (harder end of the Dynamic Programming section)
- Subtopic: String DP
- One-line description: Compute the minimum number of single-character insertions, deletions, and replacements to transform one string into another.
- Why it's a good hard problem: The canonical 2D string-alignment DP; a solid checkpoint before tackling the pattern-matching and constrained variants (wildcard/regex) above.

### Subsequences (hard version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1183/H
- Difficulty: CF 1900
- Subtopic: String DP
- One-line description: Given a string of length up to 100 and a target count k (up to 1e12), repeatedly add distinct subsequences to a set at cost (n - length); find the minimum total cost to reach k distinct subsequences.
- Why it's a good hard problem: Requires counting distinct subsequences of each length via DP (not just total distinct subsequences), then greedily consuming the cheapest (longest) ones first — a layered combination of counting-DP and greedy selection.
