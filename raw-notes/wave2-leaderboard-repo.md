# Wave 2 — Leader-board/OA-and-Interviews GitHub repo (non-Tibra/Rokos entries)

### IQ examination stage: 50 questions, 15 minutes, no skip/return, covering math, English (including vocabulary), and logical reasoning
- Company: Maverick Derivatives
- Role: Junior Quant Trader
- Type: OA
- Round/Stage: Stage 1 (automatic IQ test)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2020-21/Maverick%20Derivatives/Junior%20Quant%20Trader.md
- Answer/Discussion: none found (no specific questions recorded, only format description)

### HackerRank examination: 75 minutes, 4 questions — two LeetCode Mediums and two LeetCode Hards (both DP); candidate ran out of time on the last one. Language required was Python despite the platform allowing any language.
- Company: Maverick Derivatives
- Role: Junior Quant Trader
- Type: OA
- Round/Stage: Stage 2 (HackerRank exam)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2020-21/Maverick%20Derivatives/Junior%20Quant%20Trader.md
- Answer/Discussion: none found

### HackerRank entrance exam: pick any 2 of 3 LeetCode Mediums (one simulation-based greedy, one standard greedy, one simple memoisation/pre-computation), done in C++ or Python; third question counted as bonus. Interviewer explicitly asked for code cleanliness/readability, not just correctness.
- Company: Akuna Capital
- Role: Junior Quantitative Researcher
- Type: OA
- Round/Stage: Stage 1 (HackerRank entrance exam)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Akuna%20Capital/Junior%20Quantitative%20Researcher.md
- Answer/Discussion: Candidate did test in C++, solved all 3, but hit an intermittent test-case failure on Q1 suspected to be a subtle memory-leak-type bug.

