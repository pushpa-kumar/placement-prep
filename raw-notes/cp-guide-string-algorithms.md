# String Algorithms — Hard Practice Problems (CF 1700+, LeetCode Hard, CSES)

## KMP

### Shortest Palindrome
- Judge: LeetCode
- Link: https://leetcode.com/problems/shortest-palindrome/
- Difficulty: LeetCode Hard (#214)
- Subtopic: KMP
- One-line description: Given a string s, add characters in front of it to make it a palindrome and return the shortest such palindrome.
- Why it's a good hard problem: The intended O(n) solution runs the KMP failure function on `s + '#' + reverse(s)` to find the longest palindromic prefix of s, a non-obvious reduction from "make palindrome" to "prefix function."

## Z-function

### Sum of Scores of Built Strings
- Judge: LeetCode
- Link: https://leetcode.com/problems/sum-of-scores-of-built-strings/
- Difficulty: LeetCode Hard (#2223)
- Subtopic: Z-function
- One-line description: For a string s, define score(i) as the length of the longest common prefix between s and the suffix of s ending at i; return the sum of scores over all suffixes.
- Why it's a good hard problem: The score function is exactly the Z-array by definition, so the problem is a direct, unforgiving test of correctly implementing the Z-function in O(n) rather than the naive O(n^2) comparison.

## String Hashing

### Prefix-Suffix Palindrome (Hard version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1326/D2
- Difficulty: CF 1800
- Subtopic: string hashing
- One-line description: Given a string, find the longest string formed by concatenating a prefix and a suffix of it (each possibly empty, non-overlapping) that is a palindrome.
- Why it's a good hard problem: Requires peeling off a matching outer prefix/suffix pair with two pointers, then using double hashing to find the longest palindromic prefix or suffix of the remaining middle in O(1) per check, combining hashing with careful greedy/two-pointer logic.

### Palindrome Queries
- Judge: CSES
- Link: https://cses.fi/problemset/task/2420
- Difficulty: CSES
- Subtopic: string hashing
- One-line description: Given a string, process point updates (change a character) and range queries (is the substring from a to b a palindrome) online.
- Why it's a good hard problem: Answering palindrome queries under updates forces maintaining two Fenwick-tree-based polynomial hashes (forward and reversed) so any substring's forward and reverse hash can be compared in O(log n), a step beyond static hashing.

## Manacher's Algorithm

### All Palindromes
- Judge: CSES
- Link: https://cses.fi/problemset/task/3138
- Difficulty: CSES
- Subtopic: Manacher's
- One-line description: For every position in a string, compute the length of the longest palindrome that ends exactly at that position.
- Why it's a good hard problem: Manacher's algorithm directly gives the longest palindrome centered at each position, but converting that into "longest palindrome ending at each position" requires an extra non-trivial transformation of the radius array rather than a direct read-off.

## Trie for Strings

### Counting Patterns
- Judge: CSES
- Link: https://cses.fi/problemset/task/2103
- Difficulty: CSES
- Subtopic: trie / Aho-Corasick
- One-line description: Given a text string and k patterns, count for each pattern how many times it occurs in the text.
- Why it's a good hard problem: With many patterns, per-pattern KMP is too slow; the intended solution builds a trie of all patterns with Aho-Corasick failure links to process the text in a single O(n + sum|pattern|) pass, a genuine multi-pattern-matching data structure rather than a single-string trick.

## Suffix Array / Automaton

### Martian Strings
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/149/E
- Difficulty: CF 2300
- Subtopic: suffix array / suffix automaton
- One-line description: Given two strings s and t, find the longest substring of s that can be split into two parts, the first being a substring of t and the second also being a substring of t.
- Why it's a good hard problem: Requires building suffix structures (suffix array/automaton or hashing-based binary search) over both strings to compute longest-common-prefix/suffix arrays efficiently, then combining two independent LCP computations to search over all split points.
