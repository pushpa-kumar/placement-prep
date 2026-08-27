# Advanced Dynamic Programming — Curated Hard Practice Problems (CF 1700+, LeetCode Hard, CSES)

## Bitmask DP

### Kefa and Dishes
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/580/D
- Difficulty: 1800
- Subtopic: Bitmask DP (traveling salesman / Hamiltonian path style, assignment problem, broken-profile/tiling DP)
- One-line description: Choose an ordered sequence of at most m dishes (no repeats) maximizing total satisfaction plus bonuses for specific adjacent-dish pairs.
- Why it's a good hard problem: Classic Hamiltonian-path-flavored bitmask DP over "set of dishes eaten so far, last dish eaten" with up to 18 dishes.

### Vladik and cards
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/743/E
- Difficulty: 2200
- Subtopic: Bitmask DP (traveling salesman / Hamiltonian path style, assignment problem, broken-profile/tiling DP)
- One-line description: Given up to 1000 cards each with a value 1-8, choose the longest subsequence that can be split into 8 non-decreasing subsequences (one per value).
- Why it's a good hard problem: Requires binary-searching the answer length, then an assignment-style bitmask DP over "last used position for each of the 8 values" combined with greedy/binary-search reasoning — a genuinely tricky state design.

### Counting Tilings
- Judge: CSES
- Link: https://cses.fi/problemset/task/2181
- Difficulty: CSES
- Subtopic: Bitmask DP (traveling salesman / Hamiltonian path style, assignment problem, broken-profile/tiling DP)
- One-line description: Count the number of ways to tile an n×m grid completely using 1×2 tiles (horizontal or vertical).
- Why it's a good hard problem: The canonical broken-profile bitmask DP — process the grid cell by cell, carrying a bitmask of which cells in the current "profile" are already filled.

### Elevator Rides
- Judge: CSES
- Link: https://cses.fi/problemset/task/1653
- Difficulty: CSES
- Subtopic: Bitmask DP (traveling salesman / Hamiltonian path style, assignment problem, broken-profile/tiling DP)
- One-line description: Partition n people (each with a weight) into the minimum number of elevator rides, each ride capacity-limited.
- Why it's a good hard problem: Classic "partition into minimum-cost groups" bitmask DP over subsets (dp[mask] = min rides, extra weight used in current ride), similar in spirit to bin-packing/TSP subset DP.

### Maximum Students Taking Exam
- Judge: LeetCode
- Link: https://leetcode.com/problems/maximum-students-taking-exam/
- Difficulty: LeetCode Hard
- Subtopic: Bitmask DP (traveling salesman / Hamiltonian path style, assignment problem, broken-profile/tiling DP)
- One-line description: Seat the maximum number of students in a classroom grid with broken seats so no student can see an adjacent-row/diagonal neighbor's answers.
- Why it's a good hard problem: Row-by-row broken-profile-style bitmask DP where each row's mask must be internally valid (no two adjacent bits) and compatible with the previous row's mask (no diagonal conflicts) — two layers of bitmask compatibility checking.

## Tree DP

### The Fair Nut and the Best Path
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1083/A
- Difficulty: 1800
- Subtopic: Tree DP (max independent set on tree, tree diameter via DP, rerooting technique)
- One-line description: Given a tree with vertex weights, find the maximum weight of a simple path (sum of vertex weights along it).
- Why it's a good hard problem: Direct generalization of tree-diameter-via-DP: at each node combine the best two "downward chains" from children while handling negative contributions correctly.

### Work Group
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/533/B
- Difficulty: 2000
- Subtopic: Tree DP (max independent set on tree, tree diameter via DP, rerooting technique)
- One-line description: On a tree where each employee has a rating, pick a subset of nodes with no supervisor-subordinate pair included, maximizing total rating minus a fixed penalty per chosen member.
- Why it's a good hard problem: Weighted maximum-independent-set-on-a-tree DP with the added twist of deciding per-subtree whether including the root subtree's answer beats zero, requiring careful combination of children's dp states.

### Tree with Maximum Cost
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1092/F
- Difficulty: 1900
- Subtopic: Tree DP (max independent set on tree, tree diameter via DP, rerooting technique)
- One-line description: For every possible choice of root, compute sum over all vertices of (vertex value × distance to root), and output the maximum over all roots.
- Why it's a good hard problem: Textbook rerooting technique — compute the answer once via one DFS, then re-derive every other root's answer in O(1) via a second DFS that transfers subtree contributions.

