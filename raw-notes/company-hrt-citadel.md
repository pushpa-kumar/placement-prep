# HRT & Citadel Securities — Real/Practice Interview & OA Question Bank (compiled 2026-08-27)

## HUDSON RIVER TRADING (HRT)

### Two rooks are to be placed on a chess board such that they don't attack each other, and the sum of the values of the squares they're placed on is maximum
- Company: HRT
- Role: unknown (Software Engineer/Algo track)
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/889638/hudson-river-trading-oa-two-rooks
- Answer/Discussion: Board given as 2D array of non-negative ints; example board [[0,1,5],[3,0,5],[1,4,1]] → answer 9. OP solved by sorting the 2D array but couldn't find a more optimized solution; a commenter suggested finding the max in each row/column and checking combos that don't share a row/col.

### Place 2 "roosters" on an m×n matrix of positive numbers (they cannot share a row or column) to maximize the sum of ALL cells EXCLUDING the rows/columns the roosters occupy
- Company: HRT
- Role: Algo Software Engineer
- Type: OA
- Round/Stage: Online Assessment (Codility)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/general-discussion/498475/hudson-river-trading-oa and https://leetcode.com/discuss/general-discussion/549526/hudson-river-trading-online-assessment/
- Answer/Discussion: Example 3x3 matrix, roosters at (0,1) and (1,0) → answer 9. Brute force O(M²N²) by trying every pair; optimized O(NM²) via precomputed rowSumExc[i][j][k]; a linear O(MN) approach was referenced (global min cell likely in optimal solution).

### An "easy" stack question requiring you to implement the described data structure verbatim
- Company: HRT
- Role: Algo Software Engineer
- Type: OA
- Round/Stage: Online Assessment (Codility)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/general-discussion/549526/hudson-river-trading-online-assessment/
- Answer/Discussion: No solution posted; described only as straightforward direct implementation.

### An "easy" string fill-in-the-blank question
- Company: HRT
- Role: Algo Software Engineer
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/general-discussion/549526/hudson-river-trading-online-assessment/
- Answer/Discussion: none found, no details shared beyond difficulty label.

### Find the longest unique path in a binary tree
- Company: HRT
- Role: Algo Software Engineer
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/general-discussion/549526/hudson-river-trading-online-assessment/
- Answer/Discussion: One respondent noted a GeeksforGeeks reference algorithm they tried failed one test case; no working solution shared.

### Given a grid of houses (1) and empty cells (0), count empty cells within Manhattan distance K of ALL houses
- Company: HRT
- Role: unknown
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/1458197/Difficult-Hudson-River-Trading-question-OA
- Answer/Discussion: Suggested multi-source BFS (max distance from any house per cell); a later commenter proposed an O(N²×M) row-based range approach since naive per-cell checking TLEs.

### Determine if a given (multi-edge/undirected) graph configuration is achievable / has an Eulerian-type path (based on odd-degree vertex counts)
- Company: HRT
- Role: unknown
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/2492212/Hudson-River-Trading
- Answer/Discussion: Rule set discussed: 0 odd-degree vertices → possible; odd count of odd-degree vertices → impossible; 2 odd-degree → check missing direct edge or an even vertex unconnected to both; 4 odd-degree → check pairability; >4 → impossible. A working C++ adjacency-matrix solution was posted by a commenter.

### 2023 SWE Intern Test: Add two binary strings together
- Company: HRT
- Role: Software Engineer Intern
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/3078249/Hudson-River-Trading-2023-SWE-Intern-Test
- Answer/Discussion: Process right to left with carry tracking, append results in reverse.

### 2023 SWE Intern Test: Diamond-pattern encryption/decryption cipher on a matrix
- Company: HRT
- Role: Software Engineer Intern
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/3078249/Hudson-River-Trading-2023-SWE-Intern-Test
- Answer/Discussion: Decryption rule discussed: if input row index is even, distribute elements to odd-indexed rows {1,3,5}; if odd, distribute to even rows {0,2,4}.

### 2023 SWE Intern Test: Answer minimum-value queries on a matrix supporting row/column "removal" operations
- Company: HRT
- Role: Software Engineer Intern
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/3078249/Hudson-River-Trading-2023-SWE-Intern-Test
- Answer/Discussion: Use two heaps to track minimum active rows/columns, skip deactivated indices, return product of minimums or -1 if none exist.

### Intern 2024 OA: counting problem solvable with a running counter in O(n)
- Company: HRT
- Role: Software Engineer Intern
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/4452641/hudson-river-trading-intern-2024/
- Answer/Discussion: Commenter notes O(n) counter-based solution suffices; no code shown.

