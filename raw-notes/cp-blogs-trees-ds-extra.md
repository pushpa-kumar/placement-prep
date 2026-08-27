# CP Guide — Extra Blogs: Trees & Data Structures Subtopics

Blogs verified via the Codeforces public API (`blogEntry.view?blogEntryId=<id>`), which returns each blog's real author handle, title, and content directly (Cloudflare blocks plain `curl` on the HTML blog pages, but the API endpoint itself is unauthenticated and worked). Lower priority per task instructions — coverage below is partial; see sourcing notes at the end.

## Trees

### [Tutorial] Sack (dsu on tree)
- Author: Arpa
- URL: https://codeforces.com/blog/entry/44351
- Topic: Trees
- Subtopic: Small-to-Large Merging (DSU on Tree)
- Takeaway: One of the most-referenced original explanations of the "sack" (dsu on tree) technique, including complexity proof and a worked example.

### [Explanation] dsu on trees (small to large)
- Author: rewhile
- URL: https://codeforces.com/blog/entry/67696
- Topic: Trees
- Subtopic: Small-to-Large Merging (DSU on Tree)
- Takeaway: A more beginner-friendly re-explanation of the same technique (explicitly written as a companion/expansion to Arpa's original blog), with clearer pseudocode for the heavy-child-first traversal order.

### Tutorial on Virtual/Auxiliary Trees and YouTube channel
- Author: radoslav11
- URL: https://codeforces.com/blog/entry/76955
- Topic: Trees
- Subtopic: Virtual Trees (Auxiliary Tree Technique)
- Takeaway: A tutorial specifically on building and using virtual/auxiliary trees (LCA-closure of a queried vertex subset) to solve subtree-DP-style problems in near-linear total time.

### Mo's Algorithm on Trees [Tutorial]
- Author: animeshf
- URL: https://codeforces.com/blog/entry/43230
- Topic: Trees
- Subtopic: Mo's Algorithm (applied to trees)
- Takeaway: Explains flattening subtree/path queries into array ranges via Euler tour so that standard Mo's algorithm can answer offline tree queries, bridging the trees and Mo's-algorithm subtopics.

## Data Structures for CP

### On "Mo's algorithm"
- Author: mnbvmar
- URL: https://codeforces.com/blog/entry/20032
- Topic: Data Structures for CP
- Subtopic: Mo's Algorithm
- Takeaway: A concise treatment of Mo's algorithm's offline sqrt-block query reordering, complexity analysis, and common pitfalls (e.g. correct block size choice, handling l/r movement order).

## Sourcing difficulties

- WebSearch was exhausted for this session (200/200 budget used) before blog research began, so all blog discovery relied on the Codeforces `blogEntry.view` API with guessed/recalled blog IDs plus `user.blogEntries` lookups for known tutorial authors (adamant, SecondThread, pajenegod, mnbvmar, Um_nik, ko_osaga, anudeep2011, etc.) rather than free-text blog search — direct HTML fetches of `codeforces.com/blog/entry/...` are Cloudflare-blocked, but the JSON API endpoint is not.
- No qualifying Codeforces blog was found and verified for **Tree Isomorphism / Canonical Form**, **Sqrt Decomposition**, or **2D Fenwick Tree / 2D Range Queries** within the available search budget. These techniques are more commonly documented on cp-algorithms.com, USACO Guide, or as sections inside larger "data structures gym" blogs (e.g. CF blog 15729, "Algorithm Gym :: Data structures" by PrinceOfPersia, which is a broad survey blog touching partial sums and DSU but was not confirmed to have a dedicated sqrt-decomposition or 2D-BIT section) rather than as their own standalone, unambiguously-titled Codeforces blog posts that could be positively identified without further guessing.
