# FFT / NTT — curated hard practice problems (Codeforces API; CSES has no dedicated FFT problem)

## Polynomial Multiplication

### The Child and Binary Tree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/438/E
- Difficulty: 3100
- Subtopic: polynomial multiplication (generating functions)
- One-line description: Count the number of distinct vertex-weighted rooted binary trees achieving each total weight from 1 to m, given an allowed set of vertex weights.
- Why it's a good hard problem: Requires setting up a generating-function functional equation and solving it with polynomial inverse/sqrt via NTT (Newton's iteration), well beyond a single convolution call.

### Thief in a Shop
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/632/E
- Difficulty: 2400
- Subtopic: polynomial multiplication (fast exponentiation)
- One-line description: Determine every total cost achievable by picking exactly k items (with repetition) from n item types with given costs.
- Why it's a good hard problem: The natural formulation needs a polynomial raised to the k-th power efficiently, forcing repeated FFT-based multiplication with careful complexity control (divide-and-conquer or binary exponentiation of polynomials).

### Lucky Tickets
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1096/G
- Difficulty: 2400
- Subtopic: polynomial multiplication (convolution counting)
- One-line description: Count n-digit tickets using only a given set of allowed digits where the digit sum of the first half equals the digit sum of the second half.
- Why it's a good hard problem: Reduces to computing a polynomial raised to a power (digit-sum generating function) and matching coefficients, a standard but non-trivial NTT counting application.

## Convolution for String Matching

### Fuzzy Search
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/528/D
- Difficulty: 2500
- Subtopic: string matching via convolution
- One-line description: Count positions where a pattern matches a text, allowing each pattern character to match within a tolerance window of k positions.
- Why it's a good hard problem: The classic introduction to using FFT for approximate/wildcard string matching by encoding character-equality convolutions per alphabet symbol.

### Rusty String
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/827/E
- Difficulty: 2700
- Subtopic: string matching via convolution
- One-line description: Given a string with wildcard characters that can be filled with one of two letters, determine which values are valid periods of the completed string.
- Why it's a good hard problem: Needs a clever cost function (e.g., cos/sin encoding of the two-letter choice) fed into FFT to test all candidate periods simultaneously instead of one at a time.

### Yet Another String Matching Problem
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/954/I
- Difficulty: 2200
- Subtopic: string matching via convolution
- One-line description: Find, for every alignment of two strings, the minimum number of global character-relabeling operations needed to make the overlapping substrings equal.
- Why it's a good hard problem: Combines a union-find/relabeling argument with FFT to evaluate the cost across all shifts in O(n log n) instead of the naive O(n^2).

## Counting via Convolution

### Nikita and Order Statistics
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/993/E
- Difficulty: 2300
- Subtopic: counting via convolution
- One-line description: For every k from 0 to n, count the number of subarrays containing exactly k elements less than a given value x.
- Why it's a good hard problem: Translating the subarray condition into prefix-sum differences and counting them for every k simultaneously requires expressing the count as a self-convolution.

---
Note: CSES's Advanced Techniques / Graph Algorithms sections were checked directly and contain no FFT/NTT/polynomial-multiplication problem (e.g. "Polynomial Queries" is a segment-tree range-update problem, not FFT-related), so this topic is sourced entirely from Codeforces.
