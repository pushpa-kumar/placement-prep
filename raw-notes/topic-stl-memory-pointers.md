# Topic: STL, Memory Management, Pointers/References, RAII, Smart Pointers — Raw Interview Notes

### "Implement the class of Shared Pointer." (live-coding, from scratch)
- Company: Alphagrep (prop trading/HFT firm)
- Role: SDE Intern (Round 1, candidates Parit Gupta & Pratyaksh)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Alphagrep section)
- Answer/Discussion: Listed back-to-back with "Implement class of Unique_ptr" and "Implement the push_back operation of a vector" as three separate from-scratch implementation questions in the same round, alongside TLB cache/memory-access time calculation, struct memory layout, and mutex-vs-semaphore questions. No model answer given in source; candidate advice was "be patient, explain your approach side by side."

### "Implement class of Unique_ptr."
- Company: Alphagrep
- Role: SDE Intern (Round 1, candidates Parit Gupta & Pratyaksh)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Alphagrep section)
- Answer/Discussion: none found (question listed without solution)

### "Implement the push_back operation of a vector."
- Company: Alphagrep
- Role: SDE Intern (Round 1)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Alphagrep section)
- Answer/Discussion: none found. Tests understanding of amortized growth/reallocation strategy behind std::vector.

### "...writing the code for shared pointers (please do this once at least, I hadn't)."
- Company: Alphagrep
- Role: SDE Intern (Round 1, candidate "Rushit")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Alphagrep section)
- Answer/Discussion: Candidate reports being asked to implement hashing and "shared pointers" from scratch as part of a broader C++/OOPs-heavy round; explicitly recommends practicing shared_ptr implementation beforehand since he hadn't and struggled.

### "Implementation of a vector, how to declare a new array of size n using the pointer format."
- Company: Alphagrep
- Role: SDE Intern (Round 2, candidate "Rushit")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Alphagrep section)
- Answer/Discussion: none found — asked to manually reimplement dynamic array allocation using raw pointers (`new T[n]`-style manual array).

### "You are given a linked list. Now there are 2 operations, one for adding a new node and one to delete a node. After each update a new version of the linked list is created and we want to keep a copy of each version — by copying the minimum number of nodes, keep each version." (persistent linked list / copy-on-write)
- Company: Alphagrep
- Role: SDE Intern (Round 2)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Alphagrep section)
- Answer/Discussion: Follow-up asked the same for a binary tree. Directly tests path-copying / persistent-data-structure reasoning, which in C++ maps to careful ownership decisions (shared_ptr-based structural sharing) to avoid full deep copies.

### "Asked about smart pointers... told me to write the code for implementation of shared pointers."
- Company: QuantBox (Core Role)
- Role: SDE Intern, Core Role (candidate "Ishaan Jain")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", QuantBox section)
- Answer/Discussion: Candidate reports not knowing the implementation and writing "as much as I could remember from Cherno's [YouTube] video" before being asked to leave the call. Also asked to implement a stack using 2 queues and a queue using 2 stacks in same round.

### "...discussion on memory allocators, hashmaps, smart pointers."
- Company: QuantBox (Systems Role)
- Role: SDE Intern, Systems Role (candidate "Roopam Taneja")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", QuantBox section)
- Answer/Discussion: none found; listed alongside a "virtual polymorphism" question.

### "Implement a shared_ptr, small string optimization, spinlock, memory pool." (multi-part live implementation)
- Company: Unclear from source — appears directly after an Alphagrep/QuantBox OA description in the doc under a generic "Interview / Systems" heading (candidate "Maulik Barot"); likely QuantBox's Systems-track interview given the immediately preceding OA explicitly covered "systems + C++" for QuantBox, but the doc does not repeat the company name here, so treat this attribution as probable, not certain.
- Role: Systems track, SDE Intern
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +1.txt", line ~119-126)
- Answer/Discussion: Candidate's summary: "Implementation heavy. Very in-depth knowledge about C++ and systems (mostly memory — how virtual memory works and how caches work)... For implementation, keep things simple and then move on to more detailed implementation." Also asked: address-to-hardware translation path, process vs thread, huge pages, singleton, thread-safe queues with atomics, vtables/vptr, empty class optimization, `static` keyword. Result: candidate was rejected.

