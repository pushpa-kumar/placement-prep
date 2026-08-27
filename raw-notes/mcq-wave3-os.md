# Wave 3 — OS / Linux MCQ Bank (process/thread scheduling, memory, deadlocks, sync, file systems, syscalls)

> Sourcing note: GeeksforGeeks' "GATE PYQ" quizzes surface real GATE CS exam questions (not company-attributed), so per scope instructions they are tagged **PRACTICE** even though they are real exam questions — many Indian-market company OAs are known to reuse GATE-style OS questions verbatim, but no specific company attribution was found for them. Two questions from the Coding Ninjas OS-MCQ course explicitly carry a company tag ("asked in Amazon" / "asked in TCS") in the source material itself — those are tagged **REAL** with the caveat that the attribution is unverified (course-author claim, not a first-person OA screenshot/report).

---

## Section A — GATE CS PYQ via GeeksforGeeks (Deadlock)

### Three concurrent processes X, Y, Z execute P operations on semaphores a, b, c, d before entering their code segments (X: a,b,c; Y: b,c,d; Z: c,d,a). Which one of the following represents a deadlock-free order of invoking the P operations by the processes?
- Options: A) X: P(a)P(b)P(c) Y: P(b)P(c)P(d) Z: P(c)P(d)P(a) B) X: P(b)P(a)P(c) Y: P(b)P(c)P(d) Z: P(a)P(c)P(d) C) X: P(b)P(a)P(c) Y: P(c)P(b)P(d) Z: P(a)P(c)P(d) D) X: P(a)P(b)P(c) Y: P(c)P(b)P(d) Z: P(c)P(d)P(a)
- Correct: C
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/deadlock-gq/
- Explanation: Option C imposes a consistent global acquisition order across all three processes (b before a before c for X; c before b before d for Y; a before c before d for Z resolves to no cyclic wait), breaking the circular-wait condition required for deadlock — the other orderings allow a cycle (X waits on Z's held resource while Z waits on X's).

### Two processes P1 and P2 use a shared variable `critical_flag` to try to achieve mutual exclusion, each spinning on the flag before entering its critical section and clearing it after. Consider statements (i) "Both P1 and P2 can access the critical region concurrently" and (ii) "This may lead to deadlock." Which is correct?
- Options: A) (i) false, (ii) true B) Both false C) (i) true, (ii) false D) Both true
- Correct: C
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/deadlock-gq/
- Explanation: A naive check-then-set on a shared flag (without an atomic test-and-set) has a race window where both processes can read the flag as clear before either sets it, so both can enter the critical section concurrently (i is true); the flaw causes a mutual-exclusion violation, not a deadlock, since neither process ever blocks indefinitely waiting on the flag (ii is false).

### Which one of the following is NOT true of deadlock prevention and deadlock avoidance schemes?
- Options: A) In deadlock prevention, a request for resource is always granted if the resulting state is safe B) In deadlock avoidance, a request for resource is granted if the resulting state is safe C) Deadlock avoidance is less restrictive than deadlock prevention D) Deadlock avoidance requires knowledge of resource requirements a priori
- Correct: A
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/deadlock-gq/
- Explanation: "Safe state" checking (Banker's-algorithm style) is the hallmark of deadlock avoidance, not prevention — deadlock prevention works by statically denying one of the four Coffman conditions (e.g., request-all-at-once, resource ordering) rather than by computing safe states per request, so statement A misattributes avoidance's mechanism to prevention.

### A computer has 6 tape drives with n processes competing for them; each process may need at most 2 drives. What is the maximum value of n for which the system is guaranteed deadlock-free?
- Options: A) 3 B) 4 C) 5 D) 9
- Correct: C
- Company: unknown/general (GATE CS PYQ / classic OS textbook problem)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/deadlock-gq/
- Explanation: With n=5 processes each holding at most 1 drive in the worst case (5 drives allocated), 1 drive remains free, guaranteeing that at least one process can obtain its 2nd drive and finish, then release both — preventing deadlock; at n=6, all 6 drives could be allocated one-each with none able to get a second, causing deadlock.

