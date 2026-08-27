# Raw notes: GitHub-mined real interview/OA questions with company attribution (quant/HFT/C++)

### 2.5 hr Codility online test, 3 questions, choice of C/C++, Python, or Golang; online references allowed but no copy-pasting code
- Company: Hudson River Trading
- Role: Systems Intern (Summer 2021)
- Type: OA
- Status: REAL
- Source: avinal.github.io (personal blog) — https://avinal.github.io/posts/hrt-interview-1 (also https://github.com/avinal/avinal.github.io/blob/main/src/content/posts/blogs/hrt-interview-1.md)
- Answer/Discussion: none found (author describes format/difficulty, not exact problems)

### 45-min non-coding telephonic interview: background, programming languages, Unix/Linux concepts, C++ pointers and memory, Python/Bash scripting, automation, tooling knowledge, resume-driven follow-ups, "why this role"
- Company: Hudson River Trading
- Role: Systems Intern (Summer 2021)
- Type: Interview
- Status: REAL
- Source: avinal.github.io (personal blog) — https://avinal.github.io/posts/hrt-interview-1
- Answer/Discussion: none found; author notes interviewer explained reasoning behind each question and stayed close to resume content

### Detect a cycle in an undirected graph
- Company: Hudson River Trading
- Role: unknown (SWE recruiting cycle, referencing Aug 2022 cycle / Glassdoor)
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar personal notes repo — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: Author notes standard approach is DFS until a back edge is found; also mentions Tortoise-and-Hare/Brent's algorithm as lower-memory alternatives

### Shortest path distance in a matrix (grid distances via BFS/flood fill)
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: Author suggests BFS flood-fill from source, taking min(neighbors)+1, possibly modifying input array in place to save memory

### Maximum value per level of a tree/graph
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: BFS level by level, comparing to a maxima array initialized to a very negative sentinel

### Swap every two nodes in a linked list
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: In-place pointer rearrangement with O(1) extra temp variable, rather than building a new list

### Implement a Binary Search Tree
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found beyond "canonical"

### Traverse a matrix in spiral order
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: Author discusses avoiding a per-step boundary compare by precomputing the decreasing run lengths (e.g. 4 up, 4 right, 4 down, 3 left, ... for a 5x5) and handling final 1xN/Nx1 edge cases carefully

### Levenshtein edit distance
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found beyond "canonical DP"

### Next greater element in a circular array
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: monotonic-stack approach

### Systems/OS trivia set: what is an Inode? Difference between RAID 5 and RAID 6? Alternative to `ls`? Why might `du` and `df` disagree? What does `mv *` do? How would you install Linux on 100 compute nodes easily? Difference between soft and hard links?
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar (labeled "GlassDoor... maybe low quality copy pasta from ~12 months back") — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found

### Take-home assessment (Verilog programming project) with a lengthy timeline (predicted 4-8 hrs, self-checking grader gave disputed/incorrect result with no easy way to contest)
- Company: Hudson River Trading
- Type: OA / take-home
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found

### Given a string of only 'A','B','C','D', repeatedly remove adjacent "AB"/"BA" and "CD"/"DC" pairs and return the result
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found (stack-based removal implied)

### Given a graph (array-represented) with nodes valued 'A' or 'B', find the longest path where no two adjacent nodes share the same value
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found

### You have 4GB physical memory but allocate an 8GB buffer — is this possible, and how? How is memory actually read as you traverse it?
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: virtual memory / overcommit / paging implied

### Thread vs process — what's the difference? Discuss common threading models. What are methods of inter-process communication (between threads, between processes)? Explain how a named pipe (FIFO) works.
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found

### What does the `inline` keyword do in C++? Pros and cons? How do virtual functions work (vtable lookup)? `map` vs `unordered_map` — how is each implemented under the hood?
- Company: Hudson River Trading
- Type: Interview
- Status: REAL
- Source: Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/blob/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds/Hudson%20River%20Trading.txt
- Answer/Discussion: none found

