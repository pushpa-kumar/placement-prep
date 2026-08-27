# Curated Codeforces blogs: Number Theory & Combinatorics, Bit Manipulation, Game Theory (all verified live via Codeforces API/pages, Aug 2026)

## Number Theory & Combinatorics

### Essentials of Elementary Number Theory
- Author: Everule
- URL: https://codeforces.com/blog/entry/97623
- Topic: Number Theory & Combinatorics
- Takeaway: Builds elementary number theory from divisibility up through GCD/Bezout's identity, Fermat's little theorem, CRT, and Miller-Rabin primality testing, with an emphasis on intuition over rote formulas.

### [Tutorial] Math note — linear sieve
- Author: Nisiyama_Suzune
- URL: https://codeforces.com/blog/entry/54090
- Topic: Number Theory & Combinatorics
- Takeaway: Explains the O(n) linear sieve (vs. the O(n log log n) Sieve of Eratosthenes) and how it simultaneously computes multiplicative functions like phi and mu for every number up to n.

### [Tutorial] Euler's phi function, its properties, and how to compute it
- Author: kamilszymczak1
- URL: https://codeforces.com/blog/entry/106851
- Topic: Number Theory & Combinatorics
- Takeaway: Proves phi's multiplicativity and prime-power formula via CRT, then shows how to compute phi(n) fast via prime factorization, useful for many modular-arithmetic counting problems.

### Problem Solving Guide to Modular Combinatorics and Exponentiation
- Author: jeqcho
- URL: https://codeforces.com/blog/entry/78873
- Topic: Number Theory & Combinatorics
- Takeaway: Walks through fast modular exponentiation, modular inverses via Fermat's little theorem, and computing nCr mod a large prime for n, k up to 10^6.

### [Tutorial] Inclusion-Exclusion Principle
- Author: Roundgod
- URL: https://codeforces.com/blog/entry/64625
- Topic: Number Theory & Combinatorics
- Takeaway: Covers the generalized inclusion-exclusion principle with formal derivation and a set of practice problems showing how to alternate-sum over overlapping "bad" conditions.

### Short modular inverse
- Author: _h_
- URL: https://codeforces.com/blog/entry/23365
- Topic: Number Theory & Combinatorics
- Takeaway: A compact one-line recursive modular-inverse routine derived from the extended Euclidean algorithm's recurrence, handy as a code-golf-style alternative to Fermat-based inverses.

## Bit Manipulation

### SOS Dynamic Programming [Tutorial]
- Author: usaxena95
- URL: https://codeforces.com/blog/entry/45223
- Topic: Bit Manipulation
- Takeaway: Derives the O(n·2^n) Sum-over-Subsets DP by progressively improving from brute force O(4^n) and submask-iteration O(3^n), the standard technique for subset-sum aggregation over bitmasks.

### A Beautiful Technique for Some XOR Related Problems
- Author: DrSwad
- URL: https://codeforces.com/blog/entry/68953
- Topic: Bit Manipulation
- Takeaway: Frames XOR as vector addition over Z_2 and shows how building a linear (XOR) basis lets you count/find achievable XOR-sums across subsets efficiently, worked through six example problems.

### XOR basis without linear algebra
- Author: Everule
- URL: https://codeforces.com/blog/entry/100066
- Topic: Bit Manipulation
- Takeaway: Reconstructs the XOR-basis algorithm from first principles using elementary DP/greedy reasoning about bit positions, avoiding formal linear-algebra vocabulary.

### Linear Basis (Xor Basis Extended)
- Author: errorgorn
- URL: https://codeforces.com/blog/entry/98376
- Topic: Bit Manipulation
- Takeaway: Generalizes the classical XOR basis to maintain a basis of vectors over (Z/mZ)^d for non-prime m, extending the technique beyond pure XOR to modular vector spaces.

## Game Theory

### A blog on the Sprague-Grundy Theorem
- Author: sirknightingfail
- URL: https://codeforces.com/blog/entry/63054
- Topic: Game Theory
- Takeaway: A rigorous, math-club-style handout that formally defines impartial games and derives the Sprague-Grundy theorem, including its reduction of arbitrary impartial games to equivalent Nim heaps.

### The Intuition Behind NIM and Grundy Numbers in Combinatorial Game Theory
- Author: Shisuko
- URL: https://codeforces.com/blog/entry/66040
- Topic: Game Theory
- Takeaway: Builds intuition for why XOR determines the winner in Nim and why the mex (minimum excludant) operation produces Grundy numbers, rather than presenting them as memorized rules.

### [Tutorial] Slight Generalization of Grundy Numbers
- Author: emorgan
- URL: https://codeforces.com/blog/entry/85984
- Topic: Game Theory
- Takeaway: Introduces "Grundy polynomials" to analyze games with infinitely many states/positions, extending standard Grundy theory to cascading Nim-like games.

### Nimbers and Sprague-Grundy theorem
- Author: adamant
- URL: https://codeforces.com/blog/entry/103785
- Topic: Game Theory
- Takeaway: Recaps Sprague-Grundy formally, then covers the rarely-discussed nimber product (multiplication of Grundy values as a field operation) and its meaning for games like turning/diminishing-rectangle games.

### Intro to Staircase Nim + Editorial for HackerRank "Move the Coins"
- Author: Shafaet
- URL: https://codeforces.com/blog/entry/44651
- Topic: Game Theory
- Takeaway: Introduces Staircase Nim, a Nim variant where stones move down a staircase instead of being removed, and shows the reduction to a standard XOR-based Nim analysis on odd-indexed steps.

### Nim (Algorithmic Game)
- Author: paladin8
- URL: https://codeforces.com/blog/entry/3657
- Topic: Game Theory
- Takeaway: A classic, concise explanation of the game of Nim and the proof that the XOR (nim-sum) of pile sizes determines whether the position is winning or losing.
