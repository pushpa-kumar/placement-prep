# Greedy Algorithms — Curated Hard Practice Problems

### Buy Low Sell High
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/865/D
- Difficulty: CF 2400
- Subtopic: greedy + data structure ("regret" greedy with a min-heap)
- One-line description: Given n days of known future stock prices, repeatedly buy/sell one share per day (never short) to maximize total profit.
- Why it's a good hard problem: The optimal strategy isn't simple local matching — you push every price twice into a min-heap and "undo" a bad earlier buy by reselling-and-rebuying through the heap whenever a better price appears, a non-obvious exchange argument that's a template for a whole family of regret-based greedy problems.

### Shichikuji and Power Grid
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1245/D
- Difficulty: CF 1900
- Subtopic: greedy reduction to MST
- One-line description: For n cities, decide for each whether to build its own power station or connect it by wire to another powered city, minimizing total cost of stations plus wires.
- Why it's a good hard problem: The key insight is a non-obvious modeling trick — add a virtual "source" node connected to every city with an edge weight equal to that city's own-station cost, then the whole problem collapses into finding a Minimum Spanning Tree, whose greedy correctness (Prim/Kruskal) has to be re-justified in this transformed setting.

### Stressful Training
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1132/D
- Difficulty: CF 2300
- Subtopic: binary search + greedy feasibility check
- One-line description: n students with given starting charge and per-minute battery drain must survive w minutes of lecture; you may buy identical power banks of some capacity and hand at most k of them out per minute — find the minimum sufficient power bank capacity.
- Why it's a good hard problem: The check-function for a candidate capacity is itself a non-trivial greedy simulation (always rescue whichever student is closest to dying, via a priority queue), so the problem combines two layers of exact reasoning: binary search monotonicity plus proving the inner greedy allocation is optimal.

### Tasks and Deadlines
- Judge: CSES
- Link: https://cses.fi/problemset/task/1630
- Difficulty: CSES (Sorting and Searching, high end)
- Subtopic: exchange argument (sort by duration, not deadline)
- One-line description: Process n tasks (each with a duration and a deadline) one after another to maximize the total reward, where each task's reward is its deadline minus its finishing time.
- Why it's a good hard problem: The deadlines are a red herring in the objective's structure — a swap-adjacent-tasks exchange argument shows only the order of durations matters (shortest job first), which is counter-intuitive on first read since deadlines appear in the reward formula.

### Reading Books
- Judge: CSES
- Link: https://cses.fi/problemset/task/1631
- Difficulty: CSES (Sorting and Searching, high end)
- Subtopic: greedy pairing / scheduling with two workers
- One-line description: Two people must read all n books together (never the same book at the same time); given each book's reading time, find the minimum total time for both to finish everything.
- Why it's a good hard problem: The answer isn't simply "split books evenly" — you must reason about the interaction between the single longest book and the sum of all reading times to derive the correct greedy lower bound and a matching construction.

### Movie Festival II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1632
- Difficulty: CSES (Sorting and Searching, high end)
- Subtopic: greedy interval scheduling with k resources
- One-line description: With k movie-club members attending a festival of n movies (each with a start/end time), maximize the total number of movies watched, allowing members to watch different movies in parallel.
- Why it's a good hard problem: It generalizes classic single-resource interval scheduling to k parallel resources — sorting by end time is still correct, but you additionally need a data structure (e.g. a multiset of members' free times) to greedily assign each movie to the "least wasteful" available member.

### Candy
- Judge: LeetCode
- Link: https://leetcode.com/problems/candy/
- Difficulty: Hard
- Subtopic: exchange argument (two-pass greedy)
- One-line description: Distribute the minimum number of candies to children standing in a line so every child gets at least one candy and any child with a higher rating than a neighbor gets more candies than that neighbor.
- Why it's a good hard problem: A single left-to-right or right-to-left pass is provably insufficient; the minimal correct assignment requires two independent greedy passes whose results are combined by taking the max at each position, and proving that this actually achieves the global minimum is non-obvious.

### Set Intersection Size At Least Two
- Judge: LeetCode
- Link: https://leetcode.com/problems/set-intersection-size-at-least-two/
- Difficulty: Hard
- Subtopic: greedy on intervals with a non-obvious proof
- One-line description: Given a list of integer intervals, find the minimum-size set of integers such that every interval contains at least two elements from the set.
- Why it's a good hard problem: The natural single-point interval-greedy idea (from "minimum points to stab all intervals") doesn't extend cleanly to "at least two" — the correct approach sorts by right endpoint (tie-broken by left endpoint) and greedily appends the two largest missing values from the interval's tail, and justifying why this greedy choice is always safe is considerably subtler than the classic single-cover version.
