# Wave 3: C++ MCQ / Output-Prediction Questions (Real OA + Real Assessment Sources)

---

### What is the output of the following C++ program?

```cpp
#include <iostream>
using namespace std;

void Q(int x) {
    try {
        if (x < 0)
            throw x + 5;
        else
            throw x;
    } catch (int x) {
        cout << " A " << x;
    }
}

int main() {
    Q(-2);
    cout << " C ";
    return 0;
}
```
- Options: A) `A -3 C` B) `A 3 C` C) `A -4 C` D) `A 4 C`
- Correct: B
- Company: Deloitte (campus OA, IIT Kharagpur)
- Type: MCQ (output-prediction)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/deloitee.md (Q5)
- Explanation: `Q(-2)` throws `x + 5 = -2 + 5 = 3`, caught by `catch(int x)`, printing " A 3". Control returns to main which prints " C ", giving "A 3 C".

---

### What will be the output of the C program given below? (used in the same C/C++ MCQ block of the OA)

```c
main() {
    auto int p = 4 - 2;
    p++;
    static int s;
    s = (p = ++s) + p;
    printf("%d", s++);
}
```
- Options: A) 3 B) 4 C) 2 D) 1
- Correct: C
- Company: Deloitte (campus OA, IIT Kharagpur)
- Type: MCQ (output-prediction)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/deloitee.md (Q14)
- Explanation: `p` starts at 2, `p++` makes it 3 (unused after). `static int s` defaults to 0; `++s` makes it 1; `p = ++s` sets p=1; `s = p + p = 2`; `printf` prints current `s` (2) then post-increments to 3.

---

### What is the output of the following C program?

```c
#include <stdio.h>
int main() {
    char arr[] = "abcd";
    char *p = arr;
    printf("%c\t", ++*p);
    printf("%c\t", *p++);
    printf("%c\t", (*p)++);
    printf("%c\n", *p);
    return 0;
}
```
- Options: A) b b b c B) b c c d C) b b c c D) b c c c
- Correct: A
- Company: Oracle (campus OA, IIT Kharagpur)
- Type: MCQ (output-prediction, pointer/char arithmetic — commonly grouped in "C/C++ MCQ" OA sections)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/Oracle.md (Q7 under MCQ section)
- Explanation: `++*p` increments 'a'->'b' and prints 'b'. `*p++` prints current char 'b' then advances pointer to arr[1]. `(*p)++` prints old value 'b' (arr[1] was 'b') then increments it to 'c'. Final `*p` prints 'c' (post-increment already applied). Result: "b b b c".

---

### What is the output of the following C program?

```c
#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
int main() {
    int x = 5, y = 10;
    printf("%d %d %d\n", MAX(x++, y++), x, y);
    return 0;
}
```
- Options: A) 11 6 12 B) 12 6 12 C) 11 7 12 D) 12 7 12
- Correct: A
- Company: Oracle (campus OA, IIT Kharagpur)
- Type: MCQ (output-prediction, macro side-effect pitfall)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/Oracle.md (Q23 under MCQ section)
- Explanation: Classic macro double-evaluation trap. `MAX(x++, y++)` expands to `((x++) > (y++) ? (x++) : (y++))`; the comparison evaluates `x++` and `y++` once each (x becomes 6, y becomes 11), 5>10 is false, so the false branch `(y++)` is evaluated again, returning 11 and incrementing y to 12. Final x=6, y=12, printed value 11.

---

### Which one of the following statements is correct about C preprocessor macros?

- Options: A) A macro must be defined in capital letters. B) Once preprocessing is over and the program is sent for compilation, the macros are removed from the expanded source code. C) Macros have a local scope. D) In a macro call, the control is passed to the macro.
- Correct: B
- Company: IBM (Diversity Hiring Pool Campus OA, IIT Kharagpur)
- Type: MCQ (conceptual)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/IBM%20Diversity%20Hiring%20Pool%20Campus.md (Q13)
- Explanation: The preprocessor textually expands macros before compilation; the compiler never sees the macro names, only expanded text.