### Intern 2024 OA: word-search-in-matrix style problem (find given words occurring in a character grid)
- Company: HRT
- Role: Software Engineer Intern
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/4452641/hudson-river-trading-intern-2024/
- Answer/Discussion: Top-down DP/DFS with memoization solution posted, O(m×n×words.length×max word length).

### Intern 2024 OA: time-based query — convert arrival time strings to minutes and answer queries via binary search on sorted times
- Company: HRT
- Role: Software Engineer Intern
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/4452641/hudson-river-trading-intern-2024/
- Answer/Discussion: Binary search on sorted converted times.

### OA: a minor variant of "remove comments from C++ source code"
- Company: HRT
- Role: unknown (SWE)
- Type: OA
- Round/Stage: Online Assessment (2hr10min, 3 questions)
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-what-to-expect-wy1hgi2m (corroborated by InterviewDB.io "Comment-Free Code Length" — https://www.interviewdb.io/question/hrt)
- Answer/Discussion: Candidate wrote ~7 edge cases for this question; felt confident but was still rejected.

### OA: "permutation of palindrome" — determine if a string's characters can be rearranged into a palindrome
- Company: HRT
- Role: unknown (SWE)
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-what-to-expect-wy1hgi2m (corroborated by InterviewDB.io "Ways to Make Palindrome" — https://www.interviewdb.io/question/hrt)
- Answer/Discussion: No solution detail beyond edge-case testing mentioned.

### OA: given a chemical equation, determine whether it's balanced
- Company: HRT
- Role: unknown (SWE)
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-what-to-expect-wy1hgi2m (corroborated by InterviewDB.io "Chemical Reaction" — https://www.interviewdb.io/question/hrt)
- Answer/Discussion: Candidate wrote 10+ edge cases for this question specifically, calling it the hardest of the three.

### OA (Algo Web Engineer): a "trivial" question — pure implementation of the spec, no algorithmic insight needed
- Company: HRT
- Role: Algo (Web) Engineer
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-svkrykwf
- Answer/Discussion: Respondent spent ~5 minutes on it.

### OA (Algo Web Engineer): a recursive divide-and-conquer problem (available in similar form on LeetCode forums)
- Company: HRT
- Role: Algo (Web) Engineer
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-svkrykwf
- Answer/Discussion: Respondent spent ~10 minutes.

### OA (Algo Web Engineer): "a very annoying string parsing question" that tests whether you can think of all edge cases
- Company: HRT
- Role: Algo (Web) Engineer
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-svkrykwf
- Answer/Discussion: Respondent spent ~60 minutes on this one alone.

### First round covered OS internals and algorithms (general topics, no specific prompt given)
- Company: HRT
- Role: Algo (Web) Engineer
- Type: Interview
- Round/Stage: Phone screen round 1
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-svkrykwf
- Answer/Discussion: OP had expected math-heavy questions but respondent said "there was no math."

### Implement a game with many edge cases (live coding)
- Company: HRT
- Role: Algo (Web) Engineer
- Type: Interview
- Round/Stage: Phone screen round 2
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/hudson-river-trading-oa-svkrykwf
- Answer/Discussion: none found beyond "a lot of edge cases."

### Design problem: build a piece of a trading system, writing OO code that must be as performance-efficient as possible
- Company: HRT
- Role: unknown (SWE/Algo Dev)
- Type: Interview
- Round/Stage: Onsite/technical round
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/general-discussion/628687/hudson-river-trading-interview
- Answer/Discussion: Candidate says they "solved the problem, but none of their TC could pass — time-limit-exceeded," noting HRT "nails down on your OO C++ performance skills."

### How would you design a system to route network packets between one hub and multiple node servers?
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite (system design)
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/How-would-you-design-a-system-to-route-network-packets-between-one-hub-and-multiple-node-servers-QTN_8479239.htm (corroborated first-hand on Taro — https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineer-united-states-april-1-2025-no-offer-negative-2a2ca5aa/)
- Answer/Discussion: Candidate reported interviewers were rigid about matching an answer key even when correct answers (incl. modern C++20 approaches) were given; candidate did not receive an offer and rated the round negatively.

### 2-hour coding session with 4 questions progressing from a warm-up parsing problem to full algorithm/data-structure challenges
- Company: HRT
- Role: C++ Engineer
- Type: OA/Interview
- Round/Stage: Computer-based coding round
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/87MxP0h4 ("hudson river trading interview process")
- Answer/Discussion: Emphasis on real-world efficiency over pure theoretical complexity.

### Technical round: optimize/improve a backtracking problem
- Company: HRT
- Role: C++ Engineer
- Type: Interview
- Round/Stage: Onsite technical round
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/87MxP0h4
- Answer/Discussion: none found; listed alongside math-focused and memory-management questions.

### System design round: take a written spec, produce a design, then incorporate new/changed facts into that design on the fly
- Company: HRT
- Role: C++ Engineer
- Type: Interview
- Round/Stage: Onsite system design round
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/87MxP0h4
- Answer/Discussion: Candidate: "a large coding task where you take a spec and implement it, questions on OS/'how computers work,' and system design questions are the main things usually covered." Candidate ultimately got an offer (~$600k TC after negotiation) but declined.

### We draw a person at random from the street, then keep drawing people until we find someone taller than the first person. What is the expected number of draws we have to wait?
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: unknown (likely phone screen, probability)
- Status: REAL
- Source: Glassdoor (aggregate) — https://www.glassdoor.com/Interview/Hudson-River-Trading-Interview-Questions-E470937.htm
- Answer/Discussion: none found in excerpt (classic "records" expectation problem — the expectation diverges/is infinite, since P(record at step n) ~ 1/n).

### How would you design a system to route network packets between a central hub and multiple node servers? (duplicate framing of above, listed separately by aggregator)
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### Given that a survey asks each student to report the size of their room and there is no other information available, how would you estimate the average room size?
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### Compare a sorted map and a hashmap, including time complexities; explain how a hashmap works and how to resolve hash collisions
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### Given two dates, calculate the number of days between them
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### How does a dictionary work under the hood in Python?
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### What is the difference between a vector and a linked list?
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### Implement stoi (string to integer) in C
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found.

### There's a race track with 5 lanes and 25 bunnies, no timer, and you only learn relative finishing order per race — how many races are needed to find the top 3 fastest?
- Company: HRT
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Quantt — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: none found (classic "25 horses, 5 tracks" puzzle; canonical answer is 7 races).

### Design a data structure backed by a deque that supports push front, push back, pop front, pop back, and O(1) access by logical index
- Company: HRT
- Role: unknown (Software Engineer)
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (title/prompt only; difficulty listed as Hard).

### Given an array of unique numbers, return any element that is smaller than both its neighbors (local minimum in 1D and 2D)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Hard).

### Design a wrapper API read(n) that returns any requested number of bytes, backed by a fixed-chunk stream reader
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Hard).

### Explain large memory allocation, swap behavior, and C++ inline trade-offs
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Hard).

### Count matrix cells whose row and column neighbors match
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### Design Insert/Delete/GetRandom supporting weighted sampling
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### Minimize array amplitude (max-min) after removing one contiguous block
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### Find the longest common digit prefix across two arrays
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### Explain C++ inline, segfaults, virtual memory, and std::string internals
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Hard).

