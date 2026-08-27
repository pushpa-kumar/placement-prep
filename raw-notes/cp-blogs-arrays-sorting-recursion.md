# Verified Codeforces blogs: Arrays & Strings, Sorting & Binary Search, Recursion & Backtracking

## Arrays & Strings

### Two Pointers Algorithm
- Author: code_tle
- URL: https://codeforces.com/blog/entry/77127
- Topic: Arrays & Strings
- Takeaway: Explains the classic opposite-ends two-pointer technique for sorted arrays (O(n) pair-sum search by moving pointers based on whether the current sum is above/below target), then extends it to closest-pair-sum, merging two sorted arrays, and 3-sum-style triplet problems.

### Minimum in sliding window: two different but similar solutions
- Author: oversolver
- URL: https://codeforces.com/blog/entry/71687
- Topic: Arrays & Strings
- Takeaway: Gives two O(n) approaches to sliding-window minimum — the standard monotonic deque, and a lesser-known two-stack (prefix/suffix) trick — worth reading specifically to see that the deque isn't the only clean way to do it.

### Kadane's Algorithm — (Dynamic Programming) — For new Solvers!
- Author: Binary_ToothLess
- URL: https://codeforces.com/blog/entry/13713
- Topic: Arrays & Strings
- Takeaway: A clean, beginner-oriented derivation of Kadane's algorithm for maximum subarray sum in O(n) by tracking "best sum ending here" versus "best sum overall."

### An Introduction To Difference Arrays
- Author: arujbansal
- URL: https://codeforces.com/blog/entry/78762
- Topic: Arrays & Strings
- Takeaway: Shows how difference arrays support O(1) range updates (with a single O(n) prefix-sum pass to materialize final values) and generalizes to 2D — the natural companion/inverse trick to prefix sums for range-update-heavy problems.

### prefix sum
- Author: Noob_Coder_Anti
- URL: https://codeforces.com/blog/entry/81123
- Topic: Arrays & Strings
- Takeaway: Generalizes the prefix-sum idea beyond addition to any associative binary operator, useful for range queries (e.g. range XOR) where naive "PreSum[R] - PreSum[L-1]" subtraction needs an inverse operation to exist.

## Sorting & Binary Search

### The most comprehensive Binary Search lecture
- Author: Errichto
- URL: https://codeforces.com/blog/entry/67509
- Topic: Sorting & Binary Search
- Takeaway: A widely-cited, from-scratch treatment of binary search aimed at removing boundary/off-by-one guesswork, including binary search on monotonic predicates and on mountain-shaped (bitonic) arrays.

### Binary search implementation
- Author: pllk
- URL: https://codeforces.com/blog/entry/9901
- Topic: Sorting & Binary Search
- Takeaway: Presents an unusual step-halving binary search implementation (treat it like linear search but with exponentially shrinking steps n, n/2, n/4, ..., 1) that sidesteps fiddly bound adjustments and adapts cleanly to counting duplicate occurrences.

### Binary search on real values
- Author: Maxim
- URL: https://codeforces.com/blog/entry/63085
- Topic: Sorting & Binary Search
- Takeaway: A precision trick for binary-searching over floating-point answers: reinterpret the float/double's bit pattern as an integer and binary search on that integer directly, avoiding the usual epsilon-vs-iteration-count tradeoff.

### An alternative and very interesting approach on binary search
- Author: Pankin
- URL: https://codeforces.com/blog/entry/76182
- Topic: Sorting & Binary Search
- Takeaway: When the two branches of a binary search have very different costs, splits the range in a tuned 1:D ratio (solving D·ln(D) = K) rather than always halving, minimizing total work instead of just the number of steps.

### Parallel Binary Search [tutorial]
- Author: himanshujaju
- URL: https://codeforces.com/blog/entry/45578
- Topic: Sorting & Binary Search
- Takeaway: Explains how to answer many independent "binary search on the answer" queries at once by advancing all of their search ranges together level-by-level, turning O(Q log Q · log M) redundant work into a single O(Q log Q log M) sweep.

### Minimum swaps to sort an array
- Author: GRAYRHINO
- URL: https://codeforces.com/blog/entry/80983
- Topic: Sorting & Binary Search
- Takeaway: Derives the minimum-swap-count-to-sort via cycle decomposition of the target permutation (for distinct elements), and discusses why the problem becomes much harder — related to the NP-complete Feedback Arc Set — once duplicates are allowed.

## Recursion & Backtracking

### Backtracking [Guide]
- Author: AlRntn
- URL: https://codeforces.com/blog/entry/131470
- Topic: Recursion & Backtracking
- Takeaway: A genuine ground-up backtracking tutorial covering the check/generate-choices/recurse/undo template, worked through string generation, counting knight moves on a board, and a probability-based "WiFi" problem.

### Meet in the Middle (Topic Stream)
- Author: Errichto
- URL: https://codeforces.com/blog/entry/95571
- Topic: Recursion & Backtracking
- Takeaway: Walks through meet-in-the-middle across seven problems, showing how splitting a brute-force search space into two halves turns an infeasible O(2^n) into O(2^(n/2)), pushing feasible n from ~20 up to ~40.

### Algorithm Tour: Meet in the Middle
- Author: mingisminion
- URL: https://codeforces.com/blog/entry/105404
- Topic: Recursion & Backtracking
- Takeaway: Explains meet-in-the-middle concretely via the XOR-Paths problem — computing partial results from both endpoints toward a common midpoint and combining them — with accompanying C++ implementation.

### Introduction to DP with Bitmasking
- Author: kartik8800
- URL: https://codeforces.com/blog/entry/81516
- Topic: Recursion & Backtracking
- Takeaway: Covers representing subsets as bitmasks and enumerating/transitioning between them for exponential state-space search (TSP, job assignment) — the subset-generation half of bitmask-driven backtracking/DP.

### Tips and tricks for solving permutation problems
- Author: peltorator
- URL: https://codeforces.com/blog/entry/88283
- Topic: Recursion & Backtracking
- Takeaway: An informal but genuinely useful mental trick from an LGM: track permutation swaps visually (physical cards / redrawn cycle diagrams) instead of pure index algebra, which helps avoid common bugs when generating or backtracking over permutations.

### Derangement Generation of an Array [Tutorial]
- Author: lazyneuron
- URL: https://codeforces.com/blog/entry/66176
- Topic: Recursion & Backtracking
- Takeaway: A constructive O(n log n) way to generate a derangement (no element stays in its original position) via sort-with-index-tracking plus a rotation by the maximum frequency — avoids generate-and-reject backtracking entirely.
