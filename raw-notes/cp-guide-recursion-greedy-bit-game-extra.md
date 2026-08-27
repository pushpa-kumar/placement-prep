# Recursion/Greedy/Bit/Game Extensions — Hard Practice Problems (CF 1700+, LeetCode Hard, CSES)

Covers 7 new subtopics: Divide and Conquer, Minimax with Alpha-Beta Pruning, Huffman Coding & Optimal Merge,
Fractional vs. 0/1 Greedy Recognition, Bit Tricks & Gray Code, Bitset Optimization for Brute-Force Speedup,
and Combinatorial Game Sums & Misère Play. All problems verified live via the Codeforces public API, CSES
problemset pages, or LeetCode's problem listing/description (Aug 2026).

## Divide and Conquer

### Minimum Euclidean Distance
- Judge: CSES
- Link: https://cses.fi/problemset/task/2194
- Difficulty: CSES
- Subtopic: Divide and Conquer (closest pair of points)
- One-line description: Given up to 2*10^5 points in the plane, find the minimum squared Euclidean distance between any two distinct points.
- Why it's a good hard problem: The naive O(n^2) all-pairs check is too slow at this size, forcing the classical O(n log n) divide-and-conquer closest-pair algorithm — split by x-coordinate, recurse, then carefully bound the merge-step strip search to O(n).

### Merge Sort
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/873/D
- Difficulty: CF 1800
- Subtopic: Divide and Conquer (constructive, recursion-tree structure)
- One-line description: Construct a permutation of size n such that running the classic recursive mergesort (which early-exits on already-sorted subranges) makes exactly k recursive calls.
- Why it's a good hard problem: Forces you to reason precisely about the shape of a divide-and-conquer recursion tree — which subranges recurse and which short-circuit — and reverse-engineer an input that produces a target call count.

### Pashmak and Parmida's problem
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/459/D
- Difficulty: CF 1800
- Subtopic: Divide and Conquer (counting with merge step)
- One-line description: Count pairs (i, j) with i < j such that the count of a[i] in the prefix ending at i exceeds the count of a[j] in the suffix starting at j.
- Why it's a good hard problem: A classic "count inversion-like pairs across a split" problem solved by divide and conquer, computing cross-pair contributions during the merge step (an alternative to a BIT-based approach) — a direct generalization of counting inversions.

### Painting Fence
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/448/C
- Difficulty: CF 1900
- Subtopic: Divide and Conquer (recursive range minimum splitting)
- One-line description: Given fence-plank heights, find the minimum number of horizontal/vertical brush strokes needed to paint every plank, where a horizontal stroke of length k costs 1 and covers a contiguous range at one height.
- Why it's a good hard problem: The classic solution recurses on segments by finding the minimum height in the range (splitting at the minimum), comparing "one horizontal stroke across the whole segment" against "recurse on the pieces above and around the minimum" — structurally identical to Largest Rectangle in Histogram solved via divide and conquer.

## Minimax with Alpha-Beta Pruning