### Split a message into length-limited parts, where each part must end with a suffix like <X/Y> (X = 1-based part number, Y = total parts)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### Define flipdigits(x) as the integer produced by reversing the decimal digits of a non-negative integer x — count digit-reversal equivalent pairs
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### A lab has one molecular reactor; each accepted sample takes exactly 5 minutes to process — calculate completion time (single-server queue simulation)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### Return true if there is at least one root-to-leaf path in a binary tree whose values sum to a target
- Company: HRT
- Role: Software Engineer/Intern
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Easy).

### Choose mean or median for a trading profit metric (statistics reasoning)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (difficulty Medium).

### A bird is building a nest in a forest represented by an array — simulate alternating stick collection
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### A one-dimensional road starts at 0 and ends at a given length — simulate players/"watchers" moving along it and convert results to an integer
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### Evaluate proficiency in low-level C++ buffer parsing, memory and pointer management by implementing buffer parsers and a generic map class
- Company: HRT
- Role: Data Scientist
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### Develop an automatic moderation system: count length-3 chat substrings containing a vowel
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### Implement an order-modification feature for a C++ trading system with a client/server architecture
- Company: HRT
- Role: Software Engineer/New Grad
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Hard).

### 1-dimensional line segment with a right boundary at position L — count people/entities reaching the boundary
- Company: HRT
- Role: Machine Learning Engineer
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Easy).

