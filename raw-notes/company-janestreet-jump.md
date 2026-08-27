# Jane Street & Jump Trading — Real Reported Interview / OA Questions (SWE / Quant Dev / C++ focus)

## Jane Street

### Build/Design Tetris (implement the game state / core logic, no UI required)
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite technical/coding round (~75 min); also reported as one of several final-round questions after a phone screen
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20240910034014/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm ; corroborated by interviewing.io — https://interviewing.io/jane-street-interview-questions
- Answer/Discussion: Candidate (US, Feb 2024, difficulty "Difficult", no offer) reported: "Several questions. One involving Tetris. Generally fast paced. Implementation accuracy is important... phone question, then 3 final rounds." interviewing.io separately lists "Design Tetris" as a ~75-min onsite round requiring candidates to design, code, and explore the logic in depth, with clarifying questions expected before implementation (underspecified problem statement style).

### Design a video player API
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite technical/coding round (~75 min)
- Status: REAL
- Source: interviewing.io — https://interviewing.io/jane-street-interview-questions
- Answer/Discussion: Listed alongside "Design Tetris" as one of the onsite design+implementation problems; candidates are expected to ask clarifying questions since the prompt is deliberately underspecified, then design and implement, going deep on logic/edge cases.

### Implement the game state for a variant of Connect Four with infinite width (columns), pieces enter from the bottom
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Remote tech screen (Coderpad) → onsite with 3 similar coding questions + "explain a past project" question
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20240910034014/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (New York, accepted offer, Feb 2024): "One round of remote tech screen with a relatively straightforward (but fun!) coding question on Coderpad, an onsite with three more similar coding questions and one 'explain a past project to us' question." Rated Average difficulty.

### Build a Connect-Four-style board game ("puissance 4") with infinite columns of infinite height; implement a `move` function and a `checkWin` function that detects a column of consecutive same-color pieces
- Company: Jane Street
- Role: Software Engineer / Software Developer
- Type: Interview
- Round/Stage: Phone interview, after a 1.5-hour HackerRank online test
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220902013314/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (Hastings-on-Hudson, NY, 2021, no offer): "J'ai d'abord eu un test en ligne d'1h30 sur HackerRank, après quoi j'ai eu un entretien téléphonique... Il m'a posé quelques questions générales sur les paradigmes de programmation, puis il m'a demandé de coder un jeu." Rules: infinite horizontal indices, two players (R/B) drop pieces which stack at the bottom of a column; implement `move(index)` then `checkWin()` checking for a run of same-player pieces in a column. (Same family of question as the Connect-Four variant above — recurring question type at Jane Street.)

### "To make a stack machine"
- Company: Jane Street
- Role: Software Developer
- Type: Interview
- Round/Stage: Single ~1 hour interview
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20240910034014/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (London, Dec 2023, no offer): "Simple, 1h interview, and the questions were straightforward and interesting. The selection process is very hard after the interview, with a big emphasis on the small details, which one does not think about during the interview."

### Implement custom stack with various operations on it
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Phone interview
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220808060706/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (Poland, Nov 2021, accepted... note: this specific review says "no offer" for this one, difficulty Average): "Got a phone call and needed to explain my process of implementing data structure. Little algorithm knowledge needed. No personal questions or tests of university's knowledge. Worked on a text editor so no test checking either."

### "Standard algorithmic interview questions, a bit related to time complexity analyses" (OCaml not required/tested)
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Screening interview (1 hr algorithmic task) → final round with three similar sessions
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220808060706/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (Hong Kong, Nov 2021, accepted offer): "One screening interview consisting of one 1-hour session with an algorithmic task, then one final interview with three similar sessions. There weren't any technical [language] questions. The language that the company uses, OCaml, wasn't needed." Useful data point: Jane Street's coding rounds are language-agnostic and don't require prior OCaml knowledge.

