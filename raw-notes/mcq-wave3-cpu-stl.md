# Wave 3 MCQ Bank — CPU Architecture/Caches & STL/Data Structures (sourced 2026-08-27)

## Section A: CPU Architecture & Caches

### What is cache memory?
- Options: A) Permanent storage B) Small, fast memory located close to the CPU C) Virtual memory on disk D) Network storage
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack, Flutter MCQ question bank) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: Cache memory is a small, fast memory located close to the CPU that stores frequently accessed data and instructions to reduce access time.

### In the memory hierarchy, which is typically the fastest?
- Options: A) Hard Disk B) RAM C) Cache D) SSD
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: Cache memory is the fastest in the memory hierarchy, followed by RAM, SSD, and then hard disk (registers are actually fastest of all, faster than cache, but among the listed options cache wins). Speed decreases as capacity increases.

### Which memory is fastest in the memory hierarchy? (registers included as an option)
- Options: A) Cache memory B) RAM C) Registers D) Hard disk
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE, college exam-prep site for a Computer Organization course) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Registers are fastest (1-cycle access, on-chip). Cache is second, then RAM, then secondary storage (disk). Speed is inversely related to size and cost.

### What is the main difference between RISC and CISC architectures?
- Options: A) RISC has more complex instructions than CISC B) RISC uses simple instructions, CISC uses complex instructions C) RISC is slower than CISC D) There is no difference
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: RISC (Reduced Instruction Set Computer) uses simple, fixed-length instructions; CISC (Complex Instruction Set Computer) uses complex, variable-length instructions.

### What is instruction pipelining?
- Options: A) Storing instructions in memory B) Executing multiple instructions simultaneously by overlapping their execution stages C) Compressing instructions D) Encrypting instructions
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: Instruction pipelining overlaps execution of multiple instructions, with different stages of different instructions processed simultaneously to raise throughput.

### What is a pipeline hazard?
- Options: A) A physical damage to the CPU B) A situation that prevents the next instruction from executing in its designated clock cycle C) A security vulnerability D) A power failure
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: A pipeline hazard is a situation that prevents the next instruction from executing during its designated clock cycle, causing stalls.

### Which of the following is NOT a type of pipeline hazard?
- Options: A) Structural hazard B) Data hazard C) Control hazard D) Memory hazard
- Correct: D
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: The three main pipeline hazard classes are structural, data, and control hazards. "Memory hazard" is not a standard classification.

### Which of the following is an example of a data hazard?
- Options: A) An instruction needs a result that is not ready yet B) Two source files have the same name C) A cache line is larger than RAM D) The keyboard input is slow
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "COA MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/quiz.mdx
- Explanation: A data hazard occurs when an instruction depends on the result of a prior instruction that has not yet completed.

### Which of the following is a control hazard?
- Options: A) A branch changes which instructions should be fetched B) Two instructions use different registers C) An ALU performs an add D) A store writes data to memory
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "COA MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/quiz.mdx
- Explanation: Control hazards arise from branches/jumps that change the instruction fetch stream before the outcome is known.

### Which of the following is a structural hazard?
- Options: A) Two instructions need the same hardware resource in the same cycle B) A branch is taken C) A variable changes type D) A compiler emits assembly
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "COA MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/quiz.mdx
- Explanation: A structural hazard happens when two instructions in the pipeline compete for the same hardware resource in the same cycle.

### Why can a load instruction become expensive?
- Options: A) Loads always modify source code B) The data may miss in cache and take much longer to arrive C) Loads are illegal in assembly D) Loads bypass memory completely
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "COA MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/quiz.mdx
- Explanation: If the data being loaded isn't resident in cache, the load must fetch from a slower level (L2/L3/DRAM), stalling dependent instructions.

### Which hardware block is most directly associated with computing memory addresses?
- Options: A) ALU B) FPU C) AGU D) Branch predictor
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "COA MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/quiz.mdx
- Explanation: The Address Generation Unit (AGU) computes effective memory addresses for loads/stores, separate from the ALU's arithmetic/logic work.

### A branch misprediction hurts performance because:
- Options: A) The CPU may need to discard wrong-path work and restart B) It deletes the binary C) It removes all registers D) It turns RAM into cache
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "COA MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/quiz.mdx
- Explanation: Speculatively executed instructions down the wrong path must be flushed and the pipeline restarted on the correct path, wasting cycles.