### Implement a program to solve a Wordle-style word-guessing game (hidden target word of fixed length L drawn from a known dictionary)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen (also reported as fulltime quant-finance video interview)
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms (corroborated first-hand on 1point3acres — https://www.1point3acres.com/interview/thread/1145403)
- Answer/Discussion: none found beyond problem description.

### Define an inversion as a pair of indices (i, j) — count inversions in a permutation
- Company: HRT
- Role: Data Scientist
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### Return the k smallest values in ascending order from a list
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### Given a list of integers and a target, return whether two elements at distinct indices sum to the target (Two Sum)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading/categories/coding-and-algorithms
- Answer/Discussion: none found (difficulty Medium).

### Explain what a segmentation fault represents in a native program and how it relates to virtual-memory protection
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Compare C++ pointers and references: initialization, nullability, reseating, syntax, arithmetic, ownership
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Compare stack and heap memory and describe how you'd probe/determine stack growth direction
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Discuss Python language and runtime fundamentals — should the answer describe CPython specifically or Python semantics generally?
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Compare C++ new, malloc, and placement new — what happens when a new expression is evaluated?
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Explain what the C++ inline keyword means vs. actual compiler inlining/substitution
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Linux host and filesystem fundamentals (general systems knowledge)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Explain Python and React performance fundamentals
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Hard).

### Probability reasoning for modular distributions of sums of independent dice (dice probability/matrix question)
- Company: HRT
- Role: Data Scientist
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Medium).

### Build a baseline machine-learning model predicting heart disease from a dataset
- Company: HRT
- Role: Software Engineer/New Grad
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Hard).

### Why do you want to pursue full-stack engineering? (behavioral/motivation)
- Company: HRT
- Role: unknown
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading?page=2
- Answer/Discussion: none found (difficulty Hard).

### Troubleshoot a host that rejects SSH connections — build a layered plan using ping, traceroute, etc.
- Company: HRT
- Role: Site Reliability Engineer
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found.

### Explain why du and df report different disk usage numbers
- Company: HRT
- Role: Site Reliability Engineer
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found.

### Compare Python generators, decorators, and context managers
- Company: HRT
- Role: Site Reliability Engineer
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found.

### Reason about Unix signals, zombie processes, and process reaping
- Company: HRT
- Role: Site Reliability Engineer
- Type: Interview
- Round/Stage: Technical screen
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found.

### Two threads each increment a shared counter 1,000,000 times; the final count is less than 2,000,000 — why, and how would you fix it?
- Company: HRT
- Role: Software Engineer (Core Engineering)
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: Dataford.io — https://dataford.io/interview-guides/hudson-river-trading/software-engineer
- Answer/Discussion: Non-atomic read-modify-write race; fix with std::atomic<int> or a mutex. Site explicitly does not claim this came from a real candidate report — presented as "representative" of HRT's style.

### Implement a class supporting add(x) and median(), both faster than O(n) per call (running median / stream median)
- Company: HRT
- Role: Software Engineer (Core Engineering)
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: Dataford.io — https://dataford.io/interview-guides/hudson-river-trading/software-engineer
- Answer/Discussion: Two-heap solution, O(log n) add/rebalance, O(1) median lookup.

### Design a real-time risk system consuming order flow, computing P&L/risk exposures, and alerting on limit breaches within a 1ms latency budget
- Company: HRT
- Role: Software Engineer/Algo Engineer
- Type: Unknown (System Design)
- Round/Stage: unknown
- Status: PRACTICE
- Source: Dataford.io — https://dataford.io/interview-guides/hudson-river-trading/software-engineer
- Answer/Discussion: none found.

### Tell me about a time you strongly disagreed with a team member's technical approach
- Company: HRT
- Role: all roles
- Type: Unknown (Behavioral)
- Round/Stage: Final round
- Status: PRACTICE
- Source: Dataford.io — https://dataford.io/interview-guides/hudson-river-trading/software-engineer
- Answer/Discussion: none found.

### Two independent random variables X and Y, both uniform on [0,1] — what is P(X+Y<1)?
- Company: HRT
- Role: Quantitative Researcher
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: Dataford.io — https://dataford.io/interview-guides/hudson-river-trading/software-engineer
- Answer/Discussion: Answer 0.5 via geometric area argument on unit square.

### A coin lands heads with probability p — what is the expected number of flips to see two consecutive heads?
- Company: HRT
- Role: Quantitative Researcher
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: Dataford.io — https://dataford.io/interview-guides/hudson-river-trading/software-engineer
- Answer/Discussion: E = (1+p)/p²; for p=0.5, E=6.

### Romeo and Juliet each arrive at a uniformly random time in [0,1] hour; the first to arrive waits 15 minutes then leaves. What's the probability they meet?
- Company: HRT
- Role: unknown
- Type: Unknown
- Round/Stage: Technical phone screen (math/probability)
- Status: PRACTICE
- Source: Tradermath.org — https://www.tradermath.org/articles/hudson-river-trading-interview-guide (explicitly labeled "a representative HRT problem," not a confirmed real report)
- Answer/Discussion: P = 1 − (3/4)² = 7/16.

