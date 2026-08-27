# Topic: Modern C++ Core Language — Interview Question Bank (templates, value categories, move semantics, rule of 3/5/0, constexpr, output/gotcha snippets)

### Implement `std::variant<>` from scratch (variadic templates, union-based storage, index-based type tracking, move semantics for contained types)
- Company: unknown HFT firm (name withheld by poster)
- Role: C++ Developer (HFT)
- Type: Interview
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/post/6203878/C++-Interview-experience-with-High-Frequency-Trading-Company/
- Answer/Discussion: Poster (self-described as one of few public HFT C++ interview writeups) implemented a variadic-template variant with union-based storage, index-based active-type tracking, constructor forwarding, and correct destructor handling per contained type. No official model answer beyond the poster's own implementation walkthrough.

### "What is move semantics — what does `std::move` do?" — trace the output of:
```cpp
std::vector<int> vec{1,2,3,4,5};
auto mvec = std::move(vec);
std::cout << vec.size() << std::endl;
std::cout << mvec.size() << std::endl;
```
- Company: unknown/general (author is a Lead Software Engineer sharing an interview question he uses/has seen)
- Role: Software Engineer (general, not finance-specific)
- Type: Interview
- Status: REAL
- Source: Bulldogjob — https://bulldogjob.com/readme/c-frequently-failed-interview-question
- Answer/Discussion: `std::move` is only a cast-to-rvalue-reference; it does not itself move anything. It enables the vector's move constructor, which swaps the three internal pointers (`_M_start`, `_M_finish`, `_M_end_of_storage`) instead of copying. Output: `vec.size()` == 0 (moved-from, empty), `mvec.size()` == 5. Article notes even experienced engineers frequently fail this question by claiming std::move "moves memory."

### "Explain all the value categories in C++" (lvalue/xvalue/prvalue/glvalue/rvalue)
- Company: unknown (candidate failed a "C++ trivia" round; commenter tag suggests general big-tech/FAANG-adjacent)
- Role: unknown (senior-ish, trivia round separate from design round)
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/How-to-pass-C-interviews-with-C-trivia-questions-Do-I-even-want-to-LyjZzTyn
- Answer/Discussion: none found (thread discusses the question being asked and candidate not knowing the answer, but no worked answer given in thread)

### "Universal references and reference collapsing rules" (explain and give examples of `T&&` deduction and reference collapsing)
- Company: Meta/Facebook (commenter tag)
- Role: unknown (experienced C++ dev interview loop)
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/C-interview-questions-QGYMfgVu
- Answer/Discussion: none found in thread; standard answer: in template deduction, `T&& &` , `T& &&`, `T& &`, `T&& &&` all collapse to `T&` unless both are rvalue refs, in which case they collapse to `T&&` — this is what allows `std::forward` to work.

### "Do exception throws result in destructors being called?" (stack unwinding / RAII correctness under exceptions)
- Company: unnamed algo-trading firm
- Role: unknown
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/Where-to-cover-C-language-questions-for-FANG-pxm1XWiH
- Answer/Discussion: none found in thread beyond the question being listed; correct answer: yes — stack unwinding during exception propagation calls destructors of all fully-constructed local objects in scope, which is the basis of RAII-based cleanup/exception safety.

### Rule of 5 — implement/explain the rule of five, and implement `is_pointer<T>` via template (partial) specialization
- Company: NVIDIA (commenter tag "cpp-pls")
- Role: unknown
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/What-are-the-C-interview-questions-you-got-asked-for-a-mid-senior-senior-position-jcq1ksue
- Answer/Discussion: none found (thread lists topics, not full worked solutions). Also asked in same interview: RAII, single-argument-constructor pitfall (implicit conversion — should mark `explicit`), and which smart pointer type to use when.

### "Explain the diamond inheritance problem and how virtual inheritance resolves it"; also C++11+ features, move semantics, placement new, `dynamic_cast` vs `static_cast` vs `reinterpret_cast`, atomics
- Company: Goldman Sachs (commenter tag "pxhP14")
- Role: unknown (C++ dev interview loop)
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/What-are-the-C-interview-questions-you-got-asked-for-a-mid-senior-senior-position-jcq1ksue
- Answer/Discussion: none found in thread; standard answer for diamond problem: without `virtual` inheritance, a class inheriting from two classes that share a common base gets two separate subobjects of that base, causing ambiguity; `virtual` inheritance makes the base subobject shared/single.