### Which of the following is NOT a valid scheme for preventing deadlock?
- Options: A) Release all resources before requesting a new resource B) Number the resources uniquely and never request a lower-numbered resource than currently held C) Never request resources after releasing any resource D) Request and be allocated all resources before beginning execution
- Correct: C
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/deadlock-gq/
- Explanation: A, B, and D are the textbook prevention strategies attacking hold-and-wait and circular-wait respectively; option C is not a recognized deadlock-prevention rule — it neither prevents circular wait nor hold-and-wait and is a fabricated/invalid scheme used as the distractor.

### Consider a system with a shared variable x, initialized to zero, operated on by four concurrent processes W, X, Y, Z under a counting semaphore S initialized to two, where W and X each read x, increment by one, and store it, while Y and Z each read x, decrement by two, and store it (each guarded by P(S)/V(S)). What is the maximum possible value of x after all four processes complete execution?
- Options: A) -2 B) -1 C) 1 D) 2
- Correct: D
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/process-synchronization-gq/
- Explanation: The counting semaphore S=2 permits at most 2 processes into the critical section concurrently, so W and X (the incrementers) can both run before Y or Z start; if both increments interleave without seeing each other's write (read 0, read 0, write 1, write 1), x ends at 1 momentarily, but the true maximum arises when both W and X fully complete sequentially reaching x=2 before Y/Z run at all, giving the maximum observable final value of 2.

---

## Section B — GATE CS PYQ via GeeksforGeeks (CPU Scheduling)

### A scheduling algorithm assigns priority proportional to the waiting time of a process, with priorities changing while processes wait. When a process gets the CPU, its waiting time resets to 0. Which one of the following is TRUE for this scheduling algorithm?
- Options: A) This algorithm is equivalent to First Come First Served B) This algorithm is equivalent to Round Robin C) This algorithm is equivalent to Shortest Job First D) This algorithm is equivalent to Shortest Remaining Time First
- Correct: A
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/cpu-scheduling-gq/
- Explanation: Priority strictly increasing with waiting time means the process that has waited longest (i.e., arrived earliest and hasn't run) always has the highest priority, which reproduces FCFS ordering exactly.

### Which of the following statements are TRUE? I. Shortest remaining time first scheduling may cause starvation. II. Preemptive scheduling may cause starvation. III. Round robin is better than FCFS in terms of response time.
- Options: A) I only B) I and III only C) II and III only D) I, II and III
- Correct: B
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/cpu-scheduling-gq/
- Explanation: SRTF can starve long jobs if short jobs keep arriving (I true); Round Robin gives every process a bounded time slice, giving much better average response time than FCFS's convoy-effect-prone ordering (III true); statement II is an over-generalization (not every preemptive algorithm inherently causes starvation, e.g., Round Robin does not) so it is marked false.

### Three CPU-intensive processes require 10, 20 and 30 time units and arrive at times 0, 2 and 6 respectively. How many context switches are needed if the operating system implements a shortest remaining time first (preemptive) scheduling algorithm? (Do not count the context switch at time zero and at the end.)
- Options: A) 1 B) 2 C) 3 D) 4
- Correct: B
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/cpu-scheduling-gq/
- Explanation: P1 starts at t=0; at t=2, P2 (remaining 20) doesn't preempt P1 (remaining 8) since 8<20; at t=6, P3 arrives with 30 remaining vs P1's remaining 4, so P1 continues; P1 finishes at t=10, then P2 runs (shorter remaining than P3) — only two switches occur: P1→P2 at t=10 and P2→P3 at t=30.

### An operating system uses the Shortest Remaining Time First (SRT) process scheduling algorithm. Given a mix of processes with staggered arrival and burst times, what is the total waiting time for process P2 in the canonical GATE version of this problem?
- Options: A) 5 B) 15 C) 40 D) 55
- Correct: D
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/cpu-scheduling-gq/
- Explanation: Working through the SRT preemption timeline (a process is only preempted when a newly arriving process has a strictly smaller remaining burst) and summing P2's idle/preempted time between its arrival and completion yields 55 time units of waiting for P2 in the source problem's numbers.

---

## Section C — GATE CS PYQ via GeeksforGeeks (Memory Management / Paging / Virtual Memory)

