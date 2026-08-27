# CP Guide: Number Theory & Combinatorics (modular arithmetic, sieves, primality at scale, nCr mod p, inclusion-exclusion) — hard practice problems, CF rating 1700+ / CSES harder set

## Modular Arithmetic / Exponentiation

### Exponentiation II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1712
- Difficulty: CSES (Mathematics, harder set)
- Subtopic: Modular Exponentiation (tower of exponents)
- One-line description: Efficiently compute a^(b^c) mod 1e9+7 for many triples (a, b, c), with the convention 0^0 = 1.
- Why it's a good hard problem: The outer exponent b^c is astronomically large, so it must be reduced modulo (p-1) via Fermat's little theorem before the outer fast exponentiation — and the 0^0 = 1 convention plus the case a ≡ 0 (mod p) create edge cases that trip up a naive Euler-theorem application.

### Multipliers
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/615/D
- Difficulty: 2000
- Subtopic: Modular Exponentiation (divisor-pairing trick)
- One-line description: Given n, compute the product of all of its divisors, modulo 1e9+7.
- Why it's a good hard problem: Divisors pair up as (d, n/d) with product n, so the answer is n raised to (number of divisors)/2 — but that count can be odd (perfect squares) and n itself can be ≡ 0 mod p, forcing careful modular-exponentiation bookkeeping rather than a naive product loop.

## Sieve-based

### Sum of Divisors
- Judge: CSES
- Link: https://cses.fi/problemset/task/1082
- Difficulty: CSES (Mathematics, harder set)
- Subtopic: Sieve-based / divisor-function summation
- One-line description: Compute the sum of σ(i) (sum-of-divisors function) for i = 1..n, modulo 1e9+7, for n up to 10^12.
- Why it's a good hard problem: n is too large to sieve directly, so the sum must be rewritten as Σ d·⌊n/d⌋ and evaluated in O(√n) using the floor-division block technique — a step beyond a basic sieve, testing whether the solver knows the divisor-summation identity.

### Steps to One
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1139/D
- Difficulty: 2300
- Subtopic: Sieve-based DP over divisors
- One-line description: Starting from an array, repeatedly replace it with a uniformly random non-empty subset and take the GCD of the remaining elements until it becomes 1; find the expected number of steps.
- Why it's a good hard problem: Requires computing, for every x, the probability that a random subset's GCD is a multiple of x by counting multiples of x in the array, then sieving downward from large x to small x (Möbius-style subtraction of multiples) to get the exact-GCD-x probabilities before assembling the expectation.

## Primality Testing at Scale

### Next Prime
- Judge: CSES
- Link: https://cses.fi/problemset/task/3396
- Difficulty: CSES (Mathematics, harder set)
- Subtopic: Primality Testing at Scale
- One-line description: For up to 20 queries, each giving n up to 10^12, output the smallest prime strictly greater than n.
- Why it's a good hard problem: Trial division up to √n (≈10^6) per candidate, repeated across the average prime gap and multiple queries, is too slow within the time limit — the intended solution needs a fast deterministic primality test (Miller–Rabin) to check each candidate in O(log^3 n).

## nCr under modulo

### Binomial Coefficients
- Judge: CSES
- Link: https://cses.fi/problemset/task/1079
- Difficulty: CSES (Mathematics, harder set)
- Subtopic: nCr under modulo
- One-line description: Answer many queries of the form "compute C(a, b) mod 1e9+7."
- Why it's a good hard problem: With up to 10^5 queries and a, b up to 10^6, per-query computation is too slow — it forces precomputing factorials and modular inverse factorials (via Fermat's little theorem) up front to answer each query in O(1).

### Anton and School - 2
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/785/D
- Difficulty: 2300
- Subtopic: nCr under modulo (combinatorial identities)
- One-line description: Given a bracket string, for each query range count the number of ways to pick a balanced-bracket subsequence (as a sum over k of C(opens, k)·C(closes, k)).
- Why it's a good hard problem: Naively summing C(opens, k)·C(closes, k) over all k is too slow per query; the fast solution collapses the sum into a single binomial coefficient via a Vandermonde-style identity, requiring genuine combinatorial-identity manipulation on top of routine modular nCr.

## Inclusion-Exclusion

### Prime Multiples
- Judge: CSES
- Link: https://cses.fi/problemset/task/2185
- Difficulty: CSES (Mathematics, harder set)
- Subtopic: Inclusion-Exclusion
- One-line description: Given up to 20 distinct primes and n up to 10^18, count how many integers in [1, n] are divisible by at least one of the given primes.
- Why it's a good hard problem: With n up to 10^18, only inclusion-exclusion over the 2^20 subsets of the given primes (each subset contributing ⌊n / product⌋) is fast enough — a clean, large-scale test of the inclusion-exclusion principle itself.

### Unusual Sequences
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/900/D
- Difficulty: 2000
- Subtopic: Inclusion-Exclusion (Möbius function)
- One-line description: Count the number of sequences of positive integers of any length whose GCD is exactly x and whose elements sum to y.
- Why it's a good hard problem: First requires solving "count sequences with GCD exactly 1" via a stars-and-bars-style recurrence, then extending to "GCD exactly x" via a Möbius-function inclusion-exclusion over the multiples of x — a two-layer combination of combinatorics and number theory rather than a single-step formula.