---

### The `malloc()` or `realloc()` function in C/C++ allocates memory at which time/location?

- Options: A) Compilation time on stack B) Linking time on stack C) Load time on heap D) Execution time on heap E) Execution time on stack
- Correct: D
- Company: IBM (Diversity Hiring Pool Campus OA, IIT Kharagpur)
- Type: MCQ (conceptual, memory management)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/IBM%20Diversity%20Hiring%20Pool%20Campus.md (Q18)
- Explanation: `malloc`/`realloc`/`new` allocate on the heap at runtime (execution time), not compile time or stack.

---

### A circular linked list can be used to implement:

- Options: A) A queue B) A stack C) Both a queue and a stack D) Neither
- Correct: C
- Company: IBM (Diversity Hiring Pool Campus OA, IIT Kharagpur)
- Type: MCQ (conceptual, DS)
- Status: REAL
- Source: GitHub (dsainvg001/OA_QUES_PREV_YR_KGP) — https://raw.githubusercontent.com/dsainvg001/OA_QUES_PREV_YR_KGP/main/IBM%20Diversity%20Hiring%20Pool%20Campus.md (Q19)
- Explanation: With a tail pointer, both push/pop (stack) and enqueue/dequeue (queue) can be done in O(1) on a circular linked list.

---

## LinkedIn C++ Skill Assessment questions (real assessment bank; crowd-sourced with verified correct answers, widely used as an interview/screening prep source)

### What is the output of this code?

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```
- Options: A) False B) 0 C) 1 D) This code has an error.
- Correct: C
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction)
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes) — https://raw.githubusercontent.com/Ebazhanov/linkedin-skill-assessments-quizzes/main/c%2B%2B/c%2B%2B-quiz.md (Q1)
- Explanation: `vector<int> v(22)` value-initializes all 22 ints to 0, so `v[6]` is 0, `b` is false, `!b` is true → prints 1.

---

### Which of the following is a reason why using this line is considered a bad practice?

```cpp
using namespace std;
```
- Options: A) The compiled code is always bigger because of all of the imported symbols. B) If the code uses a function defined in two different libraries with the same prototype but possibly with different implementations, there will be a compilation error due to ambiguity. C) It automatically includes all header files in the standard library. D) It causes the compiler to enforce exclusive inclusion of standard-library headers.
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual)
- Status: REAL
- Source: GitHub (Ebazhanov/linkedin-skill-assessments-quizzes) — same file (Q2)
- Explanation: `using namespace std;` pulls the entire std namespace into scope, risking name collisions/ambiguity with user or third-party symbols of the same name.

---

### What is the output of the code given below?

```cpp
#include <iostream>

int main(){
    int x=10, y=20;
    std::cout << "x = " << x++ << " and y = " << --y << std::endl;
    std::cout << "x = " << x-- << " and y = " << ++y << std::endl;
    return(0);
}
```
- Options: A) `x=10,y=20` then `x=11,y=19` B) `x=11,y=19` then `x=10,y=20` C) `x=10,y=19` then `x=11,y=20` D) `x=11,y=20` then `x=10,y=19`
- Correct: C
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction)
- Status: REAL
- Source: same file (Q15)
- Explanation: `x++` prints 10 then x becomes 11; `--y` decrements first to 19 then prints 19. Second line: `x--` prints 11 then x becomes 10; `++y` increments first to 20 then prints 20.

---

### What is the output of the code given below?

```cpp
int8_t a=200;
uint8_t b=100;
if(a>b)
    std::cout<<"greater";
else
    std::cout<<"less";
