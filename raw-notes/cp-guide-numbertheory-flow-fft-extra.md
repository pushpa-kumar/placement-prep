# Hard Practice Problems — New Subtopics (CRT, Matrix Exponentiation, Lucas/Möbius, MCMF, Hungarian, Kitamasa/Bostan-Mori)

All problems verified real via the Codeforces public API (`problemset.problems`), direct problem-page fetch (via `r.jina.ai` proxy where Cloudflare blocked raw `curl`), the CSES problem pages, or the LeetCode public GraphQL API. No invented problems/links/ratings.

## Chinese Remainder Theorem

### Remainders Game
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/687/B
- Difficulty: 1800
- Subtopic: Chinese Remainder Theorem
- One-line description: Given k and a set of moduli c_1..c_n, decide whether knowing x mod c_i for all i always determines x mod k for every possible x.
- Why it's a good hard problem: Forces you to reason about CRT existence/uniqueness conditions (lcm of the c_i vs. k) rather than just running the algorithm.

### Congruence Equation
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/919/E
- Difficulty: 2100
- Subtopic: Chinese Remainder Theorem
- One-line description: Given a, b, prime p and bound x, count integers y in [1, x] such that a^y ≡ b (mod p).
- Why it's a good hard problem: Combines discrete logarithm / multiplicative order with CRT-style periodic counting to combine residues across the full range.

### Two Chandeliers
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1500/B
- Difficulty: 2200
- Subtopic: Chinese Remainder Theorem
- One-line description: Two chandeliers cycle through colors with different periods; find the day of the k-th day their colors differ, using CRT to count matching days up to a bound.
- Why it's a good hard problem: Requires binary search over CRT-derived periodicity plus careful inclusion-exclusion on the merged cycle length (lcm of the two periods).

### Power Tower
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/906/D
- Difficulty: 2700
- Subtopic: Chinese Remainder Theorem
- One-line description: Compute a power tower w_l^(w_{l+1}^(...)) mod m for range queries, using the generalized Euler theorem (which itself needs CRT-style modulus factoring via repeated totient reduction).
- Why it's a good hard problem: Classic "CRT + Euler's theorem tower" problem; the recursive modulus-halving argument is a staple hard-NT technique.

### ConstructOR
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1748/D
- Difficulty: 2100
- Subtopic: Chinese Remainder Theorem
- One-line description: Find x < 2^60 such that a|x and b|x (bitwise OR) are both divisible by d, by reasoning over coprime bit-parity constraints reminiscent of CRT-style constraint splitting.
- Why it's a good hard problem: Good constructive-CRT-flavored problem for the "combine independent modular/bitwise constraints" mindset, verified via CF API tag `chinese remainder theorem`.

## Matrix Exponentiation (Linear Recurrences Beyond Simple Fibonacci)

### Magic Gems
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1117/D
- Difficulty: 2100
- Subtopic: Matrix Exponentiation
- One-line description: Count configurations summing to N units where each magic gem takes 1 unit or is split into M units, for N up to 1e18 — the count follows f(n) = f(n-1) + f(n-M).
- Why it's a good hard problem: Textbook "derive an order-M linear recurrence then matrix-exponentiate it" problem, a clean step beyond plain Fibonacci.

### Lunar New Year and a Recursive Sequence
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1106/F
- Difficulty: 2400
- Subtopic: Matrix Exponentiation
- One-line description: Given f_i = (f_{i-1}^{b1} · ... · f_{i-k}^{bk}) mod p for a prime p, find f_n.
- Why it's a good hard problem: The recurrence is multiplicative, so you must exponentiate the *exponent vector* via matrix power and separately handle the base via a primitive root / discrete logarithm — a genuinely harder combination than a linear additive recurrence.

### Fibonotci
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/575/A
- Difficulty: 2700
- Subtopic: Matrix Exponentiation
- One-line description: Compute F_n for a Fibonacci-like recurrence F_n = s_{n-1}F_{n-1} + s_{n-2}F_{n-2} where s is an "almost cyclic" coefficient sequence with a handful of exceptions, over huge n and many queries.
- Why it's a good hard problem: Needs precomputed matrix products over one full cycle plus careful patching for the exceptional positions — a much harder generalization of Fibonacci-by-matrix-power.

### Throwing Dice
- Judge: CSES
- Link: https://cses.fi/problemset/task/1096
- Difficulty: CSES (n up to 1e18)
- Subtopic: Matrix Exponentiation
- One-line description: Count the number of ways to reach sum n by repeatedly throwing a die (1..6), for n up to 10^18.
- Why it's a good hard problem: Canonical order-6 linear recurrence that is intractable by plain DP once n exceeds ~10^7, forcing matrix exponentiation.

## Lucas' Theorem & Möbius Inversion