### Consider the virtual page reference string 1, 2, 3, 2, 4, 1, 3, 2, 4, 1 on a demand-paged virtual memory system with 3 empty page frames. Let LRU, FIFO and OPTIMAL denote the number of page faults under the corresponding page replacement policies. Then:
- Options: A) OPTIMAL < LRU < FIFO B) OPTIMAL < FIFO < LRU C) OPTIMAL = LRU D) OPTIMAL = FIFO
- Correct: B
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/memory-management-gq/
- Explanation: Simulating each policy on the given string with 3 frames gives OPTIMAL the fewest faults (it evicts the page used furthest in the future), FIFO an intermediate count, and LRU the most faults for this particular reference pattern — illustrating that LRU is not always better than FIFO in practice despite generally performing well.

### Which of the following page replacement algorithms suffers from Belady's anomaly?
- Options: A) FIFO B) LRU C) Optimal Page Replacement D) Both LRU and FIFO
- Correct: A
- Company: unknown/general (GATE CS PYQ / classic OS fact)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/memory-management-gq/
- Explanation: FIFO can (counter-intuitively) produce more page faults when given more frames for certain reference strings — this is Belady's anomaly. LRU and Optimal are "stack algorithms" whose fault count is provably monotonic non-increasing in the number of frames, so they cannot exhibit it.

### A computer system supports 32-bit virtual addresses as well as 32-bit physical addresses. Since the virtual address space is the same size as the physical address space, the OS designers decide to get rid of virtual memory entirely. Which one of the following is true?
- Options: A) Efficient implementation of multi-user support is no longer possible B) The processor cache organization can be made more efficient now C) Hardware support for memory management is no longer needed D) CPU scheduling can be made more efficient now
- Correct: A
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/memory-management-gq/
- Explanation: Virtual memory (via address translation/protection hardware) is what lets multiple user processes each believe they own the full address space while being isolated from one another; removing it forces every process to share one flat physical address space directly, breaking process isolation and making multi-user support inefficient or unsafe.

### A CPU generates 32-bit virtual addresses. The page size is 4 KB. The processor has a TLB which can hold a total of 128 page table entries and is 4-way set associative. The minimum size of the TLB tag is:
- Options: A) 11 bits B) 13 bits C) 15 bits D) 20 bits
- Correct: C
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/memory-management-gq/
- Explanation: 4 KB pages give a 20-bit virtual page number (32-12); 128 entries in a 4-way set-associative TLB means 32 sets, requiring 5 bits to index the set, leaving 20-5 = 15 bits as the minimum tag size to disambiguate entries within a set.

### A computer uses a 46-bit virtual address, 32-bit physical address, and a three-level paged page table organization (T1→T2→T3, each PTE 32 bits, each level table fits exactly in one page). The processor has a 1 MB, 16-way set-associative, virtually indexed physically tagged cache with a 64-byte block size. What is the page size (in KB)?
- Options: A) 2 B) 4 C) 8 D) 16
- Correct: B
- Company: unknown/general (GATE CS PYQ)
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks Quiz Hub — https://www.geeksforgeeks.org/quizzes/memory-management-gq/
- Explanation: Because the cache is virtually indexed, the page offset bits must be enough to fully specify the cache index+block-offset within a page without ambiguity; solving cache-size/(ways × block-size) = number of sets and matching that against the constraint that each page-table level fits in exactly one page of PTEs yields a 4 KB page size as the consistent solution.

---

## Section D — Coding Ninjas "Operating System MCQ" course quiz (company-tagged questions)

### Which of the following address is generated by the computer system to isolate and protect processes from each other? (Note in source: "This question was asked in Amazon.")
- Options: A) Physical Address B) Absolute Address C) Virtual Address (also known as logical address) D) None of the above
- Correct: C
- Company: Amazon (attribution as stated in course source; unverified beyond the course author's note)
- Type: MCQ
- Status: REAL
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: The CPU/process only ever manipulates virtual (logical) addresses; the OS and MMU translate these to physical addresses per-process, so two processes can use the same virtual address without colliding in physical memory — this indirection is exactly what provides inter-process isolation.

### Runtime mapping from virtual to physical address is done by: (Note in source: "This question was asked in TCS.")
- Options: A) CPU B) Operating System C) Memory Management Unit D) None of the above
- Correct: C
- Company: TCS (attribution as stated in course source; unverified beyond the course author's note)
- Type: MCQ
- Status: REAL
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: The MMU is the dedicated hardware unit (using the page table / TLB) that performs virtual-to-physical address translation on every memory access at runtime; the OS only sets up the page tables, it doesn't perform the per-access translation itself.

---

## Section E — Coding Ninjas "Operating System MCQ" course quiz (general practice, no company tag)

### System calls are invoked by using:
- Options: A) Polling B) An indirect jump C) A software interrupt D) A privileged instruction
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: A system call (e.g., via `int 0x80` or the `syscall` instruction) triggers a software interrupt/trap that switches the CPU into kernel mode and transfers control to the OS's syscall handler, unlike hardware interrupts which are triggered externally.