```
- Options: A) Exception on comparison B) greater C) less D) Compiler error
- Correct: C
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, integer types/overflow)
- Status: REAL
- Source: same file (Q17)
- Explanation: `int8_t a = 200` overflows the signed 8-bit range and becomes -56 (implementation-defined but typical two's-complement wraparound). -56 > 100 is false, so "less" is printed.

---

### What is the output of this block of code?

```cpp
int8_t a=200;
uint8_t b=100;
std::cout<<"a="<<(int)a;
std::cout<<", b="<<(int)b;
```
- Options: A) a=-56, b=100 B) a=-55, b=100 C) a=200, b=-156 D) a=200, b=100
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction)
- Status: REAL
- Source: same file (Q18)
- Explanation: Implicit conversion of `int` literal 200 to `int8_t` (signed char) wraps around to -56; `uint8_t` holds 100 fine.

---

### What is the output after executing this code snippet?

```cpp
int x=5, y=2;
if(x & y) {
    /* part A */
}
else {
    /* part B */
}
```
- Options: A) Part A (logical AND true) B) Part B, because (x & y) is 0 C) Part A, because (x & y) is nonzero D) Part B, invalid statement
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, bitwise vs logical)
- Status: REAL
- Source: same file (Q19)
- Explanation: `&` is bitwise AND. 5 = 0b101, 2 = 0b010; bitwise AND = 0b000 = 0, so the else branch (Part B) executes.

---

### Which choice is the most reasonable implementation of `std::mutex::lock()` using `std::mutex::try_lock()`?

```cpp
// Option A
void std::mutex::lock(){
    while(!this->try_lock());
}
```
- Options: A) `while(!this->try_lock());` B) `return (this->try_lock());` C) `while(1) this->try_lock();` D) `while(this->try_lock());`
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency — HFT-relevant)
- Status: REAL
- Source: same file (Q60)
- Explanation: `lock()` should spin (busy-wait) until `try_lock()` succeeds (returns true), i.e. loop `while (!try_lock())`. Option D loops while it succeeds, which is backwards.

---

### What is the main difference between `std::mutex::lock()` and `std::mutex::try_lock()`?

- Options: A) `lock()` has higher privilege B) Both attempt to acquire the lock, but `lock()` blocks if unavailable while `try_lock()` returns immediately with success/failure C) `lock()` enforces preemption, `try_lock()` suggests it D) `try_lock()` snatches the mutex from the current owner
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency — HFT-relevant)
- Status: REAL
- Source: same file (Q61)
- Explanation: `lock()` blocks (waits) until the mutex is available; `try_lock()` attempts once and returns immediately, reporting whether it succeeded.

---

### What is a race condition in C++?

- Options: A) A condition where the program runs faster than expected B) A condition where multiple threads access shared data concurrently and the outcome depends on execution timing C) A condition where two threads compete for CPU time D) A condition where a loop executes too fast
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency — HFT-relevant)
- Status: REAL
- Source: same file (Q159)
- Explanation: A race condition arises when the correctness of a program depends on the relative timing of concurrent operations on shared data.

---

### Consider the following code that has a race condition. What is the correct way to fix it?

```cpp
#include <thread>
#include <vector>

int counter = 0;

void incrementCounter() {
    for(int i = 0; i < 1000; i++) {
        counter++;
    }
}

int main() {
    std::vector<std::thread> threads;
    for(int i = 0; i < 10; i++) {
        threads.push_back(std::thread(incrementCounter));
    }
    for(auto& t : threads) {
        t.join();
    }
    return 0;
}
```
- Options: A) Add `volatile` keyword B) Use `std::mutex` to lock/unlock around `counter++` C) Use `std::this_thread::sleep_for()` to delay each increment D) Change `counter++` to `++counter`
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency — HFT-relevant)
- Status: REAL
- Source: same file (Q160)
- Explanation: `volatile` does not provide atomicity or synchronization in C++; pre/post-increment form makes no difference to the race. A mutex (or std::atomic<int>) is needed to serialize the read-modify-write of `counter`.

---

### What is the purpose of `std::move` in C++11?

- Options: A) To copy an object to a new location B) To cast an object to an rvalue reference, enabling move semantics C) To physically move memory from one address to another D) To delete an object and create a new one
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, modern C++)
- Status: REAL
- Source: same file (Q161)
- Explanation: `std::move` is just a cast to an rvalue reference; it enables move constructors/assignment to be selected, it does not itself move anything.

---

### What is the output of this code?

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = std::move(v1);
    std::cout << v1.size() << " " << v2.size();
    return 0;
}
```
- Options: A) 3 3 B) 0 3 C) 3 0 D) Compilation error
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, move semantics)
- Status: REAL
- Source: same file (Q162)
- Explanation: After being moved-from, `v1` is left in a valid but unspecified state — for `std::vector` in practice it becomes empty (size 0); `v2` takes ownership of the original 3 elements.

