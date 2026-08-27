# Wave 2 — Personal Blogs / Notes Repos Mining (Shivam5022, Lazar-Ilic, avinal, hieptran1812, sgoel97)

### Detect a cycle in an undirected graph
- Company: Hudson River Trading
- Role: unknown (2022 recruiting cycle, per candidate)
- Type: OA
- Round/Stage: online assessment (August 2022 cycle)
- Status: REAL
- Source: Lazar-Ilic/Lazar (quoting AlgoDaily/GlassDoor summaries) — https://raw.githubusercontent.com/Lazar-Ilic/Lazar/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: Lazar notes DFS-until-back-edge is standard; also mentions Tortoise-and-Hare / Brent's algorithm as lower-memory alternatives.

### Shortest path distance in matrix
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file as above
- Answer/Discussion: Lazar suggests flood-fill/BFS from source, taking min(neighbors)+1, in place to save memory.

### Maximum value per level of a tree/array structure
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: BFS with a running max per level, initializing output array to a very negative sentinel rather than 0.

### Swap every two adjacent nodes in a linked list
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: In-place pointer rearrangement with O(1) extra memory rather than rebuilding a new list.

### Implement a Binary Search Tree
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Called "canonical" by candidate; no further detail given.

### Traverse a matrix in spiral order
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate discusses avoiding a per-step boundary compare by precomputing run-lengths per side (e.g., for 5x5: 4 ups, 4 rights, 4 downs, 3 lefts...) and looping with care on final 1×n/n×1 remnants.

### Levenshtein edit distance
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Standard DP; called "super canonical."

### Next greater element in a circular array
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online assessment
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Monotonic stack approach (CSES-style).

### What do you know about inode?
- Company: Hudson River Trading
- Role: Systems/SWE (Linux-heavy)
- Type: Interview
- Round/Stage: unknown (Glassdoor-sourced, aggregated)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### What is the difference between RAID 5 and RAID 6?
- Company: Hudson River Trading
- Role: Systems/SWE
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Any alternative to the ls command? Why might du and df show discrepancies? What does `mv *` do? How would you install Linux on 100 compute nodes easily? What is the difference between soft and hard links?
- Company: Hudson River Trading
- Role: Systems/SWE
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file (batch of Linux/sysadmin questions listed together)
- Answer/Discussion: none found

### Take-home assessment, predicted 4-8 hours (actually took that long), required learning new tools; self-checking but reviewer got different (incorrect) results with no way to contest
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: take-home
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate complaint about unfair/inconsistent auto-grading, no appeal process.