### "Data structure question using Python"
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Round 2 (after a phone screen focused on background/networking)
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220808060706/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (United States, Oct 2021, no offer): "2 rounds, phone interview then interview with tech team... phone interview was mostly about myself, previous experience and a few questions on the tech side of things mostly geared towards networking. then the 2nd round was meeting the tech team 2 at a time interviews varied from programming to normal interview questions." No further detail on the exact DS problem.

### "Optimal solution for flipping coin games with opponent" (game-theory/expected-value coding problem, no scratch paper allowed)
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite, mathematical/algorithmic round
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220808060706/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (Hong Kong, Oct 2021, no offer): "There was a bunch of challenging mathematical questions, including probabilities. The interview did not allow any scratch paper, and rather expected me to show how I interpreted the question and how I will solve the problem." Borderline quant-puzzle but reported under the Software Engineer interview track.

### "Leetcode style questions" given in multiple sequential steps; must run/debug code without ability to execute it for correctness during interview
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Unspecified coding round (7-day process)
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20240910034014/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (United States, June 2024, no offer, Difficult): "The questions they ask are in multiple steps. Make sure you make it to the final step if you even want a chance to proceed... the company claims to take a 'holistic' approach to interviewing but at the same time values 'complete and correct code' without allowing the interviewee to run their code for correctness." Useful process insight: expect multi-step/escalating coding prompts and no code execution in some rounds.

### Onsite format: 2 technical phone screenings (hardest coding problem in this stage) + 4 onsite rounds = 2 implementation-heavy coding interviews + 2 system-design interviews (one being "walk through a system you developed")
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Full loop (phone screen → 2 tech screens → 4 onsite rounds)
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20240910034014/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (New York, accepted offer, interviewed April 2024): "Coding problems seemed more implementation intense... interviewers have a strong emphasis on writing clean, understandable code. Communication and collaborating with the interviewer also appears important, solving the problem perfectly doesn't seem to be as important... One of the system design interviews was walking through a system you developed (I believe system design questions are only asked to lateral/experienced applicants)... I am told Jane Street doesn't have behavioral rounds for engineers in general." Also: "Although the questions interviewers ask aren't inherently difficult on the surface... it feels like the criteria they're using to judge you is more wholistic and stricter than other companies."

### "Behavioural and coding questions and systems design" (full-day onsite)
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Full-day onsite, London
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20240910034014/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (London, Feb 2024, no offer, Difficult): "Tough interview but fair questions. Interview takes place over most of the day and lots of coding and system design questions, some behavioural questions in the afternoon."

### "Can't disclose due to NDA but questions tend to involve considerable coding" — full loop: phone screen + 3×1hr coding interviews + 1 project-discussion interview, 2 interviewers per session
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Onsite day (after phone screen)
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220808060706/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (Poland, accepted offer, Nov 2021, Difficult): "Three 1 hr coding interviews + 1 project discussion interview on the day of onsite and 1 phone screen interview previously. Very smoothly run with 2 interviewers in each interview." No specific problem text given (candidate declined to share, citing NDA) but structure confirmed.

### Given a list of users and their login events (Success/Fail), flag users who have failed login exactly k times consecutively (similar to "Max Consecutive Ones")
- Company: Jane Street
- Role: Data Engineer
- Type: Interview
- Round/Stage: Round 1 — Problem Solving (Hong Kong)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/post/7701675/
- Answer/Discussion: Candidate initially missed an edge case, debugged live and fixed it, but was still rejected — attributed by the candidate to Jane Street expecting "completely flawless first-pass execution."

### Given a set of encoded "moves," write a function to encode a move, and a separate function to detect/execute a move once its full input sequence has been streamed into memory (O(n) target)
- Company: Jane Street
- Role: Software Engineer Intern
- Type: Interview
- Round/Stage: Intern technical interview
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/882072/jane-street-intern-interview/
- Answer/Discussion: OP's approach: dictionary keyed by move sequences (tuples), values = move names; check suffixes of the input stream against registered sequences. A commenter noted this closely resembles LeetCode "Stream of Characters" and suggested a Trie-based streaming matcher (track active partial matches, emit the move name when a full sequence completes). OP was ultimately rejected.