### OA on CodeSignal: 90 minutes, four easy competitive-programming questions
- Company: Hudson River Trading
- Role: C++ Software Engineer (full-time)
- Type: OA
- Status: REAL
- Source: Shivam5022/Interview-Experiences (personal GitHub README) — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### 45-min phone screen (systems-heavy): use of `inline` functions (pros/cons); `vector` vs `list` trade-offs and internals; internal working of `malloc`, demand paging; how the kernel allocates memory to user processes; system calls like `sbrk` and `mmap`
- Company: Hudson River Trading
- Role: C++ Software Engineer (full-time)
- Type: Interview
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (topics listed, not full answers)

### OA: two CP questions — one two-pointer (~CF 1600 level), one tricky implementation problem
- Company: Squarepoint Capital
- Role: C++ Software Engineer (full-time)
- Type: OA
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### Technical Screening R1: CS trivia (virtual memory, process management, page tables, real-time systems, TCP vs UDP, dangling pointers) then live-coding debug of a dummy `vector` implementation (missing destructor, needed custom copy constructor, memory leaks, out-of-range checks)
- Company: Squarepoint Capital
- Role: C++ Software Engineer (full-time)
- Type: Interview
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: Candidate lists fixes needed: add destructor, custom copy ctor, fix leaks, bounds checks

### Technical Screening R2: TCP internal state-machine handling; given a code snippet, how many times are copy/move/assignment constructors called; exercise involving `char**` pointers
- Company: Squarepoint Capital
- Role: C++ Software Engineer (full-time)
- Type: Interview
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### Technical Screening R3: given a thread-safe queue implementation and a benchmark, suggest optimizations (replace copies with moves, condition variable instead of busy-waiting, bounded queue, RAII locking, cache-friendliness of underlying container)
- Company: Squarepoint Capital
- Role: C++ Software Engineer (full-time)
- Type: Interview
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: Candidate's optimization list is given verbatim above

### OA: three C++ questions in 120 minutes — one "find the bug" in a given snippet, two LeetCode medium-to-hard
- Company: DRW
- Role: C++ Software Engineer (full-time)
- Type: OA
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### Write pseudocode to serialize a struct in binary format and write it to a file; follow-up on endianness and how to handle it
- Company: DRW
- Role: C++ Software Engineer (full-time)
- Type: Interview
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### Pen-and-paper test: two CP questions (~CF 1700 level) plus two systems questions — implement concurrent transactions between two bank accounts using locks; remove branching from a given code snippet
- Company: Graviton Research Capital
- Role: Software Engineer (full-time)
- Type: OA
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### OA: 15 CS-fundamentals MCQs in 20 minutes, followed by 3 non-CP C++ coding questions in 25 minutes
- Company: QuantBox
- Role: unknown (full-time SWE track)
- Type: OA
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found

### 3-4 hour deep systems interview covering: implement `shared_ptr`; implement a `String` class; implement a memory pool; internal workings of virtual functions/virtual dispatch; lock-free multi-threaded linked list and producer-consumer buffer; endianness detection; memory reordering (hardware/compiler level); lazy allocation and `malloc` internals; spinlock and contention optimization; Read-Copy-Update (RCU)
- Company: QuantBox
- Role: unknown (full-time SWE track)
- Type: Interview
- Status: REAL
- Source: Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (candidate notes "several open-ended follow-ups"); candidate's linked prep notes: https://github.com/Shivam5022/Knowledgebase-SV

### OCS Day interview at Citadel: "Round 1 focused on BFS" (formal, finished on time); "Round 2 focused on implementing Topological Sort"; "Round 3 about my projects and resume"
- Company: Citadel
- Role: Software Developer Intern (campus placement)
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 (personal account) — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Citadel_Pritesh_Mehta.md
- Answer/Discussion: none found

### QuantBox interview round: questions on DSA and System Design; Round 2 had "more difficult System Design questions" with 7 interviewers back-to-back
- Company: QuantBox
- Role: unknown (campus placement)
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Citadel_Pritesh_Mehta.md
- Answer/Discussion: none found

### Tower Research interview: topics included Competitive Programming, Probability, and Markets
- Company: Tower Research Capital
- Role: unknown (campus placement)
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Citadel_Pritesh_Mehta.md
- Answer/Discussion: none found

### Quadeye interview: asked about Probability, DSA, and System Design
- Company: Quadeye
- Role: unknown (campus placement)
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Citadel_Pritesh_Mehta.md
- Answer/Discussion: none found

