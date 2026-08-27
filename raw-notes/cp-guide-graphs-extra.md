# CP Guide — Graph Algorithms: Extra Subtopics (2-SAT, Euler Path/Circuit, 0/1 BFS & Multi-Source BFS, Functional Graphs)

Scope note: these are NEW subtopics for the existing Graph Algorithms guide page. Shortest paths, MST, topo sort, SCC, bridges/articulation points, and bipartite check are already covered elsewhere and are intentionally NOT duplicated here.

All problems below were verified via the Codeforces public API (`problemset.problems`, filtered to `rating >= 1700`), direct fetch of live CSES task pages, and the LeetCode public GraphQL problem-list endpoint. Ratings/tags are as returned by the CF API at verification time (2026-08-28 / 2026-08-27).

---

## 2-SAT

### Two Sets
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/468/B
- Difficulty: CF 2000
- Subtopic: 2-SAT
- One-line description: Split n integers into two groups such that the sum of no group contains a perfect square (each pair with a square sum must go into different groups) — reduce pairwise constraints to 2-SAT clauses.
- Why it's a good hard problem: Forces you to first *build* the implication constraints from a non-obvious pairwise condition before running the standard 2-SAT/SCC machinery.

### The Door Problem
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/776/D
- Difficulty: CF 2000
- Subtopic: 2-SAT
- One-line description: Each door is controlled by exactly two switches (or one, toggling on its own); determine an assignment of switch states so all doors end up in the desired open/closed state.
- Why it's a good hard problem: Classic direct 2-SAT modeling exercise (each switch is a boolean variable, each door gives a clause) — a staple "first real 2-SAT" problem, cited in cp-algorithms' own practice list.

### ±1
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1971/H
- Difficulty: CF 2100
- Subtopic: 2-SAT
- One-line description: Assign +1 or -1 to each of n numbers so that a set of prefix/segment-sum constraints are all satisfied.
- Why it's a good hard problem: Requires recognizing a segment-constraint problem as a 2-SAT instance and building implication edges efficiently (segment tree over implication graph territory).

### Radio Stations
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1215/F
- Difficulty: CF 2700
- Subtopic: 2-SAT
- One-line description: Given n radio stations with frequency and power, and m pairs that must not interfere, decide the maximum interference threshold and find a valid subset — solved with 2-SAT + binary search + clever edge construction (segment tree / sorted-pointer optimization) to keep the implication graph near-linear.
- Why it's a good hard problem: Combines 2-SAT with binary search on the answer and a nontrivial trick to avoid an O(n²) implication graph — a genuine "advanced 2-SAT" problem, also referenced directly by cp-algorithms as a 2-SAT practice problem.

### Giant Pizza
- Judge: CSES
- Link: https://cses.fi/problemset/task/1684
- Difficulty: CSES (2-SAT category)
- Subtopic: 2-SAT
- One-line description: n people each give a preference (+ or -) for m pizza toppings; find an assignment of each topping (yes/no) satisfying at least one preference per person, or report impossible.
- Why it's a good hard problem: The canonical "hello world" of 2-SAT — every serious CP course uses this to teach implication-graph construction + SCC-based satisfiability + solution reconstruction from condensation order.

---

## Euler Path / Euler Circuit (Hierholzer's Algorithm)

### Mail Delivery
- Judge: CSES
- Link: https://cses.fi/problemset/task/1691
- Difficulty: CSES (Euler circuit category)
- Subtopic: Euler Path / Euler Circuit
- One-line description: Given a connected graph (with possible multi-edges/self-loops), find a route that starts and ends at node 1 and uses every edge exactly once, or report it's impossible.
- Why it's a good hard problem: The direct textbook exercise for implementing Hierholzer's algorithm iteratively (recursive versions stack-overflow on CSES's large inputs), including handling odd-degree infeasibility.

### Bertown roads
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/118/E
- Difficulty: CF 2000
- Subtopic: Euler Path / Euler Circuit
- One-line description: Given a connected undirected road network, orient every road (make it one-way) so the resulting directed graph is still strongly connected, or report it's impossible.
- Why it's a good hard problem: The classic application of "find an Euler circuit per 2-edge-connected component (via Hierholzer's / DFS tree + back edges), then direct each edge along the traversal direction" — a non-obvious but well-known use of Euler-tour construction to guarantee strong connectivity.

### Tanya and Password
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/508/D
- Difficulty: CF 2500
- Subtopic: Euler Path / Euler Circuit
- One-line description: Given n three-letter strings, arrange (a subset covering all of them, each exactly once) into one long string so consecutive substrings overlap by two characters — equivalent to finding an Euler path in a de Bruijn-style graph over bigrams.
- Why it's a good hard problem: Requires modeling the problem as a graph (nodes = bigrams, edges = trigrams) before applying Hierholzer's algorithm — a genuinely creative Euler-path reduction, not a template application.