### Ceizenpok's formula
- Judge: Codeforces (Gym — 2015 ICL, Finals, Div. 1)
- Link: https://codeforces.com/gym/100633/problem/J
- Difficulty: No CF contest rating (ICPC Gym problem); constraints (n ≤ 1e18, m ≤ 1e6 arbitrary) put it solidly at Div.1 E/hard-2400+ equivalent difficulty
- Subtopic: Lucas' Theorem (combined with CRT)
- One-line description: Compute C(n, k) mod m for n up to 1e18, k ≤ n, and an *arbitrary* modulus m ≤ 1e6 (not necessarily prime).
- Why it's a good hard problem: The canonical "generalized Lucas' theorem" problem — factor m into prime powers via CRT, apply Lucas/Andrew Granville's extension for each prime power, then recombine with CRT. Verified by direct fetch (statement confirms exact n/k/m bounds); note this is the one genuinely well-known Lucas' theorem problem found on a Codeforces-hosted judge — standalone (non-gym) CF/CSES problems requiring pure Lucas' theorem are very rare (see summary).

### Unusual Sequences
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/900/D
- Difficulty: 2000
- Subtopic: Möbius Inversion
- One-line description: Count sequences of positive integers with given gcd x and sum y, expressed via a Möbius-function sum over divisors.
- Why it's a good hard problem: Direct, clean application of Möbius inversion to turn a gcd-constrained counting problem into a divisor sum.

### Coprime Subsequences
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/803/F
- Difficulty: 2000
- Subtopic: Möbius Inversion
- One-line description: Count the number of subsequences of an array whose gcd is 1.
- Why it's a good hard problem: Requires inclusion-exclusion via the Möbius function over multiples to avoid double counting non-coprime subsequences.

### Make It One
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1043/F
- Difficulty: 2500
- Subtopic: Möbius Inversion
- One-line description: Find the minimum-size subset of an array whose gcd is 1, using Möbius-function-weighted subset-sum DP.
- Why it's a good hard problem: Combines Möbius inversion with a nontrivial DP bound proof (answer ≤ 7) — a favorite "hard Möbius" problem in most curated lists.

### Alex and a TV Show
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1097/F
- Difficulty: 2500
- Subtopic: Möbius Inversion
- One-line description: Support union/gcd/lcm updates on multisets and answer "count of x with a given gcd" queries via randomization plus a Möbius-transform-style array.
- Why it's a good hard problem: Rare combination of Möbius/divisor-transform ideas with randomized hashing for online updates.

### Counting Coprime Pairs
- Judge: CSES
- Link: https://cses.fi/problemset/task/2417
- Difficulty: CSES
- Subtopic: Möbius Inversion
- One-line description: Given n integers up to 10^6, count the number of pairs that are coprime.
- Why it's a good hard problem: The standard entry-level-but-still-nontrivial Möbius sieve counting problem — a clean verification target before tackling 803F/1043F.

## Min-Cost Max-Flow (MCMF)

### Anti-Palindromize
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/884/F
- Difficulty: 2500
- Subtopic: Min-Cost Max-Flow
- One-line description: Rearrange a string into an antipalindromic permutation maximizing the sum of "beauty" values at positions that keep their original character.
- Why it's a good hard problem: Classic MCMF assignment: build a flow network pairing symmetric position-pairs to letter-pairs with costs, a staple "recognize the assignment structure" exercise.

### Red-Blue Graph
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1288/F
- Difficulty: 2900
- Subtopic: Min-Cost Max-Flow
- One-line description: Color bipartite-graph edges red/blue (or leave uncolored) at a cost to satisfy per-vertex majority-color constraints, minimizing total cost.
- Why it's a good hard problem: Non-obvious reduction of a combinatorial coloring/degree-constraint problem into an MCMF instance; frequently cited in curated "MCMF example" lists.

### Build String
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/237/E
- Difficulty: 2000
- Subtopic: Min-Cost Max-Flow
- One-line description: Build a target string t by deleting characters from n source strings, each character removed from string s_i costing i rubles and capped at a_i total removals, minimizing total cost.
- Why it's a good hard problem: A clean "characters = flow units, costs = per-source-string price, capacities = per-string budget" MCMF formulation.

### Four Melodies
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/818/G
- Difficulty: 2600
- Subtopic: Min-Cost Max-Flow
- One-line description: Select four disjoint, non-intersecting "melody" subsequences (each with the arithmetic/mod-7 melody property) from a note sequence to maximize total length.
- Why it's a good hard problem: Harder generalization of the well-known "Two Melodies" problem; needs a carefully constructed layered MCMF graph with node-splitting to bound the number of selected sequences.