---

### What is the difference between `std::unique_ptr` and `std::shared_ptr`?

- Options: A) unique_ptr has exclusive ownership, shared_ptr allows multiple owners B) unique_ptr is faster but less safe C) shared_ptr can only be used with classes D) There is no difference
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, smart pointers)
- Status: REAL
- Source: same file (Q165)
- Explanation: `unique_ptr` cannot be copied, only moved (single owner); `shared_ptr` uses atomic reference counting to allow multiple simultaneous owners.

---

### What is RAII in C++?

- Options: A) Random Access Iterator Interface B) Resource Acquisition Is Initialization C) Recursive Algorithm Implementation Interface D) Runtime Allocation and Initialization
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual)
- Status: REAL
- Source: same file (Q166)
- Explanation: RAII ties resource lifetime to object lifetime: acquire in the constructor, release in the destructor, so resources are automatically cleaned up via stack unwinding/scope exit.

---

### What is `std::atomic` used for?

- Options: A) Atomic energy calculations B) Thread-safe operations on shared variables without locks C) Atomic data types D) Indivisible operations on atoms
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency — HFT-relevant)
- Status: REAL
- Source: same file (Q190)
- Explanation: `std::atomic<T>` provides lock-free (on most platforms), thread-safe read/modify/write access to shared variables using specific memory-ordering guarantees.

---

### What is the difference between `std::mutex` and `std::recursive_mutex`?

- Options: A) recursive_mutex can be locked multiple times by the same thread B) mutex is faster C) recursive_mutex is deprecated D) There is no difference
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency)
- Status: REAL
- Source: same file (Q191)
- Explanation: A plain `std::mutex` deadlocks if the owning thread tries to lock it again; `std::recursive_mutex` tracks an owner and a lock count, allowing repeated locking by the same thread.

---

### What happens if a class has a virtual destructor but the base class pointer deletes an object of a derived class that has already been partially destructed?

- Options: A) Undefined behavior — double destruction / memory corruption B) The base destructor runs twice safely C) The compiler prevents the deletion D) The derived destructor runs twice without side effects
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, OOP/virtual destructors)
- Status: REAL
- Source: same file (Q222)
- Explanation: Deleting an already-destructed object through any pointer (virtual destructor or not) is undefined behavior — the object's lifetime has already ended.

---

### What is the purpose of the placement new operator in C++?

- Options: A) It constructs an object at a specific pre-allocated memory address B) It allocates memory on the heap and initializes the object C) It creates multiple objects in a single memory block automatically D) It performs garbage collection for dynamic memory
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, memory management — relevant to custom allocators/HFT)
- Status: REAL
- Source: same file (Q224)
- Explanation: `new (buffer) MyClass();` constructs an object in-place at `buffer` without allocating new memory — used in custom allocators and performance-critical systems.

---

### Suppose two threads access a shared variable without synchronization — one writes while the other reads. What is this condition called, and what does the standard say about it?

- Options: A) A data access warning but still well-defined behavior B) A data race, leading to undefined behavior under the C++ memory model C) Automatically handled by the compiler's memory barrier insertion D) Only a problem if both threads write
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, concurrency — HFT-relevant)
- Status: REAL
- Source: same file (Q225)
- Explanation: The C++ memory model defines an unsynchronized concurrent read/write (or write/write) to the same memory location as a data race, which is undefined behavior.

