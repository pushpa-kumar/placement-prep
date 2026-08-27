# Wave 2 — Thin Topics (GitHub-sourced): C++ output/debugging, concurrency/atomics, OS/networking/CPU/cache, general C++ MCQ

### Squarepoint Capital, R2: "Given a code snippet, asked how many times constructors (copy/move/assignment) would be called" + separate `char**` pointer code exercise
- Company: Squarepoint Capital
- Role: C++ Software Engineer
- Type: Interview
- Topic: C++ output/debugging
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: Exact snippet not preserved in the source notes, only the description that the candidate had to count copy-ctor/move-ctor/copy-assign/move-assign invocations from a given code sample, then separately do a coding exercise involving `char**` pointers. No transcript of the actual code or the answer is given in the source.

### `i = i++; i = i++ + ++i; arr[i] = i++; bar(puts("a"), puts("b"));`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: All of these have unsequenced/undefined side effects on the same object between sequence points (UB in C, and in C++ before C++17 for the first/third; the second is UB in all standard versions). For `bar(puts("a"), puts("b"))`, argument evaluation order is unspecified: clang evaluates left-to-right printing "a b", gcc evaluates right-to-left printing "b a". Reference: https://en.cppreference.com/w/cpp/language/eval_order

### `int x = 10; while (x --> 0) { printf("%d ", x); }`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: Prints "9 8 7 6 5 4 3 2 1 0". `x --> 0` is not a real "goes to" operator — it parses as `x-- > 0` (post-decrement then compare), a well-known "special operator" trick.

### `struct S {}; std::cout << sizeof(S);`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: Output is `1`, not `0`. The C++ object model guarantees distinct objects have distinct addresses, so an empty class/struct must have nonzero size (at least 1 byte). Reference: https://eel.is/c++draft/basic.memobj#intro.object-9.sentence-2

### `std::cout << ("a" + 1 == "");` (pointer arithmetic on a string literal compared to another literal)
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: `"a" + 1` is pointer arithmetic on the decayed `const char*`, landing one past the `'a'` character, i.e. pointing at the literal's terminating NUL — a valid empty C-string. Comparing two `const char*` pointers with `==` compares addresses, not contents, but if the compiler happens to fold both literals into overlapping/adjacent storage this can evaluate `true` in practice (implementation-defined literal pooling), which is why the repo calls it "can technically evaluate to true." Not reliable/portable — shown as a quirk, not a guarantee.

### `T foo(T());` / `T foo(T (((a))));` / `T foo((T()));` — is each one a function declaration or a variable definition?
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: This is the "most vexing parse." `T foo();`, `T foo(T());`, and even `T foo(T((())));`/`T foo(T(((a))))` are all parsed as function declarations (the last taking a parameter named `a` of type `T`), never as object definitions calling a default constructor. Only `T foo((T()));` (extra parens around the whole initializer) forces it to be parsed as a variable definition.

### `[[gnu::constructor]] [[gnu::constructor]] int main() { puts("Hello, World!"); }`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: Prints "Hello, World!" twice. `[[gnu::constructor]]` is normally deduplicated when repeated, but GCC (prior to v15, or outside pedantic mode) still also allows the attribute on `main` itself, so `main` runs once as a registered pre-main constructor and once as the normal program entry point.

### `int iseven(int n) { return n % 2 == 0; } int main() { printf("%d", iseven(2)); }`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: This is C, and the identifier `iseven` is reserved (identifiers beginning with `is` followed by a lowercase letter are reserved for future library extension in the global namespace). Declaring/defining it is undefined behavior — the repo jokingly says the "correct" outputs include printing 1, wiping your hard drive, or summoning Cthulhu; in practice it prints `1` on all real compilers today, but per the standard this is technically UB.

### `puts("??(");` and `puts("<:");` under trigraph/digraph rules
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: When trigraphs are supported (removed in C++17/C23), `??(` inside a string literal is replaced before tokenization and prints `[` instead of the literal `??(`. `puts("<:")` always prints `<:` verbatim — digraphs like `<:` (for `[`) only apply to actual token positions, not inside character/string literal content.

### `std::string('0', '0')` vs `std::string{'0', '0'}`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GitHub repo jeremy-rifkin/c-cpp-trivia (README) — https://github.com/jeremy-rifkin/c-cpp-trivia
- Answer/Discussion: `std::string('0', '0')` calls the `(size_type count, char ch)` overload — `'0'` as a char converts to its ASCII value 48, so it constructs a string of 48 `'0'` characters. `std::string{'0', '0'}` uses list-initialization, which prefers the initializer-list constructor, producing the 2-character string `"00"`.

### GeeksforGeeks C++ Pointers Quiz, Q3: `int var = 5; int *ptr = &var; cout << *ptr;` — options: 0 / 5 / Address of var / Garbage value
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GeeksforGeeks C++ Pointers Quiz, scraped copy in GitHub repo Alchemist-10/XEngine — https://github.com/Alchemist-10/XEngine/blob/main/data/raw/doc_3893.txt
- Answer/Discussion: 5. `*ptr` dereferences the pointer to read the value stored at `var`'s address.