### Graduate Trade Desk Operations Engineer (TDOE) London — process note (no single verbatim technical question surfaced): take-home test → mathematical problem-solving interview → technical coding interview; candidates are sent a "getting started" doc that is essentially plain Python syntax beforehand
- Company: Jane Street
- Role: Graduate Trade Desk Operations Engineer
- Type: Interview
- Round/Stage: Multi-stage (take-home, math interview, then coding interview)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/post/6340012/Jane-Street-or-TDOEor-London-or-Technical-or-What-to-expect/
- Answer/Discussion: Poster (graduating MSci CS, London, Jan 2025) confirmed passing the take-home test and math interview and was awaiting the technical coding round; no one in the thread's comments disclosed the actual coding questions. Included for process-stage accuracy rather than as a specific question.

### "What is an estimate of odd numbers from 0 to 60" (candidate-phrased; likely a fast-estimation/mental-math style prompt)
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Round/Stage: Single interview
- Status: REAL
- Source: Glassdoor (archived) — https://web.archive.org/web/20220808060706/https://www.glassdoor.com/Interview/Jane-Street-Software-Engineer-Interview-Questions-EI_IE255549.0,11_KO12,29.htm
- Answer/Discussion: Candidate (United Kingdom, Jan 2022, no offer, Easy): "Late to the interview, and they were very pushy and not very welcoming... but i answered the questions right." No further elaboration on exact intent of the question.

---

## Jump Trading

### Given a string consisting only of letters 'a' and 'b', determine whether it is "valid" — valid means every 'a' occurs before every 'b' (i.e., all a's, then all b's)
- Company: Jump Trading
- Role: Summer Intern (Quant)
- Type: OA
- Round/Stage: Online Assessment (3 questions, 105-minute window)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/870149/jump-trading-oa-2020-summer-internquant
- Answer/Discussion: OP solved this in the first part of a 45-minute total solve time; no code/solution posted in thread, no comments given.

### Garden/trees dynamic-programming problem — trees of varying heights, each with an associated cost (exact prompt lost; referenced an external Chegg link)
- Company: Jump Trading
- Role: Summer Intern (Quant)
- Type: OA
- Round/Stage: Online Assessment (same 2020 OA as above, Question 2 of 3)
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/870149/jump-trading-oa-2020-summer-internquant
- Answer/Discussion: Full text not preserved (linked to now-dead Chegg page); a commenter asked for the solution but none was given. Flagged as thin — topic (tree-height/cost DP) is the only detail that survives.

### Find the maximum distance between two different (unequal-valued) elements in an array
- Company: Jump Trading
- Role: unknown (general SWE/OA prep thread)
- Type: OA
- Round/Stage: Codility-administered OA
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/686727/jump-trading-codility/
- Answer/Discussion: Example: `[4, 6, 2, 2, 6, 6, 4]` → answer 5. O(n) approach discussed: "Check if first and last element are same. If they are not, you have the answer. If they are same, then check for index i for which A[i] != A[0]." Alternative approach: for each element compute distance to farthest differing element using a set to track already-seen values, scanning from the array's end inward.

### Second Codility OA question referenced only via an attached image (not recoverable as text) — a commenter suggested the intended solution involved implementing iterator interfaces / `istream_iterator` with custom comment/delimiter handling
- Company: Jump Trading
- Role: unknown
- Type: OA
- Round/Stage: Codility-administered OA
- Status: REAL
- Source: LeetCode Discuss — https://leetcode.com/discuss/interview-question/686727/jump-trading-codility/
- Answer/Discussion: Question text unrecoverable (image-only in original post); noted here only because the discussion hints at a C++ `istream_iterator`/stream-parsing style problem, which fits Jump's C++-heavy stack. Flagged thin/low-confidence.

