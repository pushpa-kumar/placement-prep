# OS/Linux Internals, Networking, CPU Architecture & Low-Latency Performance — Interview Question Bank

### Design a cache with low-latency reads (hashmap-based); follow-up: make it a time-based cache
- Company: unknown/general (phone screen, tech company, poster comparing notes on an HFT-adjacent thread)
- Role: unknown (SWE)
- Type: Interview
- Status: REAL
- Source: TeamBlind — https://www.teamblind.com/post/reddit-phone-interview-rejectionneed-some-helpful-advice-q8gvhmtf
- Answer/Discussion: Candidate implemented cache using a hashmap for low-latency reads, passed given test cases, then got a follow-up to extend it into a time-based cache (entries expire after a TTL). Also discussed eviction policies and what to consider for a distributed cache.

### "TCP inspection in Cisco routers" (networking depth question)
- Company: Jane Street
- Role: Network Engineer
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Jane-Street-Network-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,28.htm
- Answer/Discussion: none found (question text as indexed/summarized; full transcript requires a Glassdoor account to view — page was inaccessible for direct verbatim confirmation, blocked by Cloudflare during this research pass).

### Explain the TCP/IP model and the differences between the OSI and TCP/IP models
- Company: Jane Street
- Role: Analyst
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Jane-Street-Analyst-Interview-Questions-EI_IE255549.0,11_KO12,19.htm
- Answer/Discussion: none found (page blocked by Cloudflare for direct verbatim re-check; content as indexed/summarized).

### Round covering C++, IPC, operating systems, system design, multithreading, computer architecture, and cache efficiency (no single literal question captured)
- Company: unknown/general HFT firm
- Role: unknown (SWE/quant dev)
- Type: Interview
- Status: REAL
- Source: TeamBlind — https://www.teamblind.com/post/man-hedge-fund-and-hft-interviews-are-brutal-gotta-know-basically-everything-bbgpkbvx
- Answer/Discussion: Poster describes topic breadth rather than exact wording: "c++, leetcode, inter process communication, operating systems, system design, to multi threading, computer architecture, cache efficiency." Also notes every HFT interview loop they've taken has been different (some LeetCode, some system design of a trading system from scratch, some optimizing a piece of C++17/20 code).

### "I was asked a bunch of low level programming as well because my resume has [OS], compiler and kernel knowledge" (vague, no exact question text)
- Company: unknown/general (commenter reacting on an HFT interview experience thread)
- Role: unknown
- Type: Interview
- Status: REAL
- Source: TeamBlind — https://www.teamblind.com/post/interviewing-experience-for-hft-jkn1visq
- Answer/Discussion: none found — thin data point, included for completeness but no concrete question was quoted.

### Citadel Securities phone screens include small, sharp coding prompts including ring buffers (alongside merge-K and stock-DP problems)
- Company: Citadel Securities
- Role: HFT Software Engineer
- Type: Interview
- Status: REAL
- Source: 1point3acres (via search index/summary; direct page blocked by Cloudflare for this research pass) — https://www.1point3acres.com/interview/problems/company/citadel
- Answer/Discussion: none found; ring-buffer implementation is the concrete low-latency data-structure prompt reported among the phone-screen set. Site also notes Citadel's "single weak round = reject" policy.

### Take-home: given a diagram of connectivity between the company's trading server and the exchange, design a strategy to minimize latency
- Company: unknown/general (quant trading firm; company name withheld by author due to NDA)
- Role: unknown (quant developer/trader candidate)
- Type: OA
- Status: REAL
- Source: Personal blog "Radical Ideal" (jb2358) — https://jb2358.user.srcf.net/2024/09/26/quant-trading-interviews/
- Answer/Discussion: none found in detail; author notes this was one part of a broader take-home combining trading-strategy analysis with a network-latency-minimization design task. Author states most of their private notes are withheld due to NDA.

---
## PRACTICE (listicle / prep-site content — presented as typical or illustrative questions, not verified as a literal transcript from a specific real candidate)

### Two threads each increment their own counter; the counters happen to be in the same cache line. What goes wrong, and how do you fix it?
- Company: unknown/general (framed as C++ quant interview prep)
- Role: Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: False sharing — the two counters share a cache line, so writes by one core invalidate the other core's cache line, causing unnecessary coherence traffic. Fix: pad/align each counter to its own cache line (e.g., alignas(64) or padding struct).

### SoA vs AoS — when do you choose each?
- Company: unknown/general
- Role: Quant Developer / HFT SWE
- Type: Unknown
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: none found beyond the prompt itself; general theme is cache-friendly data layout for hot-path iteration (SoA improves vectorization/cache-line utilization when only a few fields are touched per iteration).