### If a load instruction misses in cache, what often happens to dependent instructions?
- Options: A) They become faster automatically B) They may stall waiting for the load result C) They retire first anyway D) They change the ISA
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Instruction Flow in a Modern CPU MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/instruction-flow-modern-cpu-quiz.mdx
- Explanation: Instructions depending on the missed load's result cannot proceed (out-of-order schedulers park them) until the data returns from a lower level of the memory hierarchy.

### In direct-mapped cache, how many possible locations can a memory block be placed?
- Options: A) Any location B) One specific location C) Two locations D) Four locations
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: In a direct-mapped cache, each memory block maps to exactly one cache line, determined by (block address mod number of lines).

### What is the main advantage of fully associative cache over direct-mapped cache?
- Options: A) It's faster B) It's cheaper C) It has lower conflict misses D) It uses less power
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: Fully associative cache lets a block go into any line, eliminating conflict misses (at the cost of expensive parallel tag comparators).

### Direct mapping cache: each memory block maps to:
- Options: A) Any cache line B) Only one specific cache line C) A specific SET D) The most recently used line
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Direct Mapping: each memory block maps to exactly one cache line. Line = block_number mod (total_cache_lines). Simple but causes conflict misses.

### Associative mapping (CAM) is accessed by:
- Options: A) Address only B) Content of the data C) Both address and content D) Random access
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Associative/Content Addressable Memory (CAM) is accessed by content: an argument register is compared against all stored tag fields simultaneously (parallel search), needing no address.

### Set-Associative mapping is a compromise between:
- Options: A) SRAM and DRAM B) Direct and Associative mapping C) Write-through and Write-back D) Cache and RAM
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Set-Associative combines Direct (simple, cheap) and Associative (flexible, expensive): a block maps to one specific set, but within that set any line can be used.

### Which of the following is used in TLB (Translation Lookaside Buffer)?
- Options: A) Direct mapping B) FIFO replacement C) Associative memory (CAM) D) Write-back policy
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: The TLB uses associative memory (CAM): all TLB entries are searched simultaneously to find the matching virtual page number to physical frame mapping, for fast address translation.

### Direct mapping address is divided into:
- Options: A) Tag + Offset only B) Tag + Index + Offset C) Block + Page + Offset D) Tag + Set + Block
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Direct-mapped address = Tag (identifies which block) + Index/Line (selects cache line) + Offset (byte within block); Index = block_number mod cache_size.

### Conflict miss in direct mapping occurs when:
- Options: A) Cache is full B) Two memory blocks compete for same cache line C) Cache tag doesn't match D) Page fault
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: A conflict miss happens when two memory blocks that map to the same cache line cannot both be resident in cache simultaneously — even if other lines are empty. This is the worst-case weakness of direct mapping.

### Locality of Reference in cache means:
- Options: A) All memory accessed equally B) Memory references tend to cluster in localized areas C) Cache is local to CPU D) Memory randomly accessed
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Locality of reference means memory accesses cluster: temporal locality (reuse of the same data) and spatial locality (access to nearby addresses). Caches exploit both.

### Temporal locality in cache means:
- Options: A) Nearby addresses accessed together B) Recently used data likely used again soon C) Cache is fast D) Memory is large
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Temporal locality: if address X is accessed, it is likely to be accessed again soon (e.g. a loop counter). Caches retain recently used data to exploit this.

### Cache memory performance is measured in terms of:
- Options: A) Chat ratio B) Hit ratio C) Copy ratio D) Data ratio
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Cache performance is measured by hit ratio = fraction of memory accesses satisfied by the cache; a higher hit ratio yields a lower effective access time.

### Tc=0.4ns, Tm=1.2ns, h=0.85. Effective access time Te = ?
- Options: A) 0.4ns B) 0.58ns C) 1.2ns D) 0.85ns
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Te = Tc + (1-h)×Tm = 0.4 + (1-0.85)×1.2 = 0.4 + 0.15×1.2 = 0.4 + 0.18 = 0.58ns. (Not h×Tc + (1-h)×Tm — cache access Tc is always paid first.)

### Write Through cache policy means:
- Options: A) Write to cache only on hit B) Write to both cache and memory on hit C) Write to memory only D) Write to backup storage
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Write-through: on every write hit, data is written to both cache and memory. Memory stays current, but it's slower due to memory-write overhead on every store.

### Write Back cache policy: when is memory updated?
- Options: A) On every write B) On read miss C) Only when the block is evicted from cache D) Never
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: Write-back updates memory only when the modified ("dirty") cache block is evicted/replaced, using a dirty bit to track pending writes. Faster than write-through, but memory can be stale until eviction.