### MCF
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1766/F
- Difficulty: 2800
- Subtopic: Min-Cost Max-Flow
- One-line description: Find the minimum-cost circulation in a DAG-like flow network subject to the extra constraint that each edge's flow must match its capacity's parity.
- Why it's a good hard problem: Explicitly named "MCF" by the setters; forces adapting standard min-cost-flow machinery to handle parity constraints on edge flows.

## Hungarian Algorithm (Assignment Problem)

### Task Assignment
- Judge: CSES
- Link: https://cses.fi/problemset/task/2129
- Difficulty: CSES
- Subtopic: Hungarian Algorithm
- One-line description: Given n employees, n tasks, and a full cost matrix, assign every employee exactly one task minimizing total cost (and output the assignment).
- Why it's a good hard problem: This is the canonical, textbook statement of the assignment problem — the direct target of the Hungarian algorithm (confirmed as the flagship "assignment" practice problem in USACO Guide's Min-Cost-Flow module).

### Chef Monocarp
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1437/C
- Difficulty: 1800
- Subtopic: Hungarian Algorithm
- One-line description: Assign each of n dishes to a distinct positive-integer removal time T, minimizing the sum of |T - t_i| over all dishes.
- Why it's a good hard problem: Structurally a full bipartite min-cost perfect matching (dishes × time slots); the intended O(n log n) solution exploits the 1-D cost structure, but it is a genuine, frequently-cited real-world instance of the assignment problem.

### Vasya and Endless Credits
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1107/F
- Difficulty: 2600
- Subtopic: Hungarian Algorithm
- One-line description: Choose an order to activate n credit offers (one per month) to maximize the money available at some point before repayments catch up.
- Why it's a good hard problem: Listed by USACO Guide as a direct application of the assignment-problem/Hungarian-algorithm machinery (offers × activation-month slots with a cost/profit matrix).

## Linear Recurrences via Polynomials (Kitamasa's Method / Bostan-Mori Algorithm)

### Painting a Grid With Three Different Colors
- Judge: LeetCode
- Link: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
- Difficulty: LeetCode Hard
- Subtopic: Linear Recurrences via Polynomials
- One-line description: Count the number of ways to color an m×n grid with 3 colors so no two adjacent cells share a color, for n up to 1000.
- Why it's a good hard problem: Standard "compute valid column states, build a transfer matrix, then advance n steps" DP; verified reference solutions present the O(k^2 log n) Kitamasa method as the technique that scales better than raw matrix exponentiation as the state count k grows.

### Total Characters in String After Transformations II
- Judge: LeetCode
- Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/
- Difficulty: LeetCode Hard
- Subtopic: Linear Recurrences via Polynomials
- One-line description: After t transformations (each letter replaced by a range of following letters per a per-letter rule), find the total resulting string length, for t up to 10^9.
- Why it's a good hard problem: Reference solutions explicitly derive the linear recurrence via Berlekamp–Massey and then evaluate the n-th term with Kitamasa's method as the scalable alternative to matrix exponentiation.

### Number of ZigZag Arrays II
- Judge: LeetCode
- Link: https://leetcode.com/problems/number-of-zigzag-arrays-ii/
- Difficulty: LeetCode Hard
- Subtopic: Linear Recurrences via Polynomials
- One-line description: Count length-n zigzag arrays with values in [l, r] modulo 1e9+7, for n up to 10^9 and (r-l) up to ~100.
- Why it's a good hard problem: Requires finding the state-transition-derived recurrence via Berlekamp-Massey, then evaluating a specific huge-index term via Kitamasa — a direct, well-documented real-world Kitamasa use case.

## Sourcing Notes

- Lucas' theorem has essentially no standalone, non-gym Codeforces problem: a systematic check against several large, well-maintained curated problem lists (including a ~700-entry authoritative competitive-programming topic list) turned up **zero** plain-Codeforces or CSES problems requiring pure Lucas' theorem alone — the technique nearly always shows up folded into a broader combinatorics/CRT problem (as in the Gym problem listed above) or on judges outside our allowed set (CodeChef, LOJ, HDU). We include the one genuine CF-hosted (Gym) match plus solid Möbius-inversion coverage to round out that subtopic.
- Hungarian-algorithm-specific problems are similarly thin on Codeforces (the technique is usually subsumed by MCMF); CSES's own "Task Assignment" is the cleanest canonical fit, backed by two real CF problems that are explicitly documented (USACO Guide) as applications.
- Linear-Recurrences-via-Polynomials (Kitamasa/Bostan-Mori) problems were not findable on Codeforces or CSES with confidence; three verified LeetCode Hard problems (from a well-known, carefully-vetted Chinese competitive-programmer's public solution repository) fill this niche instead, each with reference solutions that explicitly apply Berlekamp-Massey + Kitamasa.
