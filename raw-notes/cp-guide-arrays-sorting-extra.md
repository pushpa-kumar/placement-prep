# CP Guide — Extra Problems (Arrays & Sorting subtopics)

All problems below were verified as real via the Codeforces public API
(`https://codeforces.com/api/problemset.problems`, cross-checked per-problem
tags/ratings) or the LeetCode public GraphQL API (`https://leetcode.com/graphql`,
`question(titleSlug)` query returning `questionFrontendId`/`title`/`difficulty`).
No invented problems or ratings.

## Difference Arrays

### Range Increments
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/174/C
- Difficulty: 1800
- Subtopic: Difference Arrays
- One-line description: Given the final array state (all elements start at 0), reconstruct the minimum number of `rangeIncrement(l, r)` calls (each adds 1 to every element in `[l, r]`) that could have produced it.
- Why it's a good hard problem: It is the textbook difference-array problem — the answer is exactly the sum of positive jumps in the difference array, and reconstructing actual (l, r) calls requires a stack-based matching on top of the diff-array insight.

### Too Many Segments (hard version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1249/D2
- Difficulty: 1800
- Subtopic: Difference Arrays
- One-line description: Given n segments on a line and a limit k, remove the minimum number of segments so that no integer point is covered by more than k segments.
- Why it's a good hard problem: Requires building a difference array of coverage counts, sweeping left to right, and greedily evicting the segment with the farthest right endpoint (via a multiset/heap) whenever the running coverage from the diff array exceeds k.

### Clear the Multiset
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1400/E
- Difficulty: 2200
- Subtopic: Difference Arrays
- One-line description: Given counts a_1..a_n of a multiset containing a_i copies of value i, find the minimum number of operations (remove one occurrence of every value in a contiguous range, or remove x copies of one value) to empty the multiset.
- Why it's a good hard problem: Generalizes the "min ops = sum of positive differences in the difference array" idea from Range Increments into a divide-and-conquer over the minimum value, making it a strong step up in difficulty while keeping the difference-array insight central.

### Addition on Segments
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/981/E
- Difficulty: 2200
- Subtopic: Difference Arrays
- One-line description: Starting from an all-zero array, given q range-add operations (add x_i to [l_i, r_i]), determine every value y that the array maximum can equal after applying some subset of the operations.
- Why it's a good hard problem: Combines difference-array range updates with a bitset subset-sum DP over "how much can the max at each position be pushed up", forcing you to reason about the interaction between range updates and reachability.