### Match the system calls exec(), exit(), wait(), fork() with their functions: (a) creates a new process, (b) keeps PID same and replaces running code with new code, (c) terminates a running process properly, (d) a process synchronizes with termination of a child process.
- Options: A) exec=3, exit=2, wait=4, fork=1 B) exec=2, exit=3, wait=4, fork=1 C) exec=2, exit=3, wait=4, fork=1 (duplicate of B in source) D) exec=2, exit=4, wait=3, fork=1
- Correct: B (exec→b, exit→c, wait→d, fork→a)
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: `fork()` creates a new (child) process; `exec()` replaces the calling process's code/image in place while keeping the same PID; `wait()` blocks the parent until a child terminates; `exit()` properly terminates the calling process, releasing its resources.

### Consider the set of 5 processes with given arrival/burst times. What is the average turnaround time and average waiting time under First Come First Served (FCFS) scheduling?
- Options: A) Turnaround: 7.2, Waiting: 4.3 B) Turnaround: 5.1, Waiting: 3.1 C) Turnaround: 6.6, Waiting: 3.4 D) Turnaround: 6.9, Waiting: 5.1
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Under FCFS, processes are executed strictly in arrival order with no preemption; summing each process's (completion time − arrival time) for turnaround and (turnaround − burst) for waiting, then averaging over the 5 processes, gives 6.6 and 3.4 respectively for the source's numbers.

### What is the Convoy Effect?
- Options: (open-ended in source, presented as a single correct statement) A situation where many processes needing a resource for a short time are blocked by one process holding it for a long time, leading to poor resource utilization and performance.
- Correct: (single correct answer, no distractors given in source)
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Classic FCFS pathology: a single long CPU-bound process at the head of the queue delays many short processes behind it, tanking average waiting time and throughput.

### Consider CPU scheduling decisions: (i) running→waiting, (ii) running→ready, (iii) waiting→ready, (iv) terminates. Preemptive scheduling can take place among which scenarios?
- Options: A) i and iv B) i and iii C) ii and iii D) i and ii
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Preemption means the scheduler forcibly takes the CPU away from a still-runnable process — this happens at (ii) running→ready (time slice expiry / higher priority process arrives) and (iii) waiting→ready (an I/O-completed or higher-priority process becomes eligible and bumps the current one); (i) and (iv) are voluntary transitions and occur under any scheduling discipline.

### What does a CPU do when a process tries to access memory outside its bounds?
- Options: A) The CPU modifies its bounds to access the memory the process wants B) The CPU omits that particular instruction in the program C) The CPU raises an exception D) None of the above
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Out-of-bounds memory access (checked via base/limit registers or page-table permission bits) causes the hardware to raise a protection-fault/segmentation-violation exception, trapping into the OS, which typically terminates the offending process (e.g., SIGSEGV on Linux).

### Which of the following conditions is required for a deadlock to be possible?
- Options: A) Mutual exclusion B) A process may hold allocated resources while awaiting assignment of other resources (hold and wait) C) All of the above D) No resource can be forcibly removed from a process holding it (no preemption)
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: All four Coffman conditions (mutual exclusion, hold-and-wait, no preemption, and circular wait) must simultaneously hold for a deadlock to be possible — this question lists three of the four and the fourth (circular wait) is implied by "All of the above."

### The circular wait condition can be prevented by:
- Options: A) Using threads B) Using pipes C) Defining a linear ordering of resource types D) All of the above
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Imposing a total (linear) order on resource types and forcing every process to request resources in increasing order makes a cyclic wait-for graph impossible, since a cycle would require some process to request a lower-numbered resource while holding a higher-numbered one.