### OA: time-pressured, ~1h20m total; 3 DSA problems of increasing difficulty (one confirmed DP, one likely brute-force+optimization; topics overall Greedy, Bitmasking, DP)
- Company: DE Shaw (D. E. Shaw India, Technology Developer)
- Role: Technology Developer Intern
- Type: OA
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/DEShaw_Saumitra_Garg.md
- Answer/Discussion: none found

### Round 1 (~30 min): discussion of a Cache Simulator project, then a graph problem (likely cycle detection), asked to implement in C++, followed by C++ concepts — inheritance and smart pointers
- Company: DE Shaw
- Role: Technology Developer Intern
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/DEShaw_Saumitra_Garg.md
- Answer/Discussion: none found

### Round 2 (~20 min): design a Banking System class in C++, interactive/iterative design modified based on live interviewer feedback — entirely centered on system design in C++
- Company: DE Shaw
- Role: Technology Developer Intern
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/DEShaw_Saumitra_Garg.md
- Answer/Discussion: none found

### OA: mathematics, probability puzzles, and moderate competitive-programming problems
- Company: Millennium Management
- Role: Quantitative Research Intern
- Type: OA
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Millennium_Shrenik_Sakala.md
- Answer/Discussion: none found

### Round 1: resume/project walkthrough, discussion of ML-based time-series models, probability puzzles and Brainstellar-style problems
- Company: Millennium Management
- Role: Quantitative Research Intern
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Millennium_Shrenik_Sakala.md
- Answer/Discussion: none found

### Round 2: DSA-focused coding problem, followed by discussion of favorite data structures and algorithmic trade-offs
- Company: Millennium Management
- Role: Quantitative Research Intern
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Millennium_Shrenik_Sakala.md
- Answer/Discussion: none found

### OA: two coding questions (easy-moderate, CP-style, not deep DSA) plus a general-probability/puzzle quant section
- Company: QRT (Qube Research & Technologies)
- Role: Quant Developer Intern, Mumbai
- Type: OA
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/QRT_Arnav_Jain.md
- Answer/Discussion: none found

### Onsite Round 1: general discussion about aspirations, past projects, work experience; Round 2: technical questions with on-the-spot problem solving and pseudocode writing
- Company: QRT
- Role: Quant Developer Intern, Mumbai
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/QRT_Arnav_Jain.md
- Answer/Discussion: none found

### Three technical rounds focused on probability problems and puzzles, followed by an informal conversation with a firm partner
- Company: Quadeye
- Role: Quant Intern, Gurgaon
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Quadeye_Maalav_Mehta.md
- Answer/Discussion: none found ("problems were standard and aligned with typical quant prep")

### Interview consisted only of quant puzzles (no systems questions); multiple interviewers each asked different problems, hints given, candidates encouraged to think aloud
- Company: Quantbox
- Role: Quantitative Trader Intern, Singapore
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Quantbox_Interview_Abhinav_Shripad.md
- Answer/Discussion: none found; author links a more detailed personal write-up: "Surviving the IITD Internship Marathon" — https://chlorinated-sand-491.notion.site/Surviving-the-IITD-Internship-Marathon-1cc8f10a3c60802cbf80e0e00e934ddc

### OA: graph algorithms, dynamic programming, search & sorting (many variations of CSES problem-set style questions)
- Company: AlphaGrep Securities
- Role: Quant Researcher Intern, Gurgaon
- Type: OA
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Vishakha_Alphagrep_Interview.md
- Answer/Discussion: none found

### 4 technical interview rounds (20 min-1 hr each): mental math under time pressure; given a problem statement, discuss the most appropriate data structure/algorithm and analyze time complexity; probability questions on distributions and their properties; project discussion (aim, methodology, results)
- Company: AlphaGrep Securities
- Role: Quant Researcher Intern, Gurgaon
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Vishakha_Alphagrep_Interview.md
- Answer/Discussion: none found

### Online test: "80 in 8" (80 arithmetic questions in 8 minutes, +1/-1 scoring), "Finish the Sequence" and "Zap-N" reaction games, 10 probability questions at 90 seconds each, and a personality test
- Company: Optiver
- Role: Quant Trading (and Research) Intern, Amsterdam
- Type: OA
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/optiver_tirth.md
- Answer/Discussion: none found

