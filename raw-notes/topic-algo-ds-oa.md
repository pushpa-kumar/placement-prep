# Topic: Algorithms & Data Structures — OA / Coding-Round Questions Reported at Quant/HFT Firms

### Overheat Prevention Controller — Implement firmware for a multicore processor thermal management system. Each core has a load (watts), active cooling capacity, and temperature. Pooled cooling is distributed equally among running cores: floor(pooledCooling / r) per core. Temperature change per second = load[i] - activeCooling[i] - (pooledCooling / r). Cores reaching/exceeding shutdownTemperature shut down before the next second; restarting a core resets its temperature to 0. Support operations: SetCoreLoad (set a core's load, restart if shut down) and Tick (advance simulation, return IDs of cores that changed status, sorted). Constraints: up to 200 cores, 2000 operations, timestamps up to 10^9 seconds, cores × operations ≤ 2×10^5.
- Company: Optiver
- Role: Internship (OA)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/optiver-overheat-prevention-controller
- Answer/Discussion: Simulation problem; hard difficulty. Approach: event/tick-based simulation tracking per-core temperature and cooling; must efficiently detect shutdown crossings each tick.

### Evaluating Circuit Expressions — Evaluate logical circuit expressions using bracket/prefix notation where operators appear first: [!, x] for NOT, [&, x, y] for AND, [|, x, y] for OR. Operands can be literals (0/1) or nested expressions. Given a list of such expression strings (each under 1,000,000 characters, fewer than 10 expressions total), return the evaluated result (0 or 1) for each. Example: "[|, [&, 1, [!, 0]], [!, [|, [|, 1, 0], [!, 1]]]]" → 1.
- Company: Squarepoint Capital
- Role: unknown (OA)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/squarepoint-evaluating-circuit-expressions
- Answer/Discussion: Recursive-descent / stack-based parser evaluating nested bracket expressions; medium difficulty.

### Binary Circuit / "Get Max Cost" — Given a binary string, compute the maximum total cost to segregate it (move all 1s to the right of all 0s) where each operation costs "1 + number of positions moved," and each 1 must move to its maximum possible right position. String length up to 10^5. Example: "110100" → 13.
- Company: Akuna Capital
- Role: Full-time/Internship (OA)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-get-max-cost
- Answer/Discussion: Hard difficulty; requires strategic ordering of swap/move operations to maximize (not minimize) total cost — greedy/simulation with careful accounting of positions moved.

### Items Sort — Sort an array by two criteria: first by frequency of occurrence (ascending), then by the values themselves (ascending). Example: [4,5,6,5,4,3] → [3,6,4,4,5,5]. Constraints: array length up to 2×10^5, values up to 10^6.
- Company: Akuna Capital
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-items-sort
- Answer/Discussion: Hash map for frequency counts + custom comparator sort (frequency, then value).

### Minimize Malware Spread by Removing a Node — Given an undirected network of servers and an initial set of infected ("malware") nodes, remove exactly one initially-infected node (and its edges) to minimize the total number of nodes eventually infected as malware propagates through the remaining graph. Ties broken by smallest node label. Up to 2000 nodes.
- Company: Akuna Capital
- Role: unknown (OA, Medium, Graph)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-minimize-malware-spread
- Answer/Discussion: For each infected node, simulate removal + BFS/DFS over remaining graph to count resulting infections; track minimum, break ties by smallest label. (Same family as LeetCode 928 "Minimize Malware Spread II".)

### Banking Transaction Exceptions — Implement a bank account simulator starting with balance 1500.0, processing sequential operations: deposit, withdraw (rejected with "InsufficientFundsError" if balance insufficient, without modifying state), and view_transaction_history (returns all successful transactions chronologically, formatted "Type: {type}, Amount: {amount}, Balance: {balance}"). Up to 2000 operations, amounts up to 10^9.
- Company: Virtu Financial
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-banking-transaction-exceptions
- Answer/Discussion: Straightforward stateful simulation/OOP design problem — maintain balance + transaction log list, validate withdrawals before mutating state.

### FIX Message Reconciliation — Compare two FIX (Financial Information eXchange) protocol messages given in "tag=value|" format. Return True if both messages contain four required tags (32=OrderQty, 31=Price, 54=Side, 48=SecurityID) with identical raw string values (field order doesn't matter, extra tags ignored, numeric-equivalent-but-differently-formatted values like "99.0" vs "99.00" count as different), else False.
- Company: Virtu Financial
- Role: unknown (OA, Easy, String Parsing)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-fix-message-reconciliation
- Answer/Discussion: Parse both messages into tag→value maps by splitting on "|" and "="; check required-tag presence and exact string equality.

