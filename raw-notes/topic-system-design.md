# System Design Interview Questions — Quant Dev / HFT / Trading Roles

### Sketch an order book and defend the data structure sitting under the bid and ask sides.
- Company: Tower Research Capital
- Role: Low-latency / Core Engineer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476792/how-tower-research-capital-interviews-engineers/
- Answer/Discussion: Bridges algorithm and system design — candidate must model a real trading object, choose a data structure fitting bid/ask access patterns (sorted map/price levels + FIFO per level), and defend it under interviewer challenges on edge cases. Tower frames these as "smaller and sharper" design problems tied to real trading scenarios rather than abstract distributed systems.

### Implement add, cancel, and match for a single-symbol book. Now make cancel O(1).
- Company: Optiver, IMC, Da Vinci, Citadel Securities, Jane Street, Hudson River Trading (HRT), Jump Trading
- Role: Software Engineer (low-latency/trading systems)
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477310/limit-order-book-matching-engine-interview/
- Answer/Discussion: Canonical prompt. Expected solution: sorted map of price levels each holding a FIFO queue; best bid/ask from map ordering. Key insight is that cancels dominate volume, so add a hash map from order ID to node position paired with an intrusive doubly-linked list for O(1) deletion. For fixed-tick equities, converting prices to tick indices and using arrays beats trees (O(1), better cache locality) at the cost of memory/generality. Production systems typically run one matching thread per symbol to avoid lock contention.

### Design an order book with add, cancel, and top-of-book operations, all better than O(n).
- Company: Jane Street, Hudson River Trading, Citadel Securities
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233475433/order-book-quant-interview/
- Answer/Discussion: Trading firms assume correctness/Big-O as baseline and drill into memory allocation, cache behavior, and practical performance. Recommended: ordered price levels + FIFO order tracking per level + hash-map index for O(1) cancels; discuss tradeoff of balanced trees (O(log n), flexible) vs. tick-indexed arrays (O(1), memory-heavy). Avoiding dynamic heap allocation (preallocated node pools, intrusive lists) separates strong candidates. Follow-ups: O(1) top-of-book reads, handling marketable orders crossing the spread, memory allocation strategy volunteered unprompted.

### Design an in-memory order matching system for a single trading venue processing tens to hundreds of thousands of orders/sec with microsecond-scale latency, in C++.
- Company: Da Vinci Trading (also mirrors Optiver-style practices)
- Role: Software Engineer (take-home/assessment)
- Type: OA
- Status: REAL
- Source: prachub.com — https://prachub.com/interview-questions/design-an-in-memory-order-matching-engine
- Answer/Discussion: Candidate expected to ask clarifying questions (single vs. multi-symbol, tick granularity, order types MARKET/IOC/FOK/GTC/PostOnly, trade pricing convention, durability/recovery, self-match prevention). 8-part design: core matching/partial fills/trade generation; order-type extensibility; Big-O targets; data structures (map-based levels + hash table for O(1) cancel); concurrency (single-threaded engine + message queue or lock-free sync); failure handling/state recovery; API design; performance-vs-simplicity tradeoffs. Emphasis on allocation-free hot paths and jitter reduction over asymptotic Big-O.

### Which data structure will you use to implement a Limit Order Book? and Why?
- Company: Investment banks (Goldman Sachs, Citigroup, Morgan Stanley context cited)
- Role: Java/software engineer, investment banking technical interview
- Type: Interview
- Status: REAL
- Source: javarevisited (Blogger) — https://javarevisited.blogspot.com/2017/03/2-practical-data-structure-algorithm-interview-questions-java.html
- Answer/Discussion: Classic version of the question. Recommended approach: binary search tree keyed by price for O(log N) search/add/remove of price levels, with a FIFO queue per price level for time priority. Proposed architecture: MatchingEngine holding a map of OrderBooks by symbol; OrderBook using a tree of price levels; queues within each level. Notes real HFT production systems need additional concurrency/thread-safety/latency work beyond this baseline.