### Binary Tree Cameras
- Judge: LeetCode
- Link: https://leetcode.com/problems/binary-tree-cameras/
- Difficulty: LeetCode Hard
- Subtopic: Tree DP (max independent set on tree, tree diameter via DP, rerooting technique)
- One-line description: Place the minimum number of cameras on tree nodes (each covers itself, its parent, and its children) so every node is monitored.
- Why it's a good hard problem: Requires a 3-state tree DP (node has camera / node is covered without a camera / node is uncovered) with a subtle greedy-DP hybrid argument for correctness — a step up from plain max-independent-set DP.

## Digit DP

### Beautiful numbers
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/55/D
- Difficulty: 2500
- Subtopic: Digit DP (counting numbers with a digit property up to N)
- One-line description: Count integers in [l, r] that are divisible by the sum of their own digits.
- Why it's a good hard problem: The archetypal hard digit DP: since the divisor (digit sum) varies, you must DP over (position, remainder mod LCM(1..9), digit-sum-so-far, tight-flag), forcing a clever LCM-based state compression.

### Magic Numbers
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/628/D
- Difficulty: 2200
- Subtopic: Digit DP (counting numbers with a digit property up to N)
- One-line description: Count numbers in [l, r] built by concatenating the substrings "1", "14", and "144" in some order.
- Why it's a good hard problem: Requires designing a custom finite automaton over digit positions to track partial matches of "1"/"14"/"144", then running digit DP over that automaton's states.

### Segment Sum
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1073/E
- Difficulty: 2300
- Subtopic: Digit DP (counting numbers with a digit property up to N)
- One-line description: Compute the sum of all integers in [l, r] that contain at most k distinct decimal digits.
- Why it's a good hard problem: Standard digit-DP counting is not enough — you must simultaneously track a bitmask of digits used and accumulate the actual sum contribution of each digit position, combining digit DP with careful combinatorial bookkeeping.

### Numbers At Most N Given Digit Set
- Judge: LeetCode
- Link: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
- Difficulty: LeetCode Hard
- Subtopic: Digit DP (counting numbers with a digit property up to N)
- One-line description: Given a set of allowed digits, count how many positive integers ≤ N can be formed using only those digits (repetition allowed).
- Why it's a good hard problem: A clean, from-scratch introduction to the "process digits of N one position at a time, branch at the first strictly-smaller digit" digit DP pattern, including the tricky same-length-as-N edge case.

## DP on DAGs

### Gargari and Permutations
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/463/D
- Difficulty: 1900
- Subtopic: DP on DAGs (longest/shortest path in a DAG, counting paths)
- One-line description: Given k permutations of 1..n, find the longest common subsequence that appears (as a subsequence) in all k permutations simultaneously.
- Why it's a good hard problem: Reduces multi-permutation LCS to longest-path-in-a-DAG DP, where an edge (u, v) exists only if u appears before v in every one of the k permutations.

### Toss a Coin to Your Graph...
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1679/D
- Difficulty: 1900
- Subtopic: DP on DAGs (longest/shortest path in a DAG, counting paths)
- One-line description: Binary search on a value x, keep only edges whose weight is ≥ x, and find the longest path (in number of edges) achievable in the resulting graph, restricted to a length budget k.
- Why it's a good hard problem: Combines binary search on the answer with a longest-path-in-DAG DP over a graph that must first be shown to be acyclic (or detected as having a long-enough cycle) for the chosen threshold.

### Longest Increasing Path in a Matrix
- Judge: LeetCode
- Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
- Difficulty: LeetCode Hard
- Subtopic: DP on DAGs (longest/shortest path in a DAG, counting paths)
- One-line description: Find the length of the longest strictly increasing path of adjacent cells in a matrix.
- Why it's a good hard problem: The grid's "increasing value" edges implicitly define a DAG; the intended solution is memoized DFS (longest path in a DAG) rather than naive exponential search.

### Largest Color Value in a Directed Graph
- Judge: LeetCode
- Link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
- Difficulty: LeetCode Hard
- Subtopic: DP on DAGs (longest/shortest path in a DAG, counting paths)
- One-line description: In a directed graph where each node has a color, find the largest possible count of any single color along a path, or report that a cycle makes the answer undefined.
- Why it's a good hard problem: Requires topological-sort-driven DP carrying a full 26-color frequency vector per node while simultaneously detecting non-DAG (cyclic) input.

## Game-theory DP

### Removal Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/1097
- Difficulty: CSES
- Subtopic: Game-theory DP (minimax DP, stone/coin games)
- One-line description: Two players alternately remove a number from either end of an array trying to maximize their own total; both play optimally — find the first player's best possible score.
- Why it's a good hard problem: The canonical interval minimax DP: dp[i][j] represents the best score difference achievable on subarray [i, j], built from two overlapping smaller subproblems.

