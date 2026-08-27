# Curated Codeforces blogs: Graph Algorithms, Trees, Data Structures for CP (verified 2026-08-28)

## Graph Algorithms

### [Tutorial] The DFS tree and its applications: how I found out I really didn't understand bridges
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/68138
- Topic: Graph Algorithms
- Takeaway: Builds intuition for bridges and articulation points by classifying edges (tree/back edges) in a DFS tree, generalizing the classic low-link approach to a range of structural graph problems.

### [Tutorial] Directed DFS trees (and the Tarjan algorithm for Strongly Connected Components)
- Author: de_sousa
- URL: https://codeforces.com/blog/entry/131187
- Topic: Graph Algorithms
- Takeaway: Derives Tarjan's SCC algorithm from first principles by studying edge classification in directed DFS trees, making the stack-based low-link recurrence feel like a natural consequence rather than a memorized trick.

### 0-1 BFS [Tutorial]
- Author: himanshujaju
- URL: https://codeforces.com/blog/entry/22276
- Topic: Graph Algorithms
- Takeaway: Shows how to compute shortest paths in O(V+E) on graphs with only 0/1 edge weights using a deque (push front on 0-weight relaxation, push back on 1-weight), avoiding the log factor of Dijkstra's heap.

### [Tutorial] Boruvka's Algorithm
- Author: RockyB
- URL: https://codeforces.com/blog/entry/77760
- Topic: Graph Algorithms
- Takeaway: Explains Boruvka's MST algorithm (each component finds its cheapest outgoing edge per round, halving the component count every round) and its use in non-standard MST variants like XOR-MST where edges aren't explicitly listed.

### Algorithm Gym :: Graph Algorithms
- Author: PrinceOfPersia
- URL: https://codeforces.com/blog/entry/16221
- Topic: Graph Algorithms
- Takeaway: A broad reference compilation covering DFS/BFS, Dijkstra/Bellman-Ford/Floyd-Warshall/SPFA shortest paths, Kruskal/Prim MST, max-flow (Edmonds-Karp, Dinic), and bipartite matching/LCA, useful as a single-stop refresher across topological/shortest-path/MST/matching subtopics.

### Rethink the Dijkstra algorithm -- Let's go deeper
- Author: CristianoPenaldo
- URL: https://codeforces.com/blog/entry/107810
- Topic: Graph Algorithms
- Takeaway: Generalizes Dijkstra's correctness argument to any "relaxation function" satisfying an induction base, extension, and DP property, showing it applies beyond plain sum/max shortest-path formulations.

## Trees

### Heavy-light decompositon — it can be simple!
- Author: Vladyslav
- URL: https://codeforces.com/blog/entry/12239
- Topic: Trees
- Takeaway: Presents a simplified way to implement heavy-light decomposition so that any root-to-node path crosses O(log N) chains, enabling path queries/updates via an auxiliary segment tree.

### Hybrid Tutorial #-2: Centroid Decomposition
- Author: galen_colin
- URL: https://codeforces.com/blog/entry/81661
- Topic: Trees
- Takeaway: Builds a centroid decomposition tree of logarithmic height and demonstrates it on "Xenia and Tree," illustrating how repeatedly removing centroids turns path-counting queries into an O(log N)-layer divide-and-conquer.

### [Tutorial] Sack (dsu on tree)
- Author: Arpa
- URL: https://codeforces.com/blog/entry/44351
- Topic: Trees
- Takeaway: Explains "small-to-large merging" (DSU on tree / Sack) for answering subtree-aggregate queries (e.g., distinct colors in a subtree) in O(n log n) by reusing the heavy child's data structure instead of rebuilding it.

### [Tutorial] Binary lifting
- Author: AlexLuchianov
- URL: https://codeforces.com/blog/entry/100826
- Topic: Trees
- Takeaway: Covers binary lifting for O(log N) K-th ancestor and LCA queries via precomputed 2^h-ancestor jump tables, plus extensions for path-aggregate queries (e.g., max edge weight on a path).

### [Tutorial] Diameter of a tree and its applications
- Author: TheScrasse
- URL: https://codeforces.com/blog/entry/101271
- Topic: Trees
- Takeaway: Explains the two-DFS/BFS method for finding tree diameter and shows how bounding a node's distance to the diameter endpoints solves a series of increasingly advanced CP problems.

### Algorithms Thread 8: Tree Basics (+ Gym Contest)
- Author: SecondThread
- URL: https://codeforces.com/blog/entry/81527
- Topic: Trees
- Takeaway: Covers core tree fundamentals in one place — diameter computation, binary lifting for ancestor queries, and Euler tour flattening of a tree into an array so subtree queries can be answered with a segment tree.

## Data Structures for CP

### Efficient and easy segment trees
- Author: Al.Cash
- URL: https://codeforces.com/blog/entry/18051
- Topic: Data Structures for CP
- Takeaway: Introduces a compact, fully iterative (non-recursive) segment tree using only 2n memory laid out as a flat array, covering point-update/range-query, range-update/point-query, and lazy propagation variants without recursive overhead.

### EDU: DSU
- Author: Aksenov239
- URL: https://codeforces.com/blog/entry/82413
- Topic: Data Structures for CP
- Takeaway: Official ITMO Academy lecture on Disjoint Set Union, covering union by rank/size and path compression to achieve near-constant amortized time per operation.

### [Tutorial] Sparse table
- Author: AlexLuchianov
- URL: https://codeforces.com/blog/entry/101083
- Topic: Data Structures for CP
- Takeaway: Details the sparse table construction for O(N log N) preprocessing and O(1) idempotent range queries (min/max/gcd) by splitting any interval into two overlapping power-of-two-length pieces.

### AlgorithmsThread 5: Persistent Data Structures
- Author: SecondThread
- URL: https://codeforces.com/blog/entry/79669
- Topic: Data Structures for CP
- Takeaway: Explains how persistent segment trees keep a full version history by only reallocating the O(log N) nodes on the path touched by each update, enabling queries like "k-th smallest in array range across historical versions" and persistent queues.

### using merging segment tree to solve problems about sorted list
- Author: TLE
- URL: https://codeforces.com/blog/entry/49446
- Topic: Data Structures for CP
- Takeaway: Describes implicit "merge sort tree" style segment trees over dynamic sorted sets, supporting merge/split of sorted tiles and k-th-smallest queries by lazily allocating nodes only when needed for O(n log n) total complexity.

### [Tutorial] Square root decomposition and applications
- Author: box
- URL: https://codeforces.com/blog/entry/83248
- Topic: Data Structures for CP
- Takeaway: Comprehensive guide to sqrt decomposition — splitting an array of size N into O(sqrt N) blocks to get sqrt N per-operation cost — covering offline/online query processing, Mo's algorithm ordering, and block-based lazy rebuilding.