### Trails and Glades
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/209/C
- Difficulty: CF 2400
- Subtopic: Euler Path / Euler Circuit
- One-line description: Find the minimum number of new trails (edges) to add to a multigraph so that an Euler circuit starting and ending at node 1 exists.
- Why it's a good hard problem: The classic "fix a graph to admit an Euler circuit" construction — pair up odd-degree vertices across components using DSU/greedy while reasoning correctly about component connectivity, then verify with Euler-circuit theory (all-even-degree + one connected component).

### Wizard's Tour
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/858/F
- Difficulty: CF 2300
- Subtopic: Euler Path / Euler Circuit
- One-line description: Maximize the number of length-2 "episodes" (x→y→z walks) that together use every edge of an undirected graph at most once.
- Why it's a good hard problem: Solved by adding a dummy vertex connecting all odd-degree vertices, finding an Euler circuit (Hierholzer's) on the augmented graph per component, then splitting the circuit into length-2 trails — a non-obvious but well-known extension of Euler-circuit construction.

---

## 0/1 BFS & Multi-Source BFS

### Okabe and City
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/821/D
- Difficulty: CF 2200
- Subtopic: 0/1 BFS
- One-line description: On a grid where only k cells are lit, find the minimum number of times you must "light up" a whole row or column (cost 1) to walk from the top-left to the bottom-right cell, versus free moves between already-lit adjacent cells (cost 0).
- Why it's a good hard problem: A textbook 0/1 BFS on an augmented graph (cell nodes + row/column "toggle" nodes) — one of the most frequently cited CF problems for teaching 0/1 BFS specifically.

### Cactus Wall
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1749/E
- Difficulty: CF 2400
- Subtopic: 0/1 BFS
- One-line description: On an n×m grid with some cactus cells already placed (no two adjacent), plant the minimum number of new non-adjacent cacti so no side-adjacent empty-cell path connects the top row to the bottom row.
- Why it's a good hard problem: Reduces "minimum cut to separate top from bottom" to a shortest path in the planar dual graph, where existing cacti cost 0 and new ones cost 1 — a sharp, non-templated 0/1 BFS application.

### Flights
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/241/E
- Difficulty: CF 2600
- Subtopic: 0/1 BFS
- One-line description: In a DAG from city 1 to city n, assign each edge a duration of 1 or 2 hours so every root-to-sink path has the exact same total duration.
- Why it's a good hard problem: The classic "potential function via 0/1 BFS" problem — compute per-node levels with a 0/1 BFS (or DP) and derive edge weights from level differences, then verify consistency; a deceptively hard 2600 that hinges entirely on the 0/1 BFS idea.

### Minimum Cost to Make at Least One Valid Path in a Grid
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
- Difficulty: LeetCode Hard
- Subtopic: 0/1 BFS
- One-line description: Each grid cell has a mandatory direction arrow; moving along the arrow costs 0, changing the direction of a cell (to move any other way) costs 1 — find the minimum cost path from top-left to bottom-right.
- Why it's a good hard problem: The canonical LeetCode 0/1 BFS problem — edges naturally split into weight-0 (follow arrow) and weight-1 (redirect), requiring a deque-based BFS instead of plain BFS or full Dijkstra.

### Minimum Obstacle Removal to Reach Corner
- Judge: LeetCode
- Link: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/
- Difficulty: LeetCode Hard
- Subtopic: 0/1 BFS
- One-line description: On a grid with 0 (free) and 1 (obstacle) cells, find the minimum number of obstacles to remove to travel from top-left to bottom-right.
- Why it's a good hard problem: A second, cleaner 0/1 BFS grid template (moving into a 0-cell costs 0, into a 1-cell costs 1) — good for contrasting with plain BFS/Dijkstra approaches and reinforcing when 0/1 BFS beats a full priority queue.

### Monsters
- Judge: CSES
- Link: https://cses.fi/problemset/task/1194
- Difficulty: CSES (multi-source BFS category)
- Subtopic: Multi-Source BFS
- One-line description: In a labyrinth, monsters and the player move simultaneously one step per turn; determine if the player can reach any boundary cell without ever being caught, and output a path.
- Why it's a good hard problem: Requires running a single multi-source BFS from all monster start cells to get each cell's "monster arrival time," then a second BFS/greedy check from the player against those times — the defining multi-source BFS exercise on CSES.

### Nearest Opposite Parity
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1272/E
- Difficulty: CF 1900
- Subtopic: Multi-Source BFS
- One-line description: From each index i in an array, you may jump to i±a[i]; for every index, find the minimum number of jumps to reach some index whose value has opposite parity.
- Why it's a good hard problem: The intended O(n) solution reverses the jump graph and multi-source BFSes from all same-parity-target nodes simultaneously, instead of doing a separate BFS per query — a clean lesson in why single-source-per-query BFS is too slow and multi-source BFS is the fix.

