# Game Theory (Nim / Sprague-Grundy) — Hard Practice Problems (CF 1700+, CSES)

## Nim

### Industrial Nim
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/15/C
- Difficulty: CF 2000
- Subtopic: Nim
- One-line description: n quarries each produce an arithmetic run of pile sizes (x_i, x_i+1, ..., x_i+m_i-1); playing standard Nim over the union of all these piles, determine the winner under optimal play.
- Why it's a good hard problem: With up to 10^5 ranges of up to 10^16 piles each, you cannot XOR piles individually — you must derive and apply the closed-form formula for the XOR of a full range of consecutive integers (based on the range length mod 4), then combine across ranges.

### Thanos Nim
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1147/C
- Difficulty: CF 1700
- Subtopic: Nim
- One-line description: With n (even) piles, each move a player must choose exactly n/2 nonempty piles and remove any positive number of stones from each independently; the player who cannot move (fewer than n/2 nonempty piles remain) loses — determine the winner.
- Why it's a good hard problem: The move rule breaks the standard XOR-of-piles Nim theory entirely; the actual winning condition is a slick parity argument on how many piles hold the current maximum value, which must be discovered rather than looked up.

### Stair Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/1099
- Difficulty: CSES
- Subtopic: Nim (Staircase Nim)
- One-line description: Balls sit on n numbered stairs; a move takes any positive number of balls from a stair k != 1 down to stair k-1, and the player who moves last wins — determine the winner for a given starting configuration.
- Why it's a good hard problem: This is the classic Staircase Nim reduction — the game is equivalent to ordinary Nim played only on the odd-numbered stairs (XOR of their ball counts), a non-obvious equivalence that must be proven and applied.

## Sprague-Grundy

### Not a Nim Problem
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/2004/E
- Difficulty: CF 2100
- Subtopic: Sprague-Grundy
- One-line description: n piles of stones; a move removes y stones from a pile of size x only if gcd(x, y) = 1, and the player unable to move loses — determine the winner.
- Why it's a good hard problem: The move restriction (only coprime removals allowed) means standard Nim XOR doesn't directly apply; you must compute the Grundy number of each pile size from its smallest prime factor structure and only then XOR them together.

### Game of Stones
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/768/E
- Difficulty: CF 2100
- Subtopic: Sprague-Grundy
- One-line description: n independent piles (sizes up to 60); a move removes any positive number of stones from a pile, but the exact same removal amount can never be reused on that same pile again — determine the winner.
- Why it's a good hard problem: The "no repeated move size per pile" constraint means a pile's Grundy number depends on its whole history of prior moves, not just its current size, requiring a bitmask/DP formulation of each pile's Grundy value before XOR-combining the independent games.

### Mojtaba and Arpa's game
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/850/C
- Difficulty: CF 2200
- Subtopic: Sprague-Grundy
- One-line description: Given a list of numbers, a move picks a prime power p^k dividing at least one number, and divides every number in the list divisible by p^k by p^k; the player unable to move loses — determine the winner.
- Why it's a good hard problem: Each number's prime factorization decomposes into independent per-prime subgames whose Grundy values must be derived from number-theoretic structure (exponent vectors), then combined via Sprague-Grundy XOR across primes and list elements — a genuinely layered application of the theorem.

### Grundy's Game
- Judge: CSES
- Link: https://cses.fi/problemset/task/2207
- Difficulty: CSES
- Subtopic: Sprague-Grundy
- One-line description: A heap of n coins; a move splits one heap into two nonempty heaps of different sizes, and the player who makes the last possible move wins — determine the winner.
- Why it's a good hard problem: Directly named for the theorem it teaches — computing the Grundy number of a heap requires recursively taking the mex over all ways to split it into two unequal heaps, the textbook mex/Grundy-number computation.
