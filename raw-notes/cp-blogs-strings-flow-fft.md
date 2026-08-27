# Verified Codeforces blogs: String Algorithms, Network Flow & Matching, FFT/NTT (fetched and confirmed via codeforces.com/api/blogEntry.view)

## String Algorithms

### Anti-hash test.
- Author: Zlobober
- URL: https://codeforces.com/blog/entry/4898
- Topic: String Algorithms
- Takeaway: Constructs a recursive "ABBA..." string (S, then S + NOT(S)) whose complementary-substring hash difference is divisible by 2^(Q(Q-1)/2), guaranteeing collisions for any polynomial hash taken mod 2^64 — the canonical weapon for hacking overflow-based hashing.

### On the mathematics behind rolling hashes and anti-hash tests
- Author: dacin21
- URL: https://codeforces.com/blog/entry/60442
- Topic: String Algorithms
- Takeaway: Formalizes two provably reliable randomization schemes for rolling-hash parameters (random base with fixed large prime, or random prime with fixed base) and catalogs real attacks (Thue-Morse sequences, birthday attacks, lattice reduction) against weak seeding.

### A short guide to suffix automata
- Author: quasisphere
- URL: https://codeforces.com/blog/entry/20861
- Topic: String Algorithms
- Takeaway: Concise online, linear-time suffix automaton construction built on suffix links between equivalence classes of end-position sets; shows that most SAM applications reduce to a DP over the automaton's DAG.

### Aho-Corasick algorithm. Construction
- Author: adamant
- URL: https://codeforces.com/blog/entry/14854
- Topic: String Algorithms
- Takeaway: Builds the Aho-Corasick automaton as a trie augmented with KMP-style failure/suffix links computed via BFS, enabling simultaneous multi-pattern matching in linear time.

### Manacher's Algorithm
- Author: utpalsen
- URL: https://codeforces.com/blog/entry/155241
- Topic: String Algorithms
- Takeaway: Unifies odd- and even-length palindrome cases with a `!z` bit trick and shows why the algorithm's right boundary pointer only ever moves forward, bounding total work to O(n); also covers an online variant.

### The Automaton Interpretation for the KMP Algorithm
- Author: arthur_9548
- URL: https://codeforces.com/blog/entry/146191
- Topic: String Algorithms
- Takeaway: Reframes the KMP prefix function as a deterministic finite automaton over the pattern, clarifying why prefix-function transitions are well-defined and simplifying related proofs/extensions (e.g., Aho-Corasick).

## Network Flow & Matching

### [Tutorial] My way of understanding Dinitz's ("Dinic's") algorithm
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/104960
- Topic: Network Flow & Matching
- Takeaway: Frames flow augmentation as moving between vertices of a convex polytope of valid flows, giving geometric intuition for why layered BFS graphs + blocking-flow DFS make Dinic an O(n^2·m) improvement over Edmonds-Karp.

### [Tutorial] Minimum cost (maximum) flow
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/105330
- Topic: Network Flow & Matching
- Takeaway: Proves that repeatedly augmenting along shortest (cheapest) residual paths preserves a no-negative-cycle invariant, which is exactly why successive shortest augmenting paths yields a globally optimal min-cost flow.

### [Tutorial] More about minimum cost flows: potentials and Dinitz
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/105658
- Topic: Network Flow & Matching
- Takeaway: Introduces vertex potentials (Johnson's reweighting) combined with Dijkstra and a Dinic-style blocking flow to push MCMF performance close to plain max-flow speeds.

### [Tutorial] Blossom Algorithm for General Matching in O(n^3)
- Author: Monogon
- URL: https://codeforces.com/blog/entry/92339
- Topic: Network Flow & Matching
- Takeaway: Explains how odd cycles ("blossoms") break naive augmenting-path search on general (non-bipartite) graphs, and how contracting/lifting blossoms restores correctness for O(n^3) general matching.

### [Tutorial] Hungarian algorithm in Õ(mn) or O(n^3)
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/128703
- Topic: Network Flow & Matching
- Takeaway: Derives the Hungarian algorithm from LP duality and complementary slackness, using vertex potentials plus incremental DFS over "tight" edges to find minimum-cost perfect bipartite matching.

### [Tutorial] Network simplex
- Author: brunovsky
- URL: https://codeforces.com/blog/entry/94190
- Topic: Network Flow & Matching
- Takeaway: Presents the simplex-method specialization for min-cost flow on spanning trees as a practical alternative to successive-shortest-path methods for certain flow and assignment problems.

## FFT / NTT

### [Tutorial] FFT
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/111371
- Topic: FFT / NTT
- Takeaway: Covers the coefficient/point-value duality and Cooley-Tukey FFT, plus the NTT variant under modulus 998244353, with applications to convolution and fuzzy string matching.

### Tutorial on FFT/NTT — The tough made simple. (Part 1)
- Author: sidhant
- URL: https://codeforces.com/blog/entry/43499
- Topic: FFT / NTT
- Takeaway: Builds FFT from first principles via divide-and-conquer on even/odd coefficient subsets evaluated at complex roots of unity, proving the key root-of-unity lemmas needed for correctness.

### Tutorial on FFT/NTT — The tough made simple. (Part 2)
- Author: sidhant
- URL: https://codeforces.com/blog/entry/48798
- Topic: FFT / NTT
- Takeaway: Gives visual/recursive intuition for the FFT butterfly structure and completes the round trip: coefficient form to point-value form (FFT), O(n) pointwise multiply, then back via inverse FFT.

### Notes on FFT / NTT, and the "ultimate" NTT with modulus > 9 * 10^18
- Author: Spheniscine
- URL: https://codeforces.com/blog/entry/75326
- Topic: FFT / NTT
- Takeaway: Proposes a single huge-modulus NTT (m ≈ 9223372036737335297, just under 2^63) with Barrett reduction to avoid CRT-merging or floating-point-precision workarounds when convolution outputs overflow 64-bit integers.

### [Tutorial] Bostan-Mori algorithm
- Author: Spheniscine
- URL: https://codeforces.com/blog/entry/149880
- Topic: FFT / NTT
- Takeaway: Uses generating-function manipulation (splitting even/odd terms of a rational power series) to compute the k-th term of a linear recurrence in O(d log d log k) time via NTT-based polynomial multiplication.

### Montgomery/Barret reduction and NTT [Performance optimization]
- Author: alexvim
- URL: https://codeforces.com/blog/entry/129600
- Topic: FFT / NTT
- Takeaway: Shows how Montgomery and Barrett modular-multiplication tricks eliminate slow division in the inner loop of NTT butterfly operations, giving a significant constant-factor speedup.