### Stick Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/1729
- Difficulty: CSES
- Subtopic: Game-theory DP (minimax DP, stone/coin games)
- One-line description: Two players alternately remove sticks from a pile using only a given set of allowed move sizes; determine who wins with optimal play for every pile size up to n.
- Why it's a good hard problem: A textbook win/lose-state DP (Grundy-style) over pile sizes, where each state's outcome depends on reachable smaller states — must be computed for all sizes up to n efficiently.

### Letter Picking
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1728/D
- Difficulty: 1800
- Subtopic: Game-theory DP (minimax DP, stone/coin games)
- One-line description: Two players alternately remove a letter from either end of a string, each trying to end up with the lexicographically better multiset of removed letters after optimal play from both sides.
- Why it's a good hard problem: Interval minimax DP with a three-way outcome (win/lose/draw) per state and a non-obvious per-state comparison rule between the two players' objectives.

### Stone Game III
- Judge: LeetCode
- Link: https://leetcode.com/problems/stone-game-iii/
- Difficulty: LeetCode Hard
- Subtopic: Game-theory DP (minimax DP, stone/coin games)
- One-line description: Two players alternately take 1, 2, or 3 stones from the front of a pile, each trying to maximize their own score; determine who wins (or if it's a tie) with optimal play.
- Why it's a good hard problem: Requires a suffix minimax DP tracking score differential with a branching factor of 3 per state and a careful sign-flip argument to translate "maximize my score" into a single recurrence.

## Probability & Expected-Value DP

### Fish
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/16/E
- Difficulty: 1900
- Subtopic: Probability & Expected-Value DP
- One-line description: n fish (n ≤ 18) swim in a pond; on each step two random fish meet and one eats the other with a given probability — compute, for every fish, the probability it survives to be the last one.
- Why it's a good hard problem: Combines a bitmask DP over "which fish are still alive" with probability transitions and a clever trick (fixing the encounter order) to make the state space tractable.

### Bad Luck Island
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/540/D
- Difficulty: 1900
- Subtopic: Probability & Expected-Value DP
- One-line description: On an island with rocks, scissors, and paper creatures that randomly meet and eliminate each other Rock-Paper-Scissors style, compute the probability each species survives.
- Why it's a good hard problem: A 3-dimensional probability DP over (rocks remaining, scissors remaining, paper remaining) where each state's probability flows into three possible next states — a clean example of expected-outcome DP over compound state.

### New Year and Arbitrary Arrangement
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/908/D
- Difficulty: 2200
- Subtopic: Probability & Expected-Value DP
- One-line description: Given probabilities of typing characters 'a' or 'b' at random (and a target k), compute the expected number of occurrences of the substring "ab" in a string built until k copies of "ab" appear (with a length cap).
- Why it's a good hard problem: Requires setting up an expected-value recurrence over (count of 'a's so far, count of "ab" substrings so far) and reasoning carefully about linearity of expectation combined with an early-stopping condition.

### Dice Probability
- Judge: CSES
- Link: https://cses.fi/problemset/task/1725
- Difficulty: CSES
- Subtopic: Probability & Expected-Value DP
- One-line description: Compute the probability that the sum of n dice rolls (each showing 1..6) lands in a given range [a, b].
- Why it's a good hard problem: Foundational probability DP — dp[i][s] = probability the sum after i dice is s — that scales naturally into harder biased-dice and weighted variants.

### Inversion Probability
- Judge: CSES
- Link: https://cses.fi/problemset/task/1728
- Difficulty: CSES
- Subtopic: Probability & Expected-Value DP
- One-line description: Given n elements each independently and uniformly assigned one of two possible values (with per-position choices), compute the expected number of inversions.
- Why it's a good hard problem: Uses linearity of expectation over all O(n²) pairs combined with a running-DP aggregate (expected number of "smaller" elements seen so far) to avoid the naive quadratic blow-up.

## DP Optimization Techniques

### Ciel and Gondolas
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/321/E
- Difficulty: 2600
- Subtopic: DP optimization techniques (monotonic deque optimization, divide & conquer optimization, Knuth's optimization, convex hull trick)
- One-line description: Partition n people standing in a line into exactly k contiguous, non-empty groups to minimize total "unhappiness" (sum over each group of a pairwise-cost function).
- Why it's a good hard problem: The quintessential divide-and-conquer optimization (and alternatively Knuth's optimization) problem — the naive O(n²k) DP is reduced to O(nk log n) by proving the optimal split point is monotonic in the DP layer.

### Yet Another Minimization Problem
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/868/F
- Difficulty: 2500
- Subtopic: DP optimization techniques (monotonic deque optimization, divide & conquer optimization, Knuth's optimization, convex hull trick)
- One-line description: Split an array into exactly k contiguous segments minimizing the sum, over segments, of C(count of each value in the segment, 2).
- Why it's a good hard problem: A second core divide-and-conquer optimization exercise, this time requiring an efficient two-pointer/BIT-maintained cost function as the split point recurses — combining D&C optimization with incremental cost maintenance.

### The Bakery
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/833/B
- Difficulty: 2200
- Subtopic: DP optimization techniques (monotonic deque optimization, divide & conquer optimization, Knuth's optimization, convex hull trick)
- One-line description: Split an array of shop types into exactly k contiguous "zones" to maximize the total number of distinct shop types across all zones.
- Why it's a good hard problem: Requires combining divide-and-conquer optimization on the DP layer with a segment-tree-maintained "distinct count" cost function that must be recomputed as the split boundary moves.

### Watching Fireworks is Fun
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/372/C
- Difficulty: 2100
- Subtopic: DP optimization techniques (monotonic deque optimization, divide & conquer optimization, Knuth's optimization, convex hull trick)
- One-line description: You move along a line of positions over time to maximize happiness gained from fireworks launched at given times/positions/values, with a per-second movement speed limit.
- Why it's a good hard problem: The DP transition at each time step is a sliding-window maximum over a range that shifts predictably, making it a direct application of monotonic-deque DP optimization to bring an O(n·d²) DP down to O(n·d).

### Kalila and Dimna in the Logging Industry
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/319/C
- Difficulty: 2100
- Subtopic: DP optimization techniques (monotonic deque optimization, divide & conquer optimization, Knuth's optimization, convex hull trick)
- One-line description: Cut down n trees (each requiring a specific axe strength and giving specific value if the previous tree cut used a weaker or equal axe) to maximize total value, minimizing total axe cost.
- Why it's a good hard problem: One of the most commonly cited introductory convex hull trick problems — the DP transition is a min-plus query over lines, and lines are inserted in an order that permits the simple monotonic CHT (no need for Li Chao tree).

## DP Combined with Data Structures

### Subsequences
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/597/C
- Difficulty: 1900
- Subtopic: DP combined with data structures (e.g. LIS in O(n log n), DP + Fenwick tree)
- One-line description: Given n points (x, y), find the maximum length of a sequence of points chosen in increasing order of x and non-decreasing order of y (a 2D "staircase" subsequence).
- Why it's a good hard problem: A direct 2D generalization of the O(n log n) LIS trick — requires a Fenwick tree keyed on the y-coordinate (after coordinate compression) to query "best dp value among all smaller-or-equal y so far" in O(log n).

### Increasing Subsequence II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1748
- Difficulty: CSES
- Subtopic: DP combined with data structures (e.g. LIS in O(n log n), DP + Fenwick tree)
- One-line description: Count the number of strictly increasing subsequences ending at each position of an array (not just the longest one).
- Why it's a good hard problem: Extends the classic O(n log n) LIS-length trick to counting: a Fenwick tree over compressed values must maintain running sums of subsequence counts rather than just a running maximum.

### Russian Doll Envelopes
- Judge: LeetCode
- Link: https://leetcode.com/problems/russian-doll-envelopes/
- Difficulty: LeetCode Hard
- Subtopic: DP combined with data structures (e.g. LIS in O(n log n), DP + Fenwick tree)
- One-line description: Given (width, height) pairs of envelopes, find the maximum number that can be nested inside each other (each dimension must strictly increase).
- Why it's a good hard problem: Reduces a 2D nesting problem to 1D LIS via a sort-then-patience-sorting trick (sort by width ascending, height descending for ties) so the O(n log n) LIS algorithm applies directly — a subtle but standard reduction.

### Maximum Height by Stacking Cuboids
- Judge: LeetCode
- Link: https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
- Difficulty: LeetCode Hard
- Subtopic: DP combined with data structures (e.g. LIS in O(n log n), DP + Fenwick tree)
- One-line description: Given cuboid dimensions (each freely rotatable), stack cuboids on top of each other (each dimension of the one on top must be ≤ the one below) to maximize total height.
- Why it's a good hard problem: A 3D generalization of the LIS/patience-sorting family — requires normalizing each cuboid's dimensions, sorting, then running an O(n²) or O(n log n) longest-chain DP, testing whether the LIS-style reduction insight transfers to three dimensions.