### You have a loop with an "if" that's true less than 1% of the time. How do you optimize it?
- Company: unknown/general
- Role: Quant Developer / HFT SWE
- Type: Unknown
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: Branch prediction angle — rare branch is easy for the predictor (near-100% "not taken"), so optimization should be validated by profiling first; techniques include [[unlikely]] / __builtin_expect, or restructuring to remove the branch (branchless/bitwise tricks) only if profiling shows a real stall.

### How do you write code that maximizes cache utilization?
- Company: unknown/general
- Role: HFT / low-latency C++
- Type: Unknown
- Status: PRACTICE
- Source: QuantLabsNet — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: none found beyond general cache-locality talking points (sequential access, data layout, avoiding pointer-chasing).

### How do you minimize branch mispredictions?
- Company: unknown/general
- Role: HFT / low-latency C++
- Type: Unknown
- Status: PRACTICE
- Source: QuantLabsNet — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: Branchless code via conditional moves/bitwise ops; profile first since modern predictors are already good.

### How would you implement a custom memory allocator for low-latency trading?
- Company: unknown/general
- Role: HFT / low-latency C++
- Type: Unknown
- Status: PRACTICE
- Source: QuantLabsNet — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: none found in detail; general theme is pool/arena allocators to avoid malloc/free syscalls and unpredictable latency on the hot path.

### Implement a lock-free queue ("classic HFT question" per source)
- Company: unknown/general
- Role: HFT / low-latency C++
- Type: Unknown
- Status: PRACTICE
- Source: QuantLabsNet — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: none found in detail.

### Compare and contrast mutexes, semaphores, and condition variables
- Company: unknown/general
- Role: HFT / low-latency C++
- Type: Unknown
- Status: PRACTICE
- Source: QuantLabsNet — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: none found.

### What is false sharing and how do you prevent it?
- Company: unknown/general
- Role: HFT / low-latency C++
- Type: Unknown
- Status: PRACTICE
- Source: QuantLabsNet — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: Prevent via padding/alignment so independently-written variables don't share a cache line.

### Walk through what happens when a market-data packet arrives at the network card and propagates to your trading code in a kernel-bypass setup
- Company: framed as "Jump Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/jump-trading/
- Answer/Discussion: Expected discussion covers NIC → kernel-bypass driver (DPDK/Solarflare/Mellanox) → user-space ring buffer → application parsing, contrasted with the traditional NIC → kernel interrupt → sockets path and its added latency/context-switch overhead.

### Discuss memory ordering in modern CPUs: what does memory_order_acquire actually guarantee on x86, ARM, RISC-V?
- Company: framed as "Jump Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/jump-trading/
- Answer/Discussion: none found in detail beyond the prompt; ties to C++ atomics/memory model and architecture-specific reordering guarantees.

### Reason about when an FPGA path beats a software path and when it doesn't
- Company: framed as "Jump Trading" style prep
- Role: Low-latency Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/jump-trading/
- Answer/Discussion: none found in detail.

### Describe how you'd profile a slow market-data processor — what tools, what you'd measure, how you'd interpret results
- Company: framed as "Jump Trading" style prep
- Role: Low-latency Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/jump-trading/
- Answer/Discussion: none found in detail; general theme is perf/flamegraphs, cycle counters, and tail-latency (p99/p999) measurement rather than average latency.

### Explain cache coherence at the hardware level and what it means for cross-core communication design
- Company: framed as "Jump Trading" style prep
- Role: Low-latency Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/jump-trading/
- Answer/Discussion: none found in detail; expected to touch MESI-style protocols and why cross-core writes to shared/adjacent cache lines are costly.

### Parse this fixed-layout message and give me the price field with the fewest cycles of latency
- Company: unknown/general low-latency trading firm
- Role: FPGA Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233477296/fpga-interview-low-latency-trading-firm/
- Answer/Discussion: none found in detail; framed as a market-data parsing/clock-cycle-minimization exercise.

### Cross this valid signal from the 156.25 MHz MAC clock into your 322 MHz core clock
- Company: unknown/general low-latency trading firm
- Role: FPGA Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233477296/fpga-interview-low-latency-trading-firm/
- Answer/Discussion: Clock-domain-crossing fundamentals (synchronizer chains, metastability).

### Two multicast lines, one drops a packet. How does your feed handler stay correct and still keep up?
- Company: unknown/general low-latency trading firm
- Role: FPGA/low-latency Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233477296/fpga-interview-low-latency-trading-firm/
- Answer/Discussion: A/B line arbitration for redundant multicast market-data feeds; sequence-gap detection and recovery/gap-fill while continuing to process the good line.

### A setup path is failing by 200 picoseconds. Walk me through your options
- Company: unknown/general low-latency trading firm
- Role: FPGA Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233477296/fpga-interview-low-latency-trading-firm/
- Answer/Discussion: Timing-closure trade-offs (pipeline restructuring, logic re-balancing, clock constraints).

### Where would you place a pre-trade fat-finger check so it doesn't add to the critical path?
- Company: unknown/general low-latency trading firm
- Role: FPGA/low-latency Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233477296/fpga-interview-low-latency-trading-firm/
- Answer/Discussion: none found in detail; systems-architecture trade-off between safety checks and critical-path latency.