### Which page replacement algorithm has Belady's Anomaly?
- Options: A) LRU B) OPT (Optimal) C) FIFO D) LFU
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Pravesh0005/CSE-211-EXAM-PREP-WEBSITE) — https://github.com/Pravesh0005/CSE-211-EXAM-PREP-WEBSITE/blob/main/cse211.html
- Explanation: FIFO exhibits Belady's Anomaly: increasing the number of frames can counter-intuitively increase page faults. LRU and OPT are not susceptible to this anomaly.

### What does LRU stand for in cache replacement policies?
- Options: A) Last Recently Used B) Least Recently Used C) Last Requested Unit D) Least Required Unit
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: LRU (Least Recently Used) is a cache/page replacement policy that evicts the line/page that has gone unused for the longest time.

### What is a TLB (Translation Lookaside Buffer)?
- Options: A) A type of RAM B) A cache for page table entries C) A disk buffer D) A network buffer
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: The TLB caches recent virtual-to-physical address translations, avoiding a full page-table walk on every memory access.

### What is a multi-core processor?
- Options: A) A processor with multiple cache levels B) A processor with multiple independent processing units on a single chip C) A processor with multiple instruction sets D) A processor with multiple power supplies
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: A multi-core processor contains multiple independent cores on one chip, enabling true parallel execution of multiple threads.

### What is DMA (Direct Memory Access)?
- Options: A) A type of RAM B) A technique allowing devices to transfer data directly to/from memory without CPU intervention C) A CPU instruction D) A type of cache
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: DMA lets peripherals transfer data to/from memory without continuous CPU involvement, freeing the CPU for other work.

### What is Amdahl's Law used for?
- Options: A) Calculating memory size B) Predicting the theoretical speedup of a program using multiple processors C) Measuring cache performance D) Calculating power consumption
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: Amdahl's Law predicts the theoretical maximum speedup from parallelization given the fraction of the program that can be parallelized.

### What determines the maximum memory addressable by a system?
- Options: A) Data bus width B) Address bus width C) Control bus width D) Cache size
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (md-ruhulamin/skill_stack) — https://github.com/md-ruhulamin/skill_stack/blob/main/lib/data/mcq/computer_architecture_mcq.dart
- Explanation: Address bus width sets the maximum addressable memory (e.g., a 32-bit address bus addresses 2^32 locations).

### You annotate a branch with `[[likely]]` in C++20. Which of the following is correct?
- Options: A) The branch predictor will now predict this arm is taken, reducing mispredictions at runtime B) The compiler may lay out the likely arm as fall-through in the instruction stream and move the unlikely arm out of line, improving instruction cache density and enabling certain optimisations; the hardware branch predictor's runtime behaviour is unchanged C) The branch is eliminated and replaced with a conditional move instruction D) The annotation causes the function to be inlined at all call sites
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, "Dura" Quant/HFT interview-prep curriculum, lesson "Branch Prediction Hints and Branchless Arithmetic") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-1-modern-cpp-for-hft/03-branch-prediction-and-branchless-patterns.mdx
- Explanation: `[[likely]]`/`[[unlikely]]` are compiler layout hints, not hardware hints. They affect fall-through vs. out-of-line code layout (helping icache density and optimizer decisions) but do not change the hardware branch predictor's learned runtime behavior, and they do not generate a `cmov` or force inlining.

### A loop computes `int64_t best = (a > b) ? a : b;` one hundred million times with random a and b values. A colleague says "this has a 50% misprediction rate — use a branch to make it faster." What is wrong with the reasoning?
- Options: A) Nothing — a branch would be faster with 50% misprediction B) The ternary expression on integers compiles to a `cmov` instruction, which has no branch and no prediction; the colleague is right that a branch would mispredict 50% of the time but wrong to propose switching to a branch — `cmov` is exactly the solution to the 50%-misprediction problem C) Ternary expressions are always slower than branches regardless of prediction rate D) The loop should use `std::max`, which never generates branches
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura) — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-1-modern-cpp-for-hft/03-branch-prediction-and-branchless-patterns.mdx
- Explanation: A branch on random 50/50 data mispredicts half the time, costing 10–20 cycles per misprediction — the worst case. A `cmov` (produced by the integer ternary under optimization) has no branch or prediction, always costing 1–3 cycles regardless of outcome, so `cmov` is the fix, not a branch.

