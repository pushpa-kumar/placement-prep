# Curated Codeforces blogs: Recursion/D&C, Greedy, Bit Manipulation, Game Theory extensions (all verified live via Codeforces blogEntry.view API, Aug 2026)

Covers the same 7 new subtopics as cp-guide-recursion-greedy-bit-game-extra.md: Divide and Conquer, Minimax
with Alpha-Beta Pruning, Huffman Coding & Optimal Merge, Fractional vs. 0/1 Greedy Recognition, Bit Tricks &
Gray Code, Bitset Optimization for Brute-Force Speedup, and Combinatorial Game Sums & Misère Play.

## Greedy Algorithms

### On "is this greedy or DP", forcing and rubber bands
- Author: -is-this-fft-
- URL: https://codeforces.com/blog/entry/106346
- Topic: Greedy Algorithms
- Subtopic: Fractional vs. 0/1 Greedy Recognition
- Takeaway: Discusses concrete heuristics ("forcing" moves and "rubber band" exchange arguments) for recognizing when a problem that looks like it needs DP actually admits a provably-correct greedy solution — directly the skill this subtopic targets.

### Lecture #3 — Exchange arguments (sorting with dp)
- Author: Errichto
- URL: https://codeforces.com/blog/entry/63533
- Topic: Greedy Algorithms
- Subtopic: Fractional vs. 0/1 Greedy Recognition
- Takeaway: Walks through the exchange-argument proof technique for justifying that sorting by a particular key is optimal, the same style of reasoning that certifies when a fractional-relaxation-style greedy choice generalizes correctly to the discrete/0-1 case.

## Bit Manipulation

### Bitwise operations for beginners
- Author: Errichto
- URL: https://codeforces.com/blog/entry/73490
- Topic: Bit Manipulation
- Subtopic: Bit Tricks & Gray Code
- Takeaway: Covers foundational bit tricks (extracting/setting/clearing bits, x & -x for the lowest set bit, iterating over submasks) that underlie techniques like Gray code generation and popcount manipulation.

### Bitwise operations 2 — popcount & bitsets
- Author: Errichto
- URL: https://codeforces.com/blog/entry/73558
- Topic: Bit Manipulation
- Subtopic: Bitset Optimization for Brute-Force Speedup
- Takeaway: Explains __builtin_popcount and std::bitset mechanics and shows how bitset operations (AND/OR/XOR/shift) can turn an O(n^2) brute-force loop into an O(n^2/64) one — the exact mechanism behind problems like GCD Counting and Dasha and cyclic table.

## Game Theory

### Nimbers and Sprague-Grundy theorem
- Author: adamant
- URL: https://codeforces.com/blog/entry/103785
- Topic: Game Theory
- Subtopic: Combinatorial Game Sums & Misère Play
- Takeaway: A rigorous derivation of the Sprague-Grundy theorem showing why any impartial game decomposes into a nimber, and why the Grundy value of a sum of independent games is the XOR of their individual Grundy values.

### [Incoherent Rambling] Optimal strategy in game theory
- Author: Monogon
- URL: https://codeforces.com/blog/entry/128693
- Topic: Game Theory
- Subtopic: Minimax with Alpha-Beta Pruning
- Takeaway: Discusses how to reason about and search for optimal strategies in adversarial two-player games, the general minimax framing that underlies CP problems like Letter Picking and Game on Sum even when explicit alpha-beta pruning code isn't needed at CF's typical state-space sizes.

## Sourcing notes

- No verifiable Codeforces blog specifically about Divide and Conquer (master theorem / closest-pair-of-points
  style D&C, as distinct from D&C DP optimization) was found after checking the blog lists of several authors
  known for algorithmic tutorials (adamant, Errichto, Radewoosh, Um_nik, pajenegod, Monogon, TheScrasse, and
  others) via the Codeforces API. WebSearch quota was exhausted mid-task, and Bing-via-jina.ai proxy searches
  did not surface a usable direct blog link for this topic.
- No verifiable Codeforces blog specifically about Huffman Coding & Optimal Merge was found through the same
  handle-by-handle API search; this appears to be a topic more commonly covered in textbooks/GeeksforGeeks-style
  articles than in Codeforces blog entries.
- No genuine misère-play-specific Codeforces problem (i.e., "last player to move loses," as opposed to the
  standard normal-play "player who cannot move loses" convention) was found among the game-theory problems
  checked; misère Nim's edge-case rule appears to be treated as a purely theoretical topic in the CP community
  rather than the direct subject of judge problems on Codeforces, CSES, or LeetCode. The Sprague-Grundy blog
  above discusses the theory but the problems curated in the companion file all use normal play.
