# String Algorithms — Extra CF Blogs (Suffix Automaton, Aho-Corasick, Palindromic Tree)

All entries verified live via the Codeforces public API (`blogEntry.view?blogEntryId=<id>`), which returned `status: OK` with the exact title and author handle shown below.

### A short guide to suffix automata
- Author: quasisphere
- URL: https://codeforces.com/blog/entry/20861
- Topic: String Algorithms
- Subtopic: Suffix Automaton
- Takeaway: A concise, widely-cited construction walkthrough of the suffix automaton (equivalence classes / endpos sets, transitions, and suffix links) aimed at people who found e-maxx's version too dense.

### Understanding Suffix Automaton in depth
- Author: Safrout
- URL: https://codeforces.com/blog/entry/20764
- Topic: String Algorithms
- Subtopic: Suffix Automaton
- Takeaway: A deeper, more intuition-driven follow-up explanation of why SAM states correspond to endpos-equivalence classes, useful once the short-guide construction mechanics already make sense.

### Aho-Corasick algorithm. Construction
- Author: adamant
- URL: https://codeforces.com/blog/entry/14854
- Topic: String Algorithms
- Subtopic: Aho-Corasick Multi-Pattern Matching
- Takeaway: A rigorous construction-focused writeup of the Aho-Corasick automaton (trie + fail links via BFS) from one of Codeforces' most trusted algorithm-blog authors, framing it explicitly as "just the start" of what the automaton enables.

### Aho-Corasick with additions
- Author: 1k_trash
- URL: https://codeforces.com/blog/entry/10725
- Topic: String Algorithms
- Subtopic: Aho-Corasick Multi-Pattern Matching
- Takeaway: Covers extending the basic Aho-Corasick automaton to handle incremental/dynamic pattern additions — directly relevant background for problems like CF 710F "String Set Queries."

### Palindromic tree
- Author: ADJA
- URL: https://codeforces.com/blog/entry/13958
- Topic: String Algorithms
- Subtopic: Palindromic Tree (Eertree)
- Takeaway: The original Codeforces introduction of the palindromic tree (Eertree) data structure — two suffix-linked trees (for even/odd-length palindromes) built incrementally in amortized O(n).

### Palindromic tree: behind the scenes
- Author: adamant
- URL: https://codeforces.com/blog/entry/13959
- Topic: String Algorithms
- Subtopic: Palindromic Tree (Eertree)
- Takeaway: A follow-up deep dive answering "why does the O(n) amortized bound hold," explaining the internal series/suffix-link jumping that makes Eertree insertion efficient rather than just presenting the algorithm as a black box.