### A hot loop scans 1,000,000 Order structs (32 bytes each: id, timestamp, price, quantity, flags) reading ONLY the price field. What is the cache effect of converting to structure-of-arrays (SoA) so price is its own contiguous `std::vector<int64_t>`?
- Options: A) No effect — the same total bytes are read either way B) It is strictly worse, because SoA scatters each Order's fields across five arrays and destroys spatial locality C) AoS loads a full 32-byte Order per element, so one 64-byte line holds 2 prices and 3/4 of every line is unused fields; SoA packs 8 int64 prices per line with zero unused bytes, cutting lines touched ~4x and feeding the hardware prefetcher a clean sequential stride D) SoA helps only because int64 is smaller than the struct; a double field would perform the same as AoS
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "Cache-Aware Programming") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/03-cache-aware-programming.mdx
- Explanation: You pay per cache line, not per byte used. AoS wastes 24 of 32 bytes per struct on unread fields; SoA packs only the field the loop needs, quadrupling effective density and letting the hardware prefetcher stream cleanly.

### `struct S { std::atomic<uint64_t> a; std::atomic<uint64_t> b; };` is shared by two threads: thread 1 only writes `s.a`, thread 2 only writes `s.b`. Throughput is ~6x worse than expected with no lock anywhere. What is the root cause and fix?
- Options: A) The atomics need `std::memory_order_seq_cst` instead of relaxed; tightening ordering restores throughput B) False sharing: `a` and `b` are 8 bytes each and land on the same 64-byte line, so each core's write invalidates the other's cached copy via the coherence protocol, ping-ponging the line; fix by padding so `a` and `b` occupy separate cache lines (e.g. via `alignas(std::hardware_destructive_interference_size)`) C) A data race — two threads writing the same struct is undefined behavior regardless of which fields they touch; add a mutex D) The struct is too small to align; adding a virtual function pushes `b` onto its own line and fixes it
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "Cache-Aware Programming") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/03-cache-aware-programming.mdx
- Explanation: MESI coherence operates at cache-line granularity. Even though the threads touch distinct atomic fields, both fields share one 64-byte line, so each write invalidates the other core's cached copy — classic false sharing. The fix is padding each field to its own line, not stronger memory ordering (which would make it worse) or a mutex (unnecessary — the writes are already race-free).

### An engineer adds `__builtin_prefetch(&arr[i+1], 0, 3);` inside a loop that already iterates `arr` sequentially from front to back. After measuring, the loop is unchanged or slightly slower. Why?
- Options: A) The third argument should be 0, not 3 — locality 3 disables the prefetch entirely B) Prefetch only works on heap memory; `arr` must be allocated with `new` for the hint to take effect C) The hardware prefetcher already detects the forward sequential stride and prefetches those lines automatically, so the manual hint is redundant and can mildly hurt by competing for issue slots; manual prefetch only helps access patterns the hardware cannot predict (pointer chasing, computed-index hops), issued far enough ahead to hide load latency D) Prefetch changed the computed sum slightly due to reordering, which is expected
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "Cache-Aware Programming") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/03-cache-aware-programming.mdx
- Explanation: Sequential forward scans are exactly what the hardware stride prefetcher already handles, so the manual hint is redundant instruction overhead. Manual prefetch pays off only for hardware-unpredictable patterns like pointer chasing, issued early enough to hide the ~hundreds-of-cycles load latency.

### The NIC is attached to socket 0. The strategy thread runs on socket 1. The DMA ring buffer (where the NIC writes incoming packets) is allocated by the main thread (socket 0) at startup. What happens to the strategy thread's reads from the ring buffer?
- Options: A) They hit local DRAM because the kernel migrates pages to the reading socket automatically B) They cross the QPI/UPI inter-socket link and incur 2–3x higher latency than local reads C) They hit the L3 cache on socket 1 because L3 is shared across sockets D) They are unaffected because the DMA ring is in I/O memory, not DRAM
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "NUMA Topology and Remote Memory") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/05-numa-topology-and-remote-memory.mdx
- Explanation: Linux uses a first-touch page policy: the pages backing the ring buffer live on socket 0's DRAM because the main thread (socket 0) first touched them. The strategy thread on socket 1 must cross the QPI/UPI interconnect on every read, incurring the remote-NUMA penalty. L3 is per-socket, not shared, and the kernel doesn't auto-migrate pages. Fix: allocate on the strategy's NUMA node (e.g., `numa_alloc_onnode`) or pin the whole pipeline to one socket.