### Group discussion run by an Optiver employee: 5 mathematical guesstimate questions (give lower/upper bound, score = sum of upperbound/lowerbound, target score >2) plus a card-game strategy design exercise based on expected value and variance
- Company: Optiver
- Role: Quant Trading (and Research) Intern, Amsterdam
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/optiver_tirth.md
- Answer/Discussion: none found

### Final technical interview: probability-based card-game strategy questions, emphasis on framing/communicating thought process over the final answer
- Company: Optiver
- Role: Quant Trading (and Research) Intern, Amsterdam
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/optiver_tirth.md
- Answer/Discussion: none found

### Round 1: basic programming questions, then test-case generation questions (efficient ways to randomly generate a graph or tree satisfying constraints such as minimum height); asked for a C++ implementation of `shared_ptr` functionality including design decisions and what state needs tracking, plus basic C++ OOP questions
- Company: Graviton Research Capital
- Role: Software Engineering Intern, Gurgaon
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Graviton_Interview_Arunabh_Roy.md
- Answer/Discussion: none found

### Round 2: hardware/caches, paging, and in-depth discussion of CPU pipelining (specifically RISC-based) and pipeline stalls
- Company: Graviton Research Capital
- Role: Software Engineering Intern, Gurgaon
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Graviton_Interview_Arunabh_Roy.md
- Answer/Discussion: none found

### Round 3: branch prediction in CPUs (branch miss %, what branch-prediction strategies exist, predictor performance for certain programs), and writing a binary search implementation that does not use branch instructions when compiled
- Company: Graviton Research Capital
- Role: Software Engineering Intern, Gurgaon
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Graviton_Interview_Arunabh_Roy.md
- Answer/Discussion: none found

### Pen-and-paper written test for shortlisting: three questions — a probability question, an "Alice and Bob" puzzle, and a mathematical problem (moderate-to-difficult)
- Company: Graviton Research Capital
- Role: Quantitative Research Intern, Gurgaon
- Type: OA
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Graviton_Trader_Vagesh_Mahajan.md
- Answer/Discussion: none found

### Round 2: a chess-based puzzle with multiple iterations, followed by 15-20 min project discussion (how the project could be extended/alternate directions)
- Company: Graviton Research Capital
- Role: Quantitative Research Intern, Gurgaon
- Type: Interview
- Status: REAL
- Source: devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/blob/main/Interviews/Graviton_Trader_Vagesh_Mahajan.md
- Answer/Discussion: none found

### Jane Street SWE internship (London): 45-min online coding round (coding challenge only, no algorithm-heavy DSA — relies heavily on data structures/hash-maps/sets), followed by a 3-round onsite Superday (each ~45 min, two interviewers per round, coding-only, language-agnostic in a Google-Docs-style non-runnable editor). Problems are game-like/real-world scenarios (e.g. modified connect-four, modified trading bot) that start simple and keep layering requirements to test adaptability under pressure.
- Company: Jane Street
- Role: SWE Intern, London
- Type: Interview
- Status: REAL
- Source: How-to-faang-UTCN/How-to-faang-Guide (first-person account) — https://github.com/How-to-faang-UTCN/How-to-faang-Guide/blob/main/guides/Jane_Street_Guide.md
- Answer/Discussion: none found (process/style description, not a specific verbatim problem)

### Recruiter phone interview brainteasers: "Jim has twice as many sisters as brothers. Jane, Jim's sister, has the same number of brothers as sisters. How many siblings are there?" and "You have a right-angled triangle with perpendicular sides 10 and 15. What is the area of the largest square that fits in the triangle with sides parallel to the perpendicular sides?"
- Company: Tibra Global Services (Tibra Capital)
- Role: Quant Trader Developer
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews (community repo, personal account, applied May 2023) — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Tibra/Quant%20Trader%20Developer.md
- Answer/Discussion: Candidate got the siblings puzzle right; for the square-in-triangle problem the candidate mistakenly solved for a rectangle (got 37.5) instead of a square (correct answer 36)