### "Mutable keyword usage; union keyword purpose; difference between rvalue reference and a regular (lvalue) reference; move semantics vs copy semantics"
- Company: Square (Block) — commenter tag "Rqyn35"
- Role: unknown
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/What-are-the-C-interview-questions-you-got-asked-for-a-mid-senior-senior-position-jcq1ksue
- Answer/Discussion: none found in thread

### "What is SFINAE (Substitution Failure Is Not An Error)?"
- Company: Google (commenter tag "LeeJaeDong")
- Role: unknown
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/What-are-the-C-interview-questions-you-got-asked-for-a-mid-senior-senior-position-jcq1ksue
- Answer/Discussion: none found in thread; standard answer: when template argument substitution during overload resolution produces an invalid type/expression, the compiler silently removes that overload from the candidate set instead of raising a hard error, rather than causing a compilation failure — used heavily pre-C++20 to constrain templates (now largely superseded by Concepts).

### Design/implement shared_ptr (custom smart pointer), copy-swap idiom, lock-free hash table, generic event scheduler, reference collapsing, memcpy implementation, thread-safe singleton
- Company: Ford (commenter tag "KACg63")
- Role: unknown (rapid-fire C++ language round)
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/What-are-the-C-interview-questions-you-got-asked-for-a-mid-senior-senior-position-jcq1ksue
- Answer/Discussion: none found in thread

### "Explain large memory allocation/swap behavior and C++ `inline` trade-offs" — what happens when a program requests 8 GB on a machine with 4 GB RAM, discussed alongside when `inline` helps/hurts
- Company: Hudson River Trading
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: PracHub (HRT interview question aggregator) — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found (site labels difficulty "Hard", technical screen round); ties into general discussion of virtual memory paging/swap and why `inline` is a hint, not a guarantee, and can bloat code negatively affecting icache.

### "Reason about C++ inlining, memory allocation strategies, and static vs dynamic polymorphism" (cost/perf trade-offs of virtual dispatch vs templates/CRTP)
- Company: Hudson River Trading
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found; general answer: static polymorphism (templates/CRTP) resolves at compile time, enabling inlining and no vtable indirection, at the cost of code bloat and interface rigidity; dynamic polymorphism (virtual functions) is more flexible/ABI-stable but costs a vtable pointer per object and an indirect call that can defeat branch prediction/inlining.

### "Explain `inline`, segfaults, virtual memory (MMU address translation, TLB, page tables), and `std::string` internals (e.g., SSO)"
- Company: Hudson River Trading
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: PracHub — https://prachub.com/companies/hudson-river-trading
- Answer/Discussion: none found; std::string internals point is Small String Optimization (SSO) — short strings are stored inline in the string object (no heap allocation), which is a very commonly-probed "gotcha" in modern C++ interviews since sizeof/move behavior differs from naive expectations.

### Memory-ordering question: "What's the difference between `memory_order_relaxed`, `memory_order_acquire`, `memory_order_release`, and `memory_order_seq_cst`?"
- Company: Attributed generally to low-latency trading firms (HRT, Jump Trading, Citadel Securities, Tower Research, DRW cited as typical askers)
- Role: Quant Developer / C++ Engineer
- Type: Interview
- Status: REAL (topic independently corroborated across multiple sources as a recurring HFT C++ interview question, though no single verbatim candidate transcript located)
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: `relaxed` gives no ordering/synchronization guarantee beyond atomicity; `acquire` (on a load) prevents subsequent reads/writes from being reordered before it; `release` (on a store) prevents preceding reads/writes from being reordered after it — acquire/release pairs establish a happens-before relationship; `seq_cst` (default) additionally provides a single total global order across all seq_cst operations, at extra synchronization cost.

### False sharing: "Two threads increment separate counters that happen to live in the same cache line — what goes wrong, and how do you fix it?"
- Company: unknown/general (framed by Quantt as representative of real HFT interview questions; false-sharing questions independently corroborated in other HFT-focused threads, e.g., "proprietary trading shops ask about ... false memory sharing" per Blind)
- Role: Quant/C++ Developer
- Type: Interview
- Status: PRACTICE (topic is real and recurring per multiple sources, but no single verbatim transcript found)
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: Two independent variables sharing a cache line cause the cache-coherency protocol to bounce the line between cores on every write from either thread, destroying performance despite no logical data race. Fix: pad/align each counter to its own cache line (e.g., `alignas(64)`) or otherwise ensure independent variables don't share a line.

