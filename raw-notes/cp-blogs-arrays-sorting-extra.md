# CP Guide — Extra Codeforces Blogs (Arrays & Sorting subtopics)

Every blog below was verified with the Codeforces public API:
`https://codeforces.com/api/blogEntry.view?blogEntryId=<id>` returning
`status: OK` with the author handle and title confirmed to match what is
listed here. No invented blogs, authors, or IDs.

## Arrays & Strings

### [Tutorial] 1D and 2D constant time per query range updates (a.k.a difference arrays)
- Author: the_algorithmic_eye
- URL: https://codeforces.com/blog/entry/86420
- Topic: Arrays & Strings
- Subtopic: Difference Arrays
- Takeaway: Builds up the difference-array trick from 1D constant-range-add, to range-add-of-an-arithmetic-progression, to a DP+range-update combination, to the 2D grid version, each with a motivating problem and code.

### Video about prefix sums, difference array and the power of half-closed intervals
- Author: peltorator
- URL: https://codeforces.com/blog/entry/88474
- Topic: Arrays & Strings
- Subtopic: Difference Arrays
- Takeaway: A follow-up/advanced companion to the standard difference-array tutorial, emphasizing why half-open interval conventions ([l, r+1)) avoid off-by-one bugs in range-update code.

### [Tutorial] Quick Sort
- Author: Rainbow_IQ
- URL: https://codeforces.com/blog/entry/94534
- Topic: Arrays & Strings
- Subtopic: Two-Pointer Partitioning
- Takeaway: Walks through the Hoare/Lomuto in-place partition-around-a-pivot mechanics that Dutch-National-Flag-style three-way partitioning generalizes, including why a poor pivot choice degrades to O(n^2).

### [Tutorial] Minimum Deque
- Author: k1r1t0
- URL: https://codeforces.com/blog/entry/122003
- Topic: Arrays & Strings
- Subtopic: Monotonic Deque
- Takeaway: Derives the monotonic-deque technique from first principles by building a "Minimum Stack" then a "Minimum Queue" from two stacks, then a "Minimum Deque" supporting push/pop from both ends while tracking the running minimum in O(1) amortized.

### [Tutorial] Solving Interval Problems with Geometry
- Author: Monogon
- URL: https://codeforces.com/blog/entry/98629
- Topic: Arrays & Strings
- Subtopic: Merge Intervals
- Takeaway: Reframes a collection of intervals as 2D points (l, r) that "see" down-and-right, turning interval-covering and interval-merging problems into 2D dominance/geometry queries.

### How to sweep like a Sir
- Author: DanAlex
- URL: https://codeforces.com/blog/entry/20377
- Topic: Arrays & Strings
- Subtopic: Merge Intervals
- Takeaway: Introduces the linear sweep technique with the classic "union of rectangles' area" example, directly relevant to computing the length/area covered by a merged set of intervals.

## Sorting & Binary Search

### Tutorial On Tof (Ternary Search)
- Author: Mahdi_Jfri
- URL: https://codeforces.com/blog/entry/60702
- Topic: Sorting & Binary Search
- Subtopic: Ternary Search on Unimodal Functions
- Takeaway: A from-scratch introduction to ternary search for finding the extremum of a unimodal function, including the standard iterative implementation and common pitfalls (e.g. off-by-one in the shrinking interval).

### [Tutorial] Non-unimodal ternary search
- Author: polosatic
- URL: https://codeforces.com/blog/entry/135892
- Topic: Sorting & Binary Search
- Subtopic: Ternary Search on Unimodal Functions
- Takeaway: Extends ternary search beyond strictly unimodal functions, showing when and how the technique can still be salvaged (or must be replaced) for functions with flat regions or multiple local extrema.

### Lecture #3 — Exchange arguments (sorting with dp)
- Author: Errichto
- URL: https://codeforces.com/blog/entry/63533
- Topic: Sorting & Binary Search
- Subtopic: Custom Comparators & Multi-Key Sorting
- Takeaway: Teaches how to derive and prove a custom multi-key comparator via exchange arguments (showing any two adjacent out-of-order elements can be swapped without hurting the answer), the rigorous justification behind greedy sort-based solutions.

### C++ STL: Policy based data structures
- Author: adamant
- URL: https://codeforces.com/blog/entry/11080
- Topic: Sorting & Binary Search
- Subtopic: Order Statistics / Quickselect
- Takeaway: Introduces GNU PBDS `tree` (an order-statistics tree) supporting `find_by_order` and `order_of_key` in O(log n), the standard competitive-programming shortcut for k-th-order-statistic queries on a dynamic set.

### Building my own Custom Order-Statistic Tree using RB-Trees!
- Author: Rajveer_100
- URL: https://codeforces.com/blog/entry/95575
- Topic: Sorting & Binary Search
- Subtopic: Order Statistics / Quickselect
- Takeaway: Walks through implementing an order-statistic tree from scratch on top of a red-black tree, useful for understanding what PBDS abstracts away and for environments where PBDS isn't available.