### Third stage (~3.5 hr): 2-hour individual take-home data exploration task (given stock price + 8 unlabeled signal columns, find relationships to trade the asset) presented via Teams, followed by a 1.5-hour group exercise building a backtest/PnL strategy with another candidate
- Company: Tibra Global Services
- Role: Quant Trader Developer
- Type: OA / take-home
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Tibra/Quant%20Trader%20Developer.md
- Answer/Discussion: Candidate used correlation analysis; interviewer felt "predictive power" functions were more appropriate for non-linear (e.g. quadratic) relationships than raw correlation

### Elenchus entrance exam: proctored, mostly maths and English, 30 questions in 10 minutes, including "family relationship" logic riddles (e.g. "what's the relationship between someone's mother's grandmother's son's...")
- Company: Rokos Capital Management (via Dartmouth Partners recruiting agency)
- Role: 2024 Quant Graduate Programme
- Type: OA
- Status: REAL
- Source: Leader-board/OA-and-Interviews (personal account) — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: none found

### Codility entrance exam: unproctored, 90 minutes, three LeetCode-medium-level questions — one greedy, one binary search, one tree-based
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: OA
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: none found

### Proctored handwritten maths exam: 9 questions/90 minutes/40 marks total, themed around probability & statistics — two questions directly testing variance and correlation formulas, a couple of brainteaser-adjacent questions, a couple of combinatorics questions, and one requiring a graphing calculator
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: OA
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: none found

### Finals, Part 1 (Investment Quant): compute the derivative of x² + y² = 1
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: Candidate answered correctly (implicit differentiation)

### Finals, Part 1 (Investment Quant): "Given a circle with three legs on it, a table is placed over the three legs. What is the probability the table does not fall down?"
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: Relates to centre-of-gravity being inside the triangle formed by the three legs; candidate could not solve it even with hints (screenshot referenced in repo media folder)

### Finals, Part 1 (Investment Quant): "You have n coins with different weights. Two are drawn, compared, lighter discarded, heavier becomes 'Champ'. For the next m-1 rounds, one coin is drawn and compared with the current champion, keeping the heavier. What is the probability that in the m-th round the champion does not change (i.e. the (m+1)-th coin is lighter)?"
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: Key insight candidate missed: n is irrelevant to the answer

### Finals, Part 2 (Trading Strategy): "Given a string, find the number of consecutive-character regions" (e.g. "abbccca" → 4 regions: "a","bb","ccc","a")
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: none found

### Finals, Part 2 (Trading Strategy): mortgage question — "$100 mortgaged over 5 years, you pay $7/year; sketch a graph of the remaining balance over time"
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: none found

### Finals, Part 2 (Trading Strategy): market-making role play — "Microsoft stock is at $100, quote a bid and ask. Someone buys 5 stocks from you. The next day they return — quote another bid/ask. Quote once more."
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: Candidate quoted $99/$101, then narrowed to $99.5/$100.5 reasoning the buyer might find another counterparty; interviewer's expected reasoning: repeat demand should widen (not narrow) the spread, since demand signals you can charge more, not that you need to compete more aggressively

### Finals, Part 2 (Trading Strategy): the classic 25-horses problem — minimum races to determine the winner, then determine the top 3
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: none found in detail (interviewer was rushed through this part)

### Finals, Part 3 (Core Strategy, coding): implement `int addMonths(int yyyymmdd, int ma)` — add `ma` months to an ISO-format date `yyyymmdd`; if the resulting date is invalid for that month, return the latest valid date in that month
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: Full candidate pseudocode/Java-ish solution is transcribed in the source, including year/month/day extraction via integer division and leap-year/days-in-month handling; interviewer disallowed a substring-based date parse

### Finals, Part 3 (Core Strategy, coding): given a binary tree (`Node{l, r, val}`) representation, implement `void Dump(Node n)` to print it — first any traversal order, then forced to recursive DFS, then forced to iterative BFS, then forced to iterative DFS (hardest — requires an explicit stack)
- Company: Rokos Capital Management
- Role: 2024 Quant Graduate Programme
- Type: Interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Rokos%20Capital%20Management/2024%20Quant%20Graduate%20Programme.md
- Answer/Discussion: Full step-by-step candidate code for recursive DFS, (incorrect) BFS-as-DFS attempt, and the final iterative-DFS-with-stack solution are transcribed verbatim in the source

## Promising sources for follow-up

