# Topic: Concurrency, Multithreading, Atomics, Memory Ordering, Lock-Free Programming (C++) — Quant/HFT/SWE Interview Prep

### Implement a lock-free SPSC (single-producer single-consumer) queue in C++
- Company: Headlands Technology
- Role: unknown (software/quant engineer)
- Type: Interview
- Status: REAL
- Source: efinancialcareers-canada — https://www.efinancialcareers-canada.com/news/the-expert-c-programming-technique-you-will-need-to-know-for-a-hft-interview
- Answer/Discussion: Article frames lock-free programming as "a common trend in HFT interviews," sourced from a Blind forum post citing this specific ask at Headlands Technology. Emphasizes lock-free code is "experts territory" — even experts regularly get it wrong; badly implemented lock-free code can cause terrible performance. A WorldQuant (Millennium) engineer confirmed lock-free questions "can show up" but are team-dependent; a Chicago Trading Company engineer said most firms focus more on STL/templates/modern C++ than lock-free specifically.

### Write a single-producer, single-consumer queue that two threads share without a lock — "No mutex. No std::mutex anywhere."
- Company: Citadel Securities, Hudson River Trading (described as a recurring prompt at both)
- Role: Core/Systems Developer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476386/lock-free-queue-hft-interview-question/
- Answer/Discussion: Expected solution: ring buffer with power-of-two capacity, two atomic counters (head/tail), no synchronization primitives. Interviewer follow-up probes false sharing: if the producer's and consumer's counters sit in the same cache line, every producer write to `tail_` invalidates the consumer core's cached copy of that line, tanking throughput. Fix: `alignas(64)` to place counters on separate cache lines. Also expects discussion of relaxed vs acquire/release memory ordering for the counters. Framed by the source as "a reported, recurring question at major quant trading firms."

### Tell me about false sharing and how it wrecks a lock-free counter (freeze-on-this-topic = quick rejection signal)
- Company: Hudson River Trading (Core Developer track)
- Role: Core Developer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477264/hudson-river-trading-interview/
- Answer/Discussion: Article states candidates who "struggle to explain concepts like false sharing and its impact on lock-free counters will receive quick rejections" in HRT's systems/low-latency round, which also covers kernel bypass networking, lock-free data structures, CPU cache effects, NUMA awareness, and nanosecond-resolution timestamping.

### Kernel, concurrency, CPU architecture type questions in addition to the usual algorithm topics
- Company: Jump Trading
- Role: SWE (systems track)
- Type: Interview
- Status: REAL
- Source: teamblind.com — https://www.teamblind.com/post/jump-trading-interviews-ufqxesha
- Answer/Discussion: A Microsoft-employed poster reported Jump Trading interviews include concurrency and CPU-architecture questions alongside standard algorithms; no further specifics given in-thread.