### Three States
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/590/C
- Difficulty: CF 2200
- Subtopic: Multi-Source BFS
- One-line description: Given a grid map with three separate "state" regions, find the minimum number of road cells to build so that all three regions become mutually connected.
- Why it's a good hard problem: Needs three independent multi-source BFS runs (one per state's full cell-set as sources) to get per-cell distances to each state, then combines them — directly teaches "BFS with many simultaneous sources," not just one.

### Destroying Roads
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/543/B
- Difficulty: CF 2100
- Subtopic: Multi-Source BFS
- One-line description: Destroy as many roads as possible from a connected graph while keeping two given (s,t) pairs reachable within given time limits l1 and l2.
- Why it's a good hard problem: Requires four full BFS runs (from s1, t1, s2, t2) and then reasoning over pairwise-combined distances — a good exercise in multi-run/multi-source BFS distance tables feeding into a greedy/DP combination step.

### Escape the Spreading Fire
- Judge: LeetCode
- Link: https://leetcode.com/problems/escape-the-spreading-fire/
- Difficulty: LeetCode Hard
- Subtopic: Multi-Source BFS
- One-line description: Fire starts at multiple grid cells and spreads to adjacent cells every minute; find the maximum time you can wait before starting your escape from the top-left and still reach the bottom-right before or exactly when fire does.
- Why it's a good hard problem: The fire's spread must be computed as one true multi-source BFS from all initial fire cells (not per-cell BFS), then combined with a second BFS for the player and a binary search on the wait time — a strong applied example of multi-source BFS.

---

## Functional Graphs & Cycle Detection (Binary Lifting)

### Planets Queries I
- Judge: CSES
- Link: https://cses.fi/problemset/task/1750
- Difficulty: CSES (functional graph / binary lifting category)
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: Each of n planets has exactly one teleporter to another planet; answer q queries asking "where do you end up after taking exactly k teleporters starting from planet x?"
- Why it's a good hard problem: The direct, textbook introduction to binary lifting (sparse "2^k-th successor" table) on a functional graph — the problem the technique is built to answer.

### Planets Queries II
- Judge: CSES
- Link: https://cses.fi/problemset/task/1160
- Difficulty: CSES (functional graph / binary lifting category)
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: For each functional-graph query (a, b), find the smallest number of teleporter jumps needed to reach b from a, or determine it's impossible — including detecting when a and b lie on/lead into the same eventual cycle.
- Why it's a good hard problem: Extends binary lifting with explicit cycle detection and "meeting point" reasoning in a functional graph, harder than a plain k-th-successor query.

### Planets Cycles
- Judge: CSES
- Link: https://cses.fi/problemset/task/1751
- Difficulty: CSES (functional graph / cycle detection category)
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: In the same one-out-edge-per-node functional graph, compute for every node the total number of distinct planets reachable before returning to a previously visited planet (i.e., tail length + cycle length).
- Why it's a good hard problem: A pure cycle-detection exercise on functional graphs — requires correctly separating each node's "tail" from the "cycle" it eventually enters, without binary lifting, as a complement to the two Planets Queries problems.

### Mouse Hunt
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1027/D
- Difficulty: CF 1700
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: A mouse starts in an unknown room and each second deterministically moves room i → a[i] (a functional graph); choose a minimum-cost set of rooms to trap so the mouse is guaranteed to be caught regardless of its start.
- Why it's a good hard problem: Requires recognizing that only the cycles of the functional graph matter (every tail eventually funnels into a cycle) and picking the minimum-cost node per cycle — a clean, low-rated but genuine functional-graph cycle problem.

### Analysis of Pathes in Functional Graph
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/702/E
- Difficulty: CF 2100
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: Given a functional graph with weighted edges and a huge k (up to 10^10), compute for every starting vertex the sum and the minimum edge weight along the length-k walk starting there.
- Why it's a good hard problem: The direct generalization of binary lifting to also aggregate path sums and path minimums at each power-of-two jump — a staple "binary lifting on functional graphs, doubling extra info" problem.

### Kth Ancestor of a Tree Node
- Judge: LeetCode
- Link: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
- Difficulty: LeetCode Hard
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: Preprocess a rooted tree (a special case of a functional graph where every node points to its parent) to answer many "kth ancestor of node x" queries efficiently.
- Why it's a good hard problem: The parent-pointer structure is exactly a functional graph, and the required solution is precisely the binary-lifting sparse table technique — a well-known Hard-rated binary lifting problem outside of Codeforces/CSES.

### Recover a functional graph
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/739/D
- Difficulty: CF 3400
- Subtopic: Functional Graphs & Cycle Detection
- One-line description: Given a set of n "candidate" functional graphs (each node's chosen out-edge from a list of options), reconstruct one consistent global functional graph matching the maximum number of choices via bipartite-matching-flavored reasoning.
- Why it's a good hard problem: A very hard (3400) problem literally named after functional graphs — included as a stretch/reach problem for readers who've mastered the basics and want to see functional-graph reasoning combined with matching/flow.
