# String Algorithms — Extra Hard Practice (Suffix Automaton, Aho-Corasick, Palindromic Tree)

All problems below were verified live via the Codeforces public API (`problemset.problems`), the CSES problem pages, and LeetCode's public GraphQL API (topicTags field). No invented problems/ratings.

## Suffix Automaton

### Substring Order I
- Judge: CSES
- Link: https://cses.fi/problemset/task/2108
- Difficulty: CSES (String Algorithms, hard section)
- Subtopic: Suffix Automaton
- One-line description: Given a string of length up to 1e5, find the k-th smallest string among all of its *distinct* substrings in lexicographic order.
- Why it's a good hard problem: Forces you to walk the suffix automaton's DAG while counting distinct substrings reachable from each state (endpos-class sizes), combining SAM construction with a counting-DP over the link tree.

### Substring Distribution
- Judge: CSES
- Link: https://cses.fi/problemset/task/2110
- Difficulty: CSES (String Algorithms, hard section)
- Subtopic: Suffix Automaton
- One-line description: For every length 1..n, print the number of distinct substrings of that exact length.
- Why it's a good hard problem: Requires turning per-state (len[state] - len[link[state]]) ranges from the suffix automaton into a difference array over lengths — a clean test of understanding what each SAM state actually represents.

### Longest Duplicate Substring
- Judge: LeetCode
- Link: https://leetcode.com/problems/longest-duplicate-substring/
- Difficulty: LeetCode Hard (topicTags include "Suffix Automaton", "Suffix Array", "Rolling Hash")
- Subtopic: Suffix Automaton
- One-line description: Find the longest substring of a given string (up to 3*10^4 chars) that occurs at least twice (occurrences may overlap).
- Why it's a good hard problem: The suffix-automaton solution (find the deepest state with more than one occurrence, i.e. |endpos| > 1) is a direct, elegant alternative to the binary-search+hashing approach most people default to, and LeetCode's own tag confirms SAM as an intended technique.

### Good Substrings
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/316/G2
- Difficulty: CF rating 2200 (easy subtask of a 3-part problem; G3 harder version is rated 2400)
- Subtopic: Suffix Automaton
- One-line description: Each of the 26 letters has a cost and a bad/good flag; count distinct substrings whose total letter cost falls in [minCost, maxCost] and that contain no "bad" letters.
- Why it's a good hard problem: Classic "count distinct substrings satisfying a per-letter predicate" — you build the SAM and then do a DFS/DP over the suffix-link tree tracking cumulative cost per state, a very common competitive pattern.

### Cyclical Quest
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/235/C
- Difficulty: CF rating 2700
- Subtopic: Suffix Automaton
- One-line description: Given a big string and many query strings, for each query count how many times the query and all of its cyclic rotations occur as substrings of the big string, weighted by rotation count.
- Why it's a good hard problem: Requires building a suffix automaton once, then for each query string of doubled length walking the SAM incrementally while resetting on mismatch and correctly deduplicating occurrence counts per SAM state per query — a genuinely tricky online-traversal exercise.

### Little Elephant and Strings
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/204/E
- Difficulty: CF rating 2800
- Subtopic: Suffix Automaton
- One-line description: Given n strings, for each string find the length of its longest substring that also occurs (as a substring) in at least k of the n strings.
- Why it's a good hard problem: A generalized/multi-string suffix automaton (or generalized suffix tree) problem requiring per-state counts of "how many of the n original strings reach this state," a step up from single-string SAM problems.

### Cool Slogans
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/700/E
- Difficulty: CF rating 3300
- Subtopic: Suffix Automaton
- One-line description: Find the longest chain of substrings s1, s2, ..., sk of a given string such that each si+1 is a substring of si occurring at least twice inside it (overlaps allowed).
- Why it's a good hard problem: The canonical hard suffix-automaton problem — you build the SAM's suffix-link tree, and for every pair of parent/child states merge their sets of "positions where the substring occurs at least twice" using small-to-large merging over sorted endpos sets, an advanced SAM technique.

## Aho-Corasick Multi-Pattern Matching

### Counting Patterns
- Judge: CSES
- Link: https://cses.fi/problemset/task/2103
- Difficulty: CSES (String Algorithms, hard section)
- Subtopic: Aho-Corasick Multi-Pattern Matching
- One-line description: Given a text and up to 5*10^5 total-length patterns, count for each pattern how many positions in the text it occurs at.
- Why it's a good hard problem: The direct textbook use case for the Aho-Corasick automaton — build it over all patterns, run the text through once, and use fail-link (suspect link) subtree sums to get each pattern's occurrence count in O(n + total pattern length).

### Pattern Positions
- Judge: CSES
- Link: https://cses.fi/problemset/task/2104
- Difficulty: CSES (String Algorithms, hard section)
- Subtopic: Aho-Corasick Multi-Pattern Matching
- One-line description: Same setup as Counting Patterns, but report the first (1-indexed) position at which each pattern occurs in the text, or -1 if it never occurs.
- Why it's a good hard problem: Pushes past simple counting — you must propagate "earliest hit" information up the automaton's fail-link tree (or down, depending on formulation) instead of just summing counts, testing a deeper understanding of the automaton's structure.