### GeeksforGeeks C++ Pointers Quiz, Q5: `int *ptr = NULL; ptr = new int; *ptr = 7; cout << *ptr; delete ptr;` — options: Outputs 0 / Outputs 7 / Compile-time error / Segfault
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GeeksforGeeks C++ Pointers Quiz, scraped copy in GitHub repo Alchemist-10/XEngine — https://github.com/Alchemist-10/XEngine/blob/main/data/raw/doc_3893.txt
- Answer/Discussion: Outputs 7. `new int` allocates a fresh int, `*ptr = 7` writes to it, and the `cout` happens before the `delete`, so the value read back is 7.

### GeeksforGeeks C++ Pointers Quiz, Q10: `void updateValue(int *ptr) { *ptr = 20; } int main() { int var = 10; updateValue(&var); cout << var; }` — options: 10 / 0 / 20 / Garbage value
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GeeksforGeeks C++ Pointers Quiz, scraped copy in GitHub repo Alchemist-10/XEngine — https://github.com/Alchemist-10/XEngine/blob/main/data/raw/doc_3893.txt
- Answer/Discussion: 20. Passing `&var` lets `updateValue` write through the pointer directly to `var`'s storage (pass-by-pointer mutation).

### GeeksforGeeks C++ Basics Quiz, Q3: `#include <iostream> using namespace std; int main() { cout << "Hello, World!" << endl; return 0; }` — options: "Hello, World" / "Hello, World!" / "Hello World!" / "Hello World"
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: GeeksforGeeks C++ Basics Quiz, scraped copy in GitHub repo Alchemist-10/XEngine — https://github.com/Alchemist-10/XEngine/blob/main/data/raw/doc_3916.txt
- Answer/Discussion: "Hello, World!" — exact match of the string literal, including the comma and exclamation point.

### `int x = 10; cout << x++;`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ output/debugging
- Status: PRACTICE
- Source: compilersutra docs (aabhinavg1/compilersutra), Basic C++ MCQ page — https://github.com/aabhinavg1/compilersutra/blob/main/docs/mcq/questions/basic/intro-to-cpp.md
- Answer/Discussion: Prints `10`. Post-increment `x++` yields the pre-increment value of `x` (10) as the expression result; `x` becomes 11 afterward but that's not what gets streamed.