### Profit Analysis — Given an array pnl of monthly profit/loss values (positive = profit, negative = loss) and integer k, find the maximum sum over any contiguous subarray of length at most k. Example: pnl=[-3,4,3,-2,2,5], k=4 → answer 8 (segment [3,-2,2,5]), even though a longer allowed-length segment sums higher but exceeds k. Array length up to 2×10^5.
- Company: Virtu Financial
- Role: New Grad/Intern (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-profit-analysis
- Answer/Discussion: Sliding window / prefix sums to get best sum window of length ≤ k.

### Count 2x2 Submatrices by Black Cells — Given a grid (rows × cols) and a sparse list of "black" cell coordinates, count how many 2×2 submatrices contain exactly 0, 1, 2, 3, or 4 black cells (return counts as a length-5 array). Grid up to 10^5 × 10^5, at most 500 black cells.
- Company: Hudson River Trading
- Role: Intern/New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hrt-count-black-blocks
- Answer/Discussion: Since black cells are sparse, only 2x2 windows touching a black cell can have count > 0; enumerate windows adjacent to each black cell with a hash set/map, derive count-0 by subtraction. (Same idea as LeetCode 2578-family "Count Submatrices With All Ones"/"2x2 block" problems.)

### Cumulative Unique Bytes — Astronauts receive file data in segments [start, end] (1-indexed, inclusive, up to 10^12). After processing each segment in order, output the cumulative count of unique bytes covered by all segments received so far (overlaps counted once).
- Company: Hudson River Trading
- Role: Intern/New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hrt-cumulative-unique-bytes
- Answer/Discussion: Maintain a merged-interval structure (e.g. ordered map/interval tree) since ranges up to 10^12 rule out direct byte counting; incrementally merge each new interval and track total covered length.

### Maximum L1 Distance Between Equal-Length Subarrays — Given two integer arrays a and b, choose a contiguous subarray from each of equal length (≥1, different start indices allowed) to maximize the L1 distance: sum of |a[i+k]-b[j+k]| over the subarray. Arrays up to length 2000, values up to 10^9 in magnitude.
- Company: The D. E. Shaw Group
- Role: unknown (phone screen, Medium)
- Type: Interview
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-maximum-l1-distance-equal-length-subarrays
- Answer/Discussion: O(n^2) DP over subarray lengths/offsets is feasible given n≤2000; track best L1 sum per length via prefix sums of absolute differences per diagonal offset.

### Maximum K-Star Sum — Given an undirected graph with node values and integer k, a "k-star" is a center node connected to at most k neighbors (arms); its sum is the total value of the center plus chosen arms. Find the maximum possible k-star sum over all choices of center and arms.
- Company: Akuna Capital
- Role: unknown (OA, Medium, Graph)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-maximum-k-star-sum
- Answer/Discussion: For each candidate center, take its k highest-valued neighbors (e.g. via a small heap) and sum with center value; track global max. O(n·m log k). Equivalent to LeetCode 2497 "Maximum Star Sum of a Graph".

### Initial Public Offering — Allocate IPO shares given bids as [userId, numberOfShares, biddingPrice, timestamp] and totalShares available. Distribute shares from highest bidding price to lowest; within the same price tier, allocate one share at a time to bidders in ascending timestamp order (round-robin) until satisfied or shares run out. Return the sorted list of user IDs who received zero shares. Up to 10^5 bids, totalShares up to 10^9.
- Company: Point72
- Role: Full-time (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/point72-initial-public-offering
- Answer/Discussion: Group bids by price descending; within a price group, simulate round-robin one-share-at-a-time allocation by timestamp order using a queue; track unsatisfied bidders.

### Sewer Drainage Partition — A tree-shaped sewer system has water flowing from n nodes toward root 0 (given as a parent array), each node with its own input flow; a node's total flow is its own input plus the combined flow of all its children. Cut exactly one edge to split the tree into two components; find the minimum possible absolute difference between the two components' total flow.
- Company: Two Sigma
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/twosigma-sewer-drainage-partition
- Answer/Discussion: DFS to compute each subtree's total flow; the two parts from cutting any edge are (subtree flow) and (total flow - subtree flow); take min |total - 2*subtree| over all non-root nodes.

### Count Substrings With Identical Characters — Given a string s (lowercase letters, length ≤ 100), count the number of non-empty substrings where all characters are identical. Example: "zzzyz" → 8.
- Company: Virtu Financial
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-count-identical-character-substrings
- Answer/Discussion: For each maximal run of length n of the same character, add n(n+1)/2 to the total.

### HexSpeak — Convert a decimal string to uppercase hexadecimal, then replace '0'→'O' and '1'→'I'. Return the result if every character is in {A,B,C,D,E,F,I,O}, else return "ERROR". Example: "257" → hex "101" → "IOI".
- Company: Virtu Financial
- Role: Intern/New Grad (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-hexspeak
- Answer/Discussion: Same as LeetCode 1271 "Hexspeak"; parse decimal, convert to hex, character-substitute, validate against allowed set.

### Maximum Apples That Fit in a Box — A box has capacity 5000 grams and already contains a[0] grams of items; a[1..] are weights of available apples. Return the maximum number of apples that can be added without exceeding capacity.
- Company: Virtu Financial
- Role: Intern (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-maximum-apples-in-box
- Answer/Discussion: Sort remaining apple weights ascending, greedily add lightest first until capacity exceeded. (Same as LeetCode 1727-family "Maximum Units on a Truck"/apple-box variants.)

### Minimum Steps to a Fibonacci Number — Given integer x (0 ≤ x ≤ 10^6), return the minimum number of +1/-1 steps to turn x into a Fibonacci number.
- Company: Virtu Financial
- Role: Intern/New Grad (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/virtu-minimum-steps-to-fibonacci
- Answer/Discussion: Generate Fibonacci numbers up to 10^6+buffer, find nearest to x, return the difference.

### Profitable Project Pairs — Given profit[] and implementationCost[] arrays, count pairs (i,j), i<j, where net profit (profit[i]-cost[i]) + (profit[j]-cost[j]) > 0. Array size up to 2×10^5.
- Company: Akuna Capital
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-profitable-project-pairs
- Answer/Discussion: Compute net profit per project, sort, then two-pointer count pairs with positive sum (classic "count pairs with sum > target" pattern).

### Power Cell Bank — Implement a class PowerCellBank(num_racks) where rack i has capacity 2^i. Support load_cell(timestamp, cell_id, rated_duration) installing a cell into the frontmost rack with space, and discharge(timestamp, max_dispatch) which runs "charge equalization" (swapping most-depleted front-rack cells with most-charged rear-rack cells while a rack is "below-sag") then dispatches up to max_dispatch cells via a "bus shift" (most-charged cell from the active/frontmost non-empty rack, backfilling vacancies). Cells transition charged → depleted → spent (undispatchable, frees rack slot) based on elapsed time vs. rated_duration. Ties broken by lexicographically smallest cell_id.
- Company: Optiver
- Role: Internship/New Grad (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/optiver-power-cell-bank
- Answer/Discussion: Complex stateful simulation/OOP design problem — model racks as ordered structures, track per-cell load timestamp, and implement equalization + dispatch per the multi-step rules exactly as specified.

### Rock Jumping — Cross a river (width up to 10^9) from x=0 to x=width by jumping between rocks at given positions/heights; jump cost = (distance)^2, capped by maxJump per jump and maxEnergy total. Rocks submerge once water level exceeds their height (water stops rising once the first jump begins). Find the maximum water height at which crossing is still possible; return -1 if impossible even at height 0, or 10^9 if crossing always possible.
- Company: IMC Trading
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-rock-jumping
- Answer/Discussion: Binary search on water height; for each candidate height, run a shortest-path/DP feasibility check (Dijkstra-like or DP over reachable rocks respecting maxJump and cumulative maxEnergy) over surviving rocks.

### Stack Batch Removal — Implement a stack supporting push value, pop, remove_lower value (remove all elements less than value), and remove_upper value (remove all elements greater than value), all in batch (not iteratively). After each operation output the new top element or "EMPTY". Up to 2×10^5 operations.
- Company: IMC Trading
- Role: New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-stack-batch-removal
- Answer/Discussion: Use a monotonic-stack-like structure or balanced structure (e.g. deque/multiset by position) supporting bulk conditional removal in O(log n) amortized per op rather than per-element scanning.

### Last Round for Each Player — Simulate a single-elimination tournament with N (power of 2) players of distinct skill; adjacent pairs (0,1),(2,3),... compete each round, higher skill advances. Return, for each player, the last round number they participated in.
- Company: DRW
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/drw-last-round-for-each-player
- Answer/Discussion: Simulate the bracket directly (log2(N) rounds, O(N) per round) tracking each surviving player's current round; record elimination round for losers.

### Shortest Compressed Length After Removal — Given string S and integer K, remove exactly K consecutive characters, then compute the length of the run-length-compressed representation of what remains (single chars as-is; runs of 2+ identical chars become "[count][char]"). Return the minimum achievable compressed length over all choices of the K-length window to remove.
- Company: DRW
- Role: unknown (OA, Medium, String)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/drw-shortest-compressed-length-after-removal
- Answer/Discussion: Sliding window of length K over S; for each window removed, efficiently compute compressed length of the concatenation of the two remaining pieces (careful with runs that merge across the removal boundary) — similar family to LeetCode 830/1531 "String Compression II".

### Array Challenge (QR Intern) — Given an integer array, compute a counter value per element by comparing to all elements to its left: for each left element, if it's greater than current, subtract the absolute difference; if less, add it; if equal, no change. Example: [2,4,3] → [0,2,0].
- Company: Akuna Capital
- Role: Quantitative Research Intern (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-array-challenge
- Answer/Discussion: O(n) with running counters of (count of larger, count of smaller seen so far) times value, or prefix sums, avoiding O(n^2) brute force comparisons.

### Communications Handler — Design a communications handler for a single shared channel supporting at most two simultaneous callers. Process chronological instructions: connect(user1,user2) (fails if same user or channel occupied, else establishes connection), hangup(user1,user2) (fails if same user or pair not active, else disconnects, order-agnostic), and clear_all (always clears, no output). Return the ordered list of success/exception messages. Up to 2000 instructions, up to 100 distinct callers.
- Company: Akuna Capital
- Role: New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-communications-handler
- Answer/Discussion: State-machine/simulation problem — maintain a single "active pair" (or none) and validate each instruction against exact message-format rules given.

### K Smallest Substring — Given a binary string and integer k, find the substring with exactly k occurrences of '1' having minimum length, breaking ties lexicographically. String length ≤ 1000.
- Company: Akuna Capital
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-get-substring
- Answer/Discussion: Sliding window to find all minimum-length windows containing exactly k ones, then compare lexicographically among ties.

### Chain of Command — In a rooted tree (person 1 = root), a directive from a person propagates depth-first to children in ascending index order, fully completing each child's subtree before moving to the next child (i.e., a pre-order DFS traversal starting at the issuer). For each query (person, k), find the k-th person (by this propagation order) to receive the directive starting from that person, or -1 if k exceeds the subtree size. Up to 10^5 people, 2×10^5 queries.
- Company: IMC Trading
- Role: unknown (OA, Medium, Tree)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-chain-of-command
- Answer/Discussion: Precompute an Euler-tour/pre-order index and subtree size for every node via one DFS; each query becomes an O(1) or O(log n) lookup of the k-th node in that node's pre-order range (using e.g. a sparse table or binary-indexed structure over the tour order).

### Construct Binary Tree S-Expression — Given a string of parent-child pairs like "(A,B) (B,C) (A,D)", validate and construct a binary tree, outputting an S-expression "(value leftSubtree rightSubtree)" (omitting empty children, children in lexicographic order when both present). If invalid, return the highest-priority error code among: E1 invalid input string, E2 duplicate pair, E3 a parent with more than two children, E4 multiple roots, E5 a cycle. Input length up to 10^5.
- Company: Optiver
- Role: unknown (OA, Medium, Tree)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/optiver-construct-binary-tree-s-expression
- Answer/Discussion: Parse pairs, build adjacency while checking duplicate/degree/root/cycle conditions in priority order, then recursively emit the S-expression with lexicographic child ordering.

### Days Between — Compute the number of days between two calendar dates (year1,month1,day1) and (year2,month2,day2) without using any built-in date library or system date object, correctly handling leap years and month lengths.
- Company: Optiver
- Role: Full-time (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/optiver-days-between
- Answer/Discussion: Implement a manual "days since epoch" function accounting for leap years (divisible by 4, not by 100 unless by 400) and cumulative month-day tables, then subtract.

### Delivery Management System — Given a bidirectional road network of cities and a starting "company" city, return all reachable cities ordered by shortest distance from the start, breaking ties by ascending city number; exclude unreachable cities. Up to 10^5 cities and roads.
- Company: Akuna Capital
- Role: unknown (OA, Medium, Graph/BFS)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-delivery-management-system
- Answer/Discussion: Standard BFS from the start node, processing each BFS layer sorted by node id before moving to the next layer.

### Minimum Swaps — Given an array of n unique values 1..n, find the minimum number of arbitrary-position swaps needed to sort it into decreasing order.
- Company: Akuna Capital
- Role: Internship/Entry-level (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-minimum-swaps
- Answer/Discussion: Classic permutation cycle-decomposition problem: minimum swaps = n - (number of cycles) when mapping current positions to target (sorted-descending) positions.

### Movie Ratings — Given an array of movie ratings (can be negative), select a subsequence maximizing the sum, under the constraint that you cannot skip more than one movie in a row (i.e., at most one consecutive omission at a time). Array length up to 10^5, values in [-1000,1000].
- Company: Akuna Capital
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-maximize-ratings
- Answer/Discussion: DP with state tracking "last movie included" vs "one movie just skipped", transitioning to disallow two skips in a row; O(n) time.

### Minimum Image Processing Cost — n images each need daily filtering from startDay[i] to endDay[i] at filterCost[i] per day; alternatively, on any single day you may pay discountPrice once to filter ALL images needing filtering that day. Find the minimum total cost (mod 10^9+7) across the full date range.
- Company: Citadel
- Role: unknown (Interview, Medium)
- Type: Interview
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-minimum-image-processing-cost
- Answer/Discussion: Per-day DP: compute the per-day sum of individual filterCosts (via difference array over [startDay,endDay] ranges), then day-by-day take min(individual cost, discountPrice) accumulating total mod 1e9+7.

### Doctor Appointment Slot Assignment — N patients each have exactly two preferred appointment slots (A[i], B[i]) out of S total slots; each slot holds at most one patient. Determine if all N patients can be assigned to a slot they prefer (one slot per patient, no two patients sharing a slot). N and S up to 10^5.
- Company: DRW
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/drw-doctor-appointment-slot-assignment
- Answer/Discussion: Bipartite-matching-flavored problem; since each patient has degree exactly 2, this reduces to a graph-cycle/union-find style check (build a graph on slots with an edge per patient between their two preferred slots — a valid assignment exists iff each connected component has at most one more edge than... ) — effectively solvable via DSU: a component with V vertices supports at most V edges (patients) without conflict, so track cycles; otherwise general bipartite matching/max-flow works but is overkill given the degree-2 structure.

### Maximum Even-Sum Neighboring Pairs — Given N numbers arranged in a circle, find the maximum number of non-overlapping adjacent pairs (circular adjacency included) whose sum is even (i.e., same parity), where each element can be used in at most one pair.
- Company: DRW
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/drw-maximum-even-sum-neighboring-pairs
- Answer/Discussion: Greedy/DP on a circle: since only same-parity adjacent elements can pair, this reduces to matching consecutive same-parity runs — DP over the circular array (breaking the circle by trying both cases of whether position 0 is paired with position n-1) to maximize non-overlapping adjacent pairs.

### Minimize Maximum Group Difference — Partition an array of N integers into exactly 3 non-empty groups; each group's "difference" is max-min within that group. Minimize the maximum difference across the three groups.
- Company: DRW
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/drw-minimize-maximum-group-difference
- Answer/Discussion: Sort the array; optimal groups are contiguous ranges in sorted order, so binary search on the answer D and greedily partition sorted array into ≤3 contiguous runs each with max-min ≤ D (or DP over sorted array choosing 2 cut points to minimize the max of three ranges).

### Sub-matrix Sums (Maximum Square Sub-Matrix with Sum ≤ Threshold) — Given an n×n matrix of positive integers and a threshold, find the maximum k such that every k×k contiguous square sub-matrix has sum ≤ threshold. n up to 750.
- Company: IMC Trading
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-maximum-size-square-sub-matrix-with-sum-less-than-threshold (duplicate posting also seen at https://www.fastprep.io/problems/imc-maximum-sub-square-matrix-sum-less-than-k)
- Answer/Discussion: 2D prefix sums + binary search on k (monotonic: if some k×k window exceeds threshold, no larger k works either) — for each candidate k check all windows in O(n^2) via prefix sums.

### Choose Containers — A pharma company must fulfill an array of medication order requirements using one of several candidate "container sets" (each set of container sizes can be reused any number of times per order — for each requirement, use the smallest container ≥ requirement, wasting container_size - requirement, or the order is impossible if no container in that set is large enough). For each container set, compute total waste across all requirements; return the index of the set with minimum total waste (lowest index breaks ties; -1 if no set can satisfy all requirements).
- Company: IMC Trading
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-choose-containers
- Answer/Discussion: For each container set, sort its sizes and binary-search the smallest container ≥ each requirement to compute waste in O(n log m); take the min total waste over all sets.

### Balanced Split String with Wildcards — Given a string of '(', ')', '[', ']', and '?' (wildcard, can become any bracket), count the number of ways to split it into two non-empty contiguous parts such that each part's characters can be rearranged (not reordered in place, but permuted) into a balanced bracket sequence. String length 4 to 10^5.
- Company: Two Sigma
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/two-sigma-balanced-split-string-with-wildcards
- Answer/Discussion: A multiset of brackets (with wildcards) can be rearranged into a balanced sequence iff counts of '(' equal ')' after optimally assigning wildcards to whichever fixes the paren/bracket balance, and total length is even, and per-bracket-type counts can be matched via wildcards — compute prefix counts of each symbol and check the balance condition at every split point in O(n).

### Closest Color — Given pixels as 24-bit binary strings (8 bits each for R,G,B), determine which of 5 pure colors (Black, White, Red, Green, Blue) each pixel is closest to by Euclidean RGB distance; output "Ambiguous" on ties.
- Company: Two Sigma
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/two-sigma-closest-color
- Answer/Discussion: Parse each 24-bit string into R/G/B ints, compute squared Euclidean distance to each of the 5 reference colors (avoids sqrt), pick min, detect ties.

### Can Every Package Fit in a Box — Given arrays packages (sizes) and boxes (capacities), determine if every package can be assigned to a distinct box with package_size ≤ box_capacity (one package per box). Arrays up to 2×10^5.
- Company: IMC Trading
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-package-box-fit
- Answer/Discussion: Sort both arrays and greedily two-pointer match smallest package to smallest sufficient box (same pattern as LeetCode 2136 "Earliest Possible Day of Full Bloom"-style greedy matching / classic "Boats to Save People"/interval matching).

### Multi-Level Inventory Storage System ("SquirrelResearch") — Simulate a cone-shaped multi-level nut storage system per location, where level capacities follow a Fibonacci-like sequence (1,2,3,5,...) and level 0 is deepest. Support HideNut(location, nut_id, weight, timestamp, time_to_expire) — hides the nut in the first non-full level scanning from deepest, fails if location full/doesn't exist/nut already hidden elsewhere; nuts expire when timestamp > hidden_at + time_to_expire. Support RetrieveNuts — identifies the uppermost non-empty level as "reachable" (and the level below also reachable if the uppermost is <50% full), removes/discards any expired nuts encountered, then removes the nut with greatest weight (ties broken by smallest nut_id), with the lightest nut from a level above falling down to fill a vacancy in a lower reachable level.
- Company: Optiver
- Role: unknown (OA and Phone Screen, Hard, System Design/Simulation)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/optiver-multi-level-inventory-storage-system
- Answer/Discussion: Complex multi-rule OOP simulation; requires careful per-level ordered containers (e.g. sorted structures per level by weight/id) and lazy expiration handling processed at retrieval time.

### Test the Hypothesis — Implement a two-tailed t-test comparing means of two numeric arrays x and y at a given confidence level; return ["Yes"/"No"] indicating significant difference plus a "magnitude" value (minimum absolute distance between the computed t-statistic and the critical t-value at either tail), rounded to 2 decimals.
- Company: Point72
- Role: unknown (OA, Medium, Math/Stats)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/point72-test-the-hypothesis
- Answer/Discussion: Compute sample means/variances/standard error for x,y; compute t-statistic; look up or compute the critical t-value for the given confidence/degrees of freedom; compare and compute the magnitude metric as specified.

### Minimum Frames for Equal Chunks — Given an array of positive integers (dataframe sizes), find the minimum total number of "frames" to add across all elements so every element becomes divisible into at least two equal-sized chunks (i.e., becomes even). Example: [1,6,8,2,5] → 2.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Easy, Math)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-minimum-frames-for-equal-chunks
- Answer/Discussion: Trivial: for each odd element add 1 (making it even); sum the additions.

### Non-Alternating Binary Partitions — Split a binary string into the minimum number of contiguous, non-overlapping substrings, each of length ≤ frame and not a perfectly alternating bit pattern (single characters always qualify). Example: s="101101", frame=4 → 3 (partition "1011"|"0"|"1").
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium, String)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-non-alternating-binary-partitions
- Answer/Discussion: Greedy/DP: at each position extend the current substring as far as allowed (≤ frame) while it stays valid (non-alternating once length ≥ 2, or single char); when forced to cut, take the largest valid non-alternating prefix to minimize partition count — greedy is likely optimal here, or DP over positions with O(n·frame) transitions.

### Keep Them Apart — Given array A of length n and integer d≥1, delete the minimum number of elements so that for every value x, any two remaining occurrences of x at original indices i<j satisfy j-i ≥ d (distances measured by original indices, not post-deletion positions). n,d ≤ 10^5.
- Company: Qube Research & Technologies (QRT)
- Role: New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/qrt-keep-them-apart
- Answer/Discussion: Per distinct value, greedily scan its occurrence list left to right and delete an occurrence whenever it's closer than d to the last kept occurrence (classic greedy interval/spacing problem, independent per value).

### Array Nullification — Given arrays change and arr (1-indexed), nullify all elements of arr using minimum operations: (1) decrement any element by 1, or (2) set arr[i] to NULL if change[i] > 0 and arr[i] = 0. Return minimum operations, or -1 if impossible. n ≤ 10^5.
- Company: Qube Research & Technologies (QRT)
- Role: New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/qrt-array-nullification
- Answer/Discussion: For each position needing nullification, count decrements to reach 0 plus 1 nullify-op, but only if some position j with change[j] > 0 is available/reachable per the rules; requires matching decrement targets to "change>0" trigger positions — greedy/simulation with careful bookkeeping of available triggers.

### Linear Interpolator — Given n sorted knot points (x,y) defining a piecewise-linear function, implement LI(x_input): interpolate between the two nearest knots if within range, extrapolate using the two nearest endpoints if outside range; on ties (duplicate x among knots) use smallest y if x_input ≤ x, largest y if x_input > x. n up to 10^5.
- Company: Two Sigma
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/two-sigma-linear-interpolator
- Answer/Discussion: Binary search on sorted x-coordinates to locate the bracketing segment (or extrapolation endpoints), then apply the standard two-point line formula.

### Online No-Intercept Linear Regression — Implement online linear regression fitting y = kx (no intercept) as batches of (x,y) observations arrive; maintain running sums numerator = Σ(x·y) and denominator = Σ(x²) incrementally (no rescanning), and after each batch output cumulative slope k = numerator/denominator. Up to 10^5 total observations.
- Company: Two Sigma
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/two-sigma-online-no-intercept-linear-regression
- Answer/Discussion: Straightforward running-sum accumulation; O(total observations) overall, output slope after each batch boundary.

### Backtick Identifier Converter — For every backtick-wrapped identifier in a text: if it's an all-uppercase constant (has at least one letter, all letters uppercase; underscores/digits ignored for the check), leave unchanged; otherwise treat as snake_case and convert to camelCase. Preserve backticks and all text outside them, plus incomplete backtick pairs unchanged. Text up to 10^5 chars.
- Company: Hudson River Trading
- Role: unknown (OA, Easy, String)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hrt-backtick-identifier-converter
- Answer/Discussion: Regex/scan for backtick-delimited spans, classify each as constant vs snake_case, apply camelCase conversion (split on '_', capitalize subsequent words) only to the latter.

### Calculate Portfolio Rebalancing Deltas — Given parallel arrays assetIds, currentAllocations, targetAllocations, compute for each asset the delta = targetAllocation - currentAllocation, preserving original order, output as [assetId, delta] pairs.
- Company: Akuna Capital
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-portfolio-rebalancing-deltas
- Answer/Discussion: Trivial O(n) elementwise subtraction and formatting.

### Maximum Difference (connected components) — Given an undirected graph with nodes 1..g_nodes and edge lists g_from/g_to, find connected components; for each, compute (max node value - min node value) within the component (isolated nodes have difference 0); return the maximum such difference across all components. Up to 10^5 nodes/edges.
- Company: Akuna Capital
- Role: unknown (OA, Easy, Graph)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-maximum-difference
- Answer/Discussion: Union-Find or BFS/DFS to find components, track min/max label per component, take max difference. (Near-duplicate of "Maximum Label Difference in a Connected Component" below — likely the same underlying problem reused across firms/OA sessions.)

### Maximum Label Difference in a Connected Component — Same as above: given an undirected graph (nodes 1..gNodes, edges gFrom/gTo, parallel edges/self-loops allowed), find the connected component with the largest (max label - min label); isolated nodes contribute 0.
- Company: Akuna Capital
- Role: unknown (OA, Medium, Graph)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-maximum-component-label-difference
- Answer/Discussion: Union-Find/BFS-DFS to compute per-component min/max label, return max difference.

### Integer to String Without Built-ins (itoa) — Implement itoa: convert a signed 32-bit integer to its base-10 string representation without using built-in number-to-string conversion functions, handling negative sign and the full int32 range including INT_MIN/INT_MAX, returning "0" for zero.
- Company: Hudson River Trading
- Role: unknown (phone screen, Easy)
- Type: Interview
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hudson-river-trading-integer-to-string
- Answer/Discussion: Classic itoa implementation — repeatedly extract digits via mod/divide, handle sign separately, watch for INT_MIN overflow when negating (usually solved by working with the value as negative and building digits from negative remainders, or casting to a wider/unsigned type).

### Lexicographically Smallest String After Substring Operation — Given a lowercase string, choose exactly one non-empty substring and replace every character in it with the previous letter in the alphabet (wrapping 'a'→'z'). Return the lexicographically smallest string achievable. String length up to 10^5.
- Company: Point72
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/point72-lexicographically-smallest-substring-operation
- Answer/Discussion: Same as LeetCode 3405-family problems: greedily start decrementing at the first character that isn't 'a', continue decrementing through the run of non-'a' characters, stop at the first 'a' after that (or end of string) since decrementing 'a' would turn it into 'z' and hurt lexicographic order.

### Piecewise Linear Interpolation and Extrapolation — Given n points, sort by x-coordinate and build a piecewise-linear function; answer q queries returning interpolated (between two points) or extrapolated (before first/after last point) y-values using y = ya + (yb-ya)*(xq-xa)/(xb-xa), exact if xq matches a knot. n,q up to 2×10^5, tolerance 1e-6, target O((n+q) log n).
- Company: Two Sigma
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/twosigma-piecewise-linear-interpolation
- Answer/Discussion: Sort points by x, then binary search per query for the bracketing segment (or nearest two points for extrapolation) and apply the linear formula.

### Minimum Path Sum to Target in Binary Tree — Given a binary tree (level-order string with "null" markers) and a targetSum, find a root-to-leaf path summing exactly to targetSum; among multiple valid paths, prefer fewer nodes, then lexicographically smaller sequence of values. Return the path or empty array if none exists.
- Company: Citadel
- Role: unknown (phone screen, Medium)
- Type: Interview
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-minimum-path-sum-to-target-in-binary-tree
- Answer/Discussion: DFS enumerating all root-to-leaf paths summing to target (or backtracking with early pruning), comparing candidates by (path length, then lexicographic order) to select the best. Related to LeetCode 113 "Path Sum II" with custom tie-breaking.

### Generate an Optimal Portfolio Trading Report — Given a stock price array (prices[i] = price on day i), holding at most one share at a time, generate a report of all profitable buy/sell transactions using a "maximal rising run" strategy: buy at each local bottom, sell at the following local top (only report transactions with positive profit), formatted "BUY <day> <price> SELL <day> <price> PROFIT <amount>", ending with "TOTAL PROFIT <sum>" (or just that line if 0). Array length up to 30000.
- Company: Point72
- Role: unknown (phone screen, Medium)
- Type: Interview
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/point72-portfolio-trading-optimizer
- Answer/Discussion: Classic "Best Time to Buy/Sell Stock II" (LeetCode 122) variant that also requires emitting each individual transaction, not just total profit — scan for consecutive non-decreasing runs and treat each maximal run as one buy-low/sell-high transaction.

### Simplified Tetris Engine — Implement a simplified Tetris engine on a fixed 10-column grid: 7 piece types (Q,Z,S,T,I,L,J) with fixed orientations (no rotation) fall straight down from a given leftmost column, settle on collision, and complete rows clear (rows above drop down). Given a comma-separated sequence of placements like "I0,I4,Q8", return the final stack height after all placements and clears. Max final height 100.
- Company: DRW
- Role: Full-time (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/drw-simplified-tetris-engine
- Answer/Discussion: Simulation problem — model the grid as a 2D boolean array, hardcode the cell offsets for each of the 7 piece shapes, simulate gravity (drop until collision), then check/clear full rows and shift above rows down; track resulting max height.

### Disaster Recovery — Reconstruct commit histories from a corrupted log: discard malformed entries; group commits into "repositories" via Union-Find where commits sharing at least one matching file-path↔identifier pair merge into the same repository; detect "ambiguity" when the same file path maps to more than one distinct identifier within a repository (output "AMBIGUOUS INPUT!"); answer queries returning sorted commit IDs within a timestamp range for a repository. Up to 10^7 log entries, 10^5 queries, 64-bit IDs/timestamps.
- Company: Headlands Technologies
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/headlands-disaster-recovery
- Answer/Discussion: Union-Find to merge commits by shared file-identifier pairs at scale (10^7 entries demands an efficient streaming parse + near-linear DSU); post-union, validate per-repository file→identifier uniqueness for ambiguity, then answer range queries via sorted per-repository commit lists (e.g. binary search on sorted timestamp/ID arrays).

### Process Scheduling — Count the number of ways to allocate n_processes distinct processes across n_intervals time slots such that no single process occupies two consecutive time slots, modulo 10^9+7. Example: n_intervals=3, n_processes=2 → 2 (schedules {A,B,A} and {B,A,B}).
- Company: Citadel
- Role: unknown (OA, Easy, Combinatorics)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-process-scheduling
- Answer/Discussion: Combinatorial/DP: count valid sequences of length n_intervals over an alphabet of n_processes with no two adjacent equal characters — standard formula/DP: f(1)=n_processes, f(i)=f(i-1)*(n_processes-1), mod 1e9+7.

### Calculate y/x using Patch — Given integers y (dividend) and x (nonzero divisor), compute y/x rounded to the nearest hundredth using "round half up" (away from zero on exact halfway), returned as a string with exactly two decimals; a rounded-to-zero result is formatted "0.00" without a negative sign.
- Company: Two Sigma
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/twosigma-calculate-y-over-x
- Answer/Discussion: Careful fixed-point rounding (avoid floating point division pitfalls — e.g. compute in integer scaled-by-100 arithmetic) plus formatting edge case for negative-zero.

### Best Sum Downward Tree Path — Given a tree rooted at node 0 (parent array) with integer node values (possibly negative, range [-1000,1000]), find the maximum sum along any downward (root-to-any-node, following parent→child links only, no backtracking) path. n up to 10^5.
- Company: Citadel
- Role: New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-best-sum-downward-tree-path
- Answer/Discussion: DFS from root accumulating running path sum, tracking global max downward-path sum encountered at any node (simpler than LeetCode 124 since paths need not include both children — just track max prefix sum along each root-to-node path).

### Social Media Suggestions (friend recommendation) — Given n users and friendship pairs, for each user recommend a non-friend with the maximum number of mutual friends (ties broken by lowest user index), or -1 if none qualifies. Each user has at most 15 friends. n up to 10^5, edges up to 2.5×10^5.
- Company: Citadel
- Role: Intern/New Grad (OA, Medium, Graph)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-get-recommended-friends
- Answer/Discussion: Since each user has ≤15 friends, for each user enumerate friends-of-friends (≤15×15=225 candidates), count mutual-friend overlap via hash set intersection, exclude existing friends/self, pick max count with smallest index tiebreak — overall near-linear given the degree bound.

### Get Triplet Count — Count triplets (i,j,k) with i<j<k in an array such that arr[i]+arr[j]+arr[k] is divisible by a given divisor d. (Related to LeetCode 2964 "Number of Divisible Triplet Sums".)
- Company: Point72
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/point72-get-triplet-count
- Answer/Discussion: Group elements by (value mod d); for each pair of remainder classes, count combinations whose remainders sum to 0 mod d, handling the i<j<k ordering constraint (e.g. via a two-pass approach: fix middle/right elements and count valid left remainders seen so far, or combinatorics per remainder-class multiset with an O(n^2) or O(n*d) approach).

### Price Check — Given correct prices for products and a log of sold items with recorded sale prices, count how many sale transactions have an incorrect price (using exact float comparison against the correct price for that product name).
- Company: Citadel
- Role: unknown (OA, Easy, Hash Table)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-price-check
- Answer/Discussion: Build a hash map from product name to correct price, then scan sold items comparing to expected price, counting mismatches.

### Palindromic Substrings (LC 647) — Given a string s, count the number of palindromic substrings (a substring at each distinct position counts separately even if the text repeats). String length up to 1000.
- Company: Citadel
- Role: New Grad (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-palindromic-substrings
- Answer/Discussion: Exactly LeetCode 647 "Palindromic Substrings" — expand-around-center (or Manacher's algorithm) in O(n^2) or O(n).

### Get Minimum Cost (array removal) — Repeatedly remove any two of the first three elements of an array, paying a cost equal to the larger of the two removed values, until fewer than three elements remain, at which point remove all remaining at once for a cost of their max. Minimize total cost. Array size up to 1000.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-get-min-cost
- Answer/Discussion: DP over which elements remain / which prefix window is active — at each step try all valid pairs from the first three positions and recurse/memoize on the resulting state to minimize total cost.

### Minimum Time to Process Requests — (Title only; full problem text could not be fetched — FastPrep page returned only site navigation/no content on this attempt.)
- Company: Citadel
- Role: unknown
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/1.citadel-minimum-time-to-process-requests
- Answer/Discussion: none found (fetch returned no problem content)

### Tree Points — On a tree rooted at 0 (up to 10^5 nodes, values up to 10^9), you may only collect points from a node after collecting from its parent (except root). At each node choose: Method 1 — collect A[j]-K points; or Method 2 — collect floor(A[j]/2) points AND permanently halve (floor) the value of every descendant. Maximize total points collected (can be negative).
- Company: The D. E. Shaw Group
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-tree-points
- Answer/Discussion: Tree DP where the choice at a node affects descendant values (method 2 mutates the subtree state) — likely modeled as DFS carrying a "halving count so far on this path" parameter, choosing at each node the better of two recursive options and memoizing on (node, halving depth) if halving depth is bounded (values shrink to 0 after ~30 halvings).

### Get Distinct Goodness Values — Given an array (values < 1024, up to 10^4 elements), find all distinct "goodness" values obtainable as the bitwise-OR of elements in some strictly increasing (by value) subsequence, including the empty subsequence (goodness 0). Return sorted ascending.
- Company: Citadel
- Role: Intern/New Grad (OA, Hard, DP)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-get-good-value
- Answer/Discussion: DP where state = achievable OR-bitmask set reachable using elements up to the current value threshold; since values < 1024 (10 bits), track a bitset of ≤1024 achievable OR-values, updated as values increase, respecting the strictly-increasing selection constraint (process distinct values in increasing order, for each new value OR it into all previously achievable masks plus itself).

### Get Min Operations — n jobs each need executionTime[i] total seconds. In each "operation," pick one "major" job to run x seconds and every other job runs y seconds (y<x) simultaneously; a job is done once its accumulated time ≥ its executionTime. Find the minimum number of operations to finish all jobs. n up to 3×10^5, times up to 10^9.
- Company: Citadel
- Role: Internship/New Grad (OA, Hard, Binary Search)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-get-min-operations
- Answer/Discussion: Binary search on the number of operations m; check feasibility: every job gets at least m*y "base" progress, and jobs needing more must be chosen as "major" for enough of the m operations (extra (x-y) per major-selection) — verify total extra-progress-needed can be covered by at most m major picks (one per operation) via a greedy/counting check on sorted deficits.

### Count Stable Segments — Given a "capacity" array, count contiguous subsegments of length ≥ 3 where capacity[l] = capacity[r] = sum(capacity[l+1..r-1]) (both endpoints equal the sum of the interior). n up to 10^5.
- Company: Citadel
- Role: Intern/New Grad (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-count-stable-segments
- Answer/Discussion: Naive O(n^2) checking all segments works for a rough bound but for n=10^5 needs prefix sums to compute interior sums in O(1) and then hashing/grouping by capacity[l]==capacity[r] value plus matching interior-sum condition efficiently (e.g. iterate right endpoint, use hashmap keyed by value to find candidate left endpoints with matching capacity, verify sum condition via prefix sums).

### Find Consistent Logs — Given an array of user event IDs, find the length of the longest contiguous subarray where the maximum frequency of any user within the subarray equals the minimum frequency of any user in the WHOLE array. n up to 3×10^5.
- Company: Citadel
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-find-consistent-logs
- Answer/Discussion: Compute global minimum frequency once; then sliding window (two pointers) over the array maintaining per-window frequency counts, expanding/shrinking to find the longest window where max per-window frequency equals that global minimum — needs an efficient way to track max frequency in the window (e.g. frequency-of-frequency counts) as it slides.

### Nearest Neighbouring City — Given cities at distinct (x,y) coordinates, for each query city find the nearest other city that shares the same x OR same y coordinate, using Manhattan distance; break ties by lexicographically smallest name; return "NONE" if no city shares a coordinate axis. n,m up to 10^5.
- Company: Akuna Capital
- Role: unknown (OA, Medium, Hash Table)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-find-nearest-cities
- Answer/Discussion: Group cities into hash maps keyed by x-coordinate and by y-coordinate; for each query, scan both groups' entries to find minimum Manhattan distance candidates (within-axis distance reduces to |coordinate difference| since the other coordinate matches), track best with lexicographic tiebreak.

### Subarray Removal (get number of subarrays) — Given array arr, count the number of (contiguous) subarrays whose removal leaves a non-empty array that is strictly increasing. n up to 2×10^5.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-get-num-subarrays (note: URL prefixed "akuna-" but firm attributed as D.E. Shaw in the tracker) ; near-duplicate also at https://www.fastprep.io/problems/deshaw-subarray-removal
- Answer/Discussion: Find the longest strictly-increasing prefix and suffix; for each valid right boundary of the kept suffix, binary search the furthest compatible prefix boundary such that prefix's last kept element < suffix's first kept element — sum up valid (left,right) removal-window counts. Related to LeetCode 2972 "Count the Number of Incremovable Subarrays II".

### Future Stock Prices (maximize trading profit) — Given an unordered list of (Stock, Date, Price) tuples, starting with $1000 and no shares, determine the maximum profit achievable by trading (fractional shares allowed, no fees, no short selling, need not hold a position at all times, trades processed chronologically). Round final answer to nearest dollar.
- Company: Akuna Capital
- Role: Internship (OA, Medium, Greedy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-maximum-amount-of-profit (also reused at https://www.fastprep.io/problems/hudsonriver-maximum-amount-profit for Hudson River Trading)
- Answer/Discussion: Sort events chronologically per stock; greedily buy at each local price increase opportunity and sell before drops, reinvesting all capital each time (since fractional shares + no fees means always going all-in on the best next move); essentially a greedy "buy low sell high whenever price will rise" over each stock's chronological price sequence, compounding capital.

### Empty Shelf — On a 2D shelf grid of book types (1..k), selecting a book at (row,col) removes every book of that SAME type in that row and that column simultaneously. Find the minimum number of selections to clear the entire shelf. Grid up to 100×100, k ≤ 100.
- Company: Squarepoint Capital
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/squarepoint-empty-shelf
- Answer/Discussion: Graph/set-cover-flavored optimization — likely modeled as a hypergraph/bipartite covering problem (each selection covers a "same-type-in-row" and "same-type-in-column" group); given constraints, may need a greedy or BFS/state-search approach since general set cover is NP-hard but structure here (row/col/type triples) may permit an efficient exact method.

### Suggested Products — Given an array of unique product strings and a search word, for each prefix of the search word (typed character by character) return up to 3 lexicographically smallest products that start with that prefix.
- Company: Squarepoint Capital
- Role: unknown (OA, Easy, Trie)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/squarepoint-suggested-products
- Answer/Discussion: Exactly LeetCode 1268 "Search Suggestions System" — sort products, then either binary search per prefix or build a Trie annotated with top-3 suggestions per node.

### Count the Number of Incremovable Subarrays II — Given a 0-indexed array of positive integers (up to 10^5, values up to 10^9), count the number of contiguous subarrays whose removal leaves the remaining elements strictly increasing (empty array counts as strictly increasing).
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-count-the-number-of-incremovable-subarrays-ii
- Answer/Discussion: Directly LeetCode 2972 "Count the Number of Incremovable Subarrays II" — find longest strictly-increasing prefix/suffix, then for each suffix-start use binary search on the prefix to count compatible removal windows.

### Update Release Scheduler (QR Intern) — Schedule n software updates that must launch in the order determined by their planned release dates; each update can launch on its planned date or an earlier alternate date, multiple updates can share a day, and later-ordered updates cannot launch before earlier ones already launched (non-decreasing constraint on chosen release days in planned order). Minimize the final (maximum) release day.
- Company: Akuna Capital
- Role: Quantitative Research Intern (OA, Medium, Greedy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-update-release-scheduler
- Answer/Discussion: Sort updates by planned date, then greedily process in that order choosing the earliest date (alternate if it's ≥ the previously chosen day, else the planned date, else forced later) to keep the sequence non-decreasing while minimizing the final maximum day — similar to "minimum possible last element after adjusting a non-decreasing sequence" greedy pattern.

### Count Fancy Numbers — A "fancy" number contains only digits 0 and 1 when written in base-4. Count how many fancy numbers exist below a given integer n (up to 10^9). Example: n=10 → 3 (fancy numbers {1,4,5}).
- Company: Hudson River Trading
- Role: unknown (OA, Medium, Math)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hudsonriver-count-fancy-numbers
- Answer/Discussion: Digit-DP over base-4 representation of n, counting numbers using only digits {0,1} at each base-4 position up to a given length/bound (classic bounded digit-DP / combinatorial counting rather than brute force iteration).

### Get Max Throughput — A pipeline of n services in sequence has base throughput[i]; scaling service i by factor x costs scaling_cost[i]*x and raises its throughput to throughput[i]*(1+x). The overall throughput is the minimum (bottleneck) across all services. Given a total budget, maximize the achievable overall throughput.
- Company: Citadel
- Role: Intern/New Grad (OA, Hard, Binary Search)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-get-max-throughput
- Answer/Discussion: Binary search on the target overall throughput T; for a given T, compute the minimum total cost to bring every service's throughput up to at least T, sum against budget to check feasibility; find max feasible T.

### Equal Difference Pairs — Given arrays a and b, count pairs (i,j) (including i=j) satisfying a[i]-b[j] = a[j]-b[i], which simplifies to a[i]+b[i] = a[j]+b[j].
- Company: Susquehanna International Group (SIG)
- Role: unknown (OA, Medium, Hash Table)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/sig-diff-pairs
- Answer/Discussion: Hash map counting frequency of a[i]+b[i]; for each group of size k, add k*(k+1)/2 pairs (includes i=j "diagonal" pairs per the given example).

### Increasing Paths, part 1 — On a grid up to 15×15 (values 0-65535), count all strictly-increasing paths (each step moves to a horizontally/vertically adjacent cell with strictly greater value); paths need ≥2 cells; paths through cells of equal value but different locations are distinct. Guaranteed ≤2000 total paths in test grids.
- Company: Hudson River Trading
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hudsonriver-increasing-paths-1
- Answer/Discussion: DFS/memoized DP per cell counting increasing paths starting there (process cells in increasing value order to guarantee correctness of memoized subresults), sum over all cells.

### Increasing Paths, part 2 — Same as "Increasing Paths, part 1" but the grid/result scale is much larger (answer can exceed 2 billion, requiring a 64-bit/long return type — e.g. up to 601,079,908 or more for a 15×15 grid with values 0-28 arranged diagonally).
- Company: Hudson River Trading
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hudsonriver-increasing-paths-2
- Answer/Discussion: Same memoized DFS/DP approach as part 1, but must use 64-bit accumulators throughout since path counts can be astronomically large even on small grids with many equal/near-equal values.

### Maximize Segregation Cost (duplicate of "Binary Circuit") — Segregate a binary string by moving 1s to the end one at a time (cost = 1 + positions moved, each 1 moves to the furthest right position available); maximize total cost. Same problem/example as "Binary Circuit" (Akuna "get-max-cost") above — "110100" → 13.
- Company: Akuna Capital
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-maximize-segregation-cost
- Answer/Discussion: Same as above — strategic ordering of which 1 to move first to maximize (not minimize) accumulated distances.

### No Pairs Allowed — For each word in a list, find the minimum number of single-character substitutions needed so no two adjacent characters are equal (e.g. "add"→1, "boook"→1, "break"→0). Up to 100 words, each length up to 10^5.
- Company: Akuna Capital
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-minimal-operations
- Answer/Discussion: Greedy linear scan: whenever current char equals previous, count one substitution and treat it as "changed" (skip re-comparing to the character after) so consecutive equal runs of length L need floor(L/2) changes.

### Counting Triples — Maintain a dynamic multiset supporting +x (add) and -x (remove all instances of x) queries; after each operation, count arithmetic-progression triples (x,y,z) present in the current multiset with a fixed common difference. Values in [-10^9,10^9], result fits in 32-bit int.
- Company: Susquehanna International Group (SIG)
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/counting-triples
- Answer/Discussion: Hash map of value→count; maintaining a running triple-count incrementally as elements are added/removed — when adding v, add count[v-d]*count[v+d] (and related cross terms) to the running total, adjust similarly (subtract) on removal, rather than recomputing from scratch each query.

### Effective Manager (max positive-index meetings) — n meetings each have an effectiveness delta; starting from index 0, you may REORDER meetings freely; find the maximum number of meetings you can schedule (in some order) such that the running index stays strictly positive (>0) after every included meeting.
- Company: Akuna Capital
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-max-meetings
- Answer/Discussion: Greedy: schedule all non-negative deltas first (ascending order builds a safe cushion, or any order works since they don't decrease the index below current), then add negative deltas in DESCENDING order (least negative/closest to zero first) using a max-heap, stopping (or removing the worst-added negative so far) once the running total would go non-positive — classic "IPO"/"course schedule III"-style greedy with a heap to undo the worst choice.

### An Evening of Movies (longest marathon) — Given movie runtimes, find the longest possible sequence (each movie used once) where each subsequent movie's runtime equals the previous one's runtime, or exactly one minute longer. Example: [8,4,5,7,4] → 3 (4→4→5).
- Company: Akuna Capital
- Role: Full-time (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-longest-marathon
- Answer/Discussion: Count occurrences of each runtime value; DP/greedy over sorted distinct runtimes: chain[v] = count[v] + chain[v-1] (using all copies of v plus best chain ending at v-1); track max chain length.

### Customer Checkout Duration — Simulate a multi-line supermarket checkout. Operations: CustomerEnter(id, lineNumber, numItems) adds to back of a line; BasketChange(id, newNumItems) updates a customer's remaining items (if increased, moves them to the back of their line; if decreased to ≤ items already processed, they leave immediately); LineService(lineNumber, numProcessedItems) processes items from the front customer of one line; LinesService processes one item from the front customer of every non-empty line simultaneously (ties/simultaneous departures resolved by smaller line ID first). Return departure order.
- Company: Optiver
- Role: Intern (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/optiver-customer-checkout-duration
- Answer/Discussion: Per-line FIFO queue simulation; careful handling of basket changes mid-queue (repositioning to back) and immediate-departure edge cases; process instructions in order maintaining per-customer processed-item counters.

### Stock Buy Sell Position Indicator — Given a price sequence and two "indicator" patterns (sequences of +1/-1 representing consecutive increases/decreases) — buyIndicator and sellIndicator — scan the price series for matches of each pattern ending at each index; maintain a cumulative "position" (buy pattern match → +1, sell pattern match → -1; both matching simultaneously cancel to 0; a flat price (no change) never triggers either). Return the position array (same length as prices).
- Company: Hudson River Trading
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hudsonriver-buy-sell-stock
- Answer/Discussion: Convert the price series into a sequence of +1/-1/0 movement tokens; for each index check if the trailing window matches buyIndicator and/or sellIndicator (simple pattern matching, e.g. via direct comparison or KMP if patterns are long), update and carry forward the cumulative position.

### Transform String — Given a string S of only characters A, B, C, D, repeatedly remove an adjacent "AB"/"BA" pair or an adjacent "CD"/"DC" pair (any order), until no more removals are possible; return the final resulting string (any valid full-reduction sequence gives the same final string). String length up to 250,000. Examples: "CBACD"→"C"; "CABABD"→""; "ACBDACBD"→"ACBDACBD" (no removals possible).
- Company: Jane Street
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/janestreet-transform-string
- Answer/Discussion: Classic stack-based string reduction (same family as LeetCode 1544 "Make The String Great" / 1209 "Remove All Adjacent Duplicates in String II"): push each character; if it forms a removable pair (AB/BA/CD/DC) with the stack top, pop instead of pushing; final stack content (in order) is the answer. O(n) time.

### Get Minimum Cost (paid vs. free server) — n tasks each need time[i] time units and cost cost[i] if run on the (single) paid server; a free server can process any queued task in 1 time unit each, but only while the paid server is actively running some task. Choose which task(s) to run on the paid server (and in what order) to minimize total cost of completing all tasks, given the free server can only "absorb" tasks during the paid server's busy time.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium, Greedy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-get-minimum-cost
- Answer/Discussion: Greedy: find the single task with minimum cost whose time duration is ≥ (number of remaining tasks needing the free server), i.e. use one paid-server task to "cover" the free server long enough to clear everyone else at cost 0 extra; compare against alternative splits to find the true minimum (may require trying a few candidate paid tasks by cost/time tradeoff).

### Find Number of Interesting Pairs — Given array arr and integer sumVal, count unordered pairs (i,j) where |arr[i]-arr[j]| + |arr[i]+arr[j]| = sumVal.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-find-number-of-interesting-pairs
- Answer/Discussion: Key algebraic simplification: |a-b|+|a+b| = 2*max(|a|,|b|) always. So the condition reduces to max(|arr[i]|,|arr[j]|) = sumVal/2 — count pairs via a frequency map of |arr[k]| values (pairs where max abs value equals target/2, i.e. one element has |value|=target/2 and the other has |value|≤target/2).

### Maximum Size Subarray Sum (max-subarray-length-per-peak) — For each element of array a, find the size of the largest contiguous subarray containing it in which it is the (unique) maximum value; sum these sizes over all elements. Example: [10,20,10,9,12,14] → sizes [1,6,2,1,3,4] → sum 17. n up to 10^5.
- Company: The D. E. Shaw Group
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-maximum-size-subarray-sum
- Answer/Discussion: Monotonic stack to find, for each index, the nearest strictly-greater element to the left and right (standard "next greater element" technique); the maximal window size for index i is (right_bound - left_bound - 1); sum over all i. Same family as "Calculate Region" below (near-duplicate problem, different flavor text).

### Calculate Region (equivalent to Maximum Size Subarray Sum) — For each student's height in an array, find the longest contiguous subarray where that student's height equals the subarray max; sum all such lengths. Example: [3,5,6]→6; [1,2,1]→5. n up to 10^5, heights up to 10^9.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-calculate-total-region
- Answer/Discussion: Same monotonic-stack "next greater element on both sides" technique as "Maximum Size Subarray Sum" above.

### Array Break (perfect breaks / DP) — Given array arr (length ≤3000, values ≤3000), count pairs of arrays (b,c), both length n, with b non-decreasing, c non-increasing, both all non-negative, and b[i]+c[i]=arr[i] for every i. Return count mod 1e9+7. Example: arr=[2,3,2] → 4.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Hard, DP)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-perfect-break
- Answer/Discussion: DP over positions tracking the current value of b[i] (bounded by arr[i] and by the non-decreasing/non-increasing constraints propagated from neighbors); use prefix sums over the DP's value dimension to keep transitions efficient given n,values ≤ 3000 (O(n·V) with prefix-sum optimized transitions).

### Maximize the Lottery ID — Given lotteryID and winnerID strings (≤100 chars) and a budget k (0-200) of operations, where each operation changes one character of lotteryID to an alphabet-adjacent letter (with wraparound a↔z), maximize the length of the longest common subsequence (LCS) between the modified lotteryID and winnerID.
- Company: Citadel
- Role: unknown (OA, Hard, DP)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-maximize-the-lottery-id
- Answer/Discussion: DP combining LCS structure with a budget dimension: dp[i][j][k] = best LCS length using first i chars of lotteryID (with k operations spent) and first j chars of winnerID; transition considers matching lotteryID[i] to winnerID[j] directly, or spending enough operations (min alphabet-distance with wraparound) to convert it to match.

### Permutation Operations (cycle LCM) — Given a permutation p of 1..n defining the operation temp[i]=arr[p[i]] then arr=temp, find the minimum number of times to apply this operation before an arbitrary array returns to its original state. Return mod 1e9+7. Example: p=[1,3,2] → 2.
- Company: Wolverine Trading
- Role: unknown (OA, Medium, Math)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/wolverine-trading-count-operations
- Answer/Discussion: Decompose permutation p into cycles; answer = LCM of all cycle lengths (mod 1e9+7, careful with LCM under modulus — usually compute LCM directly as an integer first if it fits, or via prime-factorization combining since final answer needed mod p).

### Shared Interest — Given a graph of "friend_nodes" nodes with weighted edges (weight = shared interests, possibly multiple edges between the same pair to sum), find all node pairs achieving the maximum total shared-interest weight, then return the maximum product of node-number pairs among those tied for the max weight.
- Company: Wolverine Trading
- Role: Full-time (OA, Medium, Graph)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/wolverine-trading-max-shared
- Answer/Discussion: Aggregate edge weights per node pair (summing multi-edges) via a hash map keyed by (u,v); find the max aggregated weight; among all pairs achieving it, compute u*v and return the maximum product.

### The Huffman Decoder — Given a set of character→binary-code mappings (Huffman codes, prefix-free, variable length, tab-separated "char\tcode" strings, with the literal token "[newline]" representing '\n') and an encoded binary string, decode it back to the original text by greedily matching the longest valid prefix against the code dictionary. Up to 100 codes, encoded string up to 7000 chars.
- Company: Wolverine Trading
- Role: Full-time (OA, Easy, Trie)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/wolverine-trading-decode
- Answer/Discussion: Build a binary Trie (or hash map of code→char) from the code table, then walk the encoded bit string bit by bit, following the Trie until a leaf/complete code is found, emit its character, and restart at the Trie root — standard Huffman decoding.

### Nums That Are Divisible by N — Count pairs (i,j), i<j, in an array where arr[i]+arr[j] is divisible by N. Array length up to 10^5, values and N up to 10^9. Result as a long/64-bit integer.
- Company: Two Sigma
- Role: Internship (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/ts-nums-that-can-be-divided-by-n
- Answer/Discussion: Classic remainder-counting problem: bucket elements by (value mod N), then for each remainder r pair with remainder (N-r) mod N, counting C(count[r],2) when r pairs with itself (r=0 or r=N/2) or count[r]*count[N-r] otherwise.

### Replacing Val (flood fill) — Given a 2D grid, a starting position, and a replacement value, replace the value at that position and recursively replace all 4-directionally-connected cells sharing the original value with the replacement value.
- Company: Two Sigma
- Role: Intern (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/ts-replacing-num
- Answer/Discussion: Directly LeetCode 733 "Flood Fill" — BFS or DFS from the starting cell replacing all matching connected cells.

### Minimum Number of Permutation Operations (duplicate of Wolverine's "Permutation Operations") — Same problem as Wolverine Trading's "Permutation Operations": given permutation p of n, find the minimum number of applications of temp[i]=arr[p[i]] before an arbitrary array returns to its original state, mod 1e9+7 (i.e. the order of the permutation = LCM of its cycle lengths).
- Company: Geneva Trading
- Role: unknown (OA, Medium, Math)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/geneva-trading-minimum-number-of-permutation-operations
- Answer/Discussion: Decompose into cycles, answer = LCM of cycle lengths mod 1e9+7. (Identical underlying problem also given as an Akuna/Optiver OA question elsewhere in this tracker — appears to be a recurring FastPrep-bank/company-shared question rather than independently sourced per firm.)

### Asteroid Collision (IMC Sydney) — Simulate asteroids in a line with sizes and directions (0=left,1=right); when two asteroids moving toward each other collide, the larger survives, equal sizes destroy both. Return the surviving asteroids in order. Example: size=[4,5,6,7,4], direction=[1,1,0,1,0] → [6,7].
- Company: IMC Trading
- Role: unknown (IMC Sydney office OA, Medium, Stack)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-asteroid-game
- Answer/Discussion: Directly LeetCode 735 "Asteroid Collision" — stack-based simulation: push right-moving asteroids; on a left-moving asteroid, pop/destroy smaller right-movers on the stack top, handle equal-size mutual destruction, push if it survives all collisions.

### Get Distinct Goodness Values (duplicate posting) — Same problem as Citadel's "Get Distinct Goodness Values" / "Get Good Value" above: find all distinct bitwise-OR values from strictly increasing subsequences of an array (values <1024), including the empty subsequence, sorted ascending.
- Company: Citadel
- Role: unknown (OA, Hard, DP)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-get-distinct-goodness-values (duplicate of https://www.fastprep.io/problems/citadel-get-good-value)
- Answer/Discussion: See "Get Distinct Goodness Values" entry above — DP tracking achievable OR-bitmask set as values increase, respecting strictly-increasing selection.

### Get Minimum Operations (duplicate posting) — Same problem as Citadel's "Get Min Operations" above: n jobs, each operation runs one "major" job for x seconds and all others for y seconds (y<x); find minimum operations to complete all jobs (each job done once accumulated time ≥ its requirement).
- Company: Citadel
- Role: unknown (OA, Hard, Binary Search)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-get-minimum-operations (duplicate of https://www.fastprep.io/problems/citadel-get-min-operations)
- Answer/Discussion: See "Get Min Operations" entry above — binary search on operation count with a feasibility check on major-job deficits.

### Print Schedule — Schedule 20,000+ production processes, each with a PID, earliest start S, and latest end E (1 to 10^6); dependency PID1→PID2 requires PID1 to start before PID2 starts AND PID2 to end before PID1 ends. Assign an actual [start,end] window (≥1 time unit) to each process respecting all constraints while maximizing total runtime, or output "IMPOSSIBLE" if infeasible. Up to 10^6 combined processes+dependencies.
- Company: Optiver (listed under "akuna-print-schedule" URL but company-tagged as Optiver)
- Role: unknown (OA, Hard, Graph/Scheduling)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-print-schedule
- Answer/Discussion: Model dependencies as a DAG-like constraint system (topological ordering needed on start times and separately on end times); likely solved via constraint propagation / difference-constraints shortest-path (Bellman-Ford-style on a graph of ≤ inequalities) or a two-pass topological tightening of start/end windows, detecting cycles as "IMPOSSIBLE".

### Police Station (min acquire cost) — Given police station coordinates on a number line and an integer capacity, choose `capacity` distinct non-station coordinates to "acquire" minimizing the sum of each chosen coordinate's distance to its nearest police station.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-min-acquire-cost
- Answer/Discussion: Binary search on the maximum distance threshold, counting how many valid distinct coordinates exist within that distance of any station (expanding outward in "rings" around each station and de-duplicating), or use a priority queue seeded with the cheapest available cell next to each station, repeatedly popping the min and pushing its outward neighbor (careful to avoid double-counting between adjacent stations' ranges).

### Avoiding the Obstacles (IMC Sydney, maximize min distance to obstacles) — Find a path on an n×m grid (n,m ≤ 200) from start to end (4-directional moves, each cell visited at most once) that maximizes the minimum Manhattan distance from any cell on the path to the nearest obstacle; visiting an obstacle cell is allowed only if unavoidable.
- Company: IMC Trading
- Role: unknown (IMC Sydney interview, Hard)
- Type: Interview
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/imc-find-best-path
- Answer/Discussion: Binary search on the answer distance D, precompute each cell's distance to the nearest obstacle (multi-source BFS), then check reachability from start to end using only cells with distance ≥ D (BFS/DFS on the filtered grid); alternatively a Dijkstra/priority-queue "widest path" (maximize the minimum edge/node weight along a path) approach directly.

### Minimum Operations to Make Array Equal (parity/interval flips) — Transform array source into array target using the minimum number of operations, where each operation picks an even-length contiguous subarray and alternately adds/subtracts 1 across it left to right (+1,-1,+1,-1,...); return -1 if impossible. n up to 10^5, values up to 1e9 in magnitude.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Hard)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-minimum-operations-to-make-array-equal
- Answer/Discussion: Consider the difference array diff[i] = target[i]-source[i]; each operation's effect on diff resembles a "difference-array" style +1/-1 alternating pulse — analyze via prefix sums of diff to determine feasibility (parity conditions) and minimum operation count, likely related to counting sign changes / "peaks" in a transformed difference sequence.

### Math with Lego Blocks (equalize array sums by filling zeros) — Two arrays rowA, rowB contain positive integers with some zeros (missing values); replace every 0 with a positive integer so both arrays' sums become equal; return the minimum achievable equal sum, or -1 if impossible. Arrays up to 10^5, values up to 10^4.
- Company: Citadel
- Role: Full-time (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/citadel-find-minimum-equal-sum
- Answer/Discussion: Compute fixed (non-zero) sums and zero-counts for both arrays; each zero must become ≥1, so minimum sum for an array with z zeros and fixed sum S is S+z; the answer is max(minSumA, minSumB) if the array with the smaller minimum has at least one zero to absorb the difference (since a zero can be inflated arbitrarily), else -1 if neither can reach the other's minimum. (This is LeetCode 2091/2610-style "Equalize sums with wildcards" logic.)

### Max Harvested Crops — On a K×K field with sparse crop values at given cells, choose a "main column" and an adjacent "entry column"; a path enters via the entry column in row 0, moves to the main column, then continues straight down the main column for all remaining rows, destroying crops on the path; harvest (sum) crop values in cells immediately left/right of the path within grid bounds (destroyed cells cannot be harvested). Maximize total harvested value over all choices of main/entry column. Field up to 10^4×10^4, up to 5×10^5 crop entries.
- Company: Hudson River Trading
- Role: unknown (OA, Hard, DP)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/hudsonriver-harvest-crops
- Answer/Discussion: Precompute per-column prefix sums of crop values in adjacent columns; for each candidate (main, entry) column pair compute harvested total via range-sum queries in O(1) after O(field size) preprocessing, iterate over feasible pairs (likely only adjacent-column pairs matter, keeping overall complexity manageable given sparse crops).

### Find Maximum Beauty (positional matching after deletions) — Given an array, repeatedly delete elements (preserving relative order of survivors) down to any final length; "beauty" = count of positions i (1-indexed) where the surviving array's value at position i equals i. Maximize beauty.
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-find-maximum-beauty
- Answer/Discussion: This is essentially finding the longest subsequence where, after compaction, each kept element's original relative rank equals its value — reduces to a longest-increasing-subsequence-style DP/patience-sorting on transformed keys (value minus running position), similar to LeetCode "maximum number of fixed points after at most k removals" family problems.

### DNS Cache Resolution — Simulate an LRU-like DNS cache of fixed cache_size: each query for a URL either hits the cache (cost cache_time, and the URL becomes most-recently-used) or misses (cost server_time, URL added to cache, evicting the oldest if full). Return the resolution time for each query in sequence. Up to 10^5 queries/cache size.
- Company: Walleye Capital
- Role: unknown (OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/walleye-get-min-time
- Answer/Discussion: Standard LRU cache implementation using a hash map + doubly linked list (or ordered dict), O(1) per query for lookup/update/evict.

### Difference Calculator (Akuna Shanghai) — Given array arr, compute Indicator 1: count of values k that appear exactly k times consecutively ANYWHERE in the array; Indicator 2: count of values k that appear exactly k times consecutively STARTING at 1-based index k. Return |Indicator1 - Indicator2|. n ≤ 100, values ≤ 15.
- Company: Akuna Capital
- Role: unknown (Akuna Shanghai OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-difference-calculator
- Answer/Discussion: Small n allows a direct scan: find all maximal runs, check run-length == run-value for Indicator 1; separately check the fixed starting-index condition for Indicator 2; take absolute difference of counts.

### Minimum Chunks Required (Akuna Shanghai) — A document is split into a total number of packets; some contiguous ranges have already been uploaded as "chunks," where a valid chunk must have a size that's a power of 2. Determine the minimum number of additional power-of-2-sized chunks needed to cover all remaining (unuploaded) packets. Total packets < 10^18, up to 10^5 already-uploaded chunks.
- Company: Akuna Capital
- Role: unknown (Akuna Shanghai OA, Hard, Greedy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-minimum-chunks-required
- Answer/Discussion: Compute the uncovered gaps between/around uploaded ranges; for each gap of length L, the minimum number of power-of-2 pieces to tile it isn't simply popcount(L) since chunk alignment/position may matter — likely requires a greedy/binary decomposition per gap (similar to "minimum number of powers of 2 summing to N" when position is unconstrained, i.e. popcount(L), summed across all gaps).

### Minimum Cost to Move Within a Grid (Akuna Shanghai) — On a grid, moving between adjacent rows costs costRows[i] and between adjacent columns costs costCols[j]; find minimum total cost to move from (initR,initC) to (finalR,finalC). Grid up to 10^5 × 10^5.
- Company: Akuna Capital
- Role: unknown (Akuna Shanghai OA, Easy)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/akuna-min-cost
- Answer/Discussion: Deterministic — cost is simply the sum of costRows between the row boundaries crossed plus costCols between the column boundaries crossed (order/path doesn't matter since every intervening boundary must be crossed exactly once); computable via prefix sums in O(1) per query after O(rows+cols) preprocessing.

### Count Increasing Triplets — (Title only; FastPrep page returned no problem content on this fetch attempt — likely a slug/permissions issue.)
- Company: Citadel
- Role: unknown
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/1.citadel-triplets
- Answer/Discussion: none found (fetch returned no problem content)

### Prime Factor Visitation — (Title only; FastPrep page returned no problem content on this fetch attempt — likely a slug/permissions issue.)
- Company: Citadel
- Role: unknown
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/1.prime-factor-visitation
- Answer/Discussion: none found (fetch returned no problem content)

### Subarray Removal (D.E. Shaw canonical posting) — Given array arr of n integers, count subarrays whose removal leaves a non-empty strictly-increasing array. Example: [1,2,1,2] → 7. (Canonical/cleaner posting of the same problem duplicated above under an "akuna-" prefixed URL.)
- Company: The D. E. Shaw Group
- Role: unknown (OA, Medium)
- Type: OA
- Status: REAL
- Source: FastPrep (via perixtar/quant-interview-oa-bank GitHub tracker) — https://www.fastprep.io/problems/deshaw-subarray-removal
- Answer/Discussion: See "Subarray Removal (get number of subarrays)" entry above — find longest increasing prefix/suffix, binary search compatible boundaries per removal window.

---

## Note on primary source above
The ~110 entries above come from **perixtar/quant-interview-oa-bank** (GitHub, https://github.com/perixtar/quant-interview-oa-bank), a daily-updated tracker of FastPrep's (fastprep.io) production problem bank filtered to quant/HFT/prop-trading firms, with dated "last seen" sightings per problem (implying these are genuinely recycled/observed OA questions, not synthetic practice content — FastPrep states these are OA/interview items attributed to real candidate reports, reconstructed to ~85-90% match rate per their own disclosure on at least one page). Firms covered by this source: Akuna Capital, Citadel, The D. E. Shaw Group, Hudson River Trading, IMC, Two Sigma, Optiver, Virtu Financial, DRW, Point72, Squarepoint Capital, Wolverine Trading, Qube Research & Technologies (QRT), Susquehanna International Group (SIG), Geneva Trading, Headlands Technologies, Jane Street, Walleye Capital.

---

## Cross-validated / independent-source entries (different GitHub repos, corroborating the above)

### Days Between two dates (DaysBetween, C++ solution posted) — Compute the number of days between two calendar dates (year,month,day) without built-in date libraries, handling leap years via a days-in-month/days-in-year lookup table approach. Posted as "Optiver Internship Question 1" with a full C++ solution.
- Company: Optiver
- Role: Internship
- Type: OA
- Status: REAL
- Source: GitHub (RonitPrasad1/Interview-Questions, "Optiver (Internship) Questions.zip") — https://github.com/RonitPrasad1/Interview-Questions
- Answer/Discussion: Full C++ solution provided in repo (template function computing days-since-epoch-ish value per date via cumulative days-in-year tables, then absolute difference). Independently corroborates the FastPrep "Days Between" entry above (same underlying problem, different source/candidate).

### Binary Tree Validation with Error Codes (E1-E5) — Given a string of parent-child pairs like "(A,B)(B,C)...", validate and build a tree, detecting error conditions E1 (invalid input), E2 (duplicate pair), E3 (parent with more than two children), E4 (multiple roots), E5 (cycle). Posted as "Optiver Internship Question 2" with a partial C++ attempt.
- Company: Optiver
- Role: Internship
- Type: OA
- Status: REAL
- Source: GitHub (RonitPrasad1/Interview-Questions, "Optiver (Internship) Questions.zip") — https://github.com/RonitPrasad1/Interview-Questions
- Answer/Discussion: Partial/incomplete C++ attempt in repo (author notes "E4: I completely have no idea for that"). Independently corroborates the FastPrep "Construct Binary Tree S-Expression" entry above — confirms this E1-E5 validation problem is a genuinely recurring Optiver OA question reported by multiple, unrelated candidates.

## LeetCode company-tag frequency lists (scraped "problems seen at this company" data — REAL in the sense of aggregated reported frequency, but presented without individual problem-statement text)
Source for this subsection: GitHub repo Ayush891f/company-wise-oa-and-interview-questions (companies/*.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions — CSV columns are problem_link, problem_name, num_occur (a frequency count implying how often each LeetCode problem was reported/tagged for that company, consistent with LeetCode's "company tag" premium data format). Top entries by num_occur per trading firm below; treat these as leads to look up directly on LeetCode rather than full problem statements.

### Citadel — top LeetCode-tagged problems by reported frequency: "Pairs of Songs With Total Durations Divisible by 60" (8), "Range Addition" (5), "Sliding Window Maximum" (4), "Trapping Rain Water" (2), "Transpose Matrix" (2), "Best Time to Buy and Sell Stock IV" (2).
- Company: Citadel
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (Ayush891f/company-wise-oa-and-interview-questions, Citadel.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions/blob/main/companies/Citadel.csv
- Answer/Discussion: Standard LeetCode problems (look up directly by name); frequency counts suggest sliding-window/hash-table/array topics are recurring themes for Citadel's coding rounds, consistent with the FastPrep-sourced Citadel entries above (palindromic substrings, get-max-throughput, etc.) which also lean array/DP/graph-heavy.

### Akuna Capital — top reported LeetCode-tagged problem: "Increasing Decreasing String" (frequency 8).
- Company: Akuna Capital
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (Ayush891f/company-wise-oa-and-interview-questions, Akuna Capital.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions/blob/main/companies/Akuna%20Capital.csv
- Answer/Discussion: LeetCode 1370 "Increasing Decreasing String" — greedy repeated min/max extraction from a character frequency map.

### The D. E. Shaw Group — top reported LeetCode-tagged problems: "Freedom Trail" (3), "Sliding Window Maximum" (2), "Number of Substrings Containing All Three Characters" (1).
- Company: The D. E. Shaw Group
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (Ayush891f/company-wise-oa-and-interview-questions, DE Shaw.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions/blob/main/companies/DE%20Shaw.csv
- Answer/Discussion: Standard LeetCode problems; "Freedom Trail" is a DP problem on a rotating dial (LC 514), "Sliding Window Maximum" is the classic monotonic deque problem (LC 239).

### DRW — top reported LeetCode-tagged problem: "Reorder Routes to Make All Paths Lead to the City Zero" (frequency 4).
- Company: DRW
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (Ayush891f/company-wise-oa-and-interview-questions, DRW.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions/blob/main/companies/DRW.csv
- Answer/Discussion: LeetCode 1466 — graph/tree problem, DFS from root counting edges pointing the "wrong way" (away from root).

### Two Sigma — top reported LeetCode-tagged problems: "Multiply Strings" (4), "Maximum Product of Splitted Binary Tree" (4), "Top K Frequent Words" (2).
- Company: Two Sigma
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (Ayush891f/company-wise-oa-and-interview-questions, Two Sigma.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions/blob/main/companies/Two%20Sigma.csv
- Answer/Discussion: Standard LeetCode problems (LC 43, LC 1339, LC 692) — string math, tree DP, heap/hashmap respectively.

### Virtu Financial — top reported LeetCode-tagged problems: "How Many Apples Can You Put into the Basket" (2), "Hexspeak" (2), "Count Substrings with Only One Distinct Letter" (2), "Array Transformation" (2), "Count Number of Homogenous Substrings" (1).
- Company: Virtu Financial
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (Ayush891f/company-wise-oa-and-interview-questions, Virtu Financial.csv) — https://github.com/Ayush891f/company-wise-oa-and-interview-questions/blob/main/companies/Virtu%20Financial.csv
- Answer/Discussion: Directly cross-validates two FastPrep-sourced Virtu entries above ("Maximum Apples That Fit in a Box" = LC 1727 "How Many Apples Can You Put into the Basket"; "HexSpeak" = LC 1271 "Hexspeak") — strong independent confirmation these are genuinely recurring Virtu OA questions, not one-off FastPrep reconstructions.

## LeetCode company-tag data (second independent source — LeetCode's own "company tag" frequency/acceptance/difficulty export)
Source for this subsection: GitHub repo geekygirl8/lc_cc (per-company CSVs with ID, Title, URL, Is Premium, Acceptance %, Difficulty, Frequency %) — https://github.com/geekygirl8/lc_cc. This is the well-known LeetCode "company tag" premium dataset format, listing problems LeetCode itself associates with each company (aggregated from user-submitted "seen at OA/interview" tags), with a Frequency % indicating relative reported frequency. New firms found here not covered by the FastPrep tracker above: Jump Trading, AQR Capital Management, Bridgewater Associates.

### Jump Trading — top LeetCode-tagged problems: "Largest Combination With Bitwise AND Greater Than Zero" (Medium, 100% freq), "Valid Sudoku" (Medium, 50% freq).
- Company: Jump Trading
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, jump-trading.csv) — https://github.com/geekygirl8/lc_cc/blob/main/jump-trading.csv
- Answer/Discussion: LeetCode 2354 and LC 36 respectively — standard bitmask-counting and grid-constraint-validation problems.

### AQR Capital Management — top LeetCode-tagged problem: "Minimum Path Sum" (Medium, 100% freq).
- Company: AQR Capital Management
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, aqr-capital-management-llc.csv) — https://github.com/geekygirl8/lc_cc/blob/main/aqr-capital-management-llc.csv
- Answer/Discussion: LeetCode 64 "Minimum Path Sum" — classic grid DP.

### Bridgewater Associates — top LeetCode-tagged problem: "Count Strictly Increasing Subarrays" (Medium).
- Company: Bridgewater Associates
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, bridgewater-associates.csv) — https://github.com/geekygirl8/lc_cc/blob/main/bridgewater-associates.csv
- Answer/Discussion: LeetCode 3350 "Count Strictly Increasing Subarrays" — count maximal strictly-increasing runs and sum triangular-number combinations per run.

### Jane Street (additional LeetCode-tagged) — "Design Snake Game" (Medium, 100% freq, Premium), "Add Two Integers" (Easy, 50% freq).
- Company: Jane Street
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, jane-street.csv) — https://github.com/geekygirl8/lc_cc/blob/main/jane-street.csv
- Answer/Discussion: LeetCode 353 "Design Snake Game" — simulation/design problem tracking snake body via deque + hash set for O(1) collision checks; LC 2235 trivial addition.

### Hudson River Trading (additional LeetCode-tagged) — top problems: "Verbal Arithmetic Puzzle" (Hard, 100% freq), "Remove Comments" (Medium, 62.8%), "Split Array Largest Sum" (Hard, 25.6%), "Add Binary" (Easy, 3.1%), "First Missing Positive" (Hard, 1.8%).
- Company: Hudson River Trading
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, hudson-river-trading.csv) — https://github.com/geekygirl8/lc_cc/blob/main/hudson-river-trading.csv
- Answer/Discussion: Notably harder/more varied set than the FastPrep-sourced HRT list — "Verbal Arithmetic Puzzle" (LC 1307) is backtracking/constraint-satisfaction, "Split Array Largest Sum" (LC 410) is binary-search-on-answer, both classic hard HRT-style algorithmic problems.

### Citadel (additional LeetCode-tagged) — top problems: "Subarray Sums Divisible by K" (Medium, 100%), "Range Addition" (Medium, 65%), "Minimum Costs Using the Train Line" (Hard, 59.5%), "Smallest Range II" (Medium, 49.2%), "The Maze" (Medium, 14.2%), "Transpose Matrix" (Easy, 7%).
- Company: Citadel
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, citadel.csv) — https://github.com/geekygirl8/lc_cc/blob/main/citadel.csv
- Answer/Discussion: Standard LeetCode problems (LC 974, LC 370, LC 910, etc.); "Subarray Sums Divisible by K" (prefix sum + mod hashmap) is a particularly common quant-firm favorite due to its overlap with financial time-series/rolling-sum patterns.

### DRW (additional LeetCode-tagged) — "Subarray Sum Equals K" (Medium, 100% freq).
- Company: DRW
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, drw.csv) — https://github.com/geekygirl8/lc_cc/blob/main/drw.csv
- Answer/Discussion: LeetCode 560 — classic prefix-sum + hashmap counting problem.

### Akuna Capital (additional LeetCode-tagged) — top problems: "Most Visited Sector in a Circular Track" (Easy, 100%), "Find the City With the Smallest Number of Neighbors at a Threshold Distance" (Medium, 72.1%), "Count and Say" (Medium, 71.1%), "Palindromic Substrings" (Medium, 43.2%), "Basic Calculator II" (Medium, 28.7%), "Binary Tree Maximum Path Sum" (Hard, 11.2%).
- Company: Akuna Capital
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, akuna-capital.csv) — https://github.com/geekygirl8/lc_cc/blob/main/akuna-capital.csv
- Answer/Discussion: "Basic Calculator II" (expression parsing/evaluation, LC 227) is thematically consistent with the FastPrep "Evaluating Circuit Expressions"-style parsing problems seen at other trading firms above.

### The D. E. Shaw Group (additional LeetCode-tagged) — top problems: "Minimum Cost to Merge Stones" (Hard, 100%), "Get the Maximum Score" (Hard, 61.9%), "Max Area of Island" (Medium, 23.8%), "Max Consecutive Ones III" (Medium, 22.6%), "Insert Delete GetRandom O(1)" (Medium, 9.8%), "Triangle" (Medium, 9.7%).
- Company: The D. E. Shaw Group
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, de-shaw.csv) — https://github.com/geekygirl8/lc_cc/blob/main/de-shaw.csv
- Answer/Discussion: "Minimum Cost to Merge Stones" (LC 1000) is a notably hard interval-DP problem; consistent with D.E. Shaw's reputation for harder algorithmic OA/interview problems relative to some peers.

### Virtu Financial (additional LeetCode-tagged) — top problems: "Array Transformation" (Easy, 100%), "Count Substrings with Only One Distinct Letter" (Easy, 71.2%), "Design Linked List" (Medium, 37.9%), "Spiral Matrix" (Medium, 4.7%).
- Company: Virtu Financial
- Role: unknown
- Type: OA
- Status: REAL
- Source: GitHub (geekygirl8/lc_cc, virtu.csv) — https://github.com/geekygirl8/lc_cc/blob/main/virtu.csv
- Answer/Discussion: "Count Substrings with Only One Distinct Letter" directly matches the FastPrep-sourced "Count Substrings With Identical Characters" entry above — same problem, independently confirmed.

### Point72 (additional LeetCode-tagged, SQL-heavy) — "Weather Type in Each Country", "Restaurant Growth", "Replace Employee ID With The Unique Identifier", "Top Travellers", "Evaluate Boolean Expression" (all Easy/Medium, all listed at 0% freq in this dataset — likely low-sample).
- Company: Point72
- Role: unknown
- Type: OA
- Status: PRACTICE
- Source: GitHub (geekygirl8/lc_cc, point72.csv) — https://github.com/geekygirl8/lc_cc/blob/main/point72.csv
- Answer/Discussion: Notably this Point72 sub-list is dominated by SQL/database problems (unlike the algorithmic Point72 problems from FastPrep above) — suggests Point72's broader interview pipeline (likely data engineering/analyst tracks) also uses SQL rounds distinct from the quant-dev algorithmic OA covered elsewhere in this file.

## Order-Book / Matching-Engine themed problems (topic-based, cross-firm) and detailed Optiver live-round candidate feedback
Source for this subsection: a candidate's personal, actively-maintained Optiver interview-prep repo (ErrolMc/OptiverInterviewPrep on GitHub — https://github.com/ErrolMc/OptiverInterviewPrep), which quotes real recruiter-relayed written feedback from failed candidates and first-hand interviewer intel, distinguishing clearly between HIGH-confidence firsthand info and MEDIUM/LOW-confidence aggregator-sourced items (their own confidence labels are preserved in entries below).

### Optiver live SWE coding round is graph/traversal-flavored, not order-book-flavored — reported live-round pattern — Multiple candidates independently received written rejection feedback describing the live ~60-min HackerRank+Zoom coding round as testing "graph/data structure concepts," specifically struggling to "extend to more complex traversal scenarios and edge cases," "loops and multiple paths," after "a solid start on parsing and handling direct conversions." The pattern is: parse input → build a graph → traverse it, handling cycles and multiple paths (e.g. an Evaluate-Division-style currency/unit conversion problem, or dependency resolution).
- Company: Optiver
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/interview-feedback.md) — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/interview-feedback.md
- Answer/Discussion: Repo author's confidence: HIGH that the round is graph/DS&A-flavored and collaborative (corroborated by Optiver's own careers page and a separate Glassdoor Sydney May-2026 report describing HackerRank with two engineers observing, video+mic, probing "space-time complexity, Big O"). Practice: LeetCode "Evaluate Division" (currency/unit conversion via weighted graph), "Clone Graph" (cycle-safe traversal), "All Paths From Source to Target," "Course Schedule I/II" (cycle detection via topological sort).

### Currency-conversion graph problem (Senior SWE, medium confidence) — Convert an amount across a set of given exchange-rate pairs by modeling rates as a weighted directed graph and traversing via DFS/BFS (Evaluate-Division-style).
- Company: Optiver
- Role: Senior Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/interview-feedback.md, citing prep-farm aggregators "The Wall Street Quants"/"prachub") — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/interview-feedback.md
- Answer/Discussion: Repo author's confidence: MEDIUM (aggregator-sourced, not firsthand-verified). A related but distinct currency-ARBITRAGE cycle-detection variant (Bellman-Ford negative-cycle detection) is separately reported but attributed instead to Optiver's Quantitative Researcher / automated-OA track, not the SWE live round.

### Dijkstra shortest path with "error on multiple equal shortest paths" twist — Standard Dijkstra's shortest-path implementation, but the interviewer adds the twist that the program must detect and error/flag when multiple paths tie for shortest.
- Company: Optiver
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/interview-feedback.md) — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/interview-feedback.md
- Answer/Discussion: Aggregator-sourced, medium confidence. Standard Dijkstra with an added tie-detection pass (track count of ways to achieve the current best distance to each node, flag if >1 way reaches the target at the minimum distance).

### Build/validate a binary tree from an edge list, detecting cycles — Given a list of edges describing parent-child relationships, build a binary tree and detect/report invalid structures such as cycles.
- Company: Optiver
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/interview-feedback.md) — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/interview-feedback.md
- Answer/Discussion: This independently corroborates (from a completely different source/candidate) the FastPrep-sourced "Construct Binary Tree S-Expression" problem AND the RonitPrasad1/Interview-Questions "Binary Tree Validation with Error Codes (E1-E5)" entry above — three separate sources now describe essentially the same Optiver "build+validate a tree from pair/edge input, detect cycles/multiple-roots/duplicate-parent errors" question, strongly suggesting it's a long-running, genuinely recurring Optiver question bank item.

### Word-pair BFS sentence transformation — A Word-Ladder-style problem: transform one sentence/word sequence into another via a sequence of valid single word-pair substitutions, found via BFS over an implicit graph of valid transformations.
- Company: Optiver
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/interview-feedback.md) — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/interview-feedback.md
- Answer/Discussion: Aggregator-sourced, medium confidence; practice analogue given is LeetCode 127 "Word Ladder."

### Array-backed queue/deque implemented without resizing — Implement a queue or deque data structure backed by a fixed-size array (no dynamic resizing allowed), a recurring "how does it work under the hood" implementation question.
- Company: Optiver
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/interview-feedback.md and docs/problem-set.md) — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/interview-feedback.md
- Answer/Discussion: Recurring per repo author's aggregated sourcing; matches Optiver's stated bias toward probing low-level "how does this work under the hood" understanding rather than pattern-matching a memorized LeetCode problem. Implement a circular buffer with head/tail indices and wraparound (modulo arithmetic), handling full/empty disambiguation (e.g. via a size counter or one wasted slot).

### Optiver's signature order-book / matching-engine build (OA-track signal, strong secondary for live round) — Process a stream of ADD orderId side(BUY/SELL) price qty / CANCEL orderId commands: ADD tries to match against the opposite side of the book (a BUY crosses a SELL when buyPrice≥sellPrice, filling at the resting order's price, matching by price-time priority — best price first, then FIFO at equal price — continuing to match while the incoming order still has quantity and the best opposite price still crosses, not stopping after one fill), resting any unfilled remainder; CANCEL removes a resting order in O(1).
- Company: Optiver
- Role: Software Engineer
- Type: OA/Interview (author notes order-book emphasis "came from automated-OA write-ups — a possibly different stage" than the live round)
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/coding-round.md and docs/problem-set.md) — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/coding-round.md
- Answer/Discussion: Repo's own recommended data structures: SortedDictionary<price, queue-of-orders> for bids (viewed descending) and asks (viewed ascending), a FIFO queue per price level for time priority, and a Dictionary<orderId, node> for O(1) cancel (splice out of the linked list, drop the price level if empty). The #1 bug to avoid per the repo: "do NOT break after a single fill" — must keep matching while incoming.Qty > 0 AND the best opposite price still crosses, taking min(incoming.Qty, front.Qty) per fill and removing exhausted price levels. Closest free LeetCode analogue: LC 1801 "Number of Orders in the Backlog" (maps ~1:1 to the sim, using two priority queues).

### "Trading Sequences" OA (counting DP / Kadane-style) — Reported recurring Optiver OA problem name; decomposes into counting-DP and Kadane's-algorithm-style state-machine DP over a price/position sequence (per repo author's synthesis of multiple 2025-26 candidate write-ups).
- Company: Optiver
- Role: unknown (OA)
- Type: OA
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/problem-set.md, "aggregator-sourced, medium confidence") — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/problem-set.md
- Answer/Discussion: Repo recommends drilling the "Best Time to Buy and Sell Stock II/III/IV" LeetCode ladder (unlimited transactions greedy/DP → at-most-2 state machine → at-most-k generalized DP) as the closest practice analogue for whatever "Trading Sequences" turns out to require.

### "Allocation / Portfolio" OA (greedy+sorting or return statistics) — Reported recurring Optiver OA problem name involving either a greedy+sorting allocation problem or computing daily-return mean/standard-deviation style statistics (per repo author's synthesis of multiple 2025-26 candidate write-ups).
- Company: Optiver
- Role: unknown (OA)
- Type: OA
- Status: REAL
- Source: GitHub (ErrolMc/OptiverInterviewPrep, docs/problem-set.md, "aggregator-sourced, medium confidence") — https://github.com/ErrolMc/OptiverInterviewPrep/blob/main/docs/problem-set.md
- Answer/Discussion: Flagged by the repo author to watch for float-accumulation precision issues (consider integer cents / careful summation order) — a recurring pitfall theme across the FastPrep-sourced trading-firm problems in this file too (e.g. "Test the Hypothesis," "Calculate y/x using Patch").

### Equity Order Matching (GS CodeSprint 2018) — Design a matching engine for buy/sell orders on a stock exchange supporting Market orders (execute immediately at best opposing price), Limit orders (execute at specified price or better, rest until matched/canceled), and IOC/Immediate-or-Cancel orders (must match within the current cycle at a capped price, unmatched portion auto-canceled). Commands: New (N, reject duplicates/invalid fields), Amend (A, modify price/qty, reject if fully matched/canceled), Cancel (X, supports partial cancellation), Match (M, execute matching for all or specific symbols, processed alphabetically), Query (Q, display book state, optionally filtered). Buy order with highest price matches sell order with lowest price; same-price ties broken by timestamp (FIFO); one buy order can match multiple sell orders if prices align. Timestamps non-decreasing (except queries); negative price/quantity rejected.
- Company: General (HackerRank-hosted "GS CodeSprint 2018" contest, explicitly trading-industry-styled; surfaced via an Optiver-prep resource as a recommended matching-engine analogue)
- Role: unknown
- Type: OA-style practice challenge (archived public contest)
- Status: REAL
- Source: HackerRank — https://www.hackerrank.com/contests/gs-codesprint-2018/challenges/equity-order-matching/problem
- Answer/Discussion: Full problem statement is publicly viewable (contest itself may be submission-locked/archived). A genuinely detailed, realistic order-matching-engine specification useful as direct practice for any trading-firm's order-book coding question — implement via a price-sorted book (e.g. std::map/multimap per side) plus an order-id lookup table for O(log n) insert / amend / cancel and priority-queue-style matching.

### Order Book "Pricer" — Given a market-data log of order-book messages (each either adding a bid/ask limit order or reducing/removing an existing order's size, read from stdin) and a command-line target-size, output the total expense to BUY target-size shares (taking asks lowest-price-first) and total income to SELL target-size shares (hitting bids highest-price-first), each time either value changes as the book updates.
- Company: unknown/general (author's own real take-home coding-challenge interview; problem statement itself widely circulates as a well-known "Pricer" market-data challenge often associated with trading-firm interviews)
- Role: unknown
- Type: Interview (take-home)
- Status: REAL
- Source: GitHub (panaali/orderbook) — https://github.com/panaali/orderbook
- Answer/Discussion: Reference C++ solution provided in repo: std::multimap (sorted by price, red-black tree) for the book, O(log n) insert; std::unordered_map from order-id to a multimap iterator for O(1) lookup/removal on reduce/cancel messages. Recomputes/prints target-size expense (sum of cheapest asks) and income (sum of richest bids) only when either value actually changes as messages stream in — an efficient incremental approach avoids full book rescans per message.

## Additional firms from an aggregator-style multi-firm HFT interview-prep repo (lower confidence — many items are aggregator-synthesized "[anecdotal]"/"[inferred]" topic guesses rather than verbatim transcripts; specific/quote-like items are called out separately below)
Source for this subsection: GitHub repo ankitkushawaha1000/HFT (content/companies/<firm>/round-NN-.../questions.md per firm/round) — https://github.com/ankitkushawaha1000/HFT. The repo itself tags each item's confidence; items below marked "[anecdotal]" per the source claim some real candidate-report basis (via Glassdoor/Blind/LeetCode Discuss, but without direct links to the original post), while "[inferred]"/"general-prep" items are the repo's own plausible guesses, not verified reports — treat those as PRACTICE-tier signal at best.

### Tower Research Capital — Technical Phone Screen (60 min, live coding + C++, via CoderPad) — Specific reported items: "Implement a generic thread-safe queue in C++17 using condition variables. Now analyze the latency characteristics."; "Given N segments on a number line, find the maximum number of overlapping segments at any point."; "Write a function to find the median of two sorted arrays in O(log(m+n))." (plus several C++-fundamentals questions on std::atomic memory ordering, vtables, variadic-template TypeAt<N,List>, and strict aliasing).
- Company: Tower Research Capital
- Role: unknown (technical phone screen)
- Type: Interview
- Status: REAL (anecdotal, aggregator-sourced — not independently verified with a primary link)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/tower-research-capital/round-02-technical-phone-screen/questions.md
- Answer/Discussion: "Maximum overlapping segments" = classic sweep-line/interval-counting (sort start/end events, scan tracking a running counter, or a difference array over coordinate-compressed points). "Median of two sorted arrays in O(log(m+n))" is exactly LeetCode 4, solved via binary search on the smaller array's partition point.

### Millennium Management — Online Assessment (~90 min, HackerRank, 2-3 problems, LC medium-to-hard) — Specific reported items: maximum subarray sum via a Kadane-style variant; given stock prices, find maximum profit with at most K buy-sell transactions; shortest path in a grid with blocked cells; implement a function to check whether a string is a valid floating-point number.
- Company: Millennium Management
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/millennium/round-02-online-assessment/questions.md
- Answer/Discussion: "At most K buy-sell transactions" = LeetCode 188 "Best Time to Buy and Sell Stock IV" (state-machine DP); "valid floating-point number" = LeetCode 65 "Valid Number" (careful finite-state-machine string parsing, a classic string-edge-case OA favorite); "shortest path in a grid with blocked cells" = standard BFS on a grid (LeetCode 1091-family).

### WorldQuant — Online Assessment / Coding Challenge (HackerRank or proprietary portal, 2-3 problems, LC medium, sometimes with a separate math/probability section) — Specific reported items: number of islands in a 2D grid; given daily returns, compute volatility and Sharpe ratio; implement a function that parses and evaluates a mathematical expression.
- Company: WorldQuant
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/worldquant/round-02-online-assessment-coding-challenge/questions.md
- Answer/Discussion: "Number of Islands" = LeetCode 200 (BFS/DFS/union-find grid connected components); "volatility/Sharpe ratio from daily returns" is a finance-flavored stats computation (mean, stddev, then mean/stddev ratio, often annualized) — thematically consistent with the "Test the Hypothesis" and similar finance-stats OA problems seen at Point72/Two Sigma above; "parse and evaluate a mathematical expression" is the classic calculator/expression-parser family (LeetCode 224/227/772), also echoed in Squarepoint's "Evaluating Circuit Expressions" above.

### XTX Markets — Online Assessment (quantitative/coding hybrid) — Specific reported items: DP-or-graph-search problem at medium-hard LeetCode level; given a stream of prices, implement an online algorithm for rolling mean and variance efficiently; implement a basic logistic regression from scratch; Bayesian coin-fairness estimation from flip counts.
- Company: XTX Markets
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal/inferred mix, aggregator-sourced — the rolling-mean/variance, logistic-regression, and Bayesian items are marked "[inferred]" by the source, i.e. plausible but unverified)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/xtx-markets/round-01-online-assessment-quantitative-coding/questions.md
- Answer/Discussion: "Online rolling mean/variance" = Welford's online algorithm (single-pass, numerically stable, O(1) update per new data point) — a strong candidate for a genuinely recurring XTX-style question given their quant/ML-flavored OA reputation.

### Squarepoint Capital (additional, technical coding assessment round) — Specific reported items: implement a function to determine if a binary tree is a valid BST; given a sequence of integers, find the longest palindromic subsequence; given N nodes and K edges, find all connected components.
- Company: Squarepoint Capital
- Role: unknown (OA/technical coding assessment)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/squarepoint/round-02-technical-coding-assessment/questions.md
- Answer/Discussion: "Valid BST" = LeetCode 98 (range-bounded recursion or in-order traversal check); "Longest Palindromic Subsequence" = LeetCode 516 (interval DP); "connected components from N nodes/K edges" = union-find or BFS/DFS component counting.

### G-Research — Coding Test (round 2, separate from the aptitude screen; HackerRank or proprietary; 2-4 problems) — Specific reported items: implement an LRU cache with complexity justification; given a stream of integers, find the median after each insertion in O(log n); topological sort/DAG shortest path; interval merging/scheduling; DP minimum-cost grid path.
- Company: G-Research
- Role: unknown (OA/coding test)
- Type: OA
- Status: REAL (anecdotal/inferred mix, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/g-research/round-02-coding-test/questions.md
- Answer/Discussion: "LRU cache" = LeetCode 146; "median after each insertion" = two-heaps/Find-Median-from-Data-Stream pattern (LeetCode 295), a recurring theme across several trading firms in this file (also seen at Optiver, Millennium-adjacent).

### Radix Trading — Technical Screen (C++ and/or Rust, concurrency-focused) — Reported topics: implement a concurrent queue in Rust using safe primitives; C++ std::mutex vs std::atomic<T> and when lock-free is preferred; one general LeetCode-medium algorithmic problem.
- Company: Radix Trading
- Role: unknown (technical screen)
- Type: Interview
- Status: PRACTICE (marked "general-prep"/"inferred" by the source — topic-area guesses, not confirmed specific reported questions)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/radix-trading/round-01-technical-screen/questions.md
- Answer/Discussion: none found beyond topic-level guesses; Radix's public-facing signal is limited (repo cites only careers page + generic Reddit r/rust searches). Included for completeness on a thin-data firm.

### Jump Trading, Maven Securities, Old Mission Capital, PDT Partners, Quadrature Capital — OA topic areas (thin/generic signal) — Reported OA topic areas without specific verbatim problems: Jump Trading (graph traversal/shortest path, string parsing, DP, stack/queue/deque implementation, occasional networking/protocol-parsing simulation); Maven Securities (trees/graphs/hash maps, sorting/searching/DP); Old Mission Capital (stack/queue implementation, array/string manipulation, graph traversal, simulation+optimization); PDT Partners (LC medium-hard algorithms, possible statistics/math component reflecting PDT's quant-research culture); Quadrature Capital (DP/memoization, BFS/DFS/shortest-path, numerical/mathematical computation e.g. square root or random-process simulation).
- Company: Jump Trading / Maven Securities / Old Mission Capital / PDT Partners / Quadrature Capital (multiple)
- Role: unknown (OA)
- Type: OA
- Status: PRACTICE (all items marked "anecdotal" or lower by the source with no specific problem text — topic-area signal only, genuinely thin public data for these firms)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/tree/main/content/companies
- Answer/Discussion: none found at the specific-problem level; useful only as a topic checklist (graphs, DP, stacks/queues, string parsing, basic simulation) to prepare broadly for these less-documented firms.

### Jane Street — Technical Phone Screens (two 45-60 min rounds, no OA platform for SWE per source) — Specific reported coding items: implement all permutations of a string / similar recursion-combinatorics problem; implement a functional map/filter/reduce pipeline; implement binary search correctly then generalize to leftmost-insertion-point; solve a graph problem (shortest path with constraints, or cycle detection in a directed graph); design a simple rate limiter.
- Company: Jane Street
- Role: Software Engineer
- Type: Interview
- Status: REAL (anecdotal, aggregator-sourced; cites Jane Street's own public "preparing for a software engineering interview" page as a format source)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/jane-street/round-02-technical-phone-screens/questions.md ; also see Jane Street's own guidance at https://www.janestreet.com/join-jane-street/interviewing/
- Answer/Discussion: "Leftmost insertion point" binary search = LeetCode 35 "Search Insert Position" generalized (bisect_left pattern); functional map/filter/reduce pipeline tests comfort with higher-order functions/OCaml-style thinking consistent with Jane Street's OCaml-heavy culture even when the interview is conducted in another language.

### IMC Trading — Online Assessment (HackerRank, 2-3 problems, 60-90 min) — Specific reported items: prefix-sum array manipulation; binary-search-on-answer ("minimum time to complete tasks"); graph BFS/DFS; string parsing/simulation (simplified command parser); "implement a simplified order matching engine" matching buy/sell orders by price-time priority.
- Company: IMC Trading
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/imc-trading/round-02-online-assessment/questions.md
- Answer/Discussion: The "simplified order matching engine" item directly reinforces the order-book/matching-engine theme as a recurring cross-firm OA pattern (see the dedicated Order-Book section above); "minimum time to complete tasks" binary-search-on-answer pattern matches several FastPrep-sourced IMC problems above (e.g. "Rock Jumping").

### DRW — Technical Phone Screen 1 (60 min, HackerRank/CoderPad) — Specific reported items: "Implement a least-recently-used (LRU) cache with O(1) get and put."; "Given a stream of trade events (symbol, side, quantity, price), implement a function returning the current VWAP for each symbol."; "Find the shortest path between two nodes in a weighted directed graph. Handle negative edges."; "Implement a function to check if a BST is valid."; "Design an algorithm to merge K sorted linked lists."; "Given a matrix, find the number of distinct islands (connected components of 1s)."
- Company: DRW
- Role: unknown (technical phone screen)
- Type: Interview
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/drw/round-02-technical-phone-screen-algorithms/questions.md
- Answer/Discussion: The VWAP-from-trade-stream item is a genuinely trading-specific, distinctive prompt not seen in the FastPrep DRW list — implement via running (price*qty) sum and running qty sum per symbol, VWAP = sum(price*qty)/sum(qty), updated incrementally per event. "Shortest path with negative edges" implies Bellman-Ford rather than plain Dijkstra — a common trap/test of whether candidates default to Dijkstra incorrectly.

### SIG (Susquehanna) — Online Assessment (HackerRank, 2-3 problems, 60-90 min) — Specific reported items: "Given a list of options trades (strike, expiry, type, quantity), compute the net delta exposure."; DP counting-paths/coin-change variants; Sieve of Eratosthenes range-prime-finding; "Simulate a card game and compute the probability of winning."; "Implement a basic expression evaluator (with +, -, *, /, parentheses)."
- Company: Susquehanna International Group (SIG)
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/sig-susquehanna/round-02-online-assessment/questions.md
- Answer/Discussion: "Net delta exposure from options trades" is a distinctly options/derivatives-flavored simulation prompt (sum signed delta*quantity per position, netting by underlying) — a rarer, more finance-domain-specific OA pattern than the pure-DSA problems dominating most other firms' lists. "Basic expression evaluator with parentheses" = LeetCode 224/227 calculator family, recurring across multiple firms in this file.

### Virtu Financial (additional, probability/coding OA round) — Specific/semi-specific reported items: string/array manipulation at LC-medium level; hash-map/sorting problem; market-making spread-capture scenario ("bid-ask spread $0.10, 1M shares/day traded — gross revenue and what risks eat into it?"); basic coin-flip probability.
- Company: Virtu Financial
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal/inferred mix, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/virtu-financial/round-01-online-assessment-probability-coding/questions.md
- Answer/Discussion: The market-making spread-capture scenario is a quantitative-reasoning question rather than a coding problem per se, but is included since Virtu's OA reportedly blends both; consistent with Virtu's HFT/market-making core business.

### Headlands Technologies — Technical Phone/Video Screen (very low confidence per source; sparse public data) — Reported items: implement a lock-free ring buffer in C++; explain std::memory_order_acquire/release; one general LeetCode-medium coding problem.
- Company: Headlands Technologies
- Role: unknown
- Type: Interview
- Status: PRACTICE (source explicitly flags "very low confidence," items marked "general-prep")
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/headlands-technologies/round-01-technical-phone-video-screen/questions.md
- Answer/Discussion: Lock-free ring buffer implementation is a classic low-latency C++ systems question theme, plausible for Headlands given their HFT focus, but not confirmed as an actually-reported question.

### The D. E. Shaw Group (additional, OA round) — Specific reported items: max profit with at most K buy-sell transactions; minimum coins for target amount (coin change); longest common subsequence; word break (dictionary segmentation); count islands (BFS/DFS grid); implement a stack with O(1) getMin.
- Company: The D. E. Shaw Group
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/de-shaw/round-02-online-assessment/questions.md
- Answer/Discussion: All classic, well-known LeetCode problems (322 Coin Change, 1143 LCS, 139 Word Break, 200 Number of Islands, 155 Min Stack, 188 Buy/Sell Stock IV) — consistent DP/graph/design mix matching D.E. Shaw's FastPrep-sourced profile above (also DP/graph-heavy).

### Two Sigma (additional, OA round) — Specific reported items: sliding-window/two-pointer "longest substring without repeating characters"-style task; "count number of ways to decode a string" (Decode Ways, LC 91-style); BFS/DFS on a grid; interval merging/meeting rooms; a custom event-order simulation problem.
- Company: Two Sigma
- Role: unknown (OA)
- Type: OA
- Status: REAL (anecdotal, aggregator-sourced)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/two-sigma/round-02-online-assessment/questions.md
- Answer/Discussion: Standard patterns; "event-order simulation" theme is consistent with the FastPrep-sourced Two Sigma "Sewer Drainage Partition" and "IPO"-style event-processing problems seen above.

### Flow Traders — Online Assessment (HackerRank, 2-3 problems, ~90 min) — Reported topic areas (no verbatim problem text): sliding-window/two-pointer array or string manipulation; BFS/DFS graph or tree traversal; sequence dynamic programming.
- Company: Flow Traders
- Role: unknown (OA)
- Type: OA
- Status: PRACTICE (topic-level only, no specific problem statements found)
- Source: GitHub (ankitkushawaha1000/HFT) — https://github.com/ankitkushawaha1000/HFT/blob/main/content/companies/flow-traders/round-01-online-assessment/questions.md
- Answer/Discussion: none found beyond topic areas; note Flow Traders is more consistently documented for its separate rapid-mental-math/numerical assessment (out of scope here — that's not an algo/DS coding round).