### What does CPU pinning buy you, and what can it break operationally?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: none found in detail; expected to cover isolcpus/taskset, avoiding scheduler migration and cache-line ping-pong, versus risks like starving other processes or unbalanced IRQ handling.

### You improved median latency but p99 regressed. What are the first three hypotheses you test?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: none found in detail; tail-latency debugging theme (GC/allocator pauses, page faults, lock contention, scheduler noise).

### When would SoA outperform AoS in an order book or market-data normalizer?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: none found in detail.

### Explain false sharing and how you'd detect it (symptoms, counters, flamegraph hints)
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: Detection via perf c2c, cache-miss counters, and flamegraphs showing unexpectedly high time in otherwise-trivial atomic increments.

### Why might huge pages help? What can go wrong operationally?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: Fewer TLB misses/page-table walks for large working sets; downsides include memory fragmentation and startup allocation stalls if hugepages aren't pre-reserved.

### Where can exceptions accidentally land on the hot path, and what's your strategy?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: none found in detail; theme of avoiding exceptions/allocations in the hot path.

### How would you redesign a shared queue that becomes a throughput bottleneck at peak?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency C++ Engineer
- Type: Unknown
- Status: PRACTICE
- Source: HackerPrep — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: none found in detail; lock-free/SPSC-ring-buffer redesign theme.

### Walk through what happens when a packet arrives at a network card and how it reaches your trading code in a kernel-bypass setup (HRT variant)
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency Systems Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/hudson-river-trading/
- Answer/Discussion: none found in detail; same theme as the Jump Trading variant above (DPDK/Solarflare/Mellanox user-space path vs kernel sockets path).

### Discuss lock-free data structures — when do they help, what are the costs, what's the difference from wait-free?
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency Systems Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/hudson-river-trading/
- Answer/Discussion: none found in detail.

### Explain how cache coherence affects cross-core communication and what you'd do to minimize cost
- Company: framed as "Hudson River Trading" style prep
- Role: Low-latency Systems Engineer
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/companies/hudson-river-trading/
- Answer/Discussion: none found in detail.

### Troubleshoot a Linux host that rejects SSH connections (layered troubleshooting: ping, traceroute, etc.)
- Company: framed as "Hudson River Trading" style prep (site claims sourced from real candidate interviews; unverifiable independently in this research pass — 1point3acres/Glassdoor-style corroboration was not accessible)
- Role: Software Engineer
- Type: Unknown
- Status: PRACTICE
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found in detail beyond prompt.

### Explain why `du` and `df` report different disk-usage numbers on the same filesystem
- Company: framed as "Hudson River Trading" style prep (same sourcing caveat as above)
- Role: Software Engineer
- Type: Unknown
- Status: PRACTICE
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: Classic cause is a deleted-but-still-open file (unlinked inode held open by a process), which df still counts against used space but du can't see via directory traversal.

### Reason about Unix signals, zombies, and process reaping (what does `kill` actually do; SIGTERM vs SIGKILL; how zombies form and get reaped)
- Company: framed as "Hudson River Trading" style prep (same sourcing caveat)
- Role: Software Engineer
- Type: Unknown
- Status: PRACTICE
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found in detail beyond prompt.

### Explain large memory allocation, swap behavior, and C++ `inline` trade-offs
- Company: framed as "Hudson River Trading" style prep (same sourcing caveat)
- Role: Software Engineer
- Type: Unknown
- Status: PRACTICE
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found in detail.

### Explain C++ `inline`, segfaults, virtual memory, and `std::string` internals (touches MMU/TLB/page tables)
- Company: framed as "Hudson River Trading" style prep (same sourcing caveat)
- Role: Software Engineer
- Type: Unknown
- Status: PRACTICE
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found in detail.

### "What Linux/systems questions might an HFT firm ask?" — CFS vs. SCHED_FIFO/SCHED_RR, TCP vs UDP for market-data feeds, IRQ affinity/NIC tuning, perf/ftrace/eBPF, huge pages, NUMA awareness, cache hierarchy & false sharing
- Company: unknown/general (speculative advice thread, not a report of an actual interview)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: Quora — https://www.quora.com/I-have-an-interview-with-a-high-frequency-trading-firm-and-they-are-going-to-ask-me-Linux-questions-What-questions-might-they-ask-me
- Answer/Discussion: Answer is explicitly a forward-looking, synthesized prep framework ("what might they ask"), not a documented list of questions actually asked to a real candidate. Useful as a topic checklist: scheduling policy trade-offs for HFT, why UDP is preferred over TCP for market data multicast feeds, tuning interface/IRQ affinity to reduce latency, profiling tools (perf, ftrace, eBPF), virtual memory/huge pages, NUMA, and cache/false-sharing awareness.
