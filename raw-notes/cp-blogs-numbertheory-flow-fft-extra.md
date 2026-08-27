# Codeforces Blogs — New Subtopics (CRT, Matrix Exponentiation, Lucas/Möbius, MCMF, Hungarian, Kitamasa/Bostan-Mori)

All blog entries verified real via the Codeforces public API (`blogEntry.view`) — title and author confirmed directly from Codeforces, not invented.

## Number Theory & Combinatorics

### [Tutorial] Chinese Remainder Theorem
- Author: Valiors
- URL: https://codeforces.com/blog/entry/61290
- Topic: Number Theory & Combinatorics
- Subtopic: Chinese Remainder Theorem
- Takeaway: Walks through the CRT construction (including the non-coprime-moduli generalization) with worked derivations, useful as the canonical reference before attempting CRT-tagged problems.

### Linear Recurrence and Berlekamp-Massey Algorithm
- Author: TLE
- URL: https://codeforces.com/blog/entry/61306
- Topic: Number Theory & Combinatorics
- Subtopic: Matrix Exponentiation / Linear Recurrences via Polynomials
- Takeaway: Explains how to recover an unknown linear recurrence from a sequence of terms and then evaluate far-out terms, bridging plain matrix-exponentiation thinking into the polynomial/Kitamasa toolbox.

### Lucas Theorem is not an equation, it's an operation!
- Author: Everule
- URL: https://codeforces.com/blog/entry/121012
- Topic: Number Theory & Combinatorics
- Subtopic: Lucas' Theorem
- Takeaway: Reframes Lucas' theorem as a digit-wise operation on base-p representations, giving sharper intuition for why C(n,k) mod p decomposes the way it does.

### [Tutorial] Math note — Möbius inversion
- Author: Nisiyama_Suzune
- URL: https://codeforces.com/blog/entry/53925
- Topic: Number Theory & Combinatorics
- Subtopic: Möbius Inversion
- Takeaway: Concise formal derivation of the Möbius inversion formula and its use for converting gcd/divisor-sum counting problems into computable divisor sums.

### [Tutorial] Solving Linear Recurrences with various methods, Including O(N logN logK) using FFT
- Author: demoralizer
- URL: https://codeforces.com/blog/entry/97627
- Topic: Number Theory & Combinatorics
- Subtopic: Linear Recurrences via Polynomials (Kitamasa's method / Bostan-Mori)
- Takeaway: Surveys multiple approaches to the k-th-term-of-a-linear-recurrence problem, culminating in the polynomial/FFT-based method that generalizes Kitamasa's method for large recurrence orders.

## Network Flow & Matching

### [Tutorial] Graph Potentials, Johnson's Algorithm, and Min Cost Max Flow
- Author: Monogon
- URL: https://codeforces.com/blog/entry/95823
- Topic: Network Flow & Matching
- Subtopic: Min-Cost Max-Flow (MCMF)
- Takeaway: Explains the Johnson potential trick that lets MCMF use Dijkstra instead of Bellman-Ford on graphs with negative-cost edges, the key implementation detail behind fast MCMF.

### [Tutorial] Minimum cost (maximum) flow
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/105330
- Topic: Network Flow & Matching
- Subtopic: Min-Cost Max-Flow (MCMF)
- Takeaway: A from-scratch, implementation-focused MCMF tutorial covering both SPFA-based and Dijkstra-with-potentials variants.

### [Tutorial] Hungarian algorithm in Õ(mn) or O(n^3)
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/128703
- Topic: Network Flow & Matching
- Subtopic: Hungarian Algorithm
- Takeaway: Derives the Hungarian algorithm via the same successive-shortest-augmenting-path / potential framework used for MCMF, giving both the classic O(n^3) and a faster O(mn log n)-style variant.

### Algorithms Dead Episode 0: Hungarian Algorithm
- Author: SecondThread
- URL: https://codeforces.com/blog/entry/78596
- Topic: Network Flow & Matching
- Subtopic: Hungarian Algorithm
- Takeaway: An accessible, example-driven walkthrough of the assignment problem and the Hungarian algorithm aimed at competitive programmers seeing it for the first time.
