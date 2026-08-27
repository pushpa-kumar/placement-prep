# CP Guide — Graph Algorithms (hard practice problems, CF 1700+/LC Hard/CSES harder variants)

## Dijkstra

### Complete The Graph
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/715/B
- Difficulty: CF 2300
- Subtopic: Dijkstra
- One-line description: Given required shortest-path distances from a source to two special vertices, and a graph with some fixed edge weights and some edges of unknown weight, assign positive integer weights to the unknown edges so Dijkstra's shortest distances match the targets exactly (or report impossible).
- Why it's a good hard problem: It inverts Dijkstra — instead of computing shortest paths from given weights, you must reconstruct valid weights from target distances, requiring a binary-search-style greedy weight assignment plus repeated Dijkstra verification.

## Bellman-Ford

### High Score
- Judge: CSES
- Link: https://cses.fi/problemset/task/1673
- Difficulty: CSES (Graph Algorithms section)
- Subtopic: Bellman-Ford
- One-line description: Find the maximum possible total score of a path from node 1 to node n in a weighted directed graph, or report that the score is unbounded because of a reachable-and-escapable positive cycle.
- Why it's a good hard problem: Requires adapting Bellman-Ford to maximize (negate weights) and, crucially, to distinguish "any positive cycle exists" from "a positive cycle lies on some path from 1 to n" — a common source of wrong answers.

## Floyd-Warshall

### Minimum Path
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1473/E
- Difficulty: CF 2400
- Subtopic: Floyd-Warshall
- One-line description: Given a weighted graph, you may halve the weight of at most one edge; find the minimum possible distance between two fixed vertices s and t after the change.
- Why it's a good hard problem: Needs all-pairs shortest distances from Floyd-Warshall as a base, then an O(n^2) scan over candidate edges to halve, using distance decomposition (dist(s,u) + w/2 + dist(v,t)) to evaluate each candidate in O(1).

## MST

### Minimum spanning tree for each edge
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/609/E
- Difficulty: CF 2100
- Subtopic: MST (Kruskal, hard variant)
- One-line description: For every edge of a weighted graph, compute the minimum total weight of a spanning tree that is forced to include that specific edge.
- Why it's a good hard problem: Requires building one MST with Kruskal, then for every non-tree edge finding the maximum-weight edge on the tree path between its endpoints via binary lifting/LCA over the MST — a genuine two-algorithm combination, not plain Kruskal.

## Topological Sort

### Coloring Edges
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1217/D
- Difficulty: CF 2100
- Subtopic: Topological Sort
- One-line description: Color the edges of a directed graph with as few colors as possible so that no cycle is monochromatic.
- Why it's a good hard problem: The answer is 1 exactly when a topological sort exists (DAG); otherwise it's 2, and constructing a valid 2-coloring requires finding SCCs and using each SCC's internal topological order — a real application of topological sort beyond a single yes/no check.

## SCC

### Reachability from the Capital
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/999/E
- Difficulty: CF 2000
- Subtopic: SCC (Tarjan/Kosaraju)
- One-line description: Given a directed graph and a capital city, find the minimum number of new roads to add so every city is reachable from the capital.
- Why it's a good hard problem: Requires condensing the graph into strongly connected components (Tarjan or Kosaraju), then counting "source" components (in-degree zero) in the condensation DAG, excluding the capital's own component.

## Bridges/Articulation Points

### Critical Connections in a Network
- Judge: LeetCode
- Link: https://leetcode.com/problems/critical-connections-in-a-network/
- Difficulty: LeetCode Hard
- Subtopic: Bridges/Articulation Points
- One-line description: Given an undirected connected network of servers, find every connection (edge) whose removal would disconnect the network.
- Why it's a good hard problem: It is a direct, large-scale implementation of Tarjan's bridge-finding algorithm (discovery time / low-link values), which is notoriously easy to get subtly wrong around recursion depth, parent edges, and multi-edges.

## Bipartite Check

### Graph Without Long Directed Paths
- Judge: Codeforces
- Link: https://codeforces.com/problemset/problem/1144/F
- Difficulty: CF 1900
- Subtopic: Bipartite Check
- One-line description: Orient every edge of an undirected graph so that the resulting directed graph contains no directed path of two or more edges, or determine this is impossible.
- Why it's a good hard problem: The core insight — a valid orientation exists if and only if the graph is bipartite — must be proven before the standard BFS/DFS 2-coloring can be applied to actually construct the orientation.
