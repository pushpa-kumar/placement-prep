# Sorting & Binary Search — hard practice problems (binary search on the answer over hard optimization problems)

### Present
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/460/C
- Difficulty: 1700
- Subtopic: binary search on the answer + difference array
- One-line description: Given n flowers with initial heights, w days, and the ability to water m consecutive flowers (raising each by 1) once per day, maximize the minimum flower height after w days.
- Why it's a good hard problem: The answer (final minimum height) is monotonic in feasibility, so you binary search on it; checking feasibility for a candidate value efficiently requires a difference-array/sliding-window-sum technique rather than brute-force simulation.

### Boxes Packing
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1066/D
- Difficulty: 1800
- Subtopic: binary search on the answer + greedy feasibility check
- One-line description: Given n boxes with fixed weights that must be packed in order into k bags of equal, unknown capacity, find the minimum bag capacity that lets all boxes be packed using at most k bags.
- Why it's a good hard problem: The feasibility check (can capacity x pack everything into ≤k bags) is a simple greedy scan, but recognizing that the answer space is monotonic and binary-searchable — rather than trying to compute the capacity directly — is the non-trivial insight.

### Renting Bikes
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/363/D
- Difficulty: 1800
- Subtopic: binary search on the answer + greedy budget allocation
- One-line description: Given a group of friends each with personal money and a shared budget, and a target number of bikes to rent, find the minimum price per bike (same for everyone) at which enough friends can afford a bike using their own money plus the shared budget.
- Why it's a good hard problem: Feasibility for a candidate price requires a careful greedy pass (cap each friend's contribution at their own money, sum the shortfalls, compare against the shared budget), and the monotonic structure that makes binary search valid is not obvious at first glance.

### Factory Machines
- Judge: CSES
- Link: https://cses.fi/problemset/task/1620
- Difficulty: CSES
- Subtopic: binary search on the answer
- One-line description: Given k machines each with a fixed time-per-product rate, find the minimum total time needed for the machines (working in parallel) to produce at least n products.
- Why it's a good hard problem: The canonical "binary search on the answer" optimization problem — feasibility (can we hit n products by time t) is a trivial O(k) check, but realizing the answer is monotonic in time and binary-searchable (over a huge time range) rather than computable directly is the key idea.

### Array Division
- Judge: CSES
- Link: https://cses.fi/problemset/task/1085
- Difficulty: CSES
- Subtopic: binary search on the answer (minimize the maximum)
- One-line description: Split an array into k contiguous subarrays so as to minimize the maximum sum among the subarrays.
- Why it's a good hard problem: A textbook "minimize the maximum" binary search problem — binary search on the candidate maximum sum, with a greedy linear-time feasibility check counting how many subarrays are needed.

### Split Array Largest Sum
- Judge: LeetCode
- Link: https://leetcode.com/problems/split-array-largest-sum/
- Difficulty: Hard
- Subtopic: binary search on the answer (minimize the maximum)
- One-line description: Split an array of non-negative integers into m contiguous non-empty subarrays to minimize the largest sum among the subarrays.
- Why it's a good hard problem: The LeetCode-Hard twin of CSES's Array Division; recognizing that the minimum possible "largest sum" is monotonic in feasibility and binary-searchable, backed by a greedy O(n) feasibility check, is the crux insight rather than any direct DP.

### Median of Two Sorted Arrays
- Judge: LeetCode
- Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
- Difficulty: Hard
- Subtopic: binary search on a partition point
- One-line description: Given two sorted arrays of sizes m and n, find the median of the combined sorted array in O(log(min(m,n))) time.
- Why it's a good hard problem: Rather than merging, the intended solution binary searches over a partition index in the smaller array to find a split where all left-side elements are ≤ all right-side elements — a famously tricky, off-by-one-prone binary search that goes well beyond "find element in sorted array."

### Find K-th Smallest Pair Distance
- Judge: LeetCode
- Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
- Difficulty: Hard
- Subtopic: binary search on the answer + two-pointer counting
- One-line description: Given an integer array, find the k-th smallest absolute difference among all pairs of elements.
- Why it's a good hard problem: Binary searches over the candidate distance value, using a two-pointer pass over the sorted array as the O(n) counting subroutine for "how many pairs have distance ≤ mid" — a direct combination of binary-search-on-answer with two-pointer counting.