### "Maze with Portals" and "Longest Path With Different Adjacent Characters" (representative coding-round problems)
- Company: HRT
- Role: unknown
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: TechPrep.app — https://www.techprep.app/blog/hudson-river-trading-interview-process
- Answer/Discussion: none found.

### Generic algorithm practice set associated with HRT's profile: Next Greater Element in a Circular Array; Levenshtein Edit Distance; Traverse a Matrix in Spiral Order; Implement a Binary Search Tree; Course Prerequisites (cycle/topological sort); Swap Every Two Nodes in a Linked List; Max Value Per Level in a Binary Tree; Shortest Path (Manhattan) in a Matrix; Detect a Cycle in an Undirected Graph
- Company: HRT
- Role: unknown
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: AlgoDaily — https://algodaily.com/companies/hudson-river-trading
- Answer/Discussion: no candidate attribution, listed as company-associated practice set.

### Brainteaser titles referenced for phone-screen prep: "Weighing Coins I," "Trading Places," "Christmas Cards," "Rolling 1s and 2s" (full text not published)
- Company: HRT
- Role: unknown
- Type: Unknown
- Round/Stage: unknown
- Status: PRACTICE
- Source: Tradermath.org — https://www.tradermath.org/articles/hudson-river-trading-interview-guide
- Answer/Discussion: none found.

## CITADEL SECURITIES

### Write a "producer" class that batches messages and sends them to a network endpoint once either a max message count or a max hold-time is reached (no immediate send-per-message; needs internal caching/flush logic)
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite coding round, NYC office
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/4138096/Citadel-Software-Engineer-All-Rounds/
- Answer/Discussion: No worked solution captured; described as a coding-round implementation problem (buffer/flush design) at LeetCode-medium-ish difficulty.

### Given a list of currency pairs and exchange rates (e.g., BTC-USD), find the best exchange rate from currency1 to currency2
- Company: Citadel Securities
- Role: Senior Software Engineer
- Type: Interview
- Round/Stage: Coding round (one of two rounds)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-experience/5565531/Citadel-or-Senior-Software-Engineer-or-Reject/
- Answer/Discussion: Candidate solved it as a graph best-path problem within time but missed edge cases (e.g., self-loops), which the interviewer flagged; candidate was ultimately rejected.

### Best time to buy and sell a stock — find the trade pair that gives maximum profit
- Company: Citadel Securities
- Role: Senior Software Engineer
- Type: Interview
- Round/Stage: Screening round
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/1792523/citadel-screening-round-senior-software-engineer
- Answer/Discussion: No answer captured in snippet; standard classic-DP/greedy problem.

