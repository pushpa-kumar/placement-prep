# Bit Manipulation — Hard Practice Problems (CF 1700+, LeetCode Hard, CSES)

## Subset Enumeration

### Maximum Xor Subset
- Judge: CSES
- Link: https://cses.fi/problemset/task/3191
- Difficulty: CSES
- Subtopic: subset enumeration / XOR linear basis
- One-line description: Given an array of n integers, find the maximum XOR sum achievable by any subset of it.
- Why it's a good hard problem: The brute-force answer requires enumerating 2^n subsets; the real solution builds a linear (XOR) basis of the array via Gaussian elimination over GF(2), a core technique for reasoning about which XOR values are reachable from a set.

### Number of Subset Xors
- Judge: CSES
- Link: https://cses.fi/problemset/task/3211
- Difficulty: CSES
- Subtopic: subset enumeration / XOR linear basis
- One-line description: Given an array of n integers, count how many distinct XOR values can be formed by some subset.
- Why it's a good hard problem: Once you build the XOR linear basis, the answer is 2^(rank of the basis) — the problem tests whether you understand *why* the reachable-subset-XOR space is a vector space over GF(2), not just how to compute the max.

### Compatible Numbers
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/165/E
- Difficulty: CF 2200
- Subtopic: subset enumeration (Sum over Subsets / SOS DP)
- One-line description: Given n numbers each less than 2^22, for every number find another number in the array whose bitwise AND with it is zero, or report none exists.
- Why it's a good hard problem: This is the canonical Sum-over-Subsets (SOS) DP problem — you need to precompute, for every bitmask, whether some array element is a submask of it, propagating existence bit-by-bit over all 2^22 masks rather than enumerating subsets directly.

### Maximum Students Taking Exam
- Judge: LeetCode
- Link: https://leetcode.com/problems/maximum-students-taking-exam/
- Difficulty: LeetCode Hard (#1349)
- Subtopic: subset enumeration (bitmask DP)
- One-line description: Given a classroom grid with some broken seats, seat the maximum number of students such that no student can see an adjacent-left, adjacent-right, or diagonally-adjacent-front-row student cheating.
- Why it's a good hard problem: Requires enumerating valid seatings (bitmasks with no two adjacent bits) per row and, for each pair of consecutive rows, checking diagonal-compatibility bitmask conditions — real subset enumeration compounded across rows in a DP.

## XOR Properties

### Vasiliy's Multiset
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/706/D
- Difficulty: CF 1800
- Subtopic: XOR properties (binary trie)
- One-line description: Maintain a multiset of integers supporting insertion, deletion, and "find the maximum XOR of a given value x with any element currently in the multiset."
- Why it's a good hard problem: The standard approach is a binary trie over bit representations with per-node counters to support deletion, greedily walking the trie bit-by-bit from the most significant bit to maximize XOR — the foundational data structure for XOR-maximization problems.

### Maximum XOR With an Element From Array
- Judge: LeetCode
- Link: https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
- Difficulty: LeetCode Hard (#1707)
- Subtopic: XOR properties (binary trie, offline queries)
- One-line description: Given an array and queries of the form (x, m), find the maximum XOR of x with any array element that is <= m, or -1 if none qualifies.
- Why it's a good hard problem: Naive per-query trie search doesn't respect the <= m constraint, so queries and array elements must be sorted together and processed offline, inserting elements into the binary trie only once they are <= the current query's bound.

### Sum of XOR Functions
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1879/D
- Difficulty: CF 1700
- Subtopic: XOR properties
- One-line description: Given an array, compute the sum over all subarrays [l, r] of (XOR of the subarray) times (r - l + 1).
- Why it's a good hard problem: Summing a bitwise-XOR-derived quantity over all O(n^2) subarrays forces a divide-and-conquer-on-bits or trie-based approach that tracks, bit by bit, how many subarray XORs have that bit set, rather than any direct closed-form sum.