- Leader-board/OA-and-Interviews — https://github.com/Leader-board/OA-and-Interviews — Large multi-year (2020-21 through 2023-24) community-maintained repo of extremely detailed, first-person OA/interview reports with verbatim questions, at firms including Tibra, Rokos, SIG, Akuna Capital, Maven Securities, Virtu, TPP, Bloomberg, Microsoft, Oracle, Maverick Derivatives, Epoch Capital, Improbable, Mustard Systems. Only Tibra and Rokos were mined here; the rest of "Application experiences/2021-22" and "2022-23" folders are unmined and look equally rich.
- devclub-iitd/Intern-Prep-Series-25 — https://github.com/devclub-iitd/Intern-Prep-Series-25/tree/main/Interviews — IIT Delhi student-run repo of first-person internship interview accounts; mined 10 of ~23 files. Unmined files include Google, JPMC (QA), Wells Fargo, Salesforce, Eightfold AI (x2), Bain, L.E.K., ITC, GS (Goldman Sachs), Civil Core — lower priority for quant/HFT/C++ but quick to check.
- Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md — Single very detailed personal account covering Stripe, Hudson River Trading, Squarepoint Capital, DRW, Graviton, and QuantBox full-time C++/systems interviews; fully mined here, but the author's linked prep-notes repo (https://github.com/Shivam5022/Knowledgebase-SV) was not opened and may contain more sourced material.
- Lazar-Ilic/Lazar — https://github.com/Lazar-Ilic/Lazar/tree/main/Notes/Computer%20Science/Algorithms/Interviews%20Coding%20Rounds — A personal notes repo with per-company interview-question files (seen: "Hudson River Trading.txt" and a "Jane Street" mention); the same "Interviews Coding Rounds" directory likely has more per-company .txt files (e.g. Jane Street, other HFT firms) that were not enumerated/fetched.
- ankitkushawaha1000/HFT — https://github.com/ankitkushawaha1000/HFT — Extremely large, structured, round-by-round company interview-question repo covering ~30 companies (Jane Street, Citadel Securities, Optiver, IMC, DRW, Jump Trading, Hudson River Trading, Two Sigma, Point72, Millennium, SIG-Susquehanna, Tower Research, DE Shaw, Five Rings, Flow Traders, G-Research, Headlands, Maven Securities, Old Mission Capital, PDT Partners, Quadrature Capital, Radix Trading, Squarepoint, Virtu, Worldquant, Akuna Capital, plus big tech). CAUTION: every question is explicitly tagged `[anecdotal]` or `[inferred]` and the README states it is a self-built/possibly AI-assisted study aid, not verbatim sourced reports — treat as PRACTICE-tier and re-verify individual claims before treating as REAL, but the sheer coverage (many rounds x many firms) makes it worth a systematic second pass.
- Leader-board/OA-and-Interviews "Getting the feedback through GDPR.md" — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences — a "media" folder in this repo also contains screenshots (e.g. rokos1.pdf, rokos3.png, rokos4.png) referenced by the interview writeups with additional verbatim question text/hints not transcribed in the markdown — worth pulling directly.
- avinal.github.io / avinal/website — https://github.com/avinal/avinal.github.io (also mirrored at https://github.com/avinal/website) — personal blog with at least one HRT interview post mined; check the rest of the blog's `posts/blogs` directory for more interview write-ups.
- hieptran1812/my-website — https://github.com/hieptran1812/my-website/tree/main/content/blog/trading — personal blog with multiple posts specifically on quant interview process/strategy, "Optiver and IMC playbook: the mental math gauntlet", and "the interview loop round by round" — not yet fetched/read in full.
- sgoel97/blog — https://github.com/sgoel97/blog/blob/main/content/blog/quant-interview/index.md — personal blog post specifically titled about quant interview experience — not yet fetched.
- kishanBhandary/Projects-and-Interview-Question C++_INTERVIEW/experiences.md — https://github.com/kishanBhandary/Projects-and-Interview-Question/blob/main/C%2B%2B_INTERVIEW/experiences.md — explicitly labeled "anonymized reports collected from engineers" but contains a leftover ChatGPT citation artifact (`:contentReference[oaicite:0]{index=0}`), strongly suggesting the "real" company reports (Google, Microsoft, Amazon, Apple, Meta, Bloomberg, NVIDIA) are LLM-fabricated rather than genuine — deprioritize/verify before use.