### Minimum Operations to Make Array Equal to Target
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/
- Difficulty: Hard (LeetCode #3454)
- Subtopic: Difference Arrays
- One-line description: Given `nums` and `target` of the same length, find the minimum number of operations to turn `nums` into `target`, where one operation increments or decrements a contiguous subarray by 1.
- Why it's a good hard problem: Direct generalization of the classic "minimum range-increment operations" difference-array problem to signed deltas, requiring you to track running sums of positive and negative jumps in the difference array of `target - nums`.

## Two-Pointer Partitioning

### Array Partition
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1454/F
- Difficulty: 2100
- Subtopic: Two-Pointer Partitioning
- One-line description: Split an array into three non-empty contiguous parts x, y, z such that max of the first part equals min of the second part equals max of the third part, or report impossible.
- Why it's a good hard problem: Solved by scanning prefix/suffix max and min arrays with pointers that advance the boundary positions in one pass, an in-place multi-region partition search analogous to Dutch-flag-style boundary maintenance.

### Range and Partition
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1630/B
- Difficulty: 1800
- Subtopic: Two-Pointer Partitioning
- One-line description: Choose a value range [x, y] and split the array into k contiguous subarrays such that every subarray has strictly more elements inside [x, y] than outside, minimizing y − x.
- Why it's a good hard problem: Requires partitioning the whole array into an "inside/outside" two-coloring driven by a chosen threshold range, then greedily walking the array with pointers to carve out valid subarrays — a direct extension of two-way in-place partitioning.

### Recover the Original Array
- Judge: LeetCode
- Link: https://leetcode.com/problems/recover-the-original-array/
- Difficulty: Hard
- Subtopic: Two-Pointer Partitioning
- One-line description: Given an array formed by interleaving `arr[i]-k` and `arr[i]+k` for an unknown k, recover a valid original array `arr`.
- Why it's a good hard problem: After sorting, you must partition the multiset into a "low" group and a "high" group that are a perfect k-shifted match of each other, using a two-pointer/multiset scan that mirrors the low/high region bookkeeping of Dutch-flag partitioning.

### Partition Array Into Two Arrays to Minimize Sum Difference
- Judge: LeetCode
- Link: https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
- Difficulty: Hard
- Subtopic: Two-Pointer Partitioning
- One-line description: Partition a 2n-length array into two arrays of size n each so that the absolute difference of their sums is minimized.
- Why it's a good hard problem: Requires splitting the array into two balanced halves via meet-in-the-middle, then two-pointer scanning across sorted subset-sum lists to find the closest complementary partition — a genuine in-place partition-search problem at Hard difficulty.

## Monotonic Deque

### Sliding Window Maximum
- Judge: LeetCode
- Link: https://leetcode.com/problems/sliding-window-maximum/
- Difficulty: Hard (LeetCode #239)
- Subtopic: Monotonic Deque
- One-line description: Given an array and window size k, return the maximum of every contiguous window of size k as it slides across the array.
- Why it's a good hard problem: The canonical monotonic-deque problem — LeetCode itself tags it "Monotonic Queue" and rates it Hard because the O(n) deque invariant (pop smaller-from-back, pop out-of-window-from-front) is easy to get subtly wrong.

### Constrained Subsequence Sum
- Judge: LeetCode
- Link: https://leetcode.com/problems/constrained-subsequence-sum/
- Difficulty: Hard (LeetCode #1425)
- Subtopic: Monotonic Deque
- One-line description: Choose a subsequence where consecutive chosen indices are at most k apart, maximizing the sum of the subsequence.
- Why it's a good hard problem: A DP where `dp[i] = a[i] + max(0, dp[i-k..i-1])` must be computed online, which is only fast with a monotonic deque holding the best dp value in the trailing window — a genuine deque-optimized DP.

### Shortest Subarray with Sum at Least K
- Judge: LeetCode
- Link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
- Difficulty: Hard (LeetCode #862)
- Subtopic: Monotonic Deque
- One-line description: Find the length of the shortest contiguous subarray whose sum is at least K (array may contain negative numbers).
- Why it's a good hard problem: Negative numbers break the standard two-pointer sliding window; the correct O(n) solution keeps a monotonically increasing deque of prefix-sum indices and is a classic "why basic sliding window fails, monotonic deque saves it" teaching example.

### Watching Fireworks is Fun
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/372/C
- Difficulty: 2100
- Subtopic: Monotonic Deque
- One-line description: You move along a street of n sections at speed ≤ d; for each of m fireworks launched at position a_i giving happiness b_i − |a_i − x|, choose your position over time to maximize total happiness.
- Why it's a good hard problem: The DP transition for each firework is a sliding-window maximum over the previous DP row (window width grows with d·Δt), so the O(n·m) DP only becomes efficient once you maintain the window max with a monotonic deque.

### Pictures with Kittens (hard version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1077/F2
- Difficulty: 2100
- Subtopic: Monotonic Deque
- One-line description: Choose exactly x pictures from n so that every window of k consecutive pictures contains at least one chosen picture, maximizing total beauty of chosen pictures.
- Why it's a good hard problem: The 2D DP `dp[i][j]` (best value picking j pictures from first i, last chosen within k of i) needs a sliding-window maximum over a fixed-size range per layer, a standard but non-trivial monotonic-deque DP optimization.

## Merge Intervals

### Data Stream as Disjoint Intervals
- Judge: LeetCode
- Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
- Difficulty: Hard
- Subtopic: Merge Intervals
- One-line description: Design a data structure that, given a stream of integers, can add a value and return the current set of disjoint intervals covering all values seen so far.
- Why it's a good hard problem: Requires an online insert-and-merge-interval routine (find neighboring intervals to merge with a new point, splice them together) that must stay efficient across repeated insertions rather than a one-shot batch merge.

### Range Module
- Judge: LeetCode
- Link: https://leetcode.com/problems/range-module/
- Difficulty: Hard
- Subtopic: Merge Intervals
- One-line description: Design a data structure to track ranges of integers, supporting adding a range, removing a range, and querying whether every integer in a range is currently tracked, with ranges auto-merging.
- Why it's a good hard problem: A direct generalization of "merge intervals" into a full mutable interval-set data structure supporting add/remove/query, forcing careful handling of partial overlaps and interval splitting, not just a static merge.

### Count Integers in Intervals
- Judge: LeetCode
- Link: https://leetcode.com/problems/count-integers-in-intervals/
- Difficulty: Hard
- Subtopic: Merge Intervals
- One-line description: Design a data structure that supports adding an interval of integers and querying the total count of distinct integers currently covered by all added intervals (with automatic merging of overlaps).
- Why it's a good hard problem: Maintaining a dynamically merged set of intervals while tracking total covered length under repeated insertions is a harder, stateful version of the static "merge intervals" exercise.

### Minimum Interval to Include Each Query
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-interval-to-include-each-query/
- Difficulty: Hard
- Subtopic: Merge Intervals
- One-line description: Given a list of intervals and a list of query points, for each query find the size of the smallest interval that contains it.
- Why it's a good hard problem: Requires sorting intervals and queries together and sweeping with a min-heap keyed by interval size, a technique that builds directly on interval-sorting fundamentals but adds an offline sweep over queries.

### The Union of k-Segments
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/612/D
- Difficulty: 1800
- Subtopic: Merge Intervals
- One-line description: Given n segments and an integer k, find the minimal set of disjoint segments whose union is exactly the set of points covered by at least k of the input segments.
- Why it's a good hard problem: Combines a coverage-counting sweep (via segment endpoint events) with merging the resulting "covered ≥ k times" points back into a minimal list of maximal merged segments.

## Ternary Search on Unimodal Functions

### Weakness and Poorness
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/578/C
- Difficulty: 2000
- Subtopic: Ternary Search on Unimodal Functions
- One-line description: Find a real number x minimizing the "weakness" of the sequence a_i − x, where weakness is the maximum absolute subarray sum (poorness) over all segments.
- Why it's a good hard problem: A pure, classic ternary-search-on-a-real-valued-convex-function problem — the weakness as a function of x is provably convex, and each evaluation itself needs a Kadane-style max/min subarray sum pass.

### Restorer Distance
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1355/E
- Difficulty: 2100
- Subtopic: Ternary Search on Unimodal Functions
- One-line description: Given N pillars of bricks with costs to add, remove, or move a brick, find the minimum cost to make all pillars the same height.
- Why it's a good hard problem: The total cost as a function of the target height is convex/unimodal, so the optimal height is found via ternary search, with each evaluation requiring careful accounting of how many bricks can be "moved" versus added/removed.

### Maximize!
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/939/E
- Difficulty: 1800
- Subtopic: Ternary Search on Unimodal Functions
- One-line description: Maintain a growing multiset (with a "add" query keeping it sorted) and, for "query" operations, find the subset maximizing max(s) minus the average of s.
- Why it's a good hard problem: For a fixed maximum element, the value max − average(s) is unimodal in how many of the smallest remaining elements are included, so each query is answered via ternary search on that count, combined with maintained prefix sums.

### Searching Local Minimum
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1479/A
- Difficulty: 1700
- Subtopic: Ternary Search on Unimodal Functions
- One-line description: Interactively query values of a hidden permutation a_1..a_n (with a_0 = a_{n+1} = +infinity) to find any local minimum index using at most 100 queries.
- Why it's a good hard problem: Requires recognizing the ternary-search-style halving argument that works even though the array isn't sorted or fully unimodal — at least one boundary always leads toward a local minimum, so you can discard half the search space each query.

### Gift Set
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1538/G
- Difficulty: 2100
- Subtopic: Ternary Search on Unimodal Functions
- One-line description: Given x red and y blue candies, and set sizes (a,b), find the maximum number of gift sets you can form where each set uses either (a red, b blue) or (a blue, b red) candies.
- Why it's a good hard problem: The maximum achievable count as a function of how many sets use each orientation is unimodal, so binary/ternary search over the split combined with a feasibility check yields the answer — a good example of recognizing unimodality in a non-obvious counting setup.

## Custom Comparators & Multi-Key Sorting

### Complete the Projects (easy version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1203/F1
- Difficulty: 2100
- Subtopic: Custom Comparators & Multi-Key Sorting
- One-line description: Given n projects, each requiring rating a_i to start and changing rating by b_i (positive or negative) on completion, determine if there's an order to complete all projects without the rating ever going negative.
- Why it's a good hard problem: The classic two-key exchange-argument sort — positive-b projects must be sorted ascending by requirement, negative-b projects sorted descending by (a_i + b_i) — and proving the comparator correct requires a genuine exchange-argument proof, not just intuition.

### Complete the Projects (hard version)
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1203/F2
- Difficulty: 2300
- Subtopic: Custom Comparators & Multi-Key Sorting
- One-line description: Same setup as the easy version, but now maximize the number of projects completed rather than requiring all of them.
- Why it's a good hard problem: Builds on the same exchange-argument multi-key sort, then layers a knapsack-style DP with a greedy "remove the worst negative project so far" trick on top, testing whether the sorting insight generalizes under a harder objective.

### Maximum Performance of a Team
- Judge: LeetCode
- Link: https://leetcode.com/problems/maximum-performance-of-a-team/
- Difficulty: Hard
- Subtopic: Custom Comparators & Multi-Key Sorting
- One-line description: Given engineers with speed and efficiency ratings, choose at most k of them to maximize (sum of chosen speeds) × (minimum chosen efficiency).
- Why it's a good hard problem: Requires sorting engineers by efficiency descending (the comparator key that "unlocks" a correct greedy), then scanning with a min-heap on speed — a clean example of choosing the right sort key to make a greedy/heap approach work.

### Minimum Cost to Hire K Workers
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
- Difficulty: Hard
- Subtopic: Custom Comparators & Multi-Key Sorting
- One-line description: Given workers with quality and minimum wage-to-quality-ratio requirements, hire exactly k workers minimizing total cost while paying everyone proportionally to quality at the highest required ratio among the hired.
- Why it's a good hard problem: The workers must be sorted by wage/quality ratio (a derived comparator key, not a raw field) before a max-heap sweep on quality — a strong example of engineering a custom sort key from a ratio constraint.

### Course Schedule III
- Judge: LeetCode
- Link: https://leetcode.com/problems/course-schedule-iii/
- Difficulty: Hard
- Subtopic: Custom Comparators & Multi-Key Sorting
- One-line description: Given courses with a duration and a deadline, find the maximum number of courses you can take without missing any deadline.
- Why it's a good hard problem: Requires sorting courses by deadline (not duration) to process greedily, then using a max-heap to retroactively swap out the longest course taken so far whenever a deadline would be violated — a multi-key greedy where picking the wrong sort key breaks correctness.

## Order Statistics / Quickselect

### Sum of Medians
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/85/D
- Difficulty: 2300
- Subtopic: Order Statistics / Quickselect
- One-line description: Maintain a dynamic set under add/delete operations, and answer queries for the sum of the medians (3rd element) of every consecutive group of 5 sorted elements — motivated explicitly by the median-of-medians k-th-order-statistic algorithm.
- Why it's a good hard problem: The problem statement itself opens by describing the median-of-medians order-statistics algorithm, then asks you to build a dynamic order-statistics structure (Fenwick tree with binary search, or balanced BST) to answer the aggregate query online.

### Median of Two Sorted Arrays
- Judge: LeetCode
- Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
- Difficulty: Hard (LeetCode #4)
- Subtopic: Order Statistics / Quickselect
- One-line description: Given two sorted arrays of sizes m and n, find the median of the two arrays combined in O(log(m+n)) time.
- Why it's a good hard problem: The canonical "find the k-th order statistic without merging" problem — the O(log(m+n)) solution is a partition/binary-search generalization of quickselect across two sorted arrays, and getting the partition invariant right is notoriously tricky.

### Kth Smallest Product of Two Sorted Arrays
- Judge: LeetCode
- Link: https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
- Difficulty: Hard
- Subtopic: Order Statistics / Quickselect
- One-line description: Given two sorted arrays, find the k-th smallest product formed by picking one element from each array.
- Why it's a good hard problem: Extends the order-statistics-via-counting technique (binary search on the answer value, counting how many pairwise products are ≤ mid) to a setting complicated by mixed signs, requiring careful case analysis on the sign of each array's elements.

### Find K-th Smallest Pair Distance
- Judge: LeetCode
- Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
- Difficulty: Hard
- Subtopic: Order Statistics / Quickselect
- One-line description: Given an array of integers, find the k-th smallest absolute difference among all pairs of elements.
- Why it's a good hard problem: A classic order-statistics-by-counting problem — binary search on the candidate distance and count qualifying pairs with a two-pointer sweep on the sorted array, avoiding the O(n^2) enumeration of all pair distances.

### Find the Kth Smallest Sum of a Matrix With Sorted Rows
- Judge: LeetCode
- Link: https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
- Difficulty: Hard
- Subtopic: Order Statistics / Quickselect
- One-line description: Given a matrix where each row is sorted, choose one element per row to sum, and find the k-th smallest possible sum.
- Why it's a good hard problem: Generalizes k-th-order-statistic reasoning to combining sums across many sorted lists, requiring a heap-based or binary-search-based order-statistics merge across more than two arrays.

## Blogs by subtopic (cross-reference; see cp-blogs-arrays-sorting-extra.md for full entries)
- Difference Arrays: blog/entry/86420, blog/entry/88474
- Two-Pointer Partitioning: blog/entry/94534
- Monotonic Deque: blog/entry/122003
- Merge Intervals: blog/entry/98629, blog/entry/20377
- Ternary Search on Unimodal Functions: blog/entry/60702, blog/entry/135892
- Custom Comparators & Multi-Key Sorting: blog/entry/63533
- Order Statistics / Quickselect: blog/entry/11080, blog/entry/95575
