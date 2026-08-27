# Network Flow & Matching — curated hard practice problems (Codeforces API + CSES, verified)

## Max Flow

### Download Speed
- Judge: CSES
- Link: https://cses.fi/problemset/task/1694
- Difficulty: CSES
- Subtopic: max flow
- One-line description: Find the maximum data transfer rate from computer 1 to computer n through a network of directed connections with given capacities.
- Why it's a good hard problem: The canonical from-scratch max flow implementation exercise (Edmonds-Karp/Dinic) with no modeling trick to hide behind.

### Distinct Routes
- Judge: CSES
- Link: https://cses.fi/problemset/task/1711
- Difficulty: CSES
- Subtopic: max flow
- One-line description: Find the maximum number of edge-disjoint paths from room 1 to room n in a directed graph and output the paths themselves.
- Why it's a good hard problem: Requires not just the max-flow value but decomposing the resulting flow into explicit paths, a step many implementations skip.

### Fox and Dinner
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/510/E
- Difficulty: 2300
- Subtopic: max flow
- One-line description: Seat foxes at round tables (each with at least 3 foxes) so that the ages of any two adjacent foxes sum to a prime.
- Why it's a good hard problem: The flow network isn't given — you must notice primes > 2 force even/odd parity pairing, turning the seating constraint into a bipartite degree-exactly-2 flow model.

### Delivery Bears
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/653/D
- Difficulty: 2200
- Subtopic: max flow
- One-line description: Split a required flow between two bear species along edge capacities in a fixed ratio while maximizing total flow.
- Why it's a good hard problem: Combines binary search on the answer with a max-flow feasibility check under a ratio constraint on edge usage.

## Min Cut

### Police Chase
- Judge: CSES
- Link: https://cses.fi/problemset/task/1695
- Difficulty: CSES
- Subtopic: min cut
- One-line description: Find the minimum number of edges to remove to disconnect node 1 from node n, and report which edges to cut.
- Why it's a good hard problem: Direct application of max-flow min-cut duality, including reconstructing the actual cut edges from the residual graph.

### Petya and Graph
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1082/G
- Difficulty: 2400
- Subtopic: min cut
- One-line description: Choose a subgraph maximizing (sum of edge weights) minus (sum of weights of vertices touched by chosen edges).
- Why it's a good hard problem: A non-obvious instance of the maximum-weight closure / project-selection problem, solved by reducing to min cut via source/sink edges on vertices and edges.

### Rectangle Painting 2
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1198/E
- Difficulty: 2500
- Subtopic: min cut
- One-line description: Paint possibly-overlapping rectangles in two colors to minimize the total mismatched-color area in their pairwise overlaps.
- Why it's a good hard problem: Requires recognizing a 2-coloring cost-minimization structure as a project-selection/min-cut instance over interacting overlap regions.

## Bipartite Matching

### School Dance
- Judge: CSES
- Link: https://cses.fi/problemset/task/1696
- Difficulty: CSES
- Subtopic: bipartite matching
- One-line description: Find the maximum matching between boys and girls given a list of pairs willing to dance together.
- Why it's a good hard problem: The baseline Kuhn's algorithm / Hopcroft-Karp implementation problem, with input sizes that punish naive O(VE) blow-ups.

### Exploration Plan
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/852/D
- Difficulty: 2100
- Subtopic: bipartite matching
- One-line description: Find the minimum time limit so that N teams starting in various cities can collectively occupy at least K distinct cities.
- Why it's a good hard problem: Layers all-pairs shortest paths and binary search on top of a bipartite matching feasibility check (Hall's theorem), a common competitive pattern.

### Round Marriage
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/981/F
- Difficulty: 2500
- Subtopic: bipartite matching
- One-line description: Match bridegrooms to brides placed around a circle to minimize the maximum walking distance any bride must travel.
- Why it's a good hard problem: The circular structure and min-max objective require binary search combined with a Hall's-theorem-based matching existence check, not a direct matching computation.
