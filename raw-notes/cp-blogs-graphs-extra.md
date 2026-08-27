# CP Blogs — Graph Algorithms: Extra Subtopics (2-SAT, Euler Path/Circuit, 0/1 BFS & Multi-Source BFS, Functional Graphs)

Sourcing note: WebSearch quota was exhausted for this session. Blog discovery was attempted via `codeforces.com/api/user.blogEntries` for a broad set of well-known tutorial authors (adamant, awoo, pajenegod, YouKn0wWho, SecondThread, Ashishgup, and others) filtered for titles matching each subtopic, plus the CF catalog/search pages and third-party curated lists (cp-algorithms.com, an awesome-competitive-programming GitHub list) as pointers back into Codeforces. This turned up very few single-topic Codeforces blog posts specifically dedicated to these 4 niche subtopics — most in-depth 2-SAT/Euler/0-1-BFS/functional-graph writeups live on non-CF sites (cp-algorithms.com, USACO Guide, personal blogs) rather than as native `codeforces.com/blog/entry/...` posts, which is what this task requires. Only one entry below is a genuine single Codeforces blog post; it is a meta-resource rather than a per-topic deep dive, and that limitation is disclosed in its Takeaway.

### The Ultimate Topic List (with Resources, Problems and Templates)
- Author: YouKn0wWho
- URL: https://codeforces.com/blog/entry/95106
- Topic: Graph Algorithms
- Subtopic: 2-SAT / Euler Path / Euler Circuit / 0/1 BFS & Multi-Source BFS / Functional Graphs (all four — general index)
- Takeaway: Verified via the Codeforces API (blogEntryId 95106, author YouKn0wWho) as a real, highly-upvoted CF blog post; note that the post itself is a short pointer/index — the actual per-topic tutorial links and problem lists (covering 2-SAT, Eulerian tours, and binary lifting on functional graphs among dozens of other topics) live on the external site it links to (youkn0wwho.academy/topic-list), not in the CF post body itself.

## Sourcing difficulties encountered

- Could not verify dedicated single-subject Codeforces blog posts for 2-SAT, Euler Path/Circuit, 0/1 BFS, or Functional Graphs specifically via `blogEntry.view` — attempts included scanning the full blog-entry lists of ~10 well-known algorithmic-tutorial authors for title keyword matches ("2-SAT", "Euler", "functional graph", "binary lifting", "0-1 BFS"), none of which turned up a matching real entry.
- Codeforces's own site search (`/search?searchQuery=...`) and catalog filter pages render results client-side via JavaScript, which is not visible through static fetches (direct curl is blocked by Cloudflare on codeforces.com problem/blog pages; the `r.jina.ai` proxy renders the page shell but not the JS-populated search results).
- Cross-verified, via cp-algorithms.com's own 2-SAT reference page, that Codeforces problems 776D, 1215F, and 1971H are legitimately cited practice problems for 2-SAT — this corroborates the problem list in `cp-guide-graphs-extra.md` even though it did not yield a Codeforces *blog* link.
- Given the above, this file intentionally contains only 1 verified blog rather than the requested 1-2 per subtopic; all problem-side findings (16-24 problems, listed in `cp-guide-graphs-extra.md`) were fully achievable and verified via the Codeforces public API and direct CSES/LeetCode fetches.