### `perf stat` reports IPC (instructions per cycle) of 0.18 for a market-data update loop, versus 3.5 for a compute-bound loop on the same machine. What is the primary interpretation?
- Options: A) The loop has too many branches — use branchless patterns B) The CPU is stalled waiting for memory most of the time — the loop is memory-bound C) The loop is executing too many instructions — simplify the algorithm D) The CPU is context-switching too frequently — pin the thread to a core
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "perf stat and Cache Profiling") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/07-perf-stat-and-cache-profiling.mdx
- Explanation: IPC 0.18 means the CPU completes fewer than 1 instruction every 5 cycles, versus 3–5 IPC for a healthy compute-bound out-of-order loop. The dominant cause of such a low IPC is the pipeline stalling on memory (LLC misses to DRAM stall for 30–100+ cycles). Branch mispredictions would show as a high branch-miss counter but wouldn't crush IPC this far; context switches show in task-clock ratio, not IPC.

### A struct has 4 fields: price (8B), size (4B), flags (1B), padding (3B) — 16 bytes total. You keep 1,024 of them and loop to sum the price field. A cache line is 64 bytes. How many cache lines does the loop touch (AoS layout)?
- Options: A) 128 — only the price bytes, packed at 8B each B) 256 — the struct is 16B, so 4 per cache line, 256 lines for 1024 structs C) 1024 — one load per struct, each struct on its own line D) 512 — structs straddle lines unpredictably
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "AoS vs SoA Layout") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/04-aos-vs-soa-layout.mdx
- Explanation: The 16-byte struct packs 4 per 64-byte line; 1024 / 4 = 256 lines, but only 8 of each struct's 16 bytes (the price) are used — 50% utilization. Under SoA the 1024 contiguous int64 prices occupy only 128 lines at 100% utilization.

### Your order book's hot-path working set is 32 MB. The L2 TLB covers 6 MB at 4K pages and 2 GB at 2MB (huge) pages. What is the expected TLB behavior with 4K pages?
- Options: A) All 32 MB fits in L2 TLB because TLB entries cache any page regardless of size B) 32 MB / 6 MB ≈ 5.3x TLB overflow — most accesses miss the TLB and trigger page walks C) TLB misses are irrelevant because page walks use the L3 cache, which covers 32 MB D) 4K pages are fine because the hardware prefetcher handles page-walk latency transparently
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, lesson "TLB and Huge Pages") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/12-quant-hft/q-3-cache-aware-programming/06-tlb-huge-pages.mdx
- Explanation: At 4K pages the L2 TLB (1,536 entries × 4K = 6MB) can't cover a 32MB working set (needs 8,192 entries) — most hot accesses miss the TLB and trigger a 4-level page walk. With 2MB huge pages the same 32MB needs only 16 entries, comfortably fitting. Page walks may hit L3 for cached page-table entries but still cost 30–50 cycles versus 1–4 for a TLB hit.

### Which of the following belongs more directly to computer organization rather than architecture?
- Options: A) Instruction set semantics B) Calling convention contract C) Pipeline, cache hierarchy, and issue queues D) The legal meaning of ADD in the ISA
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: CPU/Cache
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Architecture vs Organization MCQs Quiz") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/domain/coa/architecture-vs-organization-quiz.mdx
- Explanation: Organization covers the internal implementation choices (pipeline depth, cache hierarchy, issue queues) used to realize a given architecture; the ISA's programmer-visible contract (registers, instruction semantics, calling conventions) is architecture.

---

## Section B: STL & Data Structures

### Which of the following is a true statement about the difference between pointers and iterators?
- Options: A) While pointers are variables that hold memory addresses, iterators are generic functions used to traverse containers B) Incrementing an iterator always means accessing the next element in the container (if any), no matter the container; incrementing a pointer means pointing to the next element in memory, not always the next logical element C) Pointers are variables that hold memory addresses whereas an iterator is an unsigned integer that refers to offsets in arrays D) All iterators are implemented with pointers, so all iterators are pointers but not all pointers are iterators
- Correct: B
- Company: unknown/general (LinkedIn Skill Assessment question bank — C++)
- Type: MCQ
- Topic: STL/DS
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes, crowd-sourced LinkedIn Skill Assessment questions) — https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/c%2B%2B/c%2B%2B-quiz.md
- Explanation: Iterators are an abstraction that behaves consistently across container types — incrementing always advances to the next logical element regardless of underlying storage — whereas pointer arithmetic follows raw memory layout, which is only "the next element" for contiguous containers like `std::vector`.

### Which of the following STL classes is the best fit for implementing a phonebook? Suppose each entry contains a name and a phone number, with no duplicates, and you want lookup by name.
- Options: A) `std::priority_queue` B) `std::list` C) `std::vector` D) `std::map`
- Correct: D
- Company: unknown/general (LinkedIn Skill Assessment question bank — C++)
- Type: MCQ
- Topic: STL/DS
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes) — https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/c%2B%2B/c%2B%2B-quiz.md
- Explanation: `std::map` provides ordered key-based lookup by name with no duplicate keys, which matches the phonebook requirement directly.