---

### Which of the following statements is TRUE about the virtual keyword when used with destructors?

- Options: A) A virtual destructor prevents object slicing automatically. B) A virtual destructor ensures dynamic binding for all member functions. C) A virtual destructor allows correct destruction of derived objects through a base class pointer. D) A virtual destructor makes the class abstract automatically.
- Correct: C
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, OOP)
- Status: REAL
- Source: same file (Q226)
- Explanation: Declaring the base destructor virtual ensures `delete basePtr;` invokes the derived class's destructor first, then the base's, avoiding resource leaks/UB. It does not prevent slicing or affect other member functions' dispatch.

---

### Which of the following correctly describes the behavior of static members in a C++ class?

- Options: A) Each object gets its own copy of every static data member. B) Static data members are shared by all objects of the class and exist even if no objects are created. C) Static member functions can access both static and non-static members directly. D) Static data members must be initialized inside the constructor of the class.
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, OOP)
- Status: REAL
- Source: same file (Q227)
- Explanation: Static data members belong to the class (one shared copy), exist independent of any instantiated object, and cannot be initialized in a constructor (they need out-of-class or inline definition); static member functions have no implicit `this`, so they cannot directly touch non-static members.

---

### What does this code print?

```cpp
int i = 0;
printf("%d", i++);
printf("%d", i--);
printf("%d", ++i);
printf("%d", --i);
```
- Options: A) 0,1,1,0 B) 0,1,0,1 C) 0,0,1,0 D) 1,0,1,0
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, increment/decrement)
- Status: REAL
- Source: same file (Q23)
- Explanation: `i++` prints 0 (i becomes 1); `i--` prints 1 (i becomes 0); `++i` prints 1 (i becomes 1); `--i` prints 0 (i becomes 0). Sequence: 0,1,1,0.

---

### What is the output of this code given below?

```cpp
#include <cstdio>
using namespace std;

int main(){
    char c = 255;
    if(c>10)
        printf("c = %i, which is greater than 10", c);
    else
        printf("c = %i, which is less than 10", c);
    return 0;
}
```
- Options: A) c = -1, which is less than 10 B) c = 255, which is greater than 10 C) c = -1, which is greater than 10 D) c = 255, which is less than 10
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, signed char overflow — implementation-defined, but typical on most compilers where `char` is signed)
- Status: REAL
- Source: same file (Q34)
- Explanation: On implementations where `char` is signed (most common: gcc/clang on x86/ARM Linux/macOS), assigning 255 wraps to -1, so -1 > 10 is false.

---

### Consider the following code segment. What will be the output?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main () {
int data[] = {50, 30, 40, 10, 20};
sort (&data[1], &data[4]);
for (int i = 0; i < 5; i++)
cout << data[i] << " ";
return 0;
}
```
- Options: A) 10 20 30 40 50 B) 10 30 40 50 20 C) 50 10 30 40 20 D) 50 10 20 30 40
- Correct: C
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, std::sort range semantics)
- Status: REAL
- Source: same file (Q110)
- Explanation: `sort(&data[1], &data[4])` sorts only the half-open range [index 1, index 4) = elements {30,40,10} → becomes {10,30,40}; index 0 (50) and index 4 (20) are untouched. Result: 50 10 30 40 20.

---

### Consider the following code segment. What will be the output?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int element[5];
for(int i = 1; i <= 5; i++)
*(element + i - 1) = i * 5;
rotate(element, element + 4, element + 5);
rotate(element, element + 1, element + 4);
for (int i = 0; i < 5; ++i)
cout << element[i] << " ";
return 0;
}
```
- Options: A) 5 10 15 20 25 B) 5 10 15 25 20 C) 20 10 15 25 5 D) 25 5 10 15 20
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, std::rotate)
- Status: REAL
- Source: same file (Q111)
- Explanation: Array starts as {5,10,15,20,25}. First `rotate(element, element+4, element+5)` moves the middle element (index 4, value 25) to the front of the [0,5) range → {25,5,10,15,20}. Second `rotate(element, element+1, element+4)` rotates range [0,4) so that index1 (5) becomes new front of that subrange → {5,10,15,25,20}.