### You have two threads incrementing a shared counter 1,000,000 times each. The counter ends at less than 2,000,000. Why?
- Company: Hudson River Trading (per source's HRT interview guide)
- Role: unknown
- Type: Interview
- Status: REAL (source explicitly describes this as a real question type from HRT prep guide, distinct from its otherwise generic content)
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/hudson-river-trading-interview
- Answer/Discussion: Classic lost-update race condition — `counter++` is a non-atomic read-modify-write; two threads can read the same stale value before either writes back, losing increments. Fix with `std::atomic<int>` (memory_order_relaxed is sufficient here since there's no other data being published/guarded) or a mutex.

### You have a struct with three 4-byte integers and a 1-byte flag ... how would you lay out the struct, and why? (false sharing / cache-line awareness under concurrent access)
- Company: Jump Trading (per source's Jump Trading interview guide)
- Role: unknown (Core/engineering)
- Type: Interview
- Status: REAL (source flags this as a "real pattern" type question distinct from generic multiple-choice filler in the same guide)
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/jump-trading-interview
- Answer/Discussion: Expected answer discusses avoiding false sharing under concurrent access — grouping/padding fields so data touched by different threads doesn't share a 64-byte cache line. Guide notes Jump emphasizes "memory layout, cache effects, lock-free concurrency, and the C++ memory model" broadly for engineering roles.

### Explain deadlock. How would you handle a deadlock?
- Company: Hewlett Packard Enterprise
- Role: On-campus hire (candidate: Hemlata)
- Type: Interview
- Status: REAL
- Source: Naukri Code360 (interview experience) — https://www.naukri.com/code360/interview-experiences/hewlett-packard-enterprise/interview-experience-by-hemlata-on-campus-dec-2020-270
- Answer/Discussion: Reported as part of the OS-fundamentals segment of the interview; no detailed model answer captured beyond definition + handling strategies (prevention via lock ordering, avoidance via Banker's algorithm, detection/recovery).

### Implement deadlock and multithreading using a C++ program
- Company: NCS Engineers
- Role: unknown (engineer)
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/implement-deadlock-and-multithreading-using-c-program-QTN_817733.htm
- Answer/Discussion: none found (Glassdoor page blocked for full-text extraction; title/prompt confirmed via search index)

### How do you design an alarm callback system? It can take a callback function and a time after which to call this function.
- Company: Oracle
- Role: SWE
- Type: Interview
- Status: REAL
- Source: teamblind.com — https://www.teamblind.com/post/concurrency-and-multi-threading-interview-questions-pnqffua2
- Answer/Discussion: Discussion in thread points toward a mutex + condition-variable based design (a min-heap or sorted structure of pending alarms, worker thread blocks on a condition variable with a timeout until the next alarm is due, needs to handle new alarms being inserted earlier than the current wait target). Thread also notes concurrency/multithreading questions have been reported at Oracle, Dropbox, LinkedIn, Microsoft, Google, and Amazon; one poster claims a Google backend/distributed-systems interview asked candidates to "create a mutex and semaphore in Java from scratch."

### Create a mutex and a semaphore from scratch
- Company: Google (backend/distributed systems team, per poster)
- Role: unknown
- Type: Interview
- Status: REAL
- Source: teamblind.com — https://www.teamblind.com/post/concurrency-and-multi-threading-interview-questions-pnqffua2
- Answer/Discussion: none found beyond the claim itself (reported in Java in the original post, but the underlying primitive-construction concept — building a mutex from an atomic flag/CAS loop plus a wait mechanism, and a semaphore from a counter + condition variable — is the same one asked in C++ contexts).

### Multithreading — "synchronized notify all" question; using a semaphore to achieve thread synchronization
- Company: Optiver
- Role: C++ Developer / Senior C++ Developer / New Grad SWE
- Type: Interview
- Status: REAL
- Source: Glassdoor (via search snippet) — https://www.glassdoor.com/Interview/Optiver-Interview-Questions-E243355.htm?filter.jobTitleExact=C+++Developer
- Answer/Discussion: none found (Glassdoor blocks full text retrieval; candidates reported general topics of C++ [write your own vector], CPU cache/TLB, multithreading [synchronized notify-all], semaphore-based thread synchronization, and memory-leak detection). Senior C++ Developer round reportedly includes an online C++ test followed by a video call discussing "threads, latency, and C++ features."

### Design/implement a thread pool that manages worker threads executing submitted tasks asynchronously, with a fixed thread count and task queue
- Company: unknown/general (sourced from "WallStreetCPP" HFT-focused interview prep content, presented as a representative HFT-style challenge)
- Role: unknown
- Type: Unknown (framed as representative rather than confirmed verbatim from a named company)
- Status: PRACTICE
- Source: techinterview.org (C++ for Quants) — https://www.techinterview.org/post/3233474597/cpp-quant-interviews/
- Answer/Discussion: Notes solutions can use either a classic condition-variable/mutex worker-pool pattern or newer C++23 coroutines/senders-receivers approaches.

### What's the difference between memory_order_relaxed, memory_order_acquire, memory_order_release, and memory_order_seq_cst?
- Company: unknown/general (positioned by source as drawn from interviews at Hudson River Trading, Jump Trading, Citadel Securities, Tower Research, Radix, and DRW, but described as "worked examples" rather than verbatim transcripts)
- Role: Quant Developer / Core Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: relaxed = atomicity only, no ordering guarantee; acquire = prevents subsequent ops from being reordered before the load; release = prevents prior ops from being reordered after the store; acquire/release pairs establish a happens-before edge between threads; seq_cst = strongest, adds a single total global order across all seq_cst atomic operations (most expensive).

### Two threads each increment their own counter. The counters happen to be in the same cache line. What goes wrong, and how do you fix it?
- Company: unknown/general (same quantt.co.uk "worked examples" set as above)
- Role: Quant Developer / Core Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions ; also quantlabsnet.com — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: "Cache-line ping-pong" — each write invalidates the other core's cached copy of the shared line via MESI coherence traffic, forcing repeated memory fetches; can be 10-100x slower than expected. Fix: pad/align each counter to its own cache line with `alignas(64)` (or use `std::hardware_destructive_interference_size`).

### What's the difference between volatile and atomic? When does volatile suffice (if ever) for multithreading?
- Company: unknown/general (quantt.co.uk worked-examples set)
- Role: Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: `volatile` only prevents the compiler from optimizing away/reordering reads/writes to that variable in the eyes of the *compiler*; it gives no atomicity and no cross-thread memory-ordering/visibility guarantees. `std::atomic` is required for correct multithreaded shared-state access; `volatile` alone is essentially never sufficient for thread synchronization in standard C++ (it's for memory-mapped I/O / signal handlers instead).

### Implement a lock-free SPSC ring buffer (with cache-line padding and correct memory ordering)
- Company: unknown/general (quantt.co.uk / quantlabsnet.com worked-examples sets, echoed across multiple HFT-prep articles)
- Role: Quant/Core Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions ; quantlabsnet.com — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: Power-of-two-sized ring buffer; separate head/tail atomics padded with `alignas(64)` to avoid false sharing; producer uses `memory_order_relaxed` to read its own tail and `memory_order_release` to publish it, consumer uses `memory_order_acquire` to read the producer's published index — classic acquire/release handoff pattern, avoiding full `seq_cst` cost.

### What does atomic::compare_exchange_strong do, and why is the "weak" variant (compare_exchange_weak) sometimes preferred?
- Company: unknown/general (quantt.co.uk worked-examples set)
- Role: Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: `compare_exchange_strong` retries internally to rule out spurious failure; `compare_exchange_weak` may fail spuriously (e.g., on LL/SC architectures) even when the comparison would have succeeded, but is cheaper per call — preferred inside a loop (e.g., CAS-retry loops) where a spurious failure just costs one extra iteration, since the loop already handles failure.

### What's the ABA problem in lock-free programming, and how do you avoid it?
- Company: unknown/general (quantt.co.uk worked-examples set; also generic across nearly every HFT-prep source found)
- Role: Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: A CAS-based algorithm reads value A, gets preempted, another thread(s) change it A→B→A, then the original thread's CAS succeeds thinking nothing changed — but intermediate state (e.g., a freed/reallocated node) may have been invalid. Mitigations: tagged pointers / version counters (pack a monotonically incrementing counter alongside the pointer so A-then-back-to-A still has a different tag), hazard pointers, or epoch-based reclamation (e.g., RCU-style).

### When would you use hazard pointers instead of garbage collection or reference counting?
- Company: unknown/general (quantt.co.uk worked-examples set)
- Role: Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: Hazard pointers let a thread "announce" it's using a node so a reclaiming thread won't free it, giving safe memory reclamation without pausing the world (unlike tracing GC) and without the cache-contention/ABA-adjacent overhead of atomic refcounting on every access — used in lock-free data structures (queues, stacks) where nodes must be freed safely amid concurrent readers.

### Compare and contrast mutexes, semaphores, and condition variables
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: quantlabsnet.com — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: Framed generically as "expect" this in HFT interviews; no company attribution or real transcript given.

### Implement a lock-free queue (general prompt, not SPSC-specific)
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: quantlabsnet.com — https://www.quantlabsnet.com/post/how-to-ace-the-hardest-c-interview-questions-in-hft
- Answer/Discussion: Described as "a classic HFT question" requiring CAS, atomics, and memory-ordering knowledge; no verbatim transcript or company name given.

### When is acquire/release sufficient, and when do you need stronger (seq_cst) ordering? Explain using a producer/consumer example.
- Company: unknown/general (framed as HRT-style prep, not confirmed verbatim)
- Role: Core Developer (HRT track)
- Type: Unknown
- Status: PRACTICE
- Source: hackerprep.io — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: Acquire/release is sufficient whenever you only need a happens-before edge between exactly the release-store and the matching acquire-load (e.g., single flag publishing a buffer, single-writer/single-reader handoff); seq_cst is needed when multiple atomics' relative order must be seen consistently by all threads (e.g., Dekker/Peterson-style mutual exclusion built from independent atomics, or when reasoning "if thread A saw X, could it also fail to see Y").

### Explain false sharing and how you'd detect it (symptoms, counters, flamegraph hints) before "fixing" it
- Company: unknown/general (HRT-style prep)
- Role: Core Developer
- Type: Unknown
- Status: PRACTICE
- Source: hackerprep.io — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: Symptoms: throughput doesn't scale (or gets worse) as more threads/cores are added despite low apparent contention; perf counters show high `L1-dcache-load-misses` / cache-to-cache transfer events on specific lines; fix only after confirming via profiler (e.g., `perf c2c`, VTune) rather than blindly padding everything.

### Mutex vs spinlock tradeoffs — why can spinlocks hurt tail latency?
- Company: unknown/general (HRT-style prep)
- Role: Core Developer
- Type: Unknown
- Status: PRACTICE
- Source: hackerprep.io — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: Spinlocks avoid syscall/context-switch overhead when contention is brief, which helps average latency, but under real contention or if the holder is preempted, waiters burn CPU busy-waiting and can create priority-inversion / convoying effects that blow out tail latency — mutexes (which park the thread) trade a bit of average latency for much better worst-case behavior under contention.

### How would you redesign a shared queue that becomes a throughput bottleneck at peak load?
- Company: unknown/general (HRT-style prep)
- Role: Core Developer
- Type: Unknown
- Status: PRACTICE
- Source: hackerprep.io — https://hackerprep.io/blog/hrt-low-latency-cpp-system-design-prep
- Answer/Discussion: Discussion points: shard the queue per consumer/producer to reduce contention, move to single-writer/single-reader design where possible, replace mutex-protected queue with a lock-free SPSC/MPSC ring buffer, batch dequeues to amortize synchronization cost.

### Explain the difference between concurrency and parallelism / What is a race condition and how do you prevent it / Explain deadlocks and prevention strategies (Coffman conditions) / Describe lock-free and wait-free data structures / How does the C++ memory model affect concurrent programming? / Explain the producer-consumer pattern / Explain linearizability / How do you design a thread-safe cache or concurrent task scheduler?
- Company: unknown/general
- Role: Senior Engineer (generic)
- Type: Unknown
- Status: PRACTICE
- Source: Algoroq — https://www.algoroq.io/interview-questions/concurrency/
- Answer/Discussion: Listicle of 15 generic concurrency interview questions spanning race conditions, deadlocks (Coffman conditions / breaking circular wait), lock-free/wait-free structures (CAS, ABA problem), memory models (happens-before), producer-consumer (blocking queues, channels, lock-free ring buffers), linearizability, and concurrent scheduler/cache design. No company attribution; explicitly generic prep content, not language-specific to C++ (mentions Java/Go/C++ memory models interchangeably).

### Design a thread-safe hash map for read-heavy workloads
- Company: unknown/general (quantt.co.uk worked-examples set)
- Role: Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: quantt.co.uk — https://www.quantt.co.uk/resources/quant-developer-interview-questions
- Answer/Discussion: Approaches discussed: reader-writer locks at the bucket level, lock-free open addressing with atomic CAS on slots, or RCU (read-copy-update) style patterns for read-mostly workloads.

### Design/implement a "Safe Vector" using lock-free / persistent-data-structure techniques for memory efficiency
- Company: unknown/general (WallStreetCPP-sourced, per techinterview.org)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233474597/cpp-quant-interviews/
- Answer/Discussion: Article suggests attempting this problem using lock-free techniques as an extension exercise; no verbatim transcript or company confirmation given.

### What strategies can be used to minimize latency in HFT systems?
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233474597/cpp-quant-interviews/
- Answer/Discussion: Open-ended discussion question mentioned without a model answer in the source; typically expects coverage of lock-free data structures, kernel bypass, cache-friendly layouts, and avoiding syscalls/allocations on the hot path.

### General topic confirmation: HFT interviews test "multithreading with use of atomics, locks, and semaphores" and "lock-free programming using atomics" as core hard C++ topics
- Company: unknown/general (multiple unnamed HFT firms per poster)
- Role: SWE / Quant Developer
- Type: Interview (topic-level, not a single verbatim question)
- Status: REAL
- Source: teamblind.com — https://www.teamblind.com/post/How-to-clear-HFT-interviews-fxq1f8SR ; https://www.teamblind.com/post/c-books-for-breaking-into-hft-tmz64md1
- Answer/Discussion: Posters (claiming HFT interview experience) list "metaprogramming/compile-time programming," "multithreading with atomics/locks/semaphores," and "lock-free programming using atomics" as the hardcore C++ areas most HFT firms probe; CppCon talks recommended as prep for lock-free/atomics specifically. Companies referenced in the surrounding thread ecosystem: Jump Trading, Citadel, Eclipse Trading, Akuna Capital, Chicago Trading Company (per a related thread, teamblind.com/post/Teaching-for-HFT-SWE-interviews-YbkNFS5P), though no single verbatim question tied to one firm was captured.

### Atomics, Lock-free/Wait-free Implementations, Priority Queues, Contention Detection in Multithreaded code (topic area named by a candidate preparing for "close-to-the-metal" low-latency interviews)
- Company: unknown/general (poster preparing for unnamed low-latency trading firms)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: teamblind.com — https://www.teamblind.com/post/close-to-the-metal-optimization-techniques-for-low-latency-systems-cadvnupm
- Answer/Discussion: none found — thread is a question asking which teams focus on this, not a report of an actual asked question.