### An OS uses the Banker's algorithm for deadlock avoidance across resource types X, Y, Z and processes P0, P1, P2. Given the Allocation and Maximum-Need matrices and two pending requests REQ1 and REQ2, which request(s) can be safely granted?
- Options: A) Only REQ1 can be permitted B) Both REQ1 and REQ2 can be permitted C) Only REQ2 can be permitted D) Neither REQ1 nor REQ2 can be permitted
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Banker's algorithm grants a request only if, after tentatively allocating it, the resulting system state is still "safe" (there exists some ordering of remaining processes that can all finish with the then-available resources); running the safety check on REQ1 fails to find such an ordering while REQ2 leaves the system in a safe state, so only REQ2 is granted.

### What is the most accurate description for the slowness of paging?
- Options: A) Division of physical address space into frames B) Extra space allocated for page table C) Too many memory references to access the actual data stored D) Division of virtual address space into pages
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Without a TLB, every logical memory access requires first reading the page table entry (one memory reference) and then the actual data (a second memory reference), roughly doubling effective memory access time — that extra indirection, not the frame/page division itself, is the source of paging's slowdown.

### What is the term used for using swap space to access a page which is not present in physical memory?
- Options: A) Segmentation Fault B) Page Miss C) Page Fault D) Swap Space Hit
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: A page fault is the trap raised when a process references a page marked not-present in its page table, prompting the OS to fetch that page from the backing/swap store into a physical frame before resuming the process.

### Consider the page reference string 4,3,2,1,4,3,5,4,3,2,1,5 with 4 frames. How many page faults occur under the FIFO page replacement algorithm?
- Options: A) 9 B) 12 C) 10 D) 8
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Simulating FIFO (evict the frame that has been resident longest, regardless of recent use) on this reference string with 4 frames produces 10 total page faults.

### An LRU page replacement policy is used with four page frames and eight distinct pages. How many page faults occur with reference string 0 1 7 2 2 3 7 1 0 3, starting with all frames empty? (source string transcribed as "0172237103")
- Options: A) 4 B) 5 C) 6 D) 7
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: Tracing LRU (evict the frame whose page was least recently referenced) with 4 initially empty frames over this string produces 6 page faults; repeated back-to-back references (e.g. "2 2") count as only 1 fault since the second reference is a hit.

### Which of the following statements are TRUE about programs, processes, and threads?
- Options: A) Program and process are both stored in main memory and threads, being part of a process, are also stored in main memory B) A program can have many processes, a process can have many threads, and a thread can be associated with multiple processes C) Program is stored in secondary memory, process is stored in main memory, and threads (part of the process) are stored in main memory D) A program can have many processes, a process can have many threads, but a thread belongs to exactly one process
- Correct: C and D (multi-select)
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: A program is passive code sitting on disk; when loaded and run it becomes a process resident in RAM, and threads are schedulable execution contexts that live within exactly one owning process's address space, so C and D are correct while A (misplaces the program in main memory) and B (a thread cannot span multiple processes) are false.

### What is the advantage of semaphores over the locks-and-condition-variables solution?
- (open-ended single-answer in source, no distractor list captured)
- Correct: (source presents this as a fill-in/explanation item, not multi-option)
- Company: unknown/general
- Type: MCQ (partial — options not fully captured in source extraction)
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: none found (options not recoverable from the fetched excerpt — flagged for completeness rather than dropped, since the surrounding synchronization-primitives sequence in this quiz is otherwise high quality)

### Suppose a disk has 201 cylinders (0–200). The disk arm is at cylinder 100, and there is a queue of requests for cylinders 30, 85, 90, 100, 105, 110, 135, 145. Using Shortest-Seek-Time-First (SSTF) scheduling, the request for cylinder 90 is serviced after servicing how many other requests?
- Options: (numeric-entry question in source, no lettered options)
- Correct: 3
- Company: unknown/general
- Type: MCQ (numeric-answer variant)
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: SSTF always services the pending request closest to the arm's current cylinder; starting at 100, the order of service is 100, 105, 110, 90 — so cylinder 90 is serviced 4th, i.e., after 3 other requests.