### Implement `is_pointer<T>` (or similar trait) using template partial specialization
- Company: NVIDIA
- Role: unknown
- Type: Interview
- Status: REAL
- Source: Blind — https://www.teamblind.com/post/What-are-the-C-interview-questions-you-got-asked-for-a-mid-senior-senior-position-jcq1ksue
- Answer/Discussion: none found; canonical solution: primary template `is_pointer<T>` inherits `false_type`; partial specialization `is_pointer<T*>` inherits `true_type`.

### Explain FPGAs in HFT, clock synchronization in distributed HFT systems, RAII, latency-minimization strategies (paired with the four "hardest C++ HFT coding challenges" below)
- Company: unknown/general (aggregator citing "WallStreetCPP" prep material)
- Role: HFT C++ Engineer
- Type: OA/Interview (unclear which)
- Status: PRACTICE (curated prep list, not a single verified candidate report)
- Source: eFinancialCareers — https://www.efinancialcareers.de/en/news/c-plus-plus-interview-questions-hft-high-frequency-trading
- Answer/Discussion: none found in article beyond question prompts

### "Implement a template metaprogram that removes adjacent duplicates from a compile-time vector of integers" (compile-time list represented as a variadic-integer template struct)
- Company: unknown/general (cited as one of the "hardest" HFT-style C++ template questions)
- Role: HFT C++ Engineer
- Type: OA/Interview (unclear)
- Status: PRACTICE
- Source: eFinancialCareers — https://www.efinancialcareers.de/en/news/c-plus-plus-interview-questions-hft-high-frequency-trading
- Answer/Discussion: none found; would require a recursive variadic template (e.g., `template<int...> struct Vec;`) with pattern-matching partial specializations comparing adjacent head elements and recursively building a deduplicated pack.

### Implement a memory pool class for efficient allocation/deallocation from a pre-allocated chunk; implement a thread pool class; implement a "safe vector" that keeps iterators valid across modification
- Company: unknown/general
- Role: HFT C++ Engineer
- Type: OA/Interview (unclear)
- Status: PRACTICE
- Source: eFinancialCareers — https://www.efinancialcareers.de/en/news/c-plus-plus-interview-questions-hft-high-frequency-trading
- Answer/Discussion: none found in article