### One-way mathematical video interview: five math questions ranging from tricky probability questions (e.g., working with moments) to checking whether an integral diverges/converges; candidate given 5 minutes to think AND answer each, no notes allowed, final numeric answer required.
- Company: Akuna Capital
- Role: Junior Quantitative Researcher
- Type: Interview
- Round/Stage: Stage 2 (one-way video math interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Akuna%20Capital/Junior%20Quantitative%20Researcher.md (referenced screenshot: media/akuna1.png)
- Answer/Discussion: Candidate reports getting only about one of the five right, but still advanced to the next stage anyway.

### Technical interview: a tricky probability problem involving expectations (exact wording withheld per candidate's agreement with company not to share); candidate applied conditioning repeatedly but could not fully solve it
- Company: Akuna Capital
- Role: Junior Quantitative Researcher
- Type: Interview
- Round/Stage: Stage 3 (technical interview with quant team member, via HackerRank CodePair)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Akuna%20Capital/Junior%20Quantitative%20Researcher.md
- Answer/Discussion: Candidate did not solve it; no coding questions were given in this round despite the CodePair platform being used. Rejection feedback cited wanting "stronger proficiency in probability and statistics, as well as strong coding skills."

### LeetCode "Design Underground System" (https://leetcode.com/problems/design-underground-system) — describe approach, code it (asked to use a class), then give time/space complexity; follow-up: is there a way to avoid using a pair (hint toward string concatenation)? Follow-up 2: what if a user can lose their card (garbage-collect stale entries so hashmap doesn't grow unbounded)?
- Company: Bloomberg
- Role: 2022 Software Engineer
- Type: Interview
- Round/Stage: First round (phone, HackerRank CodePair)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Bloomberg/Software%20Engineer.md (screenshot: media/bloomberg1.png)
- Answer/Discussion: Candidate solved it, described time/space complexity correctly, and proposed a garbage-collection idea for the follow-up. Advanced to onsite. Cited as "the most popular Bloomberg problem in the last 6 months" per krishnadey30/LeetCode-Questions-CompanyWise repo.

### Variant of "All Paths From Source to Target" (https://leetcode.com/problems/all-paths-from-source-to-target/): end node is given (not just target=n-1), and the graph is NOT guaranteed acyclic (though no multigraphs). DFS/backtracking approach required; then give time and space complexity (worst case is a complete graph K_n).
- Company: Bloomberg
- Role: 2022 Software Engineer
- Type: Interview
- Round/Stage: Onsite Part 1, Question 1
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Bloomberg/Software%20Engineer.md (screenshots: media/bloomberg2.png, media/bloomberg3.png)
- Answer/Discussion: Candidate gave DFS with a LinkedHashSet (initially without backtracking), fixed by deleting the node after each recursion. Messed up worst-case time complexity — said O(n^2) (edge count of complete graph) instead of the correct O((n-1)!) / O(n!) path count; interviewer had to correct him. Number-of-paths-in-complete-graph reasoning: from node 1 there are (n-1) choices, then (n-2), etc., giving (n-1)! paths.

### Collatz conjecture problem, framed "from a production point of view": (1) what is the time complexity of the naive recursive version? (2) what issues could the naive version have in production? (3) how can performance be optimized in an amortised manner? (4) how would you clean up the code?
- Company: Bloomberg
- Role: 2022 Software Engineer
- Type: Interview
- Round/Stage: Onsite Part 1, Question 2
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Bloomberg/Software%20Engineer.md (screenshot: media/bloomberg4.png; also referenced: https://leetcode.com/discuss/interview-experience/1504782/bloomberg-phone-interview-1042021-collatz-conjecture-rejection)
- Answer/Discussion: (1) No time complexity bound possible since it's an open conjecture — confirmed correct. (2) Candidate initially guessed overflow/time; correct answer per interviewer was recursion stack-space exhaustion. (3) Fixed via memoisation (candidate's first memoised solution didn't work for the given example and had to be rewritten). (4) Candidate made suggestions on cleanup but was unsure if convincing.

### Behavioral: "cheeky" question about resolving conflicts in a team project; standard "Why Bloomberg" / describe a project / tell me about yourself
- Company: Bloomberg
- Role: 2022 Software Engineer
- Type: Interview
- Round/Stage: First round and Onsite Part 1
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Bloomberg/Software%20Engineer.md
- Answer/Discussion: Feedback call (paraphrased notes) said candidate's technical performance was reasonable/good in both rounds, but weak communication skills and weak/inconsistent "Why Bloomberg" answers were cited as the actual reason for rejection — not the technical mistakes.

### "Do you require visa sponsorship?" (asked after a largely non-technical HR screen)
- Company: Epoch Capital
- Role: Quant Analyst
- Type: Interview
- Round/Stage: First (HR/non-technical) interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Epoch%20Capital/Quant%20Analyst.md
- Answer/Discussion: Candidate answered yes (needed sponsorship); interviewer explained Australia's 482 visa requires 2 years' relevant experience, so they could not proceed, and suggested watching London openings instead. Candidate was rejected shortly after.

### Immersive online assessment (auto-sent after application): situational judgement, reading comprehension, and mathematics sections, untimed
- Company: HSBC
- Role: Markets & Securities Services - Quantitative Finance - Full-Time Associate Programme
- Type: OA
- Round/Stage: Stage 1
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/HSBC/Markets%20%26%20Securities%20Services%20-%20Quantitative%20Finance%20-%20Full-Time%20Associate%20Programme.md
- Answer/Discussion: Candidate passed. Received a generic strengths/development-areas feedback report (Critical Analyst, Numerical Reasoning, We Take Responsibility as strengths; Learning Agility as a development area) that candidate found unhelpful/generic.

### Hirevue "Job Simulation" assessment (~35 min): video question giving a schedule with constraints that cannot all be satisfied (how would you arrange it?); video behavioral/SJT-style questions; SJT questions around data; personality questions; written email-response question analyzing data
- Company: HSBC
- Role: Markets & Securities Services - Quantitative Finance - Full-Time Associate Programme
- Type: OA
- Round/Stage: Stage 2 (Hirevue job simulation)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/HSBC/Markets%20%26%20Securities%20Services%20-%20Quantitative%20Finance%20-%20Full-Time%20Associate%20Programme.md
- Answer/Discussion: Candidate failed here (no individual feedback given — form rejection citing comparison to a benchmark group). Candidate notes surprise this "quant finance" role's assessment had no quantitative/coding content, testing the same as a generic markets role.

### HackerRank entrance exam Q1: a slightly ambiguous LeetCode Medium requiring chaining a pair of 1-D DP arrays
- Company: Improbable
- Role: Graduate Applied Scientist, Defence - 2022 Start
- Type: OA
- Round/Stage: Entrance exam (75 min, 2 questions)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Improbable/Graduate%20Applied%20Scientist%2C%20Defence%20-%202022%20Start.md
- Answer/Discussion: Candidate hit a few false starts due to ambiguity, took longer than desired but completed it. Company stated a full mark was not required to progress.

### HackerRank entrance exam Q2: a LeetCode Hard tricky subsequence problem — reducible to O(n^2) via sorting + two pointers, with an O(n log n) solution possible via an improved two-pointer approach
- Company: Improbable
- Role: Graduate Applied Scientist, Defence - 2022 Start
- Type: OA
- Round/Stage: Entrance exam (75 min, 2 questions)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Improbable/Graduate%20Applied%20Scientist%2C%20Defence%20-%202022%20Start.md
- Answer/Discussion: Candidate got the O(n^2) sort+2-pointer version working (14/15 test cases) but ran out of time optimizing to O(n log n). Notes the brute-force O(n·2^n) approach would not have passed most test cases (too large n).

### Stage 1 HackerRank exam: Math/ML MCQ section (7 questions, 20 min) on probability, statistics, and basic ML, followed by coding section — one LeetCode Easy (greedy), one LeetCode Medium (stack-based), one LeetCode Medium (tricky 2D DP); sections were strictly sectional/timed with no going back once a section was exited
- Company: Maven Securities
- Role: Quant Researcher
- Type: OA
- Round/Stage: Stage 1 entrance exam
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Maven%20Securities/Quant%20Researcher.md
- Answer/Discussion: Candidate fully solved the MCQ and first two coding questions; ran out of time fixing a bug in the 2D DP memoisation table for Q3 (figured out the fix minutes after the test ended). Notes that the strict sectional time limits prevented "banking" spare time across sections.

### Stage 2 HackerRank exam: 4-hour data science/ML take-home-style problem requiring a statistical/ML modeling approach (question and code pixelated per repo policy)
- Company: Maven Securities
- Role: Quant Researcher
- Type: OA
- Round/Stage: Stage 2 entrance exam
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Maven%20Securities/Quant%20Researcher.md (screenshot: media/maven1.png)
- Answer/Discussion: Candidate used a Bayesian inference approach (deducing the best posterior from the available prior to solve a maximisation problem), but suspects — since the problem referenced using a "pickle" which his solution did not — that this was not the intended approach. This was the stage candidate ultimately failed at.

### (Prior-year, referenced in prelude) Codility entrance exam: a LeetCode Medium flood-fill problem, 150 minutes
- Company: Maven Securities
- Role: Graduate Software Engineer (2020-21 season, referenced in the Quant Researcher writeup's prelude)
- Type: OA
- Round/Stage: Entrance exam
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Maven%20Securities/Quant%20Researcher.md
- Answer/Discussion: Candidate passed this exam but failed at the subsequent one-way video interview stage. Company FAQ states unsuccessful graduate-programme applicants face a permanent re-application ban for graduate roles specifically (candidate confirmed this via email with recruiting).

### Shuffled deck of cards on a stack: find probability of drawing a certain type of card, then find the expectation, then find a 95% confidence interval for the scenario
- Company: Mustard Systems
- Role: Graduate Trading Operations Analyst (renamed Data Scientist mid-process)
- Type: Interview
- Round/Stage: Onsite interview (with Head of Trading remote + in-person Quant team member)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Candidate solved the probability and expectation parts independently; needed guidance on the confidence-interval part (had not formally studied statistics, only probability) but got there combining probability knowledge with interviewer hints.

### "Heard on the Street" Chapter-4-style question: are two bets with the same expected return the same?
- Company: Mustard Systems
- Role: Graduate Trading Operations Analyst
- Type: Interview
- Round/Stage: Onsite interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Answer is No — because variance must also be considered even when expected return is equal. Candidate got the base version right; struggled more on a harder variant.

### Sharpe ratio question (definition given), solved using properties of the normal distribution
- Company: Mustard Systems
- Role: Graduate Trading Operations Analyst
- Type: Interview
- Round/Stage: Onsite interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Candidate got it quickly by applying normal-distribution properties.

### Six dogs, two reviewers scoring each dog: statistical reasoning question — one reviewer gave a dog a 0/100; should this be ignored when summarising the data? Why might a mark of 0 be given, and what mark should the dog "really" have gotten?
- Company: Mustard Systems
- Role: Graduate Trading Operations Analyst
- Type: Interview
- Round/Stage: Onsite interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Candidate found this "a little ML-ish" (outlier handling); no explicit final answer recorded in the writeup.

### Horse-betting model-validation question: given a model that predicts probability of horse A beating horse B (e.g. P(A wins)=0.7) and the actual race result (A won), how would you check whether the model is accurate? Follow-up reduced the amount of information available (about how much info was needed to identify the horse).
- Company: Mustard Systems
- Role: Graduate Trading Operations Analyst
- Type: Interview
- Round/Stage: Onsite interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Candidate needed clarification to understand the question but got the follow-up as well. Noted as feeling "even more related to machine learning."

### "Table of Bets" take-home exam: given a CSV dataset of fictional (but realistic) horse bets, summarise the data, identify subsets where betting would be favorable (with relevant statistics such as confidence intervals), and determine whether a new bet should be staked
- Company: Mustard Systems
- Role: Data Scientist (role renamed from Graduate Trading Operations Analyst)
- Type: OA
- Round/Stage: Take-home exam (post-onsite)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Candidate failed this stage. Actual written feedback obtained: exposition was clear, but analysing each variable in isolation (e.g. going, distance) was insufficient — expected a model predicting a bet's profitability from a game's/state's combined attributes (going, number of runners, race type), plus an overall-profitability analysis including Sharpe ratio and consistency of the strategy.

### Behavioral: how would you handle situations where you don't know the underlying theory/concept off-hand ("volatility")? How would you handle not knowing information off-hand (using a CV/project example)?
- Company: Mustard Systems
- Role: Graduate Trading Operations Analyst
- Type: Interview
- Round/Stage: Onsite interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Mustard%20Systems/Graduate%20Trading%20Operations%20Analyst.md
- Answer/Discussion: Candidate used an undergraduate research example.

### Mathematical entrance exam: 14 questions, 20 minutes total, mainly probability with a focus on expectations plus a couple of brain-teasers; mix of MCQ and fill-in-the-blank (usually integer answers)
- Company: SIG (Susquehanna)
- Role: Quantitative Trader - 2022 Programme
- Type: OA
- Round/Stage: Entrance exam (not automatic — given selectively)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md
- Answer/Discussion: Candidate later obtained via GDPR a full copy of the actual exam questions plus statistical benchmarking data on his performance vs. other candidates (screenshots media/sig1.png, media/sig2.png — not shareable per repo policy, but confirms this exam is recycled across candidates).

### "Matching heads" problem: given a set of three coin tosses with a certain probability, and a bet paying out (e.g. £3) for a specific outcome (e.g. two heads and a tail) or £0 otherwise, is the bet worth taking for a given price? (Solve via a probability table then compute expectation.)
- Company: SIG (Susquehanna)
- Role: Quantitative Trader - 2022 Programme
- Type: Interview
- Round/Stage: Round 1 (recruiter interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md
- Answer/Discussion: Candidate solved it, though recruiter comments obtained later via GDPR note he "had seen something very similar to Matching Heads, so [interviewer didn't] feel like that counts for much."

### "Painting" question: given a scenario with a stated probability the painting is real vs. fake, find its expected value; harder variant of the same question also asked
- Company: SIG (Susquehanna)
- Role: Quantitative Trader - 2022 Programme
- Type: Interview
- Round/Stage: Round 1 (recruiter interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md
- Answer/Discussion: Candidate got the base question but performed worse on the harder variant (self-scored a "3"). Per recruiter comments via GDPR: candidate was "on the wrong path" for 2 of the 4 probability questions and needed hints.

### "Box game" — find the expected number of boxes to open (exact scenario not fully recalled by candidate)
- Company: SIG (Susquehanna)
- Role: Quantitative Trader - 2022 Programme
- Type: Interview
- Round/Stage: Round 1 (recruiter interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md
- Answer/Discussion: none found (candidate could not recall details of his own answer)

### "Three biased coins" Bayes' theorem problem: given a fair coin, a coin with only heads, and a coin with only tails (or similarly differing probabilities) — pick a random coin, flip it, observe heads — what is the probability it was a specific coin (e.g. coin 2)?
- Company: SIG (Susquehanna)
- Role: Quantitative Trader - 2022 Programme
- Type: Interview
- Round/Stage: Round 1 (recruiter interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md
- Answer/Discussion: Candidate reports getting this one, per his own recollection.

### Non-technical: "How did you do so well in your undergraduate [given only a low First]?" and "What would your research supervisor say about you?"
- Company: SIG (Susquehanna)
- Role: Quantitative Trader - 2022 Programme
- Type: Interview
- Round/Stage: Round 1 (recruiter interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md
- Answer/Discussion: Per GDPR-obtained interviewer notes, candidate's "softs seemed fine without probing him too hard"; overall recommendation was "No" due to weak performance on the probability questions, not the soft-skill questions.

### SIG's Problem Solving Assessment (general format, from repo's OA guide, quant research roles): one-hour, 15 questions covering probability, statistics, one or two brainteasers, and single-variable calculus; time management (skip-and-return) is the main pitfall; a graphing calculator (ideally with CAS) is recommended since SIG's claim you can't access outside tools during the Mettl-proctored exam does not appear to be strictly enforced
- Company: SIG (Susquehanna)
- Role: Quant Research roles (general, not the specific Quantitative Trader writeup above)
- Type: OA
- Round/Stage: Entrance exam
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Online%20Assessments.md (section "SIG's Problem Solving Assessment")
- Answer/Discussion: none found (general OA-format guidance rather than a specific candidate report)

### In-person "Logic and Reasoning" entrance exam: ~50 questions/60 minutes, comprising a verbal reasoning section and a logic/math section (deductive reasoning, sequence completion, elementary probability); no calculators, no negative marking, closed book
- Company: TPP
- Role: Graduate Software Developer
- Type: OA
- Round/Stage: In-person entrance exam (mandatory, no remote/proctored alternative offered)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/TPP/Graduate%20Software%20Developer.md
- Answer/Discussion: Candidate passed (marked "P" plus verbal/logic subscores, obtained later via GDPR request). Company insisted on running this in-person even during UK COVID lockdowns, citing a "key worker" exemption.

### "25 horses puzzle": you have 25 horses and want to find the fastest 3; each race can have at most 5 horses (5 tracks); no stopwatch available. What is the minimum number of races needed to determine the 3 fastest horses?
- Company: TPP
- Role: Graduate Software Developer
- Type: Interview
- Round/Stage: Onsite interview (whiteboard brainteaser)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/TPP/Graduate%20Software%20Developer.md (cites https://matt-croak.medium.com/google-interview-25-horses-c982d0a9b3af for the canonical problem writeup)
- Answer/Discussion: Candidate had previously seen a variant of this puzzle from Optiver in 2020 and solved it correctly in a few minutes despite the interviewer initially expecting he might not solve it; standard answer is 7 races (not reproduced in full by candidate, who points to external solutions).

### Describe a technical topic/module to a non-technical audience (candidate chose to describe the Markowitz portfolio optimisation problem); plus: name 3 factors favoring a centralised vs. decentralised system; describe the role of a software developer in your own words; why TPP; hobbies
- Company: TPP
- Role: Graduate Software Developer
- Type: Interview
- Round/Stage: Onsite interview
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/TPP/Graduate%20Software%20Developer.md
- Answer/Discussion: Interviewer seemed satisfied with the Markowitz explanation. Candidate ultimately failed the interview (generic rejection, no specific feedback given; GDPR request later confirmed only that the "first interview" outcome was a "no").

### (Secondhand, via Glassdoor review quoted in the candidate's writeup) Third-stage TPP interview mental-math and opinion questions: "What is the cube root of 10648?"; "What do you think about the COVID pandemic?"; "Where do you stand on mandatory vaccines vs. freedom of choice?" (interviewer reportedly challenged any view given); "Would you enforce mandatory vaccines if uptake was only 30%?"
- Company: TPP
- Role: Graduate Software Developer (role/stage per a different Glassdoor reviewer, not this repo author's own interview)
- Type: Interview
- Round/Stage: Third interview stage (per Glassdoor; candidate's own interview reportedly never reached this many stages)
- Status: REAL (secondhand — quoted by the repo author from a public Glassdoor review of TPP's interview process, not the repo author's own first-person experience)
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/TPP/Graduate%20Software%20Developer.md (quoting http://www.glassdoor.co.uk/Interview/TPP-Interview-RVW60763390.htm)
- Answer/Discussion: Cube root of 10648 = 22. No answers recorded for the opinion-based questions (they are reported as controversial/off-topic by the reviewer).

### Codility entrance exam: 5 questions, 75 minutes, mostly on the lower end of LeetCode Medium (some Easy-level); candidate finished in half the allotted time
- Company: Virtu Financial
- Role: Quantitative Trading Analyst
- Type: OA
- Round/Stage: Entrance exam
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Virtu/Quantitative%20Trading%20Analyst.md
- Answer/Discussion: Candidate passed. Notes that Codility's visible sample test cases are insufficient — he had to write his own additional test cases to avoid failing hidden cases.

### "What is market making, in your own words?"
- Company: Virtu Financial
- Role: Quantitative Trading Analyst
- Type: Interview
- Round/Stage: Round 1 (phone interview with HR/recruiter)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Virtu/Quantitative%20Trading%20Analyst.md
- Answer/Discussion: none found (candidate does not record his exact answer)

### Clock-angle brainteaser: what is the angle between the minute and hour hand of a clock at 5:15 PM? Follow-up: at what time do the minute and hour hands coincide after 5 PM?
- Company: Virtu Financial
- Role: Quantitative Trading Analyst
- Type: Interview
- Round/Stage: Round 1 (phone interview)
- Status: REAL
- Source: Leader-board/OA-and-Interviews GitHub repo — https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Virtu/Quantitative%20Trading%20Analyst.md
- Answer/Discussion: Candidate solved both in about 30 seconds. Worked solution given in writeup: at 5:15, minute hand = 90° from 12; hour hand = 150° + 30°/4 = 157.5° from 12; difference = |157.5° − 90°| = 67.5°. For the follow-up, letting x = minutes past 5:00, hour-hand angle = 150° + (30x/60)°, minute-hand angle = 6x°; solving 150 + x/2 = 6x gives x = 300/11 ≈ 27.27, i.e., hands coincide between 5:27 and 5:28 PM. Despite solving both, candidate was rejected the next day with no feedback given.