### Multi-exchange order book: implement get_exchange_bbo(exchange_id) [best bid/offer per exchange] and get_nbbo() [national best bid/offer across all exchanges].
- Company: Citadel
- Role: Software Engineer (SWE)
- Type: Interview
- Status: REAL
- Source: dev.to — https://dev.to/net_programhelp_e160eef28/citadel-swe-interview-experience-order-book-design-in-depth-behavioral-interview-3hb0
- Answer/Discussion: Candidate account of a Citadel SWE interview coding round. Suggested approach: HashMaps partitioned by exchange with a MaxHeap for bids / MinHeap for asks; interviewer pushes further on real-world optimization, and the article recommends proposing TreeMap structures to show awareness that production systems value fast insertion/deletion/modification over simple heap ops. Followed by a ~20-minute behavioral round probing ownership, technical depth (framework choices, bottleneck ID), and communication.

### Coding exercise: parse an order-book message stream (add/cancel/modify/trade) and maintain the book; print mid-price after every message and periodic book snapshots.
- Company: Jump Trading
- Role: Software Engineer (take-home coding exercise)
- Type: OA
- Status: REAL
- Source: GitHub (candidate's own submitted solution, public repo) — https://github.com/stanleywu111/jump-orderbook
- Answer/Discussion: Real take-home artifact ("Coding exercise I did ages ago for a Jump Trading interview"). Messages: `A,<id>,<side>,<qty>,<price>` (add), `X,<id>,<side>,<qty>,<price>` (cancel), `T,<qty>,<price>` (trade). After every message, output the mid-price (avg of top bid/ask); every 10th message print the book; after every trade print traded volume at that level. Design: prices converted to uint32_t (×1000, rounded) to avoid float compare issues; separate PriceLevelMap per side (std::map + std::unordered_map hybrid) giving O(1) jump to existing levels, O(log N) level create/delete; each level is an OrderList (linked list) with O(1) insert/remove at ends; a separate hash table maps order_id → OrderList::iterator for O(1) cancel/modify. Custom pool allocator (recycling) used instead of tcmalloc/boost pool for orders/nodes/lists/trades. Discusses worst-case O(N) tree degeneration, exception-avoidance via error counters instead of throwing on the hot path, and ambiguity resolutions for cancel/modify semantics.

### Design/build a Risk server: TCP server that computes the hypothetical worst net position per financial instrument from an incoming binary order/trade feed and accepts or rejects each order against a configurable threshold.
- Company: Flow Traders
- Role: Graduate Software Development Program, C++
- Type: OA
- Status: REAL
- Source: GitHub (candidate's repo containing the official case-study PDF) — https://github.com/gxyau/flow (case study PDF: Flow_Traders_C++_Case_Study.pdf)
- Answer/Discussion: Genuine take-home case study (36-hour time limit, submit as a git branch `flow/graduates/2021`, GCC/CLANG-compatible C++17, no Win API sockets). Requirements: TCP server ingesting Orders (Add/Modify/Cancel) and Trade confirmations over a packed binary protocol (16-byte header with protocol version/payload size/sequence number/nanosecond timestamp, followed by typed messages: NewOrder, DeleteOrder, ModifyOrderQuantity, Trade, OrderResponse). For every instrument: NetPos = net sum of trade quantities, BuyQty/SellQty = net sum of resting buy/sell order quantities; worst-case Buy side = max(BuyQty, NetPosition + BuyQty), worst-case Sell side = max(SellQty, SellQty − NetPosition). If the hypothetical worst position exceeds a command-line threshold (separate max buy/sell), reject the order (state unchanged); otherwise accept and update state. Disconnecting traders have their state discarded.

### Design a market data pipeline: how market data fans out to many consumers, how you keep the hot path allocation-free, where you'd place a sequencer, and how you reason about tail latency when the mean looks fine.
- Company: XTX Markets
- Role: Software/Trading Systems Engineer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476791/xtx-markets-interview-process/
- Answer/Discussion: Described as the core system-design round for engineering candidates — distributed low-latency fan-out design rather than a typical product-design prompt (e.g., not "design Twitter"). Emphasizes concrete tradeoffs: allocation-free hot path, sequencer placement for deterministic ordering, and tail-latency (p99+) reasoning distinct from mean latency.

### A UDP multicast market-data packet lands on your network card — walk me through everything that happens before your trading strategy sees the price.
- Company: Optiver, IMC (also recurring across desks per follow-ups)
- Role: Low-latency / HFT Software Engineer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477282/hft-kernel-bypass-interview/
- Answer/Discussion: Tests kernel-bypass networking knowledge. Candidate should explain standard kernel receive path cost (interrupt, context switch, two copies, ~5-15µs) vs. polling-based bypass (~1µs, predictable tail). Recurring near-verbatim follow-ups across HFT desks: "Why is the kernel network stack too slow for market data, specifically?"; "You've got a Solarflare card — Onload or ef_vi, and why?"; "Your p99 tick-to-trade doubled overnight — network or code?"; "Sketch a lock-free SPSC queue between the poll thread and the strategy thread"; "When would you not bypass the kernel?" Discussion covers OpenOnload vs. ef_vi tradeoffs, hardware timestamping, and that most latency actually hides in application code, not networking.

### Write a single-producer, single-consumer (SPSC) queue two threads share without a lock — a ring buffer with two atomic counters, no mutex.
- Company: Citadel Securities, Hudson River Trading (HRT), Jump Trading, Tower Research, DRW
- Role: Low-latency / HFT Software Engineer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476386/lock-free-queue-hft-interview-question/
- Answer/Discussion: Fixed-size ring buffer, power-of-two capacity, head/tail indices each owned by one thread. Tests memory-ordering understanding: `memory_order_relaxed` safe for a thread's own index, `memory_order_acquire`/`release` pairing needed to make writes visible before the reader touches them. Tests false-sharing awareness (head/tail on the same 64B cache line "ping-pong" between cores) — fix with `alignas(64)`. Follow-ups: non-trivially-copyable types, batched ops, branch prediction in the hot path, using this queue as the foundation for an order book.

### Walk me through what happens to a marketable limit order from the socket to the fill. / A market order and a cancel for the same resting order arrive in the same microsecond — who wins? / Your matching box loses power mid-session — what's the state when it comes back, and how long does that take? / How do you stop one firm's algo from trading against its own quote?
- Company: Nasdaq, CME, Coinbase, Robinhood, IMC, Optiver, Da Vinci Markets
- Role: Software Engineer (matching-engine / exchange systems)
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477258/matching-engine-price-time-priority-system-design/
- Answer/Discussion: Strong answers cover price-time priority fundamentals, O(1)-cancel data structures (hash map + linked list), single-threaded determinism per instrument for reproducible replay, monotonic sequence numbers + append-only journals for crash recovery, and keeping pre-trade risk checks upstream of the hot path (self-match prevention = "the sequencer already decided" who wins on simultaneous events).

### Walk me through exactly what happens, component by component, when a marketable limit order arrives and crosses the spread. / Two co-located clients report a different top-of-book at the same wall-clock instant — bug, or expected? / Your matching engine crashed at 10:31:04 — walk me through recovery, and how you know you lost nothing. / Where do pre-trade risk checks live, and what do they cost on the hot path?
- Company: unknown/general (article references Citadel Securities, exchange teams, crypto venues, Nasdaq INET, Island ECN as historical/production examples, not a single attributed interview)
- Role: Software Engineer (trading platform / matching engine)
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476395/trading-platform-system-design-matching-engine/
- Answer/Discussion: Framed as "you're not designing for parallelism, you're designing a deterministic pipeline" — single-threaded matching core fed by a ring buffer, sequencing for durability, cache-optimized order-book structure, and a separate thread for encoding/publishing market data so the matcher thread never blocks.

### Walk me through a single message from the exchange feed until it lands in the historical database. / What if the real-time database dies at 3pm? / A query over a year of data is slow — where do you look first? / Why keep the tickerplant deliberately thin? Why partition history by date vs. symbol?
- Company: unknown/general (kdb+/q trading-desk interviews)
- Role: kdb+/q Developer, trading desk
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477284/kdb-q-trading-desk-interview/
- Answer/Discussion: Standard architecture: feed handler → tickerplant (logs & publishes) → real-time database (in-memory) → historical database (disk, date-partitioned). RDB outage recovery = replay the tickerplant log from day start. Slow year-long query → check the `where` clause filters on date first (avoids scanning unneeded disk partitions). Tickerplant kept thin to avoid propagating latency/risk downstream; history partitioned by date because date-filtering is the dominant query pattern.

### Build a service that ingests real-time quotes from twenty venues and serves the latest price with millisecond latency. / Store ten years of tick data so a researcher can backtest a strategy over any window without waiting an hour.
- Company: Point72 (Technology/Platform track)
- Role: Software Engineer, quant platform
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477266/how-the-point72-and-cubist-interview-actually-works/
- Answer/Discussion: Strong answers address partitioning by symbol and time, columnar storage formats, hot/cold data tiers, and acceptable staleness tradeoffs for latency targets.

### Given a stream of trades, design and code a structure that returns the median price over the last N events in better than linear time. / Parse this simplified order-book format and reconstruct the book — now make it handle cancels. / You have a thread pool and a queue of dependent tasks — schedule them so nothing runs before its dependencies, without deadlocking.
- Company: Two Sigma
- Role: Software Engineer, Engineering track
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477016/two-sigma-interview-tracks/
- Answer/Discussion: Design rounds focus on working implementations, not algorithm recitation — clean interfaces, test coverage, and handling mid-interview requirement changes. Concurrency awareness (threading, synchronization primitives, memory behavior) separates strong candidates.

### Implement or extend a simple matching engine: model an order book and match incoming orders by price-time priority; add cancellation, handle partial fills, maintain price-time priority at a level, enable O(1) lookup by order ID for fast cancels.
- Company: IMC Trading
- Role: Software Engineer, final engineering round
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476458/imc-trading-interview/
- Answer/Discussion: Presented as a coding exercise more than a pure architecture discussion; expected data structures are price-level maps paired with intrusive lists. IMC's interview overall emphasizes low-level C++ optimization and cache behavior over high-level system architecture.

### Design a real-time UI that ingests huge amounts of market data per second (a trading GUI showing option chains / live prices across hundreds of thousands of instruments).
- Company: Optiver
- Role: Senior/Principal Software Engineer (C#/.NET), "Design Interview" round
- Type: Interview
- Status: REAL
- Source: GitHub — candidate's own interview-prep repo with first-hand intel from the process — https://github.com/ErrolMc/OptiverInterviewPrep (see docs/design-interview-cheatsheet.md, docs/system-design.md, docs/interview-feedback.md)
- Answer/Discussion: Extremely detailed first-hand account (2026). Format: up to 90 minutes, fully verbal, no whiteboard — graded on explaining a complex system without a visual aid. Graded core is frontend aggregation/coalescing; backend is "bonus points." Core framing: reconcile a ~6-order-of-magnitude rate mismatch between feed rate (millions of msgs/sec) and human/screen perception (~10-15 changes/sec, 60Hz) via three levers — subscribe to less (viewport/foveated subscription), conflate the rest (latest-value-wins per key), decouple ingest from render (paint on a timer, not per tick). Confirmed real architecture facts from an actual Optiver engineer and Optiver's own C# engineering blog: (1) WPF is the stack but WPF grids/graphs are too slow at their data rate, so hot grids/charts drop to WinForms immediate-mode custom drawing (`OnPaint`) instead of retained-mode per-cell elements; (2) feed handlers don't push every tick over a socket — they write latest-state-per-instrument into a Redis cache and clients poll it (server-side conflation + natural backpressure + viewport subscription). Deep-dive topics graded: conflation/coalescing semantics (last-value-wins for price, additive for volume, snapshot+delta for full book), why poll-a-cache beats push-per-tick for backpressure, WPF vs. WinForms rendering models, UI-thread marshalling/batching, backpressure policy (drop/conflate, never unbounded queues — "staleness beats wrongness"), fault tolerance (sequence-gap detection, A/B line arbitration or TCP re-snapshot, stale-data visual overlays), memory optimization (avoid hot-path allocation, pooling, Span<T>, Server GC/SustainedLowLatency), and performance tooling (PerfView, dotTrace/dotMemory, dotnet-counters, BenchmarkDotNet — profile before optimizing, measure p99 not mean). Cites Optiver's public tech blog posts on this exact problem (foveated-rendering-inspired centralized subscription backend) as corroboration.

### Design a real-time price grid/dashboard for thousands of instruments. / Design a market-data feed handler that ingests a high-throughput exchange feed, normalizes it, and publishes to internal consumers. / Design an order-entry tool where correctness/safety under failure matters more than throughput.
- Company: Optiver (companion prompts documented alongside the design-interview intel above)
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: GitHub — https://github.com/ErrolMc/OptiverInterviewPrep/blob/master/docs/system-design.md
- Answer/Discussion: General spine for any real-time-UI prompt: fast feed threads → bounded ring buffer (absorbs bursts, gives backpressure) → latest-wins cache (conflation) → coalescing/throttling → one batched dispatch at ≤~60Hz → virtualized grid. Feed-handler deep dive: snapshot+delta, sequence-gap detection/recovery (A/B line arbitration or TCP re-snapshot), UDP multicast (market data) vs. TCP (orders/recovery), zero-copy parsing (Span<T>). Order-entry deep dive: confirm-before-send/fat-finger throttle, idempotency via client order IDs, reconciliation with the exchange's view after disconnect, audit logging, stale-data overlay.

### Design a stock exchange capable of processing millions of orders per second with microsecond latency while maintaining price-time priority fairness and regulatory compliance.
- Company: unknown/general (page lists Coinbase, Stripe as companies asking "similar" questions, not verbatim-attributed)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233460621/system-design-stock-exchange/
- Answer/Discussion: Order book = sorted map (TreeMap/SortedDict) keyed by price, FIFO queue per level. Matching engine processes orders sequentially, single-threaded, no locks, to guarantee strict deterministic ordering — framed as counterintuitively more efficient than multi-threading for this workload.

### Design a stock trading platform (brokerage + matching engine + market data distribution + risk engine).
- Company: unknown/general ("commonly appears in interviews at: Robinhood, Coinbase" per the article, not individually verified)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: techinterview.org — https://www.techinterview.org/post/3233460053/design-a-stock-trading-platform/
- Answer/Discussion: Four components: order book (red-black tree, O(log n)), matching engine (single-threaded, microsecond target, kernel-bypass + co-location), market data distribution (multicast UDP, not TCP, to broadcast fills/book changes without connection overhead), risk engine (position limits, balance checks, circuit breakers pre-execution). Matching engine latency target 1-10µs; brokerage-to-exchange routing 1-5ms via leased lines/co-location.

### Design a stock exchange system (order placement/cancellation, real-time order book visibility, equities only).
- Company: unknown/general (not attributed to any specific real interview)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: GitHub — https://github.com/wuyichen24/system-design-interview/blob/master/problems/finance/Stock_Exchange_System.md
- Answer/Discussion: Non-functional focus: high availability, fault tolerance w/ fast recovery, millisecond round-trip latency, security (auth, DDoS protection). Architecture: Client Gateway (auth/validation/rate limiting/routing) → Order Manager (risk checks, wallet verification) → Sequencer (assigns sequence IDs) → Matching Engine (order books + execution). Emphasizes deterministic sequencing for distributed consistency.

### Design a stock trading platform like Robinhood: users see live prices and manage orders (market/limit, create/cancel).
- Company: unknown/general (Hello Interview teaching material, not confirmed as an actual Robinhood interview question)
- Role: unknown
- Type: Unknown
- Status: PRACTICE
- Source: Hello Interview — https://www.hellointerview.com/learn/system-design/problem-breakdowns/robinhood
- Answer/Discussion: Platform is a brokerage routing to external exchanges/market makers, not building the exchange itself. Three main deep-dives: scaling live price dissemination to many concurrent users, tracking order status changes, ensuring order consistency between local state and the exchange.

### Design an order book / limit order book for a trading system (from-scratch mock interview format).
- Company: unknown/general (fictional framing — mock interview at "Alien Technology" featuring a candidate named after a TV character)
- Role: unknown (mock)
- Type: Unknown
- Status: PRACTICE
- Source: nintyzeros (Substack) — https://nintyzeros.substack.com/p/interview-session-design-a-limit
- Answer/Discussion: Covers basic definitions — limit order book as a real-time record of pending buy/sell orders; matching occurs when buy/sell prices align, removing both orders; unmatched orders remain until execution/cancellation; distinguishes limit vs. market orders. Foundational/introductory level, explicitly a mock/practice session rather than a reported real interview.

### 100 HFT/Rust system-design prompts (curated list): design an order book (1M orders/sec, sub-µs latency); design a matching engine for spot+perpetuals; design a market-data feed handler consuming ITCH 5.0 from NASDAQ for 500 symbols with gap detection/recovery; design a pre-trade risk system validating each order in <500ns without locks; design a tick-level event-driven backtesting engine in C++; design a smart order router across 5 venues; design a real-time position/P&L tracker for 10,000 symbols at 1M executions/sec; design a low-latency intra-process pub/sub message bus between strategy, risk, and OMS components; design a cross-exchange BTC/USD arbitrage system across 5 exchanges.
- Company: unknown/general (curated compilation "asked at top HFT firms" without per-question attribution — Jane Street, Citadel Securities, Virtu, IMC, Optiver, Jump Trading, Two Sigma, DE Shaw, Susquehanna named as a firm list, not tied 1:1 to each prompt)
- Role: HFT Software Engineer / Quant Developer
- Type: Unknown
- Status: PRACTICE
- Source: GitHub — https://github.com/vermavarun/hft/blob/40fa172765315b78d93d468d313dbba12cd0e766/interview-questions.md
- Answer/Discussion: No individual answer walkthroughs given (question bank only); useful as a shortlist of realistic HFT-flavored system-design prompts to self-practice, given how scarce genuinely reported low-latency system-design questions are. Also includes a good related lock-free-IPC prompt: "You need two processes to share trade events at 10M messages/sec — design the IPC mechanism" (LMAX Disruptor pattern), and "Design a kill switch that can halt all orders in <1µs — what data does it track, how is it triggered?"

### How Hudson River Trading tests systems knowledge: what happens underneath when you allocate memory; how the cache behaves; what the kernel is doing during an I/O call; memory layout and cache-line reasoning for hot paths.
- Company: Hudson River Trading (HRT)
- Role: Core Developer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477264/hudson-river-trading-interview/
- Answer/Discussion: Article states HRT devotes "a quarter" of the loop to systems design but gives topic areas rather than one verbatim design prompt — includes value/move semantics, standard-container costs, and how memory/cache behavior shapes a tight loop. No concrete whiteboard design question captured verbatim; included as a thin/partial data point.

### Walk through the memory layout of a process (globals/stack/heap). / What does std::move actually do, and when does it buy you nothing? / You have a class managing a file handle — show how RAII cleans it up, and what goes wrong without it.
- Company: Squarepoint Capital
- Role: Developer, Systems & C++ round
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233477270/squarepoint-interview-quant-researchers-developers/
- Answer/Discussion: Not a classic "design X" system-design prompt, but architecture-adjacent systems/C++ round applicable to Squarepoint's high-volume market-data pipelines — includes virtual dispatch cost, std::function overhead, iterator invalidation in std::vector.

### What does std::vector do on reallocation, and why is that a problem in a hot path? / Here's a struct — reorder the fields for the cache and explain what you saved. / This function is slow — profile it in your head and tell me the first change you'd make.
- Company: XTX Markets
- Role: Software Engineer
- Type: Interview
- Status: REAL
- Source: techinterview.org — https://www.techinterview.org/post/3233476791/xtx-markets-interview-process/
- Answer/Discussion: C++ performance/architecture questions paired with the market-data-fanout system-design prompt in the same interview loop; probes allocation-free hot paths, cache-line layout, and tail-latency-first profiling instincts.