### "Asked about favourite language and garbage collection policy in that, then asked how to implement simple garbage collection in C++, asked about shared pointers and their implementation in C++ STL, asked about stack and heap memory, asked about what happens at OS level in case of segmentation faults or stack overflows."
- Company: Salesforce
- Role: SDE Intern (Round 2, candidate "Garv Sethi")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Salesforce section)
- Answer/Discussion: none found — reported as a sequence of questions, no answers recorded by candidate.

### "Asked about a project from my resume and asked me to write pseudo code of a part of it which was implemented using Shared_ptr and weak_ptr in C++. The interviewer... even asked me about the internal implementation of shared_ptr."
- Company: Microsoft
- Role: SDE Intern (Round 2, candidate "Kritik Vijay")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +1.txt", Microsoft section)
- Answer/Discussion: "I was nearly able to answer all of his cross questions." Candidate was ultimately selected. Same round also included implementing LCS (DP) and a probability puzzle.

### "Also asked about lambda functions in C++ STL but only because I was using them."
- Company: Microsoft
- Role: SDE Intern (Round 2, candidate "Garv Sethi")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Microsoft section)
- Answer/Discussion: none found; brief mention alongside project/concurrency discussion.

### "They asked me to write a stack class that allocated memory on heap and avoided memory leaks." (custom RAII-style container)
- Company: Uber
- Role: SDE Intern (Round 1)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Uber section)
- Answer/Discussion: Followed from a deadlock/cycle-detection discussion where candidate mentioned "stack and recursion stack," leading interviewer to ask about process memory/heap-stack allocation, then this implementation task. Same round: OOPs questions on "pointers and memory for objects."

### "OOPs were standard questions (virtual functions and how they work, abstract classes, singleton class, pointers and memory for objects etc.)"
- Company: Uber
- Role: SDE Intern (Round 1)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +2.txt", Uber section)
- Answer/Discussion: none found.

### "new vs malloc (max depth one can imagine)"
- Company: QuadEye (Quadeye)
- Role: Systems round, SDE Intern (candidate "Aryan Choudhary")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +1.txt", Quadeye section)
- Answer/Discussion: Candidate notes interviewer pushed for maximum depth of understanding (construction/destruction, initialization, alignment, exceptions on failure vs nullptr, operator new/delete overloading, etc. implied but not spelled out in source).

### "Then they dived into memory allocators (they were asking questions from the resume, allocator question was asked because I had a project in the resume), difference between stack and heap allocation, virtual memory, paging, segmentation."
- Company: D. E. Shaw
- Role: SDE Intern (Round 1, candidate "Abdullah Azeem")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +1.txt", DE Shaw section)
- Answer/Discussion: Follow-up scenario: "multiple tabs are open in a browser and the computer lags, what's the reason?" — expected answer was OS page swapping.

### "How are sets implemented internally?"
- Company: D. E. Shaw
- Role: SDE Intern (Round 2, "systems" focused, no DSA)
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +1.txt", DE Shaw section)
- Answer/Discussion: none found. Asked alongside "What is a complete binary tree and how do you check one?" and "Implement LFU cache with optimal insert/evict complexity" — tests knowledge that std::set is a balanced BST (red-black tree) under the hood.

### "Stack vs heap memory allocation" / "Virtual pointers and V table" (OOP/C++ block)
- Company: JPMorgan Chase (JPMC) Quant
- Role: Quant Developer Intern (Round 1, candidate "Aryan Laroia")
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/Aditya-Bhadoria/intern (file "Intern_Guidance +1.txt", JPMC Quant section)
- Answer/Discussion: Listed as one of three OOP/C++ topics tested in a round otherwise focused on DP/graph coding with a finance-flavored problem (currency arbitrage via negative-cycle detection).