### 3n people, person i passes a test with probability p_i; split them into n groups of 3, each group scores 1 point if at least 2 members pass — how do you assign people to groups to maximize expected total score?
- Company: Citadel Securities
- Role: Quantitative Researcher
- Type: Interview
- Round/Stage: Phone interview
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/427705/citadel-phone-interview-quant-researcher (also mirrored at https://leetcode.com/discuss/interview-question/660968/citadel-quant-researcher-phone-interview/)
- Answer/Discussion: No worked solution retrieved; framed as an expected-value optimization/greedy-pairing puzzle.

### IPO share allocation: given bidders as [bidder_id, shares_bid, price, timestamp], allocate shares (higher price gets priority; ties broken by earlier timestamp) and return bidder IDs who received zero shares
- Company: Citadel / Citadel Securities
- Role: Software Engineer (Campus / New Grad)
- Type: OA
- Round/Stage: Campus Software Engineering Challenge, 2020–2021 cycle
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/750495/citadel-and-citadel-securities-campus-software-engineering-challenge-2020-2021/
- Answer/Discussion: No solution captured in snippet; simulation/greedy allocation + sorting problem.

### Design an order book supporting real-time order insertion with two APIs: get_exchange_bbo(exchange_id) returning best bid/offer for one exchange, and get_nbbo() returning the National Best Bid and Offer across all exchanges (input: exchange_id, price, quantity, order_type bid/ask)
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: Coding round, alongside a separate in-depth behavioral round
- Status: REAL
- Source: DEV Community — https://dev.to/net_programhelp_e160eef28/citadel-swe-interview-experience-order-book-design-in-depth-behavioral-interview-3hb0 (appears to reflect the same "order book string problem" reported independently on Glassdoor)
- Answer/Discussion: Article notes the intended solution should weigh heaps vs. TreeMap for the bid/ask structures and reason about real-world trading-system tradeoffs; interviewers reportedly probe "three layers deep" on design choices.

### HackerRank OA: print the Roman numeral equivalent for numbers 1–1000
- Company: Citadel Securities
- Role: unknown (SWE track)
- Type: OA
- Round/Stage: HackerRank test
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Hackerrank-test-1-Print-Roman-number-equivalent-for-numbers-1-1000-2-Order-a-list-of-words-appearing-in-a-file-by-numb-QTN_2294098.htm
- Answer/Discussion: none found.

### HackerRank OA: order a list of words appearing in a file by number of letters, but preserve original order among words of the same length ("stable sort" requirement)
- Company: Citadel Securities
- Role: unknown (SWE track)
- Type: OA
- Round/Stage: HackerRank test
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Hackerrank-test-1-Print-Roman-number-equivalent-for-numbers-1-1000-2-Order-a-list-of-words-appearing-in-a-file-by-numb-QTN_2294098.htm
- Answer/Discussion: none found.

### HackerRank OA: implement a Stack class supporting several specific operations (exact operation list not captured)
- Company: Citadel Securities
- Role: unknown (SWE track)
- Type: OA
- Round/Stage: HackerRank test
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Hackerrank-test-1-Print-Roman-number-equivalent-for-numbers-1-1000-2-Order-a-list-of-words-appearing-in-a-file-by-numb-QTN_2294098.htm
- Answer/Discussion: none found.

### Phone/CoderPad round: given a series of prices, find the single buy/sell trade pair that gives maximum profit
- Company: Citadel Securities
- Role: unknown (SWE track)
- Type: Interview
- Round/Stage: Phone/CoderPad interview (same candidate as the HackerRank entries above)
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Hackerrank-test-1-Print-Roman-number-equivalent-for-numbers-1-1000-2-Order-a-list-of-words-appearing-in-a-file-by-numb-QTN_2294098.htm
- Answer/Discussion: none found.

### Follow-up to the above: modify the max-profit problem under a variation (multiple transactions / different constraint — exact modification text truncated in source)
- Company: Citadel Securities
- Role: unknown (SWE track)
- Type: Interview
- Round/Stage: Phone/CoderPad interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Hackerrank-test-1-Print-Roman-number-equivalent-for-numbers-1-1000-2-Order-a-list-of-words-appearing-in-a-file-by-numb-QTN_2294098.htm
- Answer/Discussion: none found (Glassdoor question text was truncated even in the search snippet).

### Software Engineer OA: two questions — one LeetCode-medium, one LeetCode-easy
- Company: Citadel Securities
- Role: Software Engineer
- Type: OA
- Round/Stage: Online Assessment
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Citadel-Securities-Software-Engineer-Interview-Questions-EI_IE1443495.0,18_KO19,36.htm
- Answer/Discussion: Reviewer called the OA "quite easy" relative to the onsite; no exact problem text captured.

### First round: standard DSA question built around an "order book" string-parsing problem
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite Round 1
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Citadel-Securities-Software-Engineer-Interview-Questions-EI_IE1443495.0,18_KO19,36.htm
- Answer/Discussion: none found beyond category description.

### Second round: heavy C++ debugging — candidate given obfuscated C++ code full of loops/complex logic and asked to comprehend and optimize it within ~2 hours
- Company: Citadel Securities
- Role: Software Engineer / C++ Software Engineer
- Type: Interview
- Round/Stage: Onsite Round 2 (C++ debugging round)
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Citadel-Securities-Software-Engineer-Interview-Questions-EI_IE1443495.0,18_KO19,36.htm (corroborated independently on Blind — https://www.teamblind.com/post/citadel-securities-swe-interview-adtkpi5w)
- Answer/Discussion: Candidate on Blind reported it was much harder than expected ("Got f***ed! Some dude on leetcode said it'd be easy... nothing like that happened") and questioned its real-world relevance; no solution given.

### Phone screen: multiple questions on how specific std:: C++ library structures/functions are implemented under the hood, plus low-level networking questions
- Company: Citadel Securities (explicitly NOT the hedge-fund side, per poster)
- Role: unknown (SWE)
- Type: Interview
- Round/Stage: Phone screen
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/citadel-hf-interview-questions-fhilphyk
- Answer/Discussion: Poster: "the guy asked me multiple questions on how some of the std C++ lib structures and functions are implemented underneath. Also got asked specific low level networking questions none of which I was prepared for." Thread also notes Citadel's system-design rounds are described as "non-standard," not the typical "Grokking the System Design" style.

### Interview combines C++ conceptual/trivia knowledge + LeetCode-style problems + system design in the same loop (not purely algorithmic like most companies)
- Company: Citadel Securities
- Role: unknown (SWE)
- Type: Interview
- Round/Stage: General loop description (two CoderPad rounds)
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/citadel-securities-interview-tips-Wzn5GACj
- Answer/Discussion: A responder (self-identified as from Block) confirmed: "it was a combination of all of them. This is one of the few companies that will ask you about your conceptual knowledge in addition to the usual stuff." Another suggested Bloomberg's interview question bank overlaps substantially with Citadel Securities'.

### Interviewer style varies by seniority: younger interviewers ask LeetCode medium/hard; older/more senior interviewers ask multithreading and systems-programming questions
- Company: Citadel Securities
- Role: Software Engineering (6 YOE candidate)
- Type: Interview
- Round/Stage: Onsite (general observation, phone screen preceded it)
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/Citadel-Securities-Interview-RLL5gFcL
- Answer/Discussion: Commenters: "Depends on who the interviewers are. Younger folks love to ask LC medium/hard, while older ones love to ask multithreading/system programming type of questions." Another guessed "LC hard questions right?"

### Round 1: a brain-teaser question (content not disclosed); Round 2: 1-hour CoderPad session with the hiring manager
- Company: Citadel Securities
- Role: unknown, explicitly "not Quant Trading"
- Type: Interview
- Round/Stage: Round 1 (brain teaser) → Round 2 (CoderPad w/ hiring manager)
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/Citadel-securities-interview-MvzsEgz0
- Answer/Discussion: Candidate passed the brain teaser; no content of either question captured. Thread notes confusion from a third-party recruiter about whether "domain knowledge questions" would appear.

### Market-making prompt: "Make me a market on the sum of three dice rolls"
- Company: Citadel Securities
- Role: Trading Intern
- Type: Interview
- Round/Stage: unknown
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Citadel-Securities-Trading-Intern-Interview-Questions-EI_IE1443495.0,18_KO19,33.htm
- Answer/Discussion: none found; flagged as trading-role rather than core SWE, included for completeness since it's a widely-cited Citadel Securities-style prompt.

### Quantitative Researcher round: statistics question about evaluating a trading strategy, plus probability questions and a small programming assignment
- Company: Citadel Securities
- Role: Quantitative Researcher
- Type: Interview
- Round/Stage: Video/telephonic rounds
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Citadel-Securities-Quantitative-Researcher-Interview-Questions-EI_IE1443495.0,18_KO19,42.htm
- Answer/Discussion: none found beyond category summary (long telephonic/video interviews, math, probability, small programming assignment).

### Implement a single-producer, multi-consumer ring buffer
- Company: Citadel Securities
- Role: Software Engineer
- Type: Unknown (Interview/OA)
- Round/Stage: unknown
- Status: REAL (aggregator states these are compiled from candidate reports; titles appear paraphrased rather than verbatim — treat wording with caution)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (medium difficulty, 159 solves listed).

### Perform an external merge sort using a heap
- Company: Citadel Securities
- Role: Software Engineer
- Type: Unknown (Interview/OA)
- Round/Stage: unknown
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (medium difficulty, 48 solves).

### Design a low-latency trading system
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: System design round
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (hard difficulty, listed as most-attempted system design question, 1,201 solves).

### Design a stock price time-series store and query system
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: System design round
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (easy difficulty, 331 solves).

### Implement a task queue supporting insert, delete, and execute operations
- Company: Citadel Securities
- Role: Software Engineer
- Type: Unknown (Interview/OA)
- Round/Stage: unknown
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (medium, 247 solves).

### Simulate the game 2048 and pack the board state into a uint64
- Company: Citadel Securities
- Role: Software Engineer
- Type: Unknown (Interview/OA)
- Round/Stage: unknown
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (medium, 311 solves — most-attempted coding question listed).

### Design a thread-safe shared counter
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: unknown
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (medium, 391 solves).

### Find the top-K largest elements in every sliding window
- Company: Citadel Securities
- Role: Software Engineer
- Type: Unknown (Interview/OA)
- Round/Stage: unknown
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (medium, 35 solves).

### Compute statistics from a frequency array
- Company: Citadel Securities
- Role: Software Engineer
- Type: Unknown (Interview/OA)
- Round/Stage: unknown
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found (hard, 148 solves).

### Behavioral: "Discuss a project you are proud of"
- Company: Citadel Securities
- Role: Software Engineer
- Type: Interview
- Round/Stage: Behavioral/leadership round
- Status: REAL (see paraphrasing caveat above)
- Source: PracHub — https://prachub.com/companies/citadel/positions/software-engineer
- Answer/Discussion: none found.

### C++: explain memory layout differences between std::vector and std::deque, and when cache locality becomes a problem in high-frequency loops
- Company: Citadel Securities
- Role: Software Engineer (low-latency)
- Type: Unknown
- Round/Stage: "Coding screen" (per prep guide's simulated loop)
- Status: PRACTICE
- Source: JobMentis — https://www.jobmentis.com/en/interviews/citadelsecurities/swe
- Answer/Discussion: none found; presented as a representative question type in an AI-style prep breakdown, not attributed to a named candidate.

### Discuss lock-free queues vs. mutex-protected queues in a multi-threaded order-matching engine, focusing on memory-ordering guarantees
- Company: Citadel Securities
- Role: Software Engineer (low-latency)
- Type: Unknown
- Round/Stage: "Coding screen"
- Status: PRACTICE
- Source: JobMentis — https://www.jobmentis.com/en/interviews/citadelsecurities/swe
- Answer/Discussion: none found.

### Design a market-data feed handler that processes UDP multicast packets with normalization, handling packet loss and out-of-order delivery without introducing jitter
- Company: Citadel Securities
- Role: Software Engineer (low-latency)
- Type: Unknown
- Round/Stage: "System design round"
- Status: PRACTICE
- Source: JobMentis — https://www.jobmentis.com/en/interviews/citadelsecurities/swe
- Answer/Discussion: none found.

### Explain how the OS scheduler affects latency on pinned threads in a high-frequency application, and how CPU isolation mitigates it
- Company: Citadel Securities
- Role: Software Engineer (low-latency)
- Type: Unknown
- Round/Stage: "System design round"
- Status: PRACTICE
- Source: JobMentis — https://www.jobmentis.com/en/interviews/citadelsecurities/swe
- Answer/Discussion: none found.

### Given production symptoms of intermittent latency spikes during high market volatility, instrument the code to isolate the cause (GC, lock contention, page faults)
- Company: Citadel Securities
- Role: Software Engineer (low-latency)
- Type: Unknown
- Round/Stage: "Onsite coding round"
- Status: PRACTICE
- Source: JobMentis — https://www.jobmentis.com/en/interviews/citadelsecurities/swe
- Answer/Discussion: none found.

### Analyze the issues with using a volatile variable for thread coordination vs. std::atomic with memory_order_seq_cst
- Company: Citadel Securities
- Role: Software Engineer (low-latency)
- Type: Unknown
- Round/Stage: "Onsite coding round"
- Status: PRACTICE
- Source: JobMentis — https://www.jobmentis.com/en/interviews/citadelsecurities/swe
- Answer/Discussion: none found.

### Coin-flip puzzle: expected number of flips to get two heads in a row
- Company: Citadel (quant-dev/quant-research prep)
- Role: Quantitative Developer / Researcher
- Type: Unknown
- Round/Stage: Probability round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: Explicitly presented as an illustrative prep example, not attributed to a real candidate report.

### "You have two children; given at least one is a boy born on a Tuesday, what's the probability both are boys?" (Boy/Girl-Tuesday paradox)
- Company: Citadel
- Role: Quantitative Developer / Researcher
- Type: Unknown
- Round/Stage: Probability round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: Generic prep example, no candidate attribution.

### Fermi estimation: "How many piano tuners are in London?"
- Company: Citadel
- Role: Quantitative Developer / Researcher
- Type: Unknown
- Round/Stage: Brain teaser / estimation round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: none found; generic estimation-style prompt.

### Pricing a die-rolling game where the player can choose to re-roll once
- Company: Citadel
- Role: Quantitative Developer / Researcher
- Type: Unknown
- Round/Stage: Probability/brain-teaser round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: none found.

### Design a data structure to answer "maximum stock price seen so far" queries in real time
- Company: Citadel
- Role: Software Engineer / Quant Developer
- Type: Unknown
- Round/Stage: Coding round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: none found.

### Put-call parity: relationship between an at-the-money call and put price
- Company: Citadel
- Role: Quantitative Developer / Researcher
- Type: Unknown
- Round/Stage: Finance round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: none found.

### "Why Citadel over Two Sigma, Jane Street, or DE Shaw?"
- Company: Citadel
- Role: Quantitative Developer / Researcher
- Type: Unknown
- Round/Stage: Behavioral round
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/citadel-interview
- Answer/Discussion: none found.

### Phone screens reportedly favor small, sharp coding prompts in the style of: merge-K (merge K sorted lists/arrays), ring-buffer implementation, and "stock DP ladder" (staged dynamic-programming stock problems)
- Company: Citadel Securities
- Role: Software Engineer / Quant Developer
- Type: Interview
- Round/Stage: Phone screen (aggregated pattern, not one verbatim question)
- Status: PRACTICE (paraphrased pattern description rather than a single verbatim reported question)
- Source: 1point3acres — https://www.1point3acres.com/interview/company/Citadel%20Securities
- Answer/Discussion: Same source describes a "single-fail" onsite policy: a weak round reportedly results in the next round being cancelled within a day.
