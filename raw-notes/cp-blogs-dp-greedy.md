# Verified Codeforces blogs: Dynamic Programming & Greedy Algorithms

## Dynamic Programming

### [Tutorial] Non-trivial DP Tricks and Techniques
- Author: zscoder
- URL: https://codeforces.com/blog/entry/47764
- Topic: Dynamic Programming
- Subtopic: fundamentals / bitmask DP / general tricks
- Takeaway: A grab-bag of intermediate DP tricks — bitmask DP for subset states, pruning unreachable states to cut memory/time, "changing the object you DP over" when the natural state is infeasible, and binary-decomposition tricks for handling huge parameter ranges.

### SOS Dynamic Programming [Tutorial]
- Author: usaxena95
- URL: https://codeforces.com/blog/entry/45223
- Topic: Dynamic Programming
- Subtopic: bitmask DP (Sum over Subsets)
- Takeaway: Derives SOS DP step by step from a brute-force O(4^N) subset-sum-over-subsets solution, through an O(3^N) improvement, to the O(N·2^N) SOS DP that processes one bit position at a time.

### Digit DP
- Author: flash_7
- URL: https://codeforces.com/blog/entry/53960
- Topic: Dynamic Programming
- Subtopic: digit DP
- Takeaway: Introduces digit DP via the classic "count numbers in [a,b] where a digit appears exactly k times" problem, explaining the digit-by-digit construction with a tight/bound-tracking flag and reducing range queries to F(b) - F(a-1).

### Dp On Trees
- Author: AghaTizi
- URL: https://codeforces.com/blog/entry/63257
- Topic: Dynamic Programming
- Subtopic: tree DP
- Takeaway: Shows how to solve "count subtrees of size ≤ K" style tree DPs in O(nK) instead of O(nK^2) by only ever iterating the merge up to min(K, current subtree size), since states beyond the actual subtree size are always zero.

### The Ultimate Reroot Template
- Author: pajenegod
- URL: https://codeforces.com/blog/entry/124286
- Topic: Dynamic Programming
- Subtopic: tree DP / rerooting technique
- Takeaway: Presents a general "black box" template for rerooting DP (computing an answer rooted at every node) that reduces the usual case-heavy rerooting logic to a single reusable structure, achieving O(n log n).

### Dynamic Programming Optimizations
- Author: indy256
- URL: https://codeforces.com/blog/entry/8219
- Topic: Dynamic Programming
- Subtopic: DP optimization (Convex Hull Trick, Divide & Conquer optimization, Knuth's optimization)
- Takeaway: A reference table of classic DP-speedup techniques — two variants of Convex Hull optimization, D&C optimization, and Knuth's optimization — each with its recurrence form, applicability condition, and resulting complexity improvement.

## Greedy Algorithms

### [Tutorial] Matroid intersection in simple words
- Author: ATSTNG
- URL: https://codeforces.com/blog/entry/69287
- Topic: Greedy Algorithms
- Subtopic: matroid theory / greedy correctness proofs
- Takeaway: Explains matroids, bases, and circuits, then the Rado-Edmonds greedy algorithm for minimum-weight bases, and extends to matroid intersection via exchange graphs and augmenting paths — the general theory underlying why many greedy strategies are provably optimal.

### On "is this greedy or DP", forcing and rubber bands
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/106346
- Topic: Greedy Algorithms
- Subtopic: greedy vs. DP problem recognition
- Takeaway: Warns against the "forcing fallacy" of prematurely labeling a problem as greedy or DP; argues for deriving structural observations about the optimal solution first and letting the right technique fall out of that analysis.

### Lecture #3 — Exchange arguments (sorting with dp)
- Author: Errichto
- URL: https://codeforces.com/blog/entry/63533
- Topic: Greedy Algorithms
- Subtopic: exchange argument technique
- Takeaway: Shows the classic exchange-argument pattern: derive a comparator for the optimal order of items by comparing two adjacent swapped elements, sort by it, then (optionally) run a DP over the sorted order.

### Beginner's Guide to Greedy
- Author: dominique38
- URL: https://codeforces.com/blog/entry/150612
- Topic: Greedy Algorithms
- Subtopic: greedy proof techniques
- Takeaway: Focuses on rigorously proving greedy choices are optimal using proof by contradiction and induction, comparing the greedy solution against a hypothetical optimal one to show equivalence or non-inferiority.

### Greedy or Not? How to Identify Greedy Algorithms in Problems
- Author: AsLegend
- URL: https://codeforces.com/blog/entry/145048
- Topic: Greedy Algorithms
- Subtopic: greedy recognition heuristics / exchange arguments
- Takeaway: Lists concrete signals that a problem is greedy (sortable data, choices independent of future decisions, local optimality implying global optimality) and recommends exchange arguments to prove correctness, especially when a DP solution is too slow.