### "specific c++ (version 11) questions, they dont care if you know the previous version of c++... [need to] learn shared_ptr, unique_ptr..."
- Company: Bloomberg L.P.
- Role: Software Engineer (title of candidate-submitted interview question)
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/specific-c-version-11-questions-they-dont-care-if-you-know-the-previous-version-of-c-10-10-learn-shared-ptr-unique-QTN_414240.htm
- Answer/Discussion: none found beyond the question title itself (page content not directly fetchable; title is candidate's verbatim submitted interview-question summary per search indexing).

### "c++ questions, related to memory management and stl implementation"
- Company: Hudson River Trading
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/c-questions-related-to-memory-management-and-stl-implementation-QTN_4298492.htm
- Answer/Discussion: none found on the question page itself. Corroborated independently by a Blind post (see next entry) describing the same style of round.

### "Lots of questions on STL containers, how it is implemented, pros and cons, stuff like that" / "general c++ stuff, like inline functions pros and cons etc"
- Company: Hudson River Trading
- Role: Core Developer / Low-Level C++
- Type: Interview
- Status: REAL
- Source: Blind (teamblind.com) — https://www.teamblind.com/post/hudson-river-trading-core-developerlow-level-c-interview-yuqksebo
- Answer/Discussion: A commenter added that "any low level programmer is expected to write vectorized code" (SIMD), and recommended studying virtual memory/paging and multithreading alongside STL internals.

### "Basic questions are to implement a smart pointer."
- Company: unknown/general HFT firm (poster describes "HFT SWE jobs, C++ experience required" without naming the specific firm for this detail)
- Role: HFT Software Engineer
- Type: Interview
- Status: REAL
- Source: Blind (teamblind.com) — https://www.teamblind.com/post/HFT-SWE-jobs-c-exp-required-u6bVuifC
- Answer/Discussion: none found; thread otherwise references threading, templates, C++ internals, and STL as commonly tested areas at HFT shops.

### "Smart pointers, lambdas, exceptions" / "move, implement move constructor and assignment" / "unordered_map, vector, algorithm header" / "pass in a lambda for a comparator"
- Company: Oculus (Meta)
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: Blind (teamblind.com) — https://www.teamblind.com/post/oculus-c-interview-0rmbcvt7
- Answer/Discussion: none found beyond topic list; also mentions default/delete keywords, constexpr, atomics/memory model, condition_variable/mutex/thread/async, and interfaces/pure-virtuals in the same interview loop.

### "Several C/C++ related questions regarding memory management, pointers, ..."
- Company: Arm
- Role: (title suggests a technical/test-management-adjacent role; exact title not confirmed beyond Glassdoor's listing)
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Several-C-C-related-questions-regarding-memory-management-pointers-QTN_3644220.htm
- Answer/Discussion: none found on the question page directly; other Arm candidate reports reference stack vs heap, cache, and device-driver-level memory questions as recurring themes.

### "function pointer, memory leak, design pattern"
- Company: Amadeus
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/function-pointer-memory-leak-design-pattern-QTN_1420207.htm
- Answer/Discussion: none found beyond the question title.

### "Memory management, C/C++ programming, Threads, OS"
- Company: Honeywell
- Role: Tech Lead
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Memory-management-C-C-programming-Threads-OS-QTN_1335029.htm
- Answer/Discussion: none found beyond the question title.

### "What is a Smart pointer? Why is it used?"
- Company: Amadeus Labs, Bangalore
- Role: Senior Software Engineer (0-2 yrs exp)
- Type: Interview
- Status: REAL
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/amadeus-labs-bangalore-interview-experience/
- Answer/Discussion: Asked in Round 2 (40-minute technical round) as a C++11 memory-management check; no model answer recorded in source.

### "Why are virtual destructors used? Can you have Virtual constructors?"
- Company: Amadeus Labs, Bangalore
- Role: Senior Software Engineer
- Type: Interview
- Status: REAL
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/amadeus-labs-bangalore-interview-experience/
- Answer/Discussion: Tests RAII-adjacent object-lifecycle understanding (why base-class destructors must be virtual for correct cleanup through a pointer to base); "Can you have virtual constructors?" checks understanding that construction requires a concrete, known type (answer: no direct virtual constructors, though "virtual constructor idiom"/clone pattern exists).

### Function returning a reference to a local int — "would this work?"
- Company: Amadeus Labs, Bangalore
- Role: Senior Software Engineer
- Type: Interview
- Status: REAL
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/amadeus-labs-bangalore-interview-experience/
- Answer/Discussion: Classic dangling-reference question — returning a reference to a stack-local variable leaves the reference pointing to destroyed/reused stack memory, invoking undefined behavior. Reported in Round 2.

### Code-reading exercise with a deliberate memory-management bug: walk through which constructors/destructors fire at each line, distinguish copy construction from copy assignment, spot the leaked heap object and the uninitialized member.
- Company: NVIDIA
- Role: Compiler Engineer Intern
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/NVIDIA-Compiler-Engineer-Intern-Interview-Questions-EI_IE7633.0,6_KO7,31.htm
- Answer/Discussion: none found beyond the described exercise (page not directly fetchable; summarized via search index). Directly tests manual memory management / RAII discipline via code review rather than live coding.

### Dangling pointers: how to avoid an already-freed pointer being freed again (double-free)
- Company: Qualcomm
- Role: Senior Embedded Software Engineer
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/Qualcomm-Senior-Embedded-Software-Engineer-Interview-Questions-EI_IE640.0,8_KO9,42.htm
- Answer/Discussion: none found beyond the topic summary (page not directly fetchable). Expected discussion likely covers setting pointers to nullptr after delete / ownership discipline / smart pointers as the fix.

### Stack vs heap allocation; how pointers access memory locations; dangers of dangling pointers and memory leaks
- Company: HCL
- Role: Junior Software Engineer
- Type: Interview
- Status: REAL
- Source: Glassdoor — https://www.glassdoor.com/Interview/HCL-Junior-Software-Engineer-Interview-Questions-EI_IE814619.0,3_KO4,28.htm
- Answer/Discussion: none found beyond the topic summary.

---
## PRACTICE (generic listicle / self-study / non-attributed content — kept for reference, not confirmed as a specific real ask)

### "Difference between vector and list?" / "Difference between map and unordered_map?" / "Does push_back() on a vector invalidate iterators?" / "How to make a custom class usable as a key in map/unordered_map?"
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: GitHub Gist (self-study notes based on r/cpp discussion) — https://gist.github.com/doevelopper/673b188b479ae66566d604df77218e20
- Answer/Discussion: Gist author explicitly frames these as self-prepared answers ("~2 years C++ experience") rather than a transcript of a real interview.

### "Difference between references and pointers?" / "Difference between stack and heap memory allocation?" / "What kinds of smart pointers exist?" / "How is unique_ptr implemented?" / "How does shared_ptr work?"
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: GitHub Gist — https://gist.github.com/doevelopper/673b188b479ae66566d604df77218e20
- Answer/Discussion: unique_ptr described as RAII-based exclusive ownership; shared_ptr described as using a shared control block with an atomic-ish reference counter.

### huihut/interview curated C/C++ knowledge base (STL container complexity table, new/delete vs malloc/free, smart pointer categories, pointers vs references)
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: GitHub — https://github.com/huihut/interview (README.md)
- Answer/Discussion: Widely-used curated reference (popular in Chinese campus recruiting prep) covering: new/delete call constructors/destructors while malloc/free do not; must pair new/delete and new[]/delete[]; vector = O(1) random access & tail ops, list = O(1) insert/erase anywhere but no random access; shared_ptr/unique_ptr/weak_ptr ownership models. Not attributed to any specific real interview transcript per question.

### "When would you use shared_ptr vs unique_ptr?" / "std::move vs std::forward" / "C++20 concepts" / "map vs unordered_map"
- Company: unknown/general (aggregator explicitly states "no specific company attribution")
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233474462/cpp-interview-questions-2025-smart-pointers-move-semantics-raii-templates-stl-concurrency-memory-model-virtual-functions/
- Answer/Discussion: unique_ptr recommended by default (single ownership, zero overhead); shared_ptr only for genuine shared ownership; weak_ptr to break cycles. std::move = unconditional cast to rvalue; std::forward = conditional, preserves value category (used in templates).

### "Implement a basic unique_ptr" (destructor, deleted copy ops, move semantics)
- Company: unknown/general — article names Hudson River Trading, Jump Trading, Citadel Securities, Optiver, Tower, Two Sigma, D.E. Shaw as firms that test this *depth* of C++, but does not attribute this specific question to any one of them
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233474597/cpp-quant-interviews/
- Answer/Discussion: Presented as an illustrative "topic area" question, not a verified transcript.

### "unique_ptr vs shared_ptr — when to use each?" / "RAII explained (with std::lock_guard / FILE* handle example)" / "std::function vs raw function pointer overhead" / "SoA vs AoS cache layout"
- Company: Listed as attributed to Hudson River Trading, Jump Trading, Citadel Securities, Tower Research, Radix, and DRW collectively, but presented listicle-style as "20 real examples" without per-question sourcing/transcripts
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: unique_ptr: "single owner; can be moved; zero overhead vs raw pointer; use 90% of the time." RAII: "acquire a resource in the constructor; release in the destructor," e.g. std::lock_guard<std::mutex>; modern alternative to manual FILE* cleanup is std::unique_ptr<FILE, decltype(&fclose)>. std::function called "5-10x slower than a function pointer in tight loops" due to type erasure.

### "What is a Shared Pointer? Give a Quantitative Finance example" / "How does shared_ptr manage reference counting?" / "What causes a memory leak with shared_ptr?" (reference cycles) / "make_shared<T>() vs shared_ptr<T>(new T)" / "Why is shared_ptr slower [than a raw pointer]?"
- Company: unknown/general (framed as "quant interview questions" generically, no specific company cited)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: C++ for Quants — https://cppforquants.com/c-shared-pointers-top-shared_ptr-quant-interview-questions/
- Answer/Discussion: Memory leak cause = reference cycles between shared_ptrs (fix: weak_ptr to break the cycle). make_shared does one combined allocation for object+control block (faster, more cache-friendly) vs two separate allocations with shared_ptr<T>(new T). Slower than raw pointer due to atomic refcount increment/decrement plus control-block allocation.

### GeeksforGeeks generic "C++ STL Interview Questions and Answers" listicle
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/cpp/cpp-stl-interview-questions/ and https://www.geeksforgeeks.org/interview-prep/stl-standard-template-library-interview-questions-c-programming/
- Answer/Discussion: Standard listicle covering containers/algorithms/iterators/functors; not attributed to a real interview transcript.

### GeeksforGeeks "How to Implement User Defined Shared Pointers in C++?" tutorial
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/cpp/how-to-implement-user-defined-shared-pointers-in-c/
- Answer/Discussion: Tutorial-style shared_ptr implementation (template class wrapping a raw pointer + refcount, copy ctor increments count, destructor decrements/deletes at zero, operator* / operator-> overloads). Not framed as a reported interview question, but a commonly-recommended prep exercise for the "implement shared_ptr" interview task seen (REAL) at Alphagrep/QuantBox above.