### Assume you have `std::map<string, int> m;`. Select the single true statement about `for (const pair<string, int>& elem : m)`.
- Options: A) The loop properly iterates over the map, creating no extra copies B) The loop will create a copy of each element in the map as the type of `elem` mismatches C) The code won't compile as a const pair cannot bind to a map
- Correct: A (note: strictly, `std::map::value_type` is `pair<const Key, T>`, so `pair<string,int>` actually mismatches and does force a copy in real compilers — this question's marked answer is disputed/imprecise; flagged here as sourced, not verified)
- Company: unknown/general (LinkedIn Skill Assessment question bank — C++)
- Type: MCQ
- Topic: STL/DS
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes) — https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/c%2B%2B/c%2B%2B-quiz.md
- Explanation: As marked in the source repo, option A is the accepted answer. Be aware `std::map`'s actual `value_type` is `std::pair<const Key, T>`, so this is a known point of subtlety/contention worth double-checking before using verbatim.

### What is the difference between `std::unique_ptr` and `std::shared_ptr`?
- Options: A) `unique_ptr` has exclusive ownership, `shared_ptr` allows multiple owners B) `unique_ptr` is faster but less safe C) `shared_ptr` can only be used with classes D) There is no difference
- Correct: A
- Company: unknown/general (LinkedIn Skill Assessment question bank — C++)
- Type: MCQ
- Topic: STL/DS
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes) — https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/c%2B%2B/c%2B%2B-quiz.md
- Explanation: `std::unique_ptr` enforces single, exclusive ownership (move-only); `std::shared_ptr` uses reference counting to allow multiple simultaneous owners of the same resource.

### What is `std::unordered_map` based on?
- Options: A) Binary search tree B) Hash table C) Linked list D) Array
- Correct: B
- Company: unknown/general (LinkedIn Skill Assessment question bank — C++)
- Type: MCQ
- Topic: STL/DS
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes) — https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/c%2B%2B/c%2B%2B-quiz.md
- Explanation: `std::unordered_map` is implemented as a hash table, giving average O(1) lookup versus O(log n) for `std::map` (a balanced tree).

### What is the default underlying container for `std::stack`?
- Options: A) `std::vector` B) `std::deque` C) `std::queue` D) `std::list`
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::stack` (and `std::queue`) default to `std::deque` as their underlying container adapter storage.

### Which container does not provide random access iterators?
- Options: A) `std::list` B) `std::deque` C) `std::array` D) `std::vector`
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::list` is a doubly-linked list, offering only bidirectional iterators; `vector`, `deque`, and `array` all support random-access iterators.

### Which of the following allows duplicate keys?
- Options: A) `std::set` B) `std::multimap` C) `std::map` D) `std::unordered_set`
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::multimap` explicitly permits multiple entries with equal keys, unlike `std::map`/`std::set`/`std::unordered_set`.

### What does `std::vector::capacity()` return?
- Options: A) Number of elements B) Allocated storage size C) Free space D) Max allowed size
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `capacity()` returns the size of the currently allocated internal storage, which is greater than or equal to `size()` (the actual element count).

### Which of these is a container adapter?
- Options: A) `std::deque` B) `std::array` C) `std::queue` D) `std::set`
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::queue`, `std::stack`, and `std::priority_queue` are container adapters — they wrap an underlying container (default `std::deque`) and restrict its interface. `deque`, `array`, and `set` are containers themselves, not adapters.

### Which of these provides constant time insertion/removal at both ends?
- Options: A) `std::vector` B) `std::deque` C) `std::array` D) `std::set`
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::deque` supports amortized O(1) `push_front`/`push_back`/`pop_front`/`pop_back`, unlike `std::vector`, which is O(1) amortized only at the back and O(n) at the front.

### What is required for `std::sort()` to work?
- Options: A) Random access iterators B) Bidirectional iterators C) Forward iterators D) None
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::sort` requires RandomAccessIterators (works on `vector`, `deque`, `array`, raw arrays), which is why `std::list` provides its own `list::sort()` member function instead.

### Which function removes consecutive duplicates in a range?
- Options: A) `unique()` B) `filter()` C) `remove()` D) `erase()`
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "STL MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/advanced/stl.md
- Explanation: `std::unique` removes consecutive duplicate elements in a range (logically, via the erase-remove idiom it needs a follow-up `container.erase(...)` to shrink the container).