### Letter Picking
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1728/D
- Difficulty: CF 1800
- Subtopic: Minimax with Alpha-Beta Pruning
- One-line description: Alice and Bob alternately take the first or last letter of a string and prepend it to their own string (Alice wants the lexicographically smaller result, Bob the opposite, both settle for a draw if they can't win); determine the outcome under optimal play.
- Why it's a good hard problem: A genuine two-player minimax over game states (a substring, defined by its two endpoints), where the "value" has three outcomes (Alice/Bob/Draw) instead of a single number — memoized minimax search (interval DP acting as the practical CP equivalent of alpha-beta pruning) is required, not a closed-form trick.

### Game on Sum (Easy Version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1628/D1
- Difficulty: CF 2100
- Subtopic: Minimax with Alpha-Beta Pruning
- One-line description: Over n turns, Alice picks a real number in [0, k] each turn and Bob decides whether to add or subtract it from a running score (constrained to add on at least m turns); Alice maximizes the final score, Bob minimizes it — find the optimal value.
- Why it's a good hard problem: A textbook continuous-choice minimax game (one player picks a value, the adversary picks a sign) that must be reduced to a tractable recurrence over remaining turns and remaining "must-add" budget — exactly the value-game generalization of alpha-beta minimax search.

### World is Mine
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1987/D
- Difficulty: CF 1800
- Subtopic: Minimax with Alpha-Beta Pruning
- One-line description: Alice and Bob alternately eat cakes (Alice can only eat a cake tastier than any she's eaten before; Bob eats anything); Alice maximizes how many cakes she eats and Bob minimizes it — find the count under optimal play.
- Why it's a good hard problem: A greedy-flavored minimax where naive simulation is exponential; the optimal-play analysis requires proving a monotonic "best response" structure so the adversarial min/max search collapses to an efficient two-pointer/greedy evaluation.

### Cat and Mouse
- Judge: LeetCode
- Link: https://leetcode.com/problems/cat-and-mouse/
- Difficulty: LeetCode Hard (#913)
- Subtopic: Minimax with Alpha-Beta Pruning
- One-line description: On a graph, a mouse and cat alternately move along edges (mouse wants to reach hole 0, cat wants to catch the mouse at the same node, draws are possible if the game repeats forever); determine which side wins with optimal play.
- Why it's a good hard problem: The state space can contain cycles (draws), which breaks naive top-down minimax memoization — the standard solution is retrograde/topological analysis (working backward from known terminal states), a key extension of minimax search beyond simple recursion.

### Cat and Mouse II
- Judge: LeetCode
- Link: https://leetcode.com/problems/cat-and-mouse-ii/
- Difficulty: LeetCode Hard (#1728)
- Subtopic: Minimax with Alpha-Beta Pruning
- One-line description: On a grid maze with walls, food, and jump-distance limits per player, a cat and mouse alternately move (cat wins by catching the mouse or reaching the food first, mouse wins by reaching the food first); determine the winner with optimal play and a move-limit draw rule.
- Why it's a good hard problem: A grid-based minimax with a much larger branching factor and an explicit move cap to bound infinite play, requiring careful memoized minimax over (mouse position, cat position, whose turn, moves remaining) — a practical-scale instance of the same search that alpha-beta pruning speeds up in real game engines.

## Huffman Coding & Optimal Merge

### Huffman Coding on Segment
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/700/D
- Difficulty: CF 3100
- Subtopic: Huffman Coding & Optimal Merge
- One-line description: For each of q queries giving a subarray [l, r] of a message, output the minimum possible length of a binary Huffman encoding of the characters in that subarray.
- Why it's a good hard problem: Directly names and requires Huffman coding, but instead of encoding the whole array once, it demands the optimal-merge cost for arbitrary online ranges — forcing a persistent/segment-tree-of-heaps style data structure layered on top of the classic greedy-merge algorithm.

### Minimum Cost to Merge Stones
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-cost-to-merge-stones/
- Difficulty: LeetCode Hard (#1000)
- Subtopic: Huffman Coding & Optimal Merge
- One-line description: Given piles of stones in a row, merge exactly K consecutive piles into one at a time (cost = sum of the merged piles) until one pile remains, minimizing total cost, or report impossible.
- Why it's a good hard problem: A direct generalization of the two-way Huffman/optimal-merge idea to K-way merges with an adjacency (interval) constraint instead of "any two smallest" — the greedy priority-queue approach that solves classic Huffman coding fails here, and interval DP is required, making it an excellent problem for contrasting when greedy optimal-merge generalizes and when it doesn't.

### Minimum Cost to Merge Sorted Lists
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/
- Difficulty: LeetCode Hard (#3801)
- Subtopic: Huffman Coding & Optimal Merge
- One-line description: Repeatedly merge two sorted lists at a time (cost = len(a) + len(b) + |median(a) - median(b)|) until one list remains, minimizing total cost.
- Why it's a good hard problem: The len(a) + len(b) term is exactly the classic Huffman/optimal-merge cost (rewarding merging small pieces first, greedily via a priority queue), but the added median-distance penalty breaks the pure greedy-by-size argument and requires reasoning about which pairs to merge — a modern, sharper test of recognizing optimal-merge structure versus its limits.

## Fractional vs. 0/1 Greedy Recognition

### Shichikuji and Power Grid
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1245/D
- Difficulty: CF 1900
- Subtopic: Fractional vs. 0/1 Greedy Recognition (valid matroid/MST-style greedy)
- One-line description: Choose which cities get their own power station (fixed cost per city) and which cables to build between cities (cost proportional to distance) to connect every city to power at minimum total cost.
- Why it's a good hard problem: Modeled as an MST problem with an extra virtual "station" node, it shows a case where a discrete, seemingly combinatorial choice (station vs. cable) reduces exactly to a greedy matroid algorithm (Kruskal/Prim) whose fractional LP relaxation is provably tight — the "greedy works" side of the contrast.

### Olympiad in Programming and Sports
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/730/I
- Difficulty: CF 2000
- Subtopic: Fractional vs. 0/1 Greedy Recognition (naive greedy fails)
- One-line description: Split n students into a disjoint programming team of exactly p and a sports team of exactly s to maximize the sum of programming skills (team 1) plus sports skills (team 2).
- Why it's a good hard problem: A naive per-student "assign to whichever skill is larger" or ratio-based fractional-style greedy is provably suboptimal because of the exact-size constraints on both teams; the correct approach starts from a size-respecting baseline assignment and refines it with an exchange-argument priority queue — a sharp illustration of where indivisible, sized-bucket constraints break simple greedy/fractional reasoning.

### Knapsack
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1132/E
- Difficulty: CF 2300
- Subtopic: Fractional vs. 0/1 Greedy Recognition (0/1 requires DP, not greedy)
- One-line description: Given items each belonging to one of two categories with a value and a per-category count limit, and a total weight budget equal to the item count limit, choose items to maximize total value.
- Why it's a good hard problem: Looks like it should admit a simple ratio-greedy (as in fractional knapsack), but the hard per-category cardinality caps and 0/1 (indivisible) selection mean the true solution needs a knapsack-style DP over category counts combined with a greedy sort within each category — a clean test of recognizing exactly which part of the problem greedy can solve and which needs DP.

## Bit Tricks & Gray Code

### Gray Code
- Judge: CSES
- Link: https://cses.fi/problemset/task/2205
- Difficulty: CSES
- Subtopic: Bit Tricks & Gray Code (construction)
- One-line description: For a given length n, output all 2^n bit strings of length n such that consecutive strings in the list differ in exactly one bit (a Gray code).
- Why it's a good hard problem: The direct definitional exercise in Gray codes — implementing the reflect-and-prefix (or i ^ (i >> 1)) construction correctly at n up to 16, and understanding why it guarantees the single-bit-difference property between all consecutive entries.

### Bits
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/484/A
- Difficulty: CF 1700
- Subtopic: Bit Tricks & Gray Code (popcount maximization)
- One-line description: For up to 10^4 queries (l, r), find the smallest x in [l, r] with the maximum possible number of set bits, where l, r can be as large as 10^18.
- Why it's a good hard problem: The efficient solution is a pure bit trick — starting from l, greedily flip the lowest unset bits on one at a time as long as the result stays <= r, directly exercising low-bit manipulation (l | (l+1)-style reasoning) instead of any search or DP.

### Bitwise Operation Wizard
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1936/A
- Difficulty: CF 1700
- Subtopic: Bit Tricks & Gray Code (bit-by-bit interactive determination)
- One-line description: In an interactive problem, find two indices whose values (a hidden permutation) XOR to the maximum possible value, using only queries that compare the bitwise OR of two chosen pairs.
- Why it's a good hard problem: Requires determining the answer's bits from most significant to least significant using only OR-comparison queries — a clean, interactive stress test of bit-by-bit greedy reasoning distinct from subset-enumeration or XOR-basis techniques.

## Bitset Optimization for Brute-Force Speedup

### Spy-string
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1360/F
- Difficulty: CF 1700
- Subtopic: Bitset Optimization for Brute-Force Speedup
- One-line description: Given m strings of length n, find any string of length n that is within Hamming distance 1 of every given string, or report impossible.
- Why it's a good hard problem: The natural approach is brute force over the O(n) candidate strings derived from fixing the first string and trying each single-character change, and checking each candidate against all m strings in O(nm/64) using std::bitset for the character-mismatch comparisons instead of O(nm) — the canonical "same asymptotic algorithm, 64x faster with bitset" pattern.

### GCD Counting
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1101/D
- Difficulty: CF 2000
- Subtopic: Bitset Optimization for Brute-Force Speedup
- One-line description: In a tree with a value on each node, find the longest path where every two adjacent nodes on the path have a GCD greater than 1.
- Why it's a good hard problem: The standard solution represents each node's prime-factor set as a std::bitset over all primes up to the value limit, then does a tree DP where merging two children's "compatible path" bitsets via AND/OR operations turns an otherwise O(n^2) or O(n * primes) check into a 64x-faster bitset operation — a widely cited example of bitset-accelerated tree DP.

### Dasha and cyclic table
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/754/E
- Difficulty: CF 2600
- Subtopic: Bitset Optimization for Brute-Force Speedup
- One-line description: Given a large cyclic character table and a smaller pattern table (with wildcard cells), count the number of cyclic shifts at which the pattern matches the table (ignoring wildcard cells).
- Why it's a good hard problem: The classic solution encodes, for each pattern row and each letter, a bitset of matching column positions, then combines per-row bitsets with shifted ANDs — turning what looks like an O(pattern_size * table_size) brute-force check per shift into a bitset-vectorized computation, a canonical 2D bitset string-matching technique.

### Substrings in a String
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/914/F
- Difficulty: CF 3000
- Subtopic: Bitset Optimization for Brute-Force Speedup
- One-line description: Given a string with point updates to characters, answer queries asking whether a given pattern occurs as a substring within a given range of the string.
- Why it's a good hard problem: The reference solution maintains, per character, a std::bitset marking positions where that character occurs, then answers a pattern-match query by ANDing shifted copies of these bitsets together — the textbook example of using bitset shifts to replace an O(n * pattern length) brute-force scan with an O(n * pattern length / 64) one.

## Combinatorial Game Sums & Misère Play

### Nim Game II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1098
- Difficulty: CSES
- Subtopic: Combinatorial Game Sums & Misère Play (Sprague-Grundy sum of games)
- One-line description: With n heaps of sticks where a move removes 1, 2, or 3 sticks from one heap, and the player who removes the last stick wins, determine the winner under optimal play.
- Why it's a good hard problem: Each heap is a distinct subtraction game whose Grundy value (x mod 4) must first be computed independently, then the Sprague-Grundy theorem combines them via XOR — a direct test of the "sum of independent games" principle beyond plain Nim, where the per-heap game itself isn't standard Nim.

### Another Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/2208
- Difficulty: CSES
- Subtopic: Combinatorial Game Sums & Misère Play (non-XOR game sum)
- One-line description: With n heaps of coins where a move selects any subset of nonempty heaps and removes one coin from each, and the player who removes the last coin wins, determine the winner under optimal play.
- Why it's a good hard problem: This move rule (remove from many heaps simultaneously) is not standard Nim and the naive Sprague-Grundy XOR-of-piles rule does not directly apply; the correct analysis works bit-by-bit across the binary representations of the heap sizes, testing whether the solver understands the limits of the basic Nim-sum shortcut and can derive the right combination rule from first principles.

### Grundy's Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/2207
- Difficulty: CSES
- Subtopic: Combinatorial Game Sums & Misère Play (mex-based Grundy computation)
- One-line description: A single heap of n coins is repeatedly split into two nonempty heaps of different sizes; the player who makes the last move wins — determine the winner for each starting n.
- Why it's a good hard problem: Requires precomputing Grundy numbers via the mex-of-reachable-states rule for every heap size up to 10^6, the foundational computational step that the Sprague-Grundy sum theorem builds on when combining multiple independent games.

### Industrial Nim
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/15/C
- Difficulty: CF 2000
- Subtopic: Combinatorial Game Sums & Misère Play (XOR-sum over derived piles)
- One-line description: Given n quarries, each contributing m_i consecutive-integer-sized dumpers (x_i, x_i+1, ..., x_i+m_i-1) as separate Nim piles, determine who wins standard Nim played across all dumpers combined.
- Why it's a good hard problem: With up to 10^5 quarries each potentially contributing up to 10^16 piles, you cannot enumerate piles directly — you need a closed-form "XOR of a range of consecutive integers" trick (via a prefix-XOR function) to fold an enormous sum of independent single-pile games into a fast computation, a strong test of scaling the sum-of-games XOR principle.