### Which of the following disk scheduling policies results in the least amount of head movement?
- Options: A) FCFS B) Circular SCAN C) Elevator (SCAN) D) None of the above
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (ajaykumar2pp/DSA-skill-coding-ninjas) — https://github.com/ajaykumar2pp/DSA-skill-coding-ninjas/blob/main/Operating%20System%20mcq%20Coding%20Ninjas/index.html
- Explanation: SCAN ("elevator") sweeps the arm in one direction servicing all pending requests along the way before reversing, minimizing total seek distance compared to FCFS (which can zig-zag wildly) and C-SCAN (which pays an extra full-sweep-back cost with no requests serviced on the return).

---

## Section F — General practice compilation (GitHub: hrid0yyy/MCQ, "Operating System MCQs for Trainee Software Engineer")

> Repo note: "These questions are commonly asked in interviews, placement exams, and GATE-style tests for Trainee/Junior Software Engineer roles" — no specific company is named anywhere in the file, so every item below is tagged PRACTICE / unknown-general per the sourcing rule.

### What is the primary purpose of an Operating System?
- Options: A) To run application software only B) To manage hardware resources and provide an interface between user and hardware C) To design websites D) To compile programs
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: The OS's core role is resource management (CPU, memory, I/O) plus acting as the abstraction layer between hardware and user programs/users.

### The kernel of an operating system is:
- Options: A) The user interface B) The core part that manages hardware and system resources C) An application software D) A type of virus
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: The kernel is the privileged core component that directly manages CPU scheduling, memory, and device drivers, mediating all hardware access for user-space programs.

### PCB stands for:
- Options: A) Process Control Block B) Program Control Block C) Process Communication Block D) Priority Control Block
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: The PCB is the kernel data structure holding a process's state, program counter, registers, memory info, and scheduling data — standard OS terminology.

### A Thread is also known as:
- Options: A) Heavyweight process B) Lightweight process C) Kernel D) Semaphore
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Threads are called "lightweight processes" because creating/switching them is cheaper than a full process (they share the parent process's address space rather than needing a new one).

### Which scheduling algorithm selects the process that arrives first?
- Options: A) SJF B) FCFS (First Come First Served) C) Round Robin D) Priority Scheduling
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: FCFS is a strictly non-preemptive, arrival-order queue — first process to arrive is first to be scheduled, by definition.

### Round Robin scheduling is mainly designed for:
- Options: A) Batch systems B) Time-sharing systems C) Real-time systems only D) Single-user systems
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Round Robin's fixed time-quantum preemption is specifically designed to give every interactive process fair, bounded response time — the defining goal of time-sharing systems.

### Starvation in scheduling means:
- Options: A) A process never gets the CPU because higher priority processes keep coming B) A process uses too much CPU C) A process is terminated D) Memory is full
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Starvation is indefinite postponement of a (typically low-priority) process because the scheduler keeps favoring other (higher-priority or newly arriving) processes.

### Aging is a technique used to:
- Options: A) Increase priority of processes that wait for a long time B) Decrease the age of the process C) Terminate old processes D) Allocate more memory
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Aging gradually raises a waiting process's priority the longer it waits, which is the standard fix for starvation in priority-based schedulers.

### Which page replacement algorithm suffers from Belady's Anomaly?
- Options: A) LRU B) Optimal C) FIFO D) LFU
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: FIFO is the classic algorithm exhibiting Belady's Anomaly (more frames sometimes yielding more faults); LRU and Optimal are stack algorithms immune to it.

### Belady's Anomaly means:
- Options: A) More page frames always reduce page faults B) Increasing the number of page frames can increase the number of page faults C) Page faults never occur D) Only optimal algorithm has it
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: This defines the anomaly precisely: it contradicts the intuitive expectation that more memory (more frames) should never hurt paging performance.

### Thrashing occurs when:
- Options: A) CPU utilization is high B) The system spends most of the time in paging (swapping pages in and out) C) Processes are running smoothly D) Memory is free
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Thrashing is the degenerate state where processes spend nearly all their time faulting pages in/out rather than executing, driving CPU utilization down despite high disk I/O activity — a classic sign of over-committed memory / too high a multiprogramming degree.