### What is a smart pointer in C++?
- Options: A) A pointer that manages dynamic memory B) A pointer that always points to a valid memory C) A pointer that can be dereferenced D) None of the above
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Smart Pointers MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/specialized/smart-pointers.md
- Explanation: A smart pointer is a class template (`unique_ptr`, `shared_ptr`, `weak_ptr`) that wraps a raw pointer and manages the lifetime of dynamically allocated memory via RAII.

### Which type of smart pointer automatically deallocates memory when it goes out of scope?
- Options: A) `std::unique_ptr` B) `std::shared_ptr` C) `std::weak_ptr` D) None of the above
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Smart Pointers MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/specialized/smart-pointers.md
- Explanation: Note: all standard smart pointers deallocate via RAII when they go out of scope (unique_ptr always; shared_ptr when the refcount hits zero). This question's phrasing/marked answer (A) is treating exclusive-ownership auto-deallocation as the more textbook-canonical case — worth double-checking against your own understanding before relying on it verbatim.

### What is the purpose of `std::shared_ptr`?
- Options: A) To manage shared ownership of a dynamically allocated object B) To avoid memory leaks C) To allocate memory for variables D) None of the above
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Smart Pointers MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/specialized/smart-pointers.md
- Explanation: `std::shared_ptr` maintains a reference count so multiple pointers can jointly own and manage the lifetime of a single dynamically-allocated object.

### What is the purpose of `std::weak_ptr`?
- Options: A) To observe an object without affecting its reference count B) To provide exclusive ownership C) To manage multiple references D) None of the above
- Correct: A
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Smart Pointers MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/specialized/smart-pointers.md
- Explanation: `std::weak_ptr` holds a non-owning ("weak") reference to an object managed by `shared_ptr`, used to break reference cycles, without incrementing the reference count.

### How does `std::unique_ptr` ensure there is only one owner of the object?
- Options: A) By deleting the object when it goes out of scope B) By preventing copying of the pointer C) By allowing shared ownership D) None of the above
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Smart Pointers MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/specialized/smart-pointers.md
- Explanation: `std::unique_ptr`'s copy constructor/assignment are deleted; only move semantics are allowed, which transfers (rather than duplicates) ownership, guaranteeing exclusivity.

### Can you assign a `std::unique_ptr` to a `std::shared_ptr`?
- Options: A) Yes B) No C) It depends on the compiler D) None of the above
- Correct: B (nuance: direct assignment is not allowed, but a `unique_ptr` can be *moved into* a `shared_ptr`'s constructor, e.g. `shared_ptr<T> sp(std::move(up));`, which transfers ownership)
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (aabhinavg1/compilersutra, "Smart Pointers MCQs") — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/specialized/smart-pointers.md
- Explanation: You cannot directly assign one to the other via `operator=`, but a `shared_ptr` can be move-constructed from a `unique_ptr` (transferring, not sharing, ownership) — worth clarifying this nuance in an interview answer rather than a flat "no."

### What is "iterator invalidation"?
- Options: A) A runtime error when an iterator goes past the end of a container B) When an operation on a container (like inserting an element into a `std::vector`) makes some or all of its existing iterators unusable C) A compile-time error when an iterator type does not match its container type D) When an iterator is used with a generic algorithm that doesn't support it
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (AndyDope/CDAC-Notes, "C++ MCQs", CDAC PG-DAC course notes) — https://github.com/AndyDope/CDAC-Notes/blob/main/C%2B%2B%20CDAC/C%2B%2B%20MCQs.md
- Explanation: For example, `push_back` on a `std::vector` may trigger a reallocation of its entire internal array, leaving previously-held iterators/pointers/references dangling (pointing at freed memory).

### Which STL container is the best choice if you need fast look-up by a unique key and also require the elements to be stored in sorted order?
- Options: A) `std::vector` B) `std::unordered_map` C) `std::list` D) `std::map`
- Correct: D
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (AndyDope/CDAC-Notes, "C++ MCQs") — https://github.com/AndyDope/CDAC-Notes/blob/main/C%2B%2B%20CDAC/C%2B%2B%20MCQs.md
- Explanation: `std::map` gives both key-based lookup (O(log n), via its underlying red-black tree) and sorted iteration order; `std::unordered_map` is faster for lookup (O(1) average) but does not maintain order.