### General C/pointers/arrays questions; "How would you store key-value pairs?"; implement a hash map from scratch — add(key, value) and get(key) methods; discuss tradeoffs between different hash map implementations; general resume/past-internship questions
- Company: Jump Trading
- Role: Software Development Intern (Engineering group)
- Type: Interview
- Round/Stage: In-person technical interview (after a behavioral phone screen), Cambridge office
- Status: REAL
- Source: Wall Street Oasis — https://www.wallstreetoasis.com/company/jump-trading/interview
- Answer/Discussion: Candidate (Aug 2019, no offer): "No difficult questions, just general questions about my resume, then general questions about C and pointers and arrays. Then I was asked about how I would store key value pairs. And then ended in a discussion about how I would implement a hash map data structure. I was asked about the tradeoffs between various implementations. I had to implement methods to add the key to the hashmap and method to retrieve a key from the hashmap."

### Whiteboard interview, two parts: (1) Convert a decimal number to its 16-bit binary representation; (2) Represent that binary as a 4×4 matrix of 0s/1s, then detect whether a path of 0s exists from the top-left to the bottom-right cell — if so print the path as a string, otherwise return "No path"
- Company: Jump Trading
- Role: Software (campus/new-grad), on-campus recruiting
- Type: Interview
- Round/Stage: Round 1 — on-campus whiteboard interview with two engineers (45 min); passing led to a full onsite day in Chicago
- Status: REAL
- Source: Wall Street Oasis — https://www.wallstreetoasis.com/company/jump-trading/interview
- Answer/Discussion: Candidate (Urbana campus recruiting, Sept 2017, no offer): "The interview was 45 minutes long and consisted of a straightforward whiteboard question with two separate tasks... Interviewers were nice and gave hints as to how to solve the problem. They let you use any language you want."

### Implement a trie in C++
- Company: Jump Trading
- Role: Algorithmic Trading Intern
- Type: Interview
- Round/Stage: Onsite "superday" — one of 4 rounds; this was the pure-coding-on-laptop round (C++)
- Status: REAL
- Source: Wall Street Oasis — https://www.wallstreetoasis.com/company/jump-trading/interview
- Answer/Discussion: Candidate (Chicago, March 2013, no offer): superday had 4 rounds — pure C++ coding round, a whiteboard math/linear-algebra round, and two pen/paper brainteaser/probability rounds. "There isn't really a way to game their system besides just knowing how to solve data structures, algorithms, and probability questions."

### Swap two variables without using any additional storage (no temp variable)
- Company: Jump Trading
- Role: Algorithmic Trading Intern
- Type: Interview
- Round/Stage: Onsite "superday," coding round (same session as the trie question)
- Status: REAL
- Source: Wall Street Oasis — https://www.wallstreetoasis.com/company/jump-trading/interview
- Answer/Discussion: Classic XOR-swap or arithmetic-swap answer expected; no explicit solution given in the source, but this is a well-known technique (`a ^= b; b ^= a; a ^= b;` for integers, or `a = a+b; b = a-b; a = a-b;`).

### How many trailing zeros are in 1000! (factorial)?
- Company: Jump Trading
- Role: Algorithmic Trading Intern
- Type: Interview
- Round/Stage: Onsite "superday" (paired with the trie/swap questions in the same loop)
- Status: REAL
- Source: Wall Street Oasis — https://www.wallstreetoasis.com/company/jump-trading/interview
- Answer/Discussion: Classic answer approach: count factors of 5 in 1000! via floor(1000/5) + floor(1000/25) + floor(1000/125) + floor(1000/625) = 200+40+8+1 = 249 trailing zeros. No solution given verbatim in the source thread.