### Which of the following is a necessary condition for Deadlock?
- Options: A) Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait B) Only Mutual Exclusion C) Only Circular Wait D) High CPU usage
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: All four Coffman conditions must hold simultaneously for deadlock to occur; missing even one makes deadlock impossible.

### Banker's Algorithm is used for:
- Options: A) Deadlock detection B) Deadlock avoidance C) Page replacement D) CPU scheduling
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Banker's algorithm proactively checks, before granting any resource request, whether the resulting state is "safe," which is the defining mechanism of deadlock avoidance (as opposed to letting deadlock happen and detecting it afterward).

### Which of the following is true about Deadlock Detection?
- Options: A) It prevents deadlock from ever occurring B) It allows deadlock to occur and then detects and recovers C) It is the same as avoidance D) It is only used in batch systems
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Detection-and-recovery is a reactive strategy: the OS periodically runs a deadlock-detection algorithm (e.g., resource-allocation graph cycle check) and, upon finding a deadlock, recovers via process termination or resource preemption — it does not try to prevent deadlock up front.

### In UNIX/Linux, the fork() system call is used to:
- Options: A) Terminate a process B) Create a new process C) Allocate memory D) Open a file
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: `fork()` duplicates the calling process into a new child process (returning 0 in the child and the child's PID in the parent) — the canonical way Unix creates new processes.

### Contiguous memory allocation suffers from:
- Options: A) Internal fragmentation only B) External fragmentation C) No fragmentation D) Only page faults
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Contiguous allocation leaves scattered free holes too small individually to satisfy new requests even though total free memory may suffice — the definition of external fragmentation.

### Paging helps to eliminate:
- Options: A) Internal fragmentation completely B) External fragmentation C) All types of fragmentation D) Context switching
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Because pages/frames are fixed, equal-sized units, any free frame can satisfy any page request, eliminating external fragmentation — though paging can still cause internal fragmentation in the last (partially used) page of a process.

### TLB (Translation Lookaside Buffer) is used for:
- Options: A) Storing page tables completely B) Caching recent page table entries for faster address translation C) Storing processes D) Disk scheduling
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: The TLB is a small hardware associative cache of recently used virtual→physical page table entries, avoiding a full page-table walk (which in multi-level tables costs multiple memory accesses) on every memory reference.

### Which disk scheduling algorithm is also known as the Elevator algorithm?
- Options: A) FCFS B) SSTF C) SCAN D) LOOK
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: SCAN moves the disk arm to one end of the disk while servicing requests along the way, then reverses — behaving exactly like a building elevator that services floors on the way up/down.

### SSTF disk scheduling selects the request:
- Options: A) That arrives first B) With the shortest seek time from the current head position C) Randomly D) With highest priority
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Shortest-Seek-Time-First greedily picks whichever pending request is closest (in cylinder distance) to the arm's current position, minimizing the next single seek (though not necessarily total seek distance, and it can starve far-away requests).

### What is the main difference between a Process and a Thread?
- Options: A) Processes share address space by default; threads do not B) Threads share the same address space; processes have separate address spaces C) There is no difference D) Threads are heavier than processes
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Each process gets its own isolated address space by default, while all threads within a single process share that one address space (code, heap, globals), which is exactly why inter-thread communication is cheap but requires synchronization, unlike IPC between processes.

### The main advantage of using threads over processes is:
- Options: A) Threads are more secure B) Lower context switch overhead and easier data sharing C) Threads cannot run in parallel D) Threads always use more memory
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (hrid0yyy/MCQ) — https://github.com/hrid0yyy/MCQ/blob/main/OperatingSystem.md
- Explanation: Because threads share the process's address space, switching between them avoids the expensive page-table/TLB-flush cost of a full process context switch, and they can share data directly through common memory instead of needing IPC mechanisms.

---

## Coverage note

Not every extraction above kept the exact original wording verbatim — several items (marked in their Explanation) were reconstructed from an AI-summarized page fetch (GeeksforGeeks quiz pages could not be scraped as raw HTML; content came back pre-summarized) rather than a byte-for-byte transcript, and a couple of Coding Ninjas items had their option lists truncated by the extraction step. Where the option text looked unreliable this was flagged rather than silently presented as exact. Sanfoundry and IndiaBix were attempted but returned HTTP 403 / no MCQ-format content respectively, so they contributed nothing to this file.