### Which of the following operations is most likely to be significantly slower on a `std::vector` than on a `std::list` for a large number of elements?
- Options: A) Accessing the element at a random index (e.g., `my_container[N/2]`) B) Adding an element to the very end (`push_back`) C) Inserting a new element at the very beginning D) Getting the total number of elements (`.size()`)
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (AndyDope/CDAC-Notes, "C++ MCQs") — https://github.com/AndyDope/CDAC-Notes/blob/main/C%2B%2B%20CDAC/C%2B%2B%20MCQs.md
- Explanation: Inserting at the front of a `vector` requires shifting every existing element — O(n). For a `std::list`, inserting at a known position (e.g., `begin()`) is O(1) since it's just pointer relinking.

### Which container would you use to implement a print job queue where jobs are processed in the order they are received?
- Options: A) `std::stack` B) `std::queue` C) `std::priority_queue` D) `std::vector`
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (AndyDope/CDAC-Notes, "C++ MCQs") — https://github.com/AndyDope/CDAC-Notes/blob/main/C%2B%2B%20CDAC/C%2B%2B%20MCQs.md
- Explanation: `std::queue` is a FIFO container adapter — exactly the ordering semantics required for a print job queue processed in arrival order.

### Why does the doubling strategy result in O(1) amortized push cost for a dynamic array, but a fixed "+10 elements" growth strategy does not?
- Options: A) Doubling is faster because multiplication is cheaper than addition B) Doubling makes resizes exponentially rarer — total copy work across n pushes sums to O(n), but +10 growth causes O(n) resizes, each costing O(n) C) Doubling reduces memory fragmentation in the heap D) Fixed growth strategies are actually the same — they are both O(1) amortized
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, CS-fundamentals module "Amortized Analysis") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/3-cs-fundamentals/3-1-complexity/07-amortized-analysis.mdx
- Explanation: With doubling, resizes happen at sizes 1, 2, 4, 8, ... n — a geometric series summing to ~2n total copy operations across n pushes, i.e., O(1) amortized per push. With +10 growth, resizes happen every 10 pushes (n/10 times), each costing O(current size), summing to O(n²) total, i.e., O(n) amortized per push. This is exactly why `std::vector`'s growth factor (typically 1.5x–2x) matters for amortized `push_back` cost.

### A dynamic array `push_back` triggers a resize that copies 1,000,000 elements. Can you still say `push_back` is O(1) amortized?
- Options: A) No — a single O(n) operation means push is O(n) B) Yes — amortized O(1) means the average over a sequence of operations is O(1), not that each individual operation is O(1) C) Yes — but only if the next million pushes do not trigger a resize D) No — amortized analysis only applies to data structures with fewer than 10,000 elements
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, "Amortized Analysis") — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/3-cs-fundamentals/3-1-complexity/07-amortized-analysis.mdx
- Explanation: Amortized analysis averages cost over a sequence of operations — the rare expensive O(n) resize is paid for by the credits deposited by the many preceding O(1) pushes since the last resize. The single worst-case push is genuinely O(n), which matters for latency-sensitive (e.g. HFT) code even though the amortized bound is O(1) — a key point interviewers probe for.

### Why does a priority queue's insert and extract-min run in O(log n) rather than O(1)?
- Options: A) Priority queues use sorting, which is always at least O(n log n) B) After each insertion or extraction, the heap must restore its ordering property by traversing up or down the tree, which has log n levels C) Priority queues are implemented as linked lists, which require O(log n) traversal D) The priority comparison itself is an O(log n) operation
- Correct: B
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, CS-fundamentals module on deques/priority queues) — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/3-cs-fundamentals/3-3-linked-lists-stacks-queues/06-deques-priority.mdx
- Explanation: A binary heap (the typical backing structure for `std::priority_queue`) is a complete binary tree of height log n; sift-up after insert and sift-down after extracting the root each traverse at most log n levels, bounding the cost at O(log n).

### In a min-heap stored as an array (zero-indexed), where is the parent of the element at index i?
- Options: A) Index i - 1 B) Index i / 2 C) Index floor((i - 1) / 2) D) Index i * 2
- Correct: C
- Company: unknown/general
- Type: MCQ
- Topic: STL/DS
- Status: PRACTICE
- Source: GitHub (Durwood-Studios/Dura, deques/priority queues module) — https://github.com/Durwood-Studios/Dura/blob/main/src/content/phases/3-cs-fundamentals/3-3-linked-lists-stacks-queues/06-deques-priority.mdx
- Explanation: For a zero-indexed array-backed heap, parent(i) = floor((i-1)/2); left child = 2i+1, right child = 2i+2. This underlies `std::priority_queue`'s (and `std::push_heap`/`std::pop_heap`'s) array-based binary heap.