### Hudson River Trading phone screen (C++ Software Engineer): "Use of `inline` functions in C++: pros and cons", "`vector` vs `list`: trade-offs and internal details", "Internal working of `malloc`, demand paging, etc.", "How the kernel allocates memory to user processes", "System calls like `sbrk` and `mmap`"
- Company: Hudson River Trading
- Role: C++ Software Engineer
- Type: Interview
- Topic: OS/networking/CPU/cache
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (topic list only, no transcript of the candidate's actual answers is preserved in the source).

### Squarepoint Capital Technical Screening R1 (C++ Software Engineer), CS-trivia segment: "virtual memory, process management, page tables, real-time systems, TCP vs UDP, dangling pointers"
- Company: Squarepoint Capital
- Role: C++ Software Engineer
- Type: Interview
- Topic: OS/networking/CPU/cache
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (topic list only).

### Squarepoint Capital Technical Screening R2 (C++ Software Engineer): "questions on TCP's internal state machine handling"
- Company: Squarepoint Capital
- Role: C++ Software Engineer
- Type: Interview
- Topic: OS/networking/CPU/cache
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found — described only as questions on the TCP state machine (i.e. the connection states like SYN_SENT/ESTABLISHED/TIME_WAIT and transitions), no verbatim Q&A given.

### DRW Technical Round: "write pseudocode to serialize a `struct` in binary format and write it to a file", with follow-up on endianness and how to handle it
- Company: DRW
- Role: unknown (general SWE round after a C++ OA)
- Type: Interview
- Topic: OS/networking/CPU/cache
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (task description only — candidate wrote pseudocode for binary struct serialization to a file, then was asked follow-ups on endianness handling, e.g. network byte order vs host byte order and portability across architectures).

### QuantBox systems interview (3–4 hrs), OS/CPU-relevant topics: "Endianness detection", "Memory reordering (hardware/compiler level)", "Lazy allocation and `malloc` internals"
- Company: QuantBox
- Role: unknown
- Type: Interview
- Topic: OS/networking/CPU/cache
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (topic list only, part of a broader long-form systems interview also covering smart-pointer/String/memory-pool implementation and virtual dispatch).

### Squarepoint Capital Technical Screening R3 (C++ Software Engineer): given a thread-safe queue implementation + benchmark, "suggest some optimizations" — expected: replace copies with move semantics, use a condition variable instead of busy-waiting, make the queue bounded, use RAII for locking/unlocking, discuss cache-friendliness of the underlying container
- Company: Squarepoint Capital
- Role: C++ Software Engineer
- Type: Interview
- Topic: Concurrency/atomics
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: Candidate's listed answer/approach: (1) replace pass-by-copy with `std::move`, (2) swap busy-wait polling for a `std::condition_variable` wait/notify, (3) bound the queue size to avoid unbounded memory growth, (4) wrap mutex lock/unlock in RAII (`std::lock_guard`/`std::unique_lock`), (5) discuss cache-friendliness of the underlying container (e.g. contiguous storage vs linked nodes for the queue).

### Graviton pen-and-paper test (Software Engineer): "Implement concurrent transactions between two bank accounts using locks"
- Company: Graviton
- Role: Software Engineer
- Type: Interview
- Topic: Concurrency/atomics
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (problem statement only — classic dual-mutex transfer problem where the expected discussion is lock ordering to avoid deadlock, e.g. always lock accounts in a consistent global order such as by address/id, or use `std::lock`/`std::scoped_lock` to acquire both atomically).

### QuantBox systems interview (3–4 hrs): "Lock-free data structures (multi-threaded linked list, producer-consumer buffer)", "Spinlock and contention optimization", "Read-Copy-Update (RCU)"
- Company: QuantBox
- Role: unknown
- Type: Interview
- Topic: Concurrency/atomics
- Status: REAL
- Source: GitHub repo Shivam5022/Interview-Experiences — https://github.com/Shivam5022/Interview-Experiences/blob/main/Readme.md
- Answer/Discussion: none found (topic list only, no transcript of the discussion/expected answers on lock-free linked lists, SPSC/MPSC producer-consumer buffers, spinlock backoff, or RCU is preserved in the source).

### "Exhaustive list of interview questions and experience from various HFT firms across the world" — implementation-style question bank
- Company: unknown/general (aggregated across multiple unnamed HFT firms)
- Role: unknown (HFT SWE)
- Type: Interview
- Topic: C++ MCQ/conceptual
- Status: REAL
- Source: GitHub repo indra215/HFT_Interview_qsn — https://github.com/indra215/HFT_Interview_qsn
- Answer/Discussion: Full list as reported: (1) Implement std::variant, (2) Implement std::any, (3) Implement std::optional, (4) Implement std::tuple, (5) Implement a circular queue (resize/push_back/pop_back/push_front/pop_front/iterator), (6) Zip multiple same-sized compile-time vectors by multiplying elements at each index, (7) Remove adjacent duplicates from a compile-time vector, (8) Prepend a number to a compile-time vector, (9) Implement specializations of a `print` function for integral types and for classes with an iterator, (10) Implement std::string focusing on SSO (small string optimization), (11) Implement memory pools, (12) Implement std::vector without using `new`, (13) Implement an LRU cache, (14) Implement a rate limiter/throttler for both static and sliding windows, (15) Implement an order book, (16) Implement a dictionary using different words, (17) Implement a matching engine supporting add/modify/cancel with trade generation on a cross. No worked solutions given in the source, only the question list.

### HFT interview-prep resource list — recommended reading/watching for OS, CPU, C++, and networking rounds
- Company: unknown/general
- Role: unknown (HFT SWE)
- Type: Unknown
- Topic: OS/networking/CPU/cache
- Status: PRACTICE
- Source: GitHub repo Unays7/HFT-Interview-Prep — https://github.com/Unays7/HFT-Interview-Prep
- Answer/Discussion: Not a Q&A source — it's a curated reading list the author says they personally used for HFT interview prep, e.g. OSTEP, Algorithmica/HPC, "What Every Programmer Should Know About Memory", easyperf book + perf-ninja labs, Linux Insides, TCP/IP Illustrated, io_uring, eBPF tutorial, Agner Fog's "Optimizing C++", rigtorp.se blog, plus a companion "Perf-Notes.md" with the author's own study notes on CPU back-end optimization (memory-bound vs core-bound, cache-friendly data structures, false sharing/padding with `alignas(64)`, DTLB/hugepages, function inlining, loop optimizations).

### "Which of the following statements is true about static variables?" — options: reinitialized every call / retain value between calls / only declared in a function / cannot be initialized
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ MCQ/conceptual
- Status: PRACTICE
- Source: GeeksforGeeks C++ Basics Quiz, scraped copy in GitHub repo Alchemist-10/XEngine — https://github.com/Alchemist-10/XEngine/blob/main/data/raw/doc_3916.txt
- Answer/Discussion: "They retain their value between function calls." Static local variables are initialized once and persist for the lifetime of the program, keeping their value across calls.

### "What is the correct way to declare a constant pointer to an integer in C++?" — options: `int const *ptr;` / `const int * const ptr;` / `const int *ptr;` / `int * const ptr;`
- Company: unknown/general
- Role: unknown
- Type: Unknown
- Topic: C++ MCQ/conceptual
- Status: PRACTICE
- Source: GeeksforGeeks C++ Pointers Quiz, scraped copy in GitHub repo Alchemist-10/XEngine — https://github.com/Alchemist-10/XEngine/blob/main/data/raw/doc_3893.txt
- Answer/Discussion: `int * const ptr;` — a "constant pointer to an integer" means the pointer itself cannot be reseated (const applies to the pointer, not the pointee); `const int *ptr` / `int const *ptr` are instead pointers to a constant int (pointee immutable, pointer reseatable), and `const int * const ptr` is a constant pointer to a constant int.