### Virtual destructor / polymorphic destruction order — trace the output:
```cpp
class base {
public:
    base() { cout<<"Constructing base \n"; }
    virtual ~base() { cout<<"Destructing base \n"; }
};
class derived: public base {
public:
    derived() { cout<<"Constructing derived \n"; }
    ~derived() { cout<<"Destructing derived \n"; }
};
int main(void) {
    derived *d = new derived();
    base *b = d;
    delete b;
}
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle, no attribution)
- Status: PRACTICE
- Source: Aticleworld — https://aticleworld.com/interview-questions-on-virtual-keyword-in-c/
- Answer/Discussion: Output: `Constructing base` → `Constructing derived` → `Destructing derived` → `Destructing base`. Because `~base()` is virtual, `delete b` correctly invokes the most-derived destructor first, then chains up to base — demonstrates why base class destructors must be virtual when deleting through a base pointer (classic gotcha: omitting `virtual` here is UB/leaks the derived part).

### Calling a virtual function from a constructor/destructor mid-teardown — trace the output:
```cpp
class Base {
    virtual void method() {std::cout << "from Base" << std::endl;}
public:
    virtual ~Base() {method();}
    void baseMethod() {method();}
};
class A : public Base {
    void method() {std::cout << "from A" << std::endl;}
public:
    ~A() {method();}
};
int main(void) {
    Base* base = new A;
    base->baseMethod();
    delete base;
}
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Toptal — https://www.toptal.com/developers/c-plus-plus/interview-questions
- Answer/Discussion: Output: `from A` (baseMethod dispatches virtually to A::method) / `from A` (A's own destructor still has a fully-formed A vtable) / `from Base` (once A's destructor body finishes, the object "becomes" a Base during Base's destructor body, so the virtual call in `~Base` now resolves to `Base::method`, NOT `A::method` — classic gotcha about virtual dispatch during destruction).

### Signed/unsigned promotion gotcha — what does this print?
```cpp
std::cout << 25u - 50;
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Toptal — https://www.toptal.com/developers/c-plus-plus/interview-questions
- Answer/Discussion: Prints a large positive number (4294967271 on 32-bit unsigned int) — the signed `50` is converted to `unsigned int` before subtraction (usual arithmetic conversions), causing wraparound instead of a negative result.

### Throwing from a destructor during stack unwinding — what happens?
```cpp
class A {
public:
    A() {}
    ~A() { throw 42; }
};
int main() {
    try {
        A a;
        throw 32;
    } catch(int a) {
        std::cout << a;
    }
}
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Toptal — https://www.toptal.com/developers/c-plus-plus/interview-questions
- Answer/Discussion: Program terminates abnormally (calls `std::terminate`) — throwing a second exception while already unwinding the stack from a first exception is fatal. This is the formal/code version of the Blind "do exception throws result in destructors being called" question above.

### Vtable pointer layout gotcha — what does this print (platform-dependent)?
```cpp
struct A {
    int data[2];
    A(int x, int y) : data{x, y} {}
    virtual void f() {}
};
int main() {
    A a(22, 33);
    int *arr = (int *) &a;
    std::cout << arr[2] << std::endl;
}
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Toptal — https://www.toptal.com/developers/c-plus-plus/interview-questions
- Answer/Discussion: Result depends on ABI/pointer size: on 32-bit, the vptr occupies the first 4 bytes so `arr[2]` lands on `data[1]` → 33; on 64-bit the vptr is 8 bytes (2 ints wide) so `arr[2]` lands on `data[0]` → 22. Demonstrates that adding a single virtual function changes an object's memory layout by inserting a hidden vptr, and that reinterpreting object memory as `int*` is UB/fragile.

### Array-index commutativity gotcha — what does this print?
```cpp
int a[] = {1, 2, 3, 4, 5, 6};
std::cout << (1 + 3)[a] - a[0] + (a + 1)[2];
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Toptal — https://www.toptal.com/developers/c-plus-plus/interview-questions
- Answer/Discussion: Prints `8`. `(1+3)[a]` is `a[4]` = 5 (since `x[y]` is `*(x+y)`, commutative); `a[0]` = 1; `(a+1)[2]` is `a[3]` = 4. So `5 - 1 + 4 = 8`.

### Private virtual function overriding — what does this print?
```cpp
class Base {
public:
    void test();
private:
    virtual void fun() { cout << "Base Function"<<endl; }
};
class Derived: public Base {
public:
    void fun() { cout << "Derived Function"<<endl; }
};
void Base::test() {
    Derived objDerived;
    Base *ptr = &objDerived;
    ptr->fun();
}
int main() {
    Base Obj;
    Obj.test();
}
```
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Aticleworld — https://aticleworld.com/interview-questions-on-virtual-keyword-in-c/
- Answer/Discussion: Prints `Derived Function`. A `private` virtual function can still be overridden by a derived class and still participates in dynamic dispatch — access control (`private`) is checked at the call site's declared type, not at the point of virtual resolution, and here the call goes through `Base::test()` which has access to `fun()`.

### Rule of Three / Rule of Five / Rule of Zero — "if you define a destructor, copy constructor, or copy assignment operator, why must you define all three (or all five with move ops), and what's the modern preferred alternative?"
- Company: unknown/general (canonical, widely corroborated across HFT prep sources — e.g., NVIDIA's "Rule of 5" question above is the REAL instance of this topic)
- Role: unknown
- Type: Unknown (concept reference)
- Status: PRACTICE
- Source: cppreference — https://en.cppreference.com/w/cpp/language/rule_of_three
- Answer/Discussion: If a class manages a resource requiring a custom destructor, the compiler-generated copy constructor/assignment will do a shallow copy, causing double-free/dangling-pointer bugs — hence Rule of Three. C++11 adds move constructor/assignment, extending it to Rule of Five. Rule of Zero: prefer designing classes so that no special member functions need to be hand-written at all, by delegating ownership to RAII types (smart pointers, containers) — this is the modern preferred default and a common follow-up answer interviewers look for.

### SFINAE and its modern replacement — "What is SFINAE and what's the C++20 alternative?"
- Company: unknown/general (Google's plain "What is SFINAE" question above is the REAL instance)
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: SFINAE = when template argument substitution produces an invalid type/expression, that overload is silently dropped from the candidate set rather than causing a hard compile error, allowing `enable_if`-style compile-time overload constraints. Modern (C++20) alternative: Concepts (`requires` clauses), which express the same constraints more directly and give much better error messages.

### `std::function` vs raw function pointer — "what's the runtime/space cost difference?"
- Company: unknown/general (a `std::function` question was independently reported as REAL in the Blind "value categories" thread as one of several topics from the same interview)
- Role: unknown
- Type: Interview / Unknown
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: A raw function pointer is a single word with no allocation and is directly inlinable in simple cases. `std::function` type-erases any callable (function pointer, lambda, functor) behind a fixed interface; if the callable exceeds the small-buffer optimization size (implementation defined, commonly ~16 bytes of captured state) it heap-allocates, and calls go through indirection that usually defeats inlining — relevant to HFT hot-path code where `std::function` is often avoided in favor of templates or plain function pointers.

### Lambda capture semantics — "difference between capture by reference `[&]` and capture by value `[=]`, and when each dangles"
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: `[&]` captures by reference — if the lambda outlives the captured variable's scope (e.g., returned from a function, or run asynchronously), it dangles. `[=]` captures by value (a copy at lambda-creation time), which is safer for escaping lambdas but can be more expensive and doesn't reflect later changes to the original variable. `this` capture also has subtleties (captures the pointer, not the object, by default).

### `const` vs `constexpr` — "what's the actual difference?"
- Company: unknown/general
- Role: unknown
- Type: Unknown (listicle)
- Status: PRACTICE
- Source: Quantt — https://www.quantt.co.uk/resources/cpp-quant-interview-questions
- Answer/Discussion: `const` only promises the value won't be modified after initialization (can still be initialized at runtime from a non-constant expression). `constexpr` requires the value (or function result, given constant-expression arguments) be computable at compile time, enabling use in contexts requiring compile-time constants (array bounds, template arguments) and potentially avoiding runtime cost entirely.

### Generic C++ questions bank (short-answer, title-only, no code) — templates, template specialization/partial specialization, template parameter packs, variadic templates, CRTP, SFINAE, type traits, decltype, rvalue/lvalue references, move constructor/assignment, perfect forwarding, `std::forward`, constexpr functions, const member functions, lambda expressions
- Company: unknown/general
- Role: unknown
- Type: Unknown (large curated prep list of ~140 numbered short-answer questions, no per-question attribution)
- Status: PRACTICE
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/3316931/C++-Basic-and-Advance-Concepts-Questions-(For-Interview-Preparation)
- Answer/Discussion: none found (question titles only, no answers or code provided in source)

### "Difference between `unique_ptr` and `shared_ptr`; can you copy a `unique_ptr` or transfer it between owners; how does `shared_ptr`'s reference count stay synchronized across threads; what are rvalue and lvalue; what do `std::move` and `std::forward` do"
- Company: unknown/general
- Role: unknown
- Type: Unknown (curated gist, titled "interview on C++", no per-question attribution or answers)
- Status: PRACTICE
- Source: GitHub Gist (doevelopper) — https://gist.github.com/doevelopper/673b188b479ae66566d604df77218e20
- Answer/Discussion: none found in source (question prompts only)

### "Can an exception be thrown from a constructor or destructor? How do you prevent problems from that?"
- Company: unknown/general
- Role: unknown
- Type: Unknown (curated gist)
- Status: PRACTICE
- Source: GitHub Gist (doevelopper) — https://gist.github.com/doevelopper/673b188b479ae66566d604df77218e20
- Answer/Discussion: none found in source; standard answer: throwing from a constructor is fine (object is considered not to have existed; already-constructed members/bases are destroyed during unwinding) — but throwing from a destructor is dangerous, especially if the destructor runs during stack unwinding from another exception, which calls `std::terminate` (see the Toptal double-throw snippet above for the concrete case). Mitigation: mark destructors `noexcept` (implicit default since C++11) and never let exceptions escape them — catch and swallow/log internally.

### "Explain how virtual inheritance works" and general OOP + C++11 features rapid-fire round (templates, class inheritance)
- Company: unknown trading firm (described generically as a prop/trading firm's "rapid fire Q&A" round)
- Role: Junior/general trading-firm SWE
- Type: Interview
- Status: PRACTICE (topic corroborated as real by multiple independent sources — e.g., Goldman Sachs diamond-inheritance question above — but this specific source gives no verbatim transcript)
- Source: Mako Blog — https://www.mako.com/blog/how-to-prepare-for-trading-industry-software-developer-interviews
- Answer/Discussion: none found; guide advises being ready to discuss differences across C++11/14/17/20 standards and give a coding example using a new feature you'd choose to use.