### Can you create a linked list? Implement it. Then: write a function to swap the positions of two given nodes in a linked list.
- Company: Jump Trading
- Role: Quantitative Researcher (Zoom interview)
- Type: Interview
- Round/Stage: Single Zoom interview round (~1 week after applying online)
- Status: REAL
- Source: Wall Street Oasis — https://www.wallstreetoasis.com/company/jump-trading/interview
- Answer/Discussion: Candidate (Oct 2022, no offer): "1) Can you create a linked list? Do it. 2) Let's say we want to change places of 2 nodes in linked list. Can you create a function for that." Included despite "Quantitative Researcher" title because it's a pure C++/DS coding question overlapping heavily with what a Quant Developer would face; the same review also had an unrelated probability/timestamp question omitted here as out-of-scope trading-puzzle content.

### On-campus interview, tough on-site follow-up (4 hours); questions "fairly difficult and focused on concurrency, mainly in C/C++" (specific questions not recoverable — review truncated behind Glassdoor's old paywall)
- Company: Jump Trading
- Role: Software Engineer
- Type: Interview
- Round/Stage: On-campus interview → 4-hour onsite
- Status: REAL
- Source: Glassdoor (archived, 2010) — https://web.archive.org/web/20101201015522/http://www.glassdoor.com:80/Interview/Jump-Trading-Interview-Questions-E251744.htm
- Answer/Discussion: Full review text is cut off ("...The questions were very…") in this 2010-era cached snapshot because Glassdoor paywalled full reviews at the time; only the topic area (C/C++ concurrency) survives. Included as a real, if thin, data point that Jump's SWE interviews have historically emphasized concurrency in C/C++.

### Auction (title only — full question text not recoverable)
- Company: Jump Trading
- Role: unknown
- Type: Unknown (listed under Coding/Phone stage)
- Round/Stage: Phone
- Status: REAL (per aggregator metadata; verbatim text unavailable)
- Source: InterviewDB — https://www.interviewdb.io/question/jumptrading
- Answer/Discussion: none found — page requires JS rendering/login; only the title and stage tag ("Coding, Phone") were recoverable.

### Card Set Detection (title only — full question text not recoverable)
- Company: Jump Trading
- Role: unknown
- Type: OA
- Round/Stage: OA
- Status: REAL (per aggregator metadata; verbatim text unavailable)
- Source: InterviewDB — https://www.interviewdb.io/question/jumptrading
- Answer/Discussion: none found

### Executable File Query Analyzer (title only — full question text not recoverable)
- Company: Jump Trading
- Role: unknown
- Type: OA
- Round/Stage: OA
- Status: REAL (per aggregator metadata; verbatim text unavailable)
- Source: InterviewDB — https://www.interviewdb.io/question/jumptrading
- Answer/Discussion: none found

### Symbol Tracker (title only — full question text not recoverable)
- Company: Jump Trading
- Role: unknown
- Type: Unknown (Coding/Phone/Onsite)
- Round/Stage: Phone or Onsite
- Status: REAL (per aggregator metadata; verbatim text unavailable)
- Source: InterviewDB — https://www.interviewdb.io/question/jumptrading
- Answer/Discussion: none found

### User Creation Endpoint (title only — full question text not recoverable; likely an API/backend design or implementation exercise)
- Company: Jump Trading
- Role: unknown
- Type: OA
- Round/Stage: OA
- Status: REAL (per aggregator metadata; verbatim text unavailable)
- Source: InterviewDB — https://www.interviewdb.io/question/jumptrading
- Answer/Discussion: none found

### Networking and OS Conceptual Questions (title only — full question text not recoverable; conceptual, non-coding)
- Company: Jump Trading
- Role: unknown
- Type: Unknown (Phone/Onsite)
- Round/Stage: Phone or Onsite
- Status: REAL (per aggregator metadata; verbatim text unavailable)
- Source: InterviewDB — https://www.interviewdb.io/question/jumptrading
- Answer/Discussion: none found