---

### Consider the following code segment. What will be the output?

```cpp
int i = 5;
const int *p = &i;
int * const q = &i;
int const *r = &i;
int const * const s = &i;
*p = 10; //STMT-1
*q = 10; //STMT-2
*r = 10; //STMT-3
*s = 10; //STMT-4
```
- Options: A) STMT-1 is valid B) STMT-2 is valid C) STMT-3 is valid D) STMT-4 is valid
- Correct: B
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (conceptual, const-correctness — classic "const pointer vs pointer to const")
- Status: REAL
- Source: same file (Q116)
- Explanation: `p` and `r` are pointers-to-const-int (`const int *` / `int const *`, equivalent forms), so `*p =` and `*r =` are illegal. `s` is a const pointer to const int, so `*s =` is also illegal. Only `q` (`int * const`, a const pointer to non-const int) allows modifying the pointee via `*q = 10`.

---

### Consider the following code segment. What will be the output?

```cpp
#include <iostream>
using namespace std;
#define SQR(x) (x)*(x)
int main() {
int a=3;
cout << SQR(a++) << endl;
return 0;
}
```
- Options: A) 12 B) 25 C) 9 D) 16
- Correct: A
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (output-prediction, macro side-effect pitfall)
- Status: REAL
- Source: same file (Q118)
- Explanation: `SQR(a++)` expands to `(a++)*(a++)`. Order of evaluation of the two `a++` is unspecified before C++17, but a common left-to-right compiler behavior yields `3 * 4 = 12` (first `a++` returns 3, a becomes 4; second `a++` returns 4, a becomes 5). This illustrates why macros with side-effecting arguments are dangerous — prefer `inline`/templates.

---

### Consider the following program. What will be the output/error(s)?

```cpp
#include <iostream>
using namespace std;
char add(char c1 = 'a') { return c1; }
char add(char c1 = 'a', char c2 = 'b') { return c1 + c2 - 'a';}
char add(char c1 = 'a', int d1 = 100){ return c1 + d1 - 'a'; }
char add(char c1 = 'a', char c2 = 'b', char c3) { return c1 + c2 + c3 - 'a'; }
int main() {
char c = add('o', 'k');
cout << c << endl;
return 0;
}
```
- Options: A) y B) z C) Compilation Error: default argument missing for "char add(char, char, char)" D) Compilation Error: call of overload "add(char, char)" is ambiguous
- Correct: C and D (both compile errors apply — a required parameter after defaulted ones, and an ambiguous overload resolution between `add(char,char)` and `add(char,int)`)
- Company: LinkedIn Skill Assessment (general)
- Type: MCQ (multi-select, output-prediction/overload resolution)
- Status: REAL
- Source: same file (Q117)
- Explanation: `add(char,char,char)` has `c3` without a default value after two defaulted parameters — invalid. Separately, `add('o','k')` is ambiguous between `add(char,char)` and `add(char,int)` since 'k' can implicitly convert to int.

---

## Summary of sourcing

- The Deloitte / Oracle / IBM entries above come from a leaked/crowd-sourced "OA questions from previous years" repository maintained by an IIT Kharagpur student, organized by company (the same repo also has D. E. Shaw, Millennium, and Neo Wealth folders, but those only contained open-ended DSA/SQL coding questions, no MCQs, in this pass).
- The LinkedIn entries come from the well-known `Ebazhanov/linkedin-skill-assessments-quizzes` repo, which crowd-sources actual questions seen on LinkedIn's official "C++" Skill Assessment test (a real, still-live assessment product, not company-specific but genuinely used to certify skills / screen candidates), with community-verified correct answers marked via `[x]`.