### Programming project in Verilog
- Company: Hudson River Trading
- Role: likely FPGA/hardware-adjacent
- Type: OA/Take-home
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Given a string containing only 'A','B','C','D', remove all adjacent "AB"/"BA" and "CD"/"DC" pairs repeatedly and return the result
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online coding round
- Status: REAL
- Source: Lazar-Ilic/Lazar — Interviews Coding Rounds.txt (task description) + Hudson River Trading.cpp (Lazar's own submitted-style solution)
- Answer/Discussion: Lazar's C++ solution (from `Hudson River Trading.cpp`): builds an output buffer, popping the last char if `(output.back()+character) % 4 == 3` (exploits ASCII values of A/B/C/D mod 4), else pushes; he also gives an in-place-on-S variant post-hoc, noting the interviewer likely wanted O(1) extra memory: `int a=-1; for(char c: S){ if(a>=0 && (S[a]+c)%4==3) a--; else S[++a]=c; } S.resize(a+1);`. He reflects afterward that he should have produced the in-place version live.

### Given a graph/array of nodes valued 'A' or 'B' (a tree via parent-array), find the longest path where no two adjacent nodes share the same value
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online coding round
- Status: REAL
- Source: Lazar-Ilic/Lazar — Interviews Coding Rounds.txt + Hudson River Trading.cpp
- Answer/Discussion: Lazar's C++ solution does a DFS computing `maxpath[node]` = 1 + best child chain (only descending into children with a different label), tracking the best `3 + c + d` (top two child chains) as the global answer; O(V) overall.

### Physical memory vs virtual memory: you have 4GB physical but allocate an 8GB buffer — is this possible, and how? How is memory actually read as you traverse it?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found (question only, per candidate report)

### Thread vs process — what's the difference? Discuss common threading models.
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### What are some methods of inter-process communication (between threads, and between processes)? Explain how a named pipe (FIFO) works.
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### What does the `inline` keyword do in C++? What are the pros and cons?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### How do virtual functions work in C++? Explain how vtable lookup works.
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### map vs unordered_map in C++ — how is each implemented under the hood, and what data structure is used?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown (asked more than once per aggregated reviews)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate-supplied answer (quoted from StackExchange in the notes): map is typically a self-balancing BST (ordered), unordered_map is a hash map (faster average lookup but more memory overhead from the bucket array; worse for heavy insert/delete churn in some implementations).

### SQL question involving joins (including CTEs); separate Python/pandas dataframe join question
- Company: Hudson River Trading
- Role: likely Quant/Data-adjacent SWE
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Python decorators; "Jason tags" [sic, likely JSON]; normal question: count frequencies of things with equivalent representations, recursively calculate score for a string; troll question: given a string that may contain newlines, print a substring in a very specific, edge-case-heavy format
- Company: Hudson River Trading
- Role: unknown
- Type: Interview/OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### What kind of work environment do you enjoy the most? / CV questions asking about ML projects from a previous company
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: behavioral
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Heap Sort variant: "Almost Sorted Array" — an array where every element is at most k positions from its sorted position; sort it efficiently
- Company: Hudson River Trading
- Role: unknown
- Type: OA/Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's approach: maintain a min-heap of size ~k, process the first k elements into it, then repeatedly pop-min/push-next left to right; works as long as no two "inversions" are ≥k apart.

### A 3x3x3 cube has its outer surface painted red; if you pick one of the 27 unit sub-cubes uniformly at random, what is P[exactly 5 faces white, 1 face red]?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: brainteaser/probability
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: this describes the 6 face-center cubes (one painted face each) out of 27, so P = 6/27 = 2/9.

### Explain the Pearson correlation coefficient — definition and application
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Find the smallest positive integer that does not occur in a given sequence (e.g., A=[1,3,4,5] → return 2)
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online coding round
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found (classic "missing positive integer" problem)

### Write an algorithm that returns whether a binary string can be partitioned into k-sized intervals, each containing a specific number of 1s
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: online coding round
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Why Hudson River Trading? (asked in at least two separate reported interviews)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: behavioral/fit
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate notes their own answer was generic ("fascinated by markets, maths, statistics, game theory, algorithms... could apply to any competitor") and that a stronger answer should weave in something HRT-specific.

### Tell me about a time you had to work with someone different from you / Tell me about a time you made a mistake / Tell me about a time you succeeded / Why did you choose your major?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: behavioral
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: For "succeeded," candidate answered by pointing to a math-competition (Project Euler) gold medal win. For "major," candidate answered: liked math, admitted into UT Austin's math major via transfer.

### Full loop reported: phone interview (research + math), then 4 onsite rounds — one coding, one data science (pandas, prediction tasks), one open-ended, one behavioral; NDA signed for onsite portion
- Company: Hudson River Trading
- Role: unknown (Data Science-adjacent)
- Type: Interview
- Round/Stage: full loop description
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### 30-minute phone interview covering OS, OOP, and basic algorithms/data structures
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: phone screen
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### System architecture and Operating Systems questions (interview round)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### 45-minute technical math interview: probability question, Bayes' Theorem, random variable distributions, normal distribution
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: math/probability round
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Describe a recent interesting bug that you have resolved
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### What's the purpose of the `yield` keyword?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### How does a hashtable work? What happens when two keys' hashes collide (lookup/insert)? What's the time complexity of hashtable operations? When does a hashtable resize (up/down) and what's the runtime complexity of that?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### How does computer memory work? How does the OS allocate memory to each process? Virtual memory vs physical memory — what happens when virtual memory exceeds physical memory? Stack vs heap — what is stored in each?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### How does the Global Interpreter Lock (GIL) work? What's the advantage vs disadvantage of the GIL?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Are C++ runtime exceptions something you handle via try/catch? Would you expect exceptions on out-of-bounds vector access but NOT on raw array access? What happens with `array[out_of_bounds]`?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate notes this is undefined behavior for raw arrays — the compiler will not help you, unlike `std::vector::at()`.

### Kernel-level questions to assess OS understanding (candidate admits not being able to answer these)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Key benefit of TCP over UDP? / Some basic networking questions: difference between TCP and UDP
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown (asked in multiple reported rounds)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: TCP is connection-oriented and lossless (reliable, with retransmission), UDP is connectionless, faster, and simpler but lossy.

### Which is better and why: list vs vector vs array? (asked in more than one reported round, sometimes paired with the TCP/UDP question)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: vector is the industry-standard dynamic array (good general-purpose performance for insert/delete/lookup); C-style arrays can be faster in some cases but vectors are preferred for memory-management reasons in practice.

### Implement `stoi` (string-to-integer conversion) in C++/C, handling corner cases — e.g., what if the input is "1234567890" but you only have 16-bit integers to work with?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview/OA
- Round/Stage: unknown (asked as both a C++ and a plain-C task in different rounds)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate flags overflow/corner-case handling as the crux, and recommends actually implementing + testing it rather than assuming it's trivial.

### Find two numbers in an array that sum to a target (Two Sum); follow-up: find the two numbers whose sum is closest to the target; follow-up: what if the values are doubles instead of ints?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: sort + two pointers, O(n log n); for doubles, `==` comparisons need an epsilon/tolerance rather than exact equality due to floating-point precision.

### How does Python's dictionary (map) work under the hood?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: a dynamically-resizing hash map with amortized O(1) lookup/insert/delete; the hash table grows as elements are inserted to keep collision probability low.

### Basic algorithm question on deletion in an array — what's the complexity? (came up in an online coding round)
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: deletion from an arbitrary index of an array/vector is O(n); deletion from the relevant end of a vector/array/queue/stack/deque is O(1).

### Round described only as: "Optimisation problem, Statistics problem, Dynamic Programming problem"
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### First round: a week-long order-router implementation project. Second round: interview on Linux, networking, and C++ concepts.
- Company: Hudson River Trading
- Role: likely low-latency/systems SWE
- Type: Interview/Take-home
- Round/Stage: round 1 (take-home) + round 2 (technical interview)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Questions related to binary trees, hash maps, and linked lists (described by candidate as "sounds trivial")
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Quite a lot of basic computer architecture questions, including thread vs process, DNS, smart pointers, and compiler internals
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate quotes a StackExchange-style definition distinguishing process (code+memory+data+resources) vs thread (a sequence of code executing within a process; multiple threads can run concurrently in one process).

### Phone interview: deep C++ questions including STL implementation details and runtime memory allocation; also asked about C++ runtime exceptions. No algorithm questions on this call, C++ only.
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: phone screen
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Explain STL implementations and how malloc works
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Deep systems questions about memory management
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate mentions expecting to discuss the memory hierarchy (L1/L2/L3 caches, machine-specific behavior).

### 2nd round: technical interview on various C++ and kernel concepts
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: round 2
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Questions about memory, stack/heap, OS basics, and networking (TCP/UDP)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Using C (not C++) to implement `stoi`
- Company: Hudson River Trading
- Role: unknown
- Type: OA/Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Given a race track with 5 lanes, 25 horses/bunnies, and no timer, how many races are required to find the top 3 fastest?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: brainteaser
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's answer: 7 — run the initial 5 heats, then a "champions" race among the 5 heat-winners; use inequality chains among the results to deduce which remaining horses can still be 2nd/3rd, needing one final race to discern them. Candidate notes HRT explicitly warns candidates on their site that they may recognize canonical puzzles.

### Some in-depth questions about polymorphism in C++
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### How do you support multi-threading without kernel support (i.e., user-level threads)?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate pastes a detailed explanation (sourced from an external OS course page) contrasting kernel-level threads (managed by the OS, PCB/TCB, slower context switches) with user-level threads (managed entirely in user space by a runtime library, fast switching, but the kernel can make poor scheduling decisions since it's unaware of them).

### Count the number of days between 2 given dates
- Company: Hudson River Trading
- Role: unknown
- Type: OA/Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate suggests near-O(1) via direct year/leap-year arithmetic rather than iteration.

### A pandas-based question ("expected knowledge if it's on your resume")
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Write a program to add two binary strings
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate discusses processing right-to-left with carry, or packing ~31/63 bits into native ints at a time for speed.

### Complete the Calculator Class (implement a basic expression calculator, handle division-by-zero etc.)
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### What is the minimum number of comparisons needed to find the 2nd-largest element in a list?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate discusses the classic tournament/decision-tree method achieving n + ceil(log2 n) − 2 comparisons, and links several references on the lower-bound proof via decision trees.

### LeetCode-style: "Remove Comments" and "Number of Atoms" (candidate flags these as ones you could "cheat" and look up mid-round)
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Given an array, determine if every number can be written as a sum of 2 Fibonacci numbers
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate notes every natural number ≥ 2 can be so written (relates to Zeckendorf's theorem).

### Given a set of 2D points, determine how many squares and how many rectangles can be formed
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's approach: O(n^2) via hashing pairs by (midpoint, squared-distance) for rectangles (count = sum of C(multiplicity, 2)); for squares, also track slope/orthogonality, or alternatively check for each pair-as-diagonal whether the other two implied corners exist in a coordinate hash set.

### Sum of all 2-digit numbers that do not contain the digits 7 or 8
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — Interviews Coding Rounds.txt + Hudson River Trading.py (candidate's own practice implementation)
- Answer/Discussion: Candidate builds a size-200 prefix-sum array over [-99,99] to answer range-sum queries in O(1), skipping numbers whose last digit is 7/8 (or, in his generalized version, 2/3 for negative numbers to mirror the positive-side exclusion). Working Python code included in `Hudson River Trading.py`.

### Coding different scenarios and games (round description only)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Computer organisation and algorithms round (round description only, candidate joked about the compensation implications of "tricking them" on C++14 knowledge)
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### How can you run multiple processes on one computer?
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate pastes a standard explanation distinguishing true parallelism (multi-core) from time-sliced scheduling (single-core).

### 1 hour to complete 4 coding questions (1 easy + 3 mediums, or 2 mediums + 1 hard) — candidate calls the time limit "very frustrating" and questions what the OA actually measures
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found (candidate opinion only — argues it mostly measures whether you've memorized similar problems, e.g. from competitive programming)

### Programming question in C++ based around stacks
- Company: Hudson River Trading
- Role: unknown
- Type: OA/Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Toss a fair die 100 times and a fair coin 400 times; compute P[sum of dice rolls > number of coin heads]
- Company: Hudson River Trading
- Role: unknown
- Type: Interview
- Round/Stage: probability/estimation
- Status: REAL
- Source: Lazar-Ilic/Lazar — Interviews Coding Rounds.txt + Hudson River Trading.py (Lazar's own working implementation)
- Answer/Discussion: Candidate notes expected values are 350 (dice) vs 200 (coin), computes the exact answer via DP (convolution of the two exact distributions) rather than simulation, getting P ≈ 0.9999999999999925 (exact fraction given). He proposes an O(a log b) approach via generating-function convolution/FFT and specifically warns that naive Monte Carlo simulation would be wrong here because the true probability is so close to 1 that many iterations would be needed to converge; also flags float/double precision loss in the naive ratio. His actual Python DP code computing this is preserved in `Hudson River Trading.py`.

### One HRT candidate review: 4 rounds of a Codesignal-style test (arrays only, not the trees/graphs/stacks the candidate expected), with 2 medium array questions where not all test cases passed
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### One round: 1 strings question, 1 array question, 1 OOP question, 1 graph question
- Company: Hudson River Trading
- Role: unknown
- Type: OA/Interview
- Round/Stage: unknown
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found

### Applied to two new-grad roles (algo engineer + SWE); algo-engineer CodeSignal OA had a 2-hour, 3-question challenge (first two LeetCode-medium, third harder than LeetCode-hard, requiring ALL test cases to pass, not just some within time/space limits); failed and was rejected quickly, but then given a separate SWE-track "General Coding Assessment" (standard CodeSignal test), scored 840+ with 20 minutes to spare, and was still rejected a week later with no explanation
- Company: Hudson River Trading
- Role: New Grad — Algorithm Engineer / Software Engineer
- Type: OA
- Round/Stage: online assessment (CodeSignal)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate's takeaway: "HRT is very happy to send out OA to applicants, but passing the OA is a mystery."

### Optiver "Prove It" Episode 1 — probability/coin-toss round involving Stirling's approximation and the probability two independent draws match
- Company: Optiver
- Role: unknown
- Type: Interview
- Round/Stage: "Prove It" (Optiver's recruiting puzzle series)
- Status: REAL
- Source: Lazar-Ilic/Lazar — Interviews Coding Rounds.txt (personal, first-person, titled "Optiver Prove It Episode 1 — Lazar Ilic")
- Answer/Discussion: Lazar walks through Stirling's approximation for the central binomial coefficient `(1/2)^(2n) * C(2n,n) ≈ 1/sqrt(nπ)`, a Cauchy-Schwarz argument that the probability two independent draws from any discrete distribution on n+1 outcomes match is ≥ 1/(n+1), and includes his own Python code (both an O(n^2) Pascal's-triangle version and a fast O(n) recurrence version) to compute the exact central-binomial-coefficient-based probabilities to high precision, noting he'd use ~48 bits of long double precision in C++ for Optiver's purposes.

### Optiver "Prove It" Episode 2 — random-walk/expected-displacement puzzle with a specific numeric answer set (16, 15, 12, 7, 0) and a biased (p=1/3) coin-toss follow-up
- Company: Optiver
- Role: unknown
- Type: Interview
- Round/Stage: "Prove It" (Optiver's recruiting puzzle series)
- Status: REAL
- Source: Lazar-Ilic/Lazar — same file (first-person, titled "Prove It Episode 2 — Lazar Ilic")
- Answer/Discussion: Lazar recounts guessing the wrong order of magnitude for expected deviation from the starting point (guessed ~12, true relevant values were larger), derives that `16,15,12,7,0` is the unique solution to the underlying system of equations (general form `n², n²−1², n²−2², ..., 2n−1, 0`), and for the p=1/3 coin-toss variant, references OEIS sequence A095264 to get exact values (e.g. `E06=234, E16=233, ... E66=0`) via the delta differences `2^(n+2) − 3n − 4`.

### Optiver-style task: given 300,000 horses with market betting odds and your own credence (probability estimate) of each horse winning, compute the betting-portfolio strategy that maximizes expected log-bankroll growth
- Company: Optiver
- Role: unknown
- Type: unknown (candidate frames it as a "potpourri task from the GlassDoor corpus," not confirmed to be his own live round)
- Round/Stage: unknown
- Status: PRACTICE
- Source: Lazar-Ilic/Lazar — Interviews Coding Rounds.txt
- Answer/Discussion: Candidate names this as a Kelly-criterion/log-utility optimal-betting problem solvable via Lagrange multipliers, citing Smoczynski & Tomkins, Whitrow, and Grant/Buchen as references for the "Dutch book"/horse-race Kelly literature.

### Minimum number of knight moves from (a,b) to (c,d) on an n×n board, for n up to ~10^9, in O(1)
- Company: Optiver (per candidate's framing as a "litmus test for HFT SWE")
- Role: HFT Software Engineer
- Type: PRACTICE (candidate frames it as a self-set practice/prep task, not a confirmed live interview question)
- Round/Stage: unknown
- Status: PRACTICE
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: Candidate flags that a naive BFS over a boolean grid is not viable at this scale and that an O(1) closed-form/case-based solution is expected; links a CS.StackExchange discussion of the closed-form knight-distance-on-infinite-board formula.

### Maximum square frame of 0s in an n×n grid (candidate's own practice framing, O(n²))
- Company: Optiver (candidate's framing)
- Role: unknown
- Type: PRACTICE
- Round/Stage: unknown
- Status: PRACTICE
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: none found (candidate just labels it "onsight flawless C in O[n^2]")

### Construct a BST from an in-order sequence and answer Lowest-Common-Ancestor queries; compute the sum of the first n integers "hit" by a vector of size m << n; count the number of increasing subsequences of length 3
- Company: Optiver (candidate's framing, listed alongside the above as practice tasks from "top trading firms")
- Role: unknown
- Type: PRACTICE
- Round/Stage: unknown
- Status: PRACTICE
- Source: Lazar-Ilic/Lazar — same file
- Answer/Discussion: For the length-3 increasing-subsequence count, candidate gives an O(n log n) approach using an ordered set to count, for each index as the middle element, how many smaller elements are to its left and how many larger are to its right, then summing the products.

### Example coding questions "asked by Meta" — array product-except-self, near-palindrome check, next permutation, minimum-window substring, group anagrams, valid-parentheses, 3Sum, BST range-sum, binary-tree-to-circular-DLL, BST iterator, tree diameter, serialize/deserialize a binary tree, max path sum, alien-dictionary character ordering, bipartite check, continuous-subarray-sum-multiple-of-k, best-time-to-buy-and-sell-stock, regex matching with `.`/`*`, target-sum via +/- assignment, k-closest-points-to-origin, array intersection, minimum meeting rooms, copy-list-with-random-pointer, reorder linked list, implement a queue using two stacks
- Company: Meta
- Role: unknown
- Type: Unknown (presented as a curated/aggregated "example questions" list by category with reported frequency percentages, not a specific personal interview account)
- Round/Stage: unknown
- Status: PRACTICE
- Source: Lazar-Ilic/Lazar — Notes/Computer Science/Algorithms/Interviews Coding Rounds/Meta.txt — https://raw.githubusercontent.com/Lazar-Ilic/Lazar/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Meta.txt
- Answer/Discussion: File gives standard solutions/approaches for each (e.g., two-pass product-except-self; sort+hash for anagrams; DFS/BFS for the tree questions; hash map of prefix-sum-mod-k for the subarray-multiple-of-k problem; two-stack queue implementation), largely reproduced from GeeksforGeeks-style write-ups rather than a personal interview narrative.

---

## avinal/avinal.github.io

### HRT Systems Internship interview process: Codility OA (2.5 hr window, 90 min test, 3 questions, choice of C/C++, Python, or Golang — no Java), followed by a 45-minute non-coding phone interview
- Company: Hudson River Trading
- Role: Systems Internship (Summer 2021)
- Type: Interview + OA
- Round/Stage: OA (Codility) then phone interview
- Status: REAL
- Source: avinal/avinal.github.io blog post "HRT (Hudson River Trading) Systems Internship Interview Experience" — https://raw.githubusercontent.com/avinal/avinal.github.io/main/src/content/posts/blogs/hrt-interview-1.md
- Answer/Discussion: Author reports the OA questions were "clear and medium level," rewarding a clean/concise approach; official guidance said a perfect score isn't required and speed matters alongside correctness. Phone round covered Linux/Unix, C++ (mainly pointers and memory), Python/Bash scripting, automation, dev tools/IDEs, and past experience — no coding, since it was a Systems (not SDE) role. Interviewer also asked "why do you want this role?" and "what makes you fit for this role?" and stuck close to the resume. Author's retrospective tips: keep a resume with only genuine tool/work experience (interviewer cross-checked it closely), don't over-talk, ask more questions about the role, and work on communication/examples-based answers.

---

## hieptran1812/my-website (content/blog/trading) — general note on this source

All posts checked (see below) are long-form, SEO-style career-advice essays built around a **recurring fictional composite candidate** ("Maya," "Wei," "Aran") rather than the blog author's own real interview experience. They read as generated/synthesized advisory content (explicitly hedged, e.g. "the firms do not publish these numbers," "illustrative," citing third-party aggregator sites like levels.fyi/efinancialcareers rather than a personal account). None of the material found qualifies as a first-person REAL interview report. All entries below are marked PRACTICE and represent the illustrative/example questions embedded in that advisory content, retained because they are genuinely representative of the question types candidates report facing at these firms.

### 47 × 53 (and similar): a batch of representative mental-math questions in the Optiver/IMC style (two/three-digit multiplication, percentages, fraction-to-decimal conversions, numeric sequences, estimation/bracketing, e.g. `48×52`, `15% of 80`, `7/8 as a percent`, `624/8`, `2,5,11,23,?`, `√90`, `34×11`, `0.375 as a fraction`)
- Company: Optiver / IMC
- Role: Quant Trader (internship-track)
- Type: OA
- Round/Stage: timed mental-math screen (reported ~60-80 questions in 8 minutes, no calculator, pass bar ~70-85%)
- Status: PRACTICE
- Source: hieptran1812/my-website — "The Optiver and IMC Playbook: The Mental-Math Gauntlet" — https://raw.githubusercontent.com/hieptran1812/my-website/main/content/blog/trading/quant-careers/optiver-and-imc-playbook-the-mental-math-gauntlet.md
- Answer/Discussion: Post gives the fast-method for each (difference-of-squares for near-equal factors, 10%+5% percentage decomposition, memorized eighths/sixteenths fraction anchors, difference-then-ratio-then-second-order triage for sequences, bracketing between perfect squares for roots) and works through the EV math of speed-vs-accuracy trade-offs under the timer.

### "I'm rolling three fair six-sided dice and summing them — make me a market on the total." / "I'm thinking of the sum of two fair six-sided dice that I've already rolled and am hiding. Make me a market."
- Company: Optiver / IMC (market-making trading-game round, generic framing)
- Role: Quant Trader
- Type: Interview
- Round/Stage: trading-games round
- Status: PRACTICE
- Source: hieptran1812/my-website — "The Optiver and IMC Playbook" and "The Interview Loop, Round by Round" — https://raw.githubusercontent.com/hieptran1812/my-website/main/content/blog/trading/quant-careers/the-interview-loop-round-by-round.md
- Answer/Discussion: Post walks through computing the fair value (expected sum 10.5 or 7), quoting a spread around it (e.g. "9 bid at 12" or "6 at 8"), and updating the quote (widening/re-centering) after the interviewer trades against you, since a fill is itself information about where the true value lies (adverse-selection reasoning).

### "What is the expected number of coin flips to get two heads in a row?" / "I roll a die repeatedly and sum the values; you can stop any time and keep the running sum, but if you roll a 1 you lose everything — what is your optimal stopping rule and expected payoff?" / "Three points are placed uniformly at random on a circle; what is the probability they all lie in some semicircle?"
- Company: unspecified prop/quant firms (generic "probability and brainteaser round" examples)
- Role: Quant Trader / Researcher
- Type: Interview
- Round/Stage: probability & brainteaser round
- Status: PRACTICE
- Source: hieptran1812/my-website — "The Interview Loop, Round by Round" — same URL as above
- Answer/Discussion: Post states these are given as illustrative "classic examples" of the round's difficulty escalation; no full solutions given (points to a separate sibling post on the same site for solving technique).

### "I flip a fair coin repeatedly until I get heads. You win 2 dollars raised to the number of flips it took. What is a fair price to play this game?" (the St. Petersburg paradox)
- Company: unspecified prop/quant firm (generic probability-round example)
- Role: Quant Trader
- Type: Interview
- Round/Stage: probability round
- Status: PRACTICE
- Source: hieptran1812/my-website — "The Interview Loop, Round by Round" — same URL as above
- Answer/Discussion: Worked in full: P(first heads on flip k) = (1/2)^k, payoff $2^k, so each branch contributes exactly $1 to EV; summing infinitely many branches means the mathematical EV diverges to infinity, but the "trader" answer distinguishes the divergent mathematical fair price from what you'd actually pay in practice (illustratively, ~$4–$8) given the huge variance and vanishingly-likely astronomical payoffs.

### "How many golf balls would fit inside a typical commercial airplane?"
- Company: Jane Street (generic framing)
- Role: Quant Trader
- Type: Interview
- Round/Stage: superday, estimation/Fermi round
- Status: PRACTICE
- Source: hieptran1812/my-website — "Jane Street Playbook: Culture, OCaml, and the Trading Games" — https://raw.githubusercontent.com/hieptran1812/my-website/main/content/blog/trading/quant-careers/jane-street-playbook-culture-ocaml-and-the-trading-games.md
- Answer/Discussion: Post frames the "right" answer as a calibrated range with named sources of uncertainty (e.g., "roughly 1 to 2.5 million, centered near 1.7 million, least sure about cabin volume and seats/cargo"), scored on decomposition and honest uncertainty-bounding rather than the exact number.

### "I'm thinking of a number. It's the sum of the digits of a random page I'll open in a 600-page book. You're the market maker. Make me a market."
- Company: Jane Street (generic framing)
- Role: Quant Trader
- Type: Interview
- Round/Stage: superday, market-making game
- Status: PRACTICE
- Source: hieptran1812/my-website — "Jane Street Playbook" — same URL as above
- Answer/Discussion: Post's worked answer: quote something like "8 at 10" (mean digit-sum of a random 1-600 page number is roughly 8-9); if the interviewer lifts your offer, that's a signal to skew the market upward on the next quote (adverse-selection/Bayesian-update reasoning), rather than freezing or re-quoting the same market.

### "I'll roll a fair die. If it comes up 6, I pay you $5. Otherwise, you pay me $1. Do you want this bet, and how much would you scale it if you could?"
- Company: Jane Street (generic framing)
- Role: Quant Trader
- Type: Interview
- Round/Stage: phone screen, betting/EV round
- Status: PRACTICE
- Source: hieptran1812/my-website — "Jane Street Playbook" — same URL as above
- Answer/Discussion: EV = (1/6)(5) + (5/6)(−1) = $0. Post frames the "good" answer as recognizing EV≈0/slightly negative and reasoning about sizing/variance (Kelly intuition) rather than jumping to a number, even discussing the case where the EV is positive but variance argues against betting the full bankroll.

### Betting scenario for Kelly-criterion/risk-of-ruin reasoning: "wager any fraction of your $100,000 bankroll; with probability 0.60 it triples, with probability 0.40 you lose the stake"
- Company: Susquehanna International Group (SIG) (generic framing)
- Role: Quant Trader
- Type: Interview
- Round/Stage: games/decision-theory round
- Status: PRACTICE
- Source: hieptran1812/my-website — "SIG/Susquehanna Playbook: Poker, Game Theory, and EV" — https://raw.githubusercontent.com/hieptran1812/my-website/main/content/blog/trading/quant-careers/sig-susquehanna-playbook-poker-game-theory-and-ev.md
- Answer/Discussion: Per-dollar EV = 0.60(+$2) + 0.40(−$1) = +$0.80 (an 80% edge), but betting the entire bankroll gives a 40% chance of total ruin; post uses this to teach Kelly-criterion sizing (full-Kelly = bet $20,000 here; many practitioners use half-Kelly, $10,000, to cut variance for a small growth-rate cost) and the "a +EV bet is not automatically the right bet" lesson.

### "This loop reads one past the end of the array on the last iteration but works on my machine — why is that a ticking bomb?" (illustrative undefined-behavior question) — plus general C++/systems depth topics: memory model & `std::atomic` orderings (`relaxed`/`acquire`/`release`/`seq_cst`), false sharing, cost of `std::shared_ptr` atomic refcounting, lock-free stack with CAS and the ABA problem, SPSC ring buffer implementation, arena/object-pool allocators, cache-hierarchy latency numbers, kernel bypass, real-time market-data-to-order systems design
- Company: Jump Trading / Hudson River Trading (generic framing for "latency-sensitive HFT" C++/systems interview round)
- Role: Low-latency / Quant Developer
- Type: Interview
- Round/Stage: C++ depth round + systems-design round
- Status: PRACTICE
- Source: hieptran1812/my-website — "The Jump and HRT Playbook: The Low-Latency Systems Bar" — https://raw.githubusercontent.com/hieptran1812/my-website/main/content/blog/trading/quant-careers/jump-and-hrt-playbook-the-low-latency-systems-bar.md
- Answer/Discussion: Post argues these rounds test whether you understand "what the machine does when your code runs" rather than syntax; explicitly notes HRT lets candidates choose C++ or Python for coding rounds, but the systems/C++ depth bar is real regardless of language choice. Recommends hands-on measurement (e.g., benchmark padded vs. unpadded counters across threads to see false-sharing throughput differences) as prep rather than passive reading.

### Same source also confirms round-structure facts relevant to C++/HFT prep: HRT "explicitly lets you pick your language (C++ or Python)" and "runs an algorithm round, a math/probability round, and a systems-design round"
- Company: Hudson River Trading
- Role: Low-latency / Quant Developer
- Type: Interview
- Round/Stage: full loop description
- Status: PRACTICE
- Source: hieptran1812/my-website — "The Interview Loop, Round by Round" — same URL as above
- Answer/Discussion: none found (general loop-structure claim, not a specific question)

---

## Dead ends / no extractable interview Q&A

- **Shivam5022/Knowledgebase-SV** — full repo tree reviewed (67 files: README, notes/*.md study notes on OS/C++/dev-tools, CPP-Internals code links). This is a curated personal study/reference wiki (links to books, YouTube lectures, and the author's own from-scratch C++ implementations like unique_ptr/shared_ptr/thread_pool/LRU_cache) with **no interview-question content or interview narratives at all** — not even generic ones. No entries extracted.
- **Lazar-Ilic/Lazar — "Garbled Garbage With ChatGPT.txt"** — a log of unrelated personal ChatGPT conversations (audio equipment, music, unrelated trivia, a short bio of the author) with no interview content. No entries extracted.
- **Lazar-Ilic/Lazar — "Cracking The Coding Interview With ChatGPT.py", "HackerRank C.c", "LeetCode*.{cpp,py,txt}", "LeetCode Top 100 Interview Questions.cpp", "Matrix Multiplication, NumPy, TensorFlow.txt", "Python..." files, "UIUC MCSO Admissions Quiz*"** — generic LeetCode/algorithm practice code and non-interview study material, not tied to any specific company or real interview account. Not mined in detail (out of scope: no company attribution).
- **sgoel97/blog — "Acing the Quant Interview"** — fully read. This is a meta/prep-strategy guide (resume tips, application timeline, recommended UC Berkeley courses, book recommendations — "A Practical Guide to Quantitative Finance Interviews" and "Quant Job Interview Questions and Answers" — and a long categorized list of firms). It contains **no specific interview questions or first-person interview narrative** to extract — it is advice about how to prepare, not a record of what was asked. No entries extracted.