### Stream of Characters
- Judge: LeetCode
- Link: https://leetcode.com/problems/stream-of-characters/
- Difficulty: LeetCode Hard (topicTag: "Aho–Corasick Algorithm", confirmed via LeetCode's own tag data)
- Subtopic: Aho-Corasick Multi-Pattern Matching
- One-line description: Design a data structure that, given up to 2*10^4 words, supports streaming individual characters and reports whether any suffix of the stream so far matches one of the words.
- Why it's a good hard problem: Because queries arrive online character-by-character rather than as a fixed text, the natural high-performance solution builds an Aho-Corasick automaton over the *reversed* words and walks it incrementally — a nice twist on the standard offline multi-pattern-matching setup.

### String Set Queries
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/710/F
- Difficulty: CF rating 2400
- Subtopic: Aho-Corasick Multi-Pattern Matching
- One-line description: Online queries that add a string to a set, remove a string from the set, or ask for the total number of occurrences (over all strings currently in the set) inside a given text — must be answered before reading the next query.
- Why it's a good hard problem: The classic "dynamic Aho-Corasick" problem — since the automaton can't be rebuilt from scratch per query, you maintain a small number of static Aho-Corasick automata of geometrically increasing size and periodically rebuild, an important amortized-rebuild trick.

### Genetic engineering
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/86/C
- Difficulty: CF rating 2500
- Subtopic: Aho-Corasick Multi-Pattern Matching
- One-line description: Count DNA sequences of length n (over a 4-letter alphabet) such that every position is covered by at least one occurrence of a given collection of up to 10 short patterns.
- Why it's a good hard problem: A classic Aho-Corasick + DP problem — states of the DP are (position in string, current automaton node, how far ahead is currently "covered"), forcing you to combine automaton transitions with a nontrivial coverage-tracking DP.

### Death DBMS
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1437/G
- Difficulty: CF rating 2600
- Subtopic: Aho-Corasick Multi-Pattern Matching
- One-line description: Maintain a database of names (patterns) each with a suspicion value that can be updated; given a query string, find the maximum suspicion value among all database names occurring as a substring of it.
- Why it's a good hard problem: One of the most cited Aho-Corasick data-structure problems — build the automaton once over all names, then use small-to-large merging of multisets (or segment tree merging) along the fail-link tree so that point updates and substring-max queries are both efficient.

## Palindromic Tree (Eertree)

### All Palindromes
- Judge: CSES
- Link: https://cses.fi/problemset/task/3138
- Difficulty: CSES (String Algorithms)
- Subtopic: Palindromic Tree (Eertree)
- One-line description: For every position in a string of length up to 2*10^5, output the length of the longest palindrome that *ends* at that position.
- Why it's a good hard problem: This is the most direct possible exercise of an Eertree's incremental-insertion behavior — as you insert characters one at a time, the "last" pointer after each insertion IS the longest palindromic suffix ending there, so this problem essentially asks you to implement the core Eertree construction correctly.

### Palindrome Queries
- Judge: CSES
- Link: https://cses.fi/problemset/task/2420
- Difficulty: CSES (String Algorithms, hard section)
- Subtopic: Palindromic Tree (Eertree)
- One-line description: Process up to 2*10^5 operations on a string: point-update a character, or check whether a given substring is currently a palindrome.
- Why it's a good hard problem: Combines palindrome-testing theory with a dynamic setting (point updates), so it's excellent practice for reasoning about which palindrome techniques (hashing, Eertree-adjacent structures) survive character updates and which require full rebuilds.

### Hossam and (sub-)palindromic tree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1771/D
- Difficulty: CF rating 2100
- Subtopic: Palindromic Tree (Eertree)
- One-line description: On a tree with a letter at every vertex, for every path between two vertices find the length of the longest palindromic *subsequence* of the letters along that path.
- Why it's a good hard problem: Literally named after the palindromic-tree structure, it forces you to combine palindrome-subsequence DP with small-to-large tree-DP merging across all O(n^2) paths, a genuinely advanced composition of two hard techniques.

### Palindrome Degree
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/7/D
- Difficulty: CF rating 2200
- Subtopic: Palindromic Tree (Eertree)
- One-line description: For every prefix of a string, define its "degree" recursively (a prefix has degree k if its first half is itself a palindrome of degree k-1); output the sum of all prefix degrees.
- Why it's a good hard problem: A classic recursive-palindrome-structure problem — efficient solutions rely on quickly testing "is this prefix a palindrome" and jumping through nested palindromic halves, which is exactly the kind of suffix-link jumping an Eertree (or Eertree-style hashing) supports natively.

### Palindrome Partition
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/932/G
- Difficulty: CF rating 2900
- Subtopic: Palindromic Tree (Eertree)
- One-line description: Count the number of ways to split a string into an even number of non-empty parts p1..pk such that each pi is "special-equal" (equal, or equal after reversal) to its mirror part pk+1-i.
- Why it's a good hard problem: The textbook hard application of the palindromic tree/Eertree in competitive programming — the "special-equal" check across mirrored parts reduces to querying palindromic structure via the Eertree combined with hashing and a counting DP, and it's routinely cited as *the* problem to test real Eertree mastery.

### Palisection
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/17/E
- Difficulty: CF rating 2900
- Subtopic: Palindromic Tree (Eertree)
- One-line description: Count the number of pairs of palindromic substrings (of length >= 2) of a given string that intersect (share at least one common position).
- Why it's a good hard problem: A famous, old (Codeforces Beta Round 7) hard palindrome-counting problem — you need to enumerate/count all palindromic substrings efficiently (Eertree or Manacher-derived), then combine per-position counts with a running-sum trick to count intersecting pairs without double counting, testing both palindrome enumeration and careful combinatorial counting.
