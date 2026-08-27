import json, re, difflib, collections

IN_PATH = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad/raw_entries.json"
OUT_PATH = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad/final_entries.json"
STATS_PATH = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad/stats.json"

with open(IN_PATH, encoding="utf-8") as f:
    entries = json.load(f)

# ---------- Company canonicalization ----------
COMPANY_PATTERNS = [
    (r'\bhudson river trading\b|\bhrt\b', "Hudson River Trading (HRT)"),
    (r'\bcitadel securities\b', "Citadel Securities"),
    (r'\bjane street\b', "Jane Street"),
    (r'\bjump trading\b', "Jump Trading"),
    (r'\boptiver\b', "Optiver"),
    (r'\bimc\b', "IMC Trading"),
    (r'\bdrw\b', "DRW"),
    (r'\bsusquehanna\b|\bsig\b', "SIG (Susquehanna)"),
    (r'\btwo sigma\b', "Two Sigma"),
    (r'\bakuna\b', "Akuna Capital"),
    (r'\btower research\b|\btower\b', "Tower Research Capital"),
    (r'\bxtx\b', "XTX Markets"),
    (r'\bflow traders\b', "Flow Traders"),
    (r'\bvirtu\b', "Virtu Financial"),
    (r'\bpoint72\b|\bpoint 72\b', "Point72"),
    (r'\bcubist\b', "Cubist Systematic Strategies"),
    (r'\bsquarepoint\b', "Squarepoint Capital"),
    (r'\bd\.?e\.? shaw\b', "D.E. Shaw"),
    (r'\bfive rings\b', "Five Rings"),
    (r'\bg-research\b|\bg research\b', "G-Research"),
    (r'\bheadlands\b', "Headlands Technologies"),
    (r'\bmaven securities\b|\bmaven\b', "Maven Securities"),
    (r'\bold mission\b', "Old Mission Capital"),
    (r'\bpdt partners\b|\bpdt\b', "PDT Partners"),
    (r'\bquadrature\b', "Quadrature Capital"),
    (r'\bradix\b', "Radix Trading"),
    (r'\bworldquant\b', "WorldQuant"),
    (r'\bmillennium\b', "Millennium"),
    (r'\btibra\b', "Tibra Capital"),
    (r'\brokos\b', "Rokos Capital Management"),
    (r'\btpp\b', "TPP"),
    (r'\bmustard\b', "Mustard Systems"),
    (r'\bimprobable\b', "Improbable"),
    (r'\bepoch capital\b', "Epoch Capital"),
    (r'\bmaverick\b', "Maverick Derivatives"),
    (r'\bbloomberg\b', "Bloomberg"),
    (r'\bgraviton\b', "Graviton Research Capital"),
    (r'\bquantbox\b', "QuantBox"),
    (r'\balphagrep\b', "AlphaGrep"),
    (r'\bquadeye\b', "QuadEye"),
    (r'\bda vinci\b', "Da Vinci Trading"),
    (r'\btradeweb\b', "Tradeweb"),
    (r'\bwolverine\b', "Wolverine Trading"),
    (r'\bqrt\b', "QRT"),
    (r'\bgeneva trading\b', "Geneva Trading"),
    (r'\bwalleye\b', "Walleye Capital"),
    (r'\bgoldman sachs\b', "Goldman Sachs"),
    (r'\bnvidia\b', "NVIDIA"),
    (r'\bmeta\b', "Meta"),
    (r'\bgoogle\b', "Google"),
    (r'\bmicrosoft\b', "Microsoft"),
    (r'\bamazon\b', "Amazon"),
    (r'\bapple\b', "Apple"),
    (r'\bford\b', "Ford"),
    (r'\boracle\b', "Oracle"),
    (r'\bcitadel\b', "Citadel Securities"),
    (r'd\.?\s*e\.?\s*shaw', "D.E. Shaw"),
    (r'\bamadeus\b', "Amadeus"),
    (r'\bhcl\b', "HCL"),
    (r'\bqualcomm\b', "Qualcomm"),
    (r'\bhoneywell\b', "Honeywell"),
    (r'\bhsbc\b', "HSBC"),
    (r'\bcoinbase\b', "Coinbase"),
    (r'\brobinhood\b', "Robinhood"),
    (r'\bstripe\b', "Stripe"),
    (r'\bjpmorgan\b|\bjpmc\b|\bjp morgan\b', "JPMorgan Chase"),
    (r'\bsalesforce\b', "Salesforce"),
    (r'\buber\b', "Uber"),
    (r'\bsquare\b|\bblock\b', "Square (Block)"),
    (r'\barm\b', "Arm"),
    (r'\bhewlett packard\b|\bhpe\b', "Hewlett Packard Enterprise"),
]

def canonical_companies(raw):
    if not raw:
        return ["General / Unspecified"]
    low = raw.lower()
    found = []
    for pat, canon in COMPANY_PATTERNS:
        if re.search(pat, low) and canon not in found:
            found.append(canon)
    if found:
        return found
    stripped = raw.strip()
    if stripped.lower() in ("unknown", "unknown/general", "general", ""):
        return ["General / Unspecified"]
    if ("unknown" in low or "unspecified" in low or "unattributed" in low
            or "(" in raw or len(raw) > 45):
        return ["General / Unspecified"]
    return [stripped]

# ---------- Topic classification ----------
TOPIC_ORDER = [
    ("System Design (Trading/Low-Latency)", [
        r'\bdesign (a|an|the)\b', r'\border book\b.*\bdesign\b', r'\bmatching engine\b',
        r'\bfeed handler\b', r'\bmarket data feed\b', r'\bpub-?sub\b', r'\brate limiter\b',
        r'\barchitecture\b', r'\bsystem design\b', r'\bwhiteboard.*design\b',
    ]),
    ("Concurrency, Atomics & Lock-Free", [
        r'\bthread\b', r'\bmutex\b', r'\batomic\b', r'\block-?free\b', r'\bwait-?free\b',
        r'\brace condition\b', r'\bdeadlock\b', r'\bcondition variable\b', r'\bsemaphore\b',
        r'\bspinlock\b', r'\bmemory[_ ]order\b', r'\bcompare-?and-?swap\b', r'\bcas\b',
        r'\baba problem\b', r'\bconcurren', r'\bmultithread', r'\bproducer.consumer\b',
        r'\bfalse sharing\b',
    ]),
    ("STL, Memory Management & Pointers", [
        r'shared_ptr', r'unique_ptr', r'weak_ptr', r'smart pointer', r'\braii\b',
        r'\bmalloc\b', r'\bnew\[?\]? and delete\b', r'memory leak', r'dangling',
        r'stack vs heap', r'\bvector\b', r'unordered_map', r'\biterator', r'allocator',
        r'pointer arithmetic', r'pointer vs reference', r'reference vs pointer',
        r'rules? of (three|five|zero)', r'\bstd::', r'\bcontainer\b', r'\ballocation\b', r'\ballocator\b',
    ]),
    ("C++ Core & Modern C++", [
        r'\btemplate', r'\bsfinae\b', r'\bconstexpr\b', r'\bvirtual\b', r'\bvtable\b',
        r'\brvalue\b', r'\blvalue\b', r'move semantic', r'copy constructor', r'move constructor',
        r'operator overload', r'\binheritance\b', r'diamond problem', r'\bpolymorphism\b',
        r'undefined behavior', r'what (will|does) this print', r'output of the following',
        r'c\+\+1[147]', r'c\+\+20', r'\bconcepts\b', r'\blambda\b', r'\bauto\b',
        r'initializer list', r'\bstatic\b.*\bkeyword\b', r'\bcopy elision\b', r'\binline\b',
        r'\bheader file', r'\bnamespace\b', r'\bexception', r'\bcompil',
    ]),
    ("OS, Linux, Networking & CPU/Cache/Performance", [
        r'cache line', r'\bnuma\b', r'\btcp\b', r'\budp\b', r'\bsocket', r'\bkernel\b',
        r'\bsyscall', r'page fault', r'virtual memory', r'\bscheduler\b', r'\bscheduling\b',
        r'branch predict', r'\bpipelin', r'out-of-order', r'\bdpdk\b', r'kernel bypass',
        r'multicast', r'\bnetwork', r'\blinux\b', r'operating system', r'cpu cache',
        r'\bl1 cache\b|\bl2 cache\b|\bl3 cache\b', r'context switch', r'\bprocess(es)? vs thread',
        r'\bswap\b', r'coalesced', r'\bgpu\b', r'\bcuda\b', r'\bregister\b', r'\bassembly\b',
        r'\bendian', r'\bmmap\b', r'\bfile system\b',
    ]),
    ("Algorithms & Data Structures (Coding/OA)", [
        r'\barray\b', r'\bstring\b', r'\bgraph\b', r'\bbfs\b', r'\bdfs\b', r'\bdynamic programming\b',
        r'\bbinary search\b', r'\bsort', r'\btree\b', r'linked list', r'\bqueue\b', r'\bstack\b',
        r'given an array', r'given a string', r'hackerrank', r'codesignal', r'codility',
        r'\bcomplexity\b', r'\bo\(n', r'leetcode', r'sliding window', r'two pointer',
        r'\binversion', r'skip list', r'connect four', r'\bshuffle\b', r'power of (two|three|four)',
        r'without using the', r'\bcount\b.*\b(pairs|inversions|components)\b', r'connected component',
        r'distinct islands', r'bitwise', r'two.s complement', r'lru cache', r'lowest common ancestor',
        r'\bmatrix\b', r'\bpermutation\b', r'\bsubsequence\b', r'\bsubarray\b', r'\bpalindrome\b',
        r'\bheap\b', r'\btrie\b', r'\bhash\s*map\b', r'\bknapsack\b', r'\bgreedy\b',
    ]),
    ("HFT & Trading Domain Concepts", [
        r'market maker', r'bid-ask', r'\bspread\b', r'latency arbitrage', r'order flow',
        r'\bmatching\b', r'\bexchange\b', r'tick data', r'market microstructure',
        r'\bpnl\b', r'trading strategy', r'\border book\b', r'\bfix protocol\b', r'\bfix connection\b',
        r'order management', r'\bexecution\b', r'\bnbbo\b', r'\bmarket data\b', r'\bsettlement\b',
    ]),
    ("Quantitative & Probability Puzzles", [
        r'\bprobability\b', r'expected value', r'\bcoin flip', r'\bfair coin\b', r'\bbiased coin\b',
        r'\bdice\b', r'\bbayes\b', r'\bkelly\b', r'\bmartingale\b', r'\bbrainteaser\b',
        r'\briddle\b', r'\bev of\b', r'card deck', r'st\. petersburg', r'random variable',
        r'\bvariance\b', r'\bexpected number of\b',
    ]),
    ("Interview Process, Format & Behavioral", [
        r'tell me about', r'why do you want', r'walk me through', r'process consisted',
        r'round structure', r'onsite consisted', r'\boa format\b', r'assessment structure',
        r'\bbehavioral\b', r'culture fit', r'interview loop', r'recruiter screen',
        r'phone screen', r'hiring process', r'interview process',
    ]),
]

def classify_topic(entry):
    if entry.get("topic_hint"):
        return entry["topic_hint"]
    tf = entry.get("topic_field", "")
    tf_map = {
        "c++ output/debugging": "C++ Core & Modern C++",
        "concurrency/atomics": "Concurrency, Atomics & Lock-Free",
        "os/networking/cpu/cache": "OS, Linux, Networking & CPU/Cache/Performance",
        "c++ mcq/conceptual": "C++ Core & Modern C++",
    }
    if tf.lower() in tf_map:
        return tf_map[tf.lower()]
    text = (entry["question"] + " " + entry.get("answer", "")).lower()
    for topic, patterns in TOPIC_ORDER:
        for pat in patterns:
            if re.search(pat, text):
                return topic
    return "General Technical / Company-Specific"

for e in entries:
    e["companies"] = canonical_companies(e["company"])
    e["topic"] = classify_topic(e)

# ---------- Dedup ----------
def norm(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

for e in entries:
    e["_norm"] = norm(e["question"])[:400]

# exact-dup pass: group by (norm question, primary company)
seen = {}
deduped = []
for e in entries:
    key = (e["_norm"], tuple(sorted(e["companies"])))
    if key in seen:
        primary = seen[key]
        # merge source
        if e["source_url"] and e["source_url"] not in primary.get("_extra_sources", []) and e["source_url"] != primary["source_url"]:
            primary.setdefault("_extra_sources", []).append((e["source_name"], e["source_url"]))
        if len(e["answer"]) > len(primary["answer"]):
            primary["answer"] = e["answer"]
        if primary["status"] != "REAL" and e["status"] == "REAL":
            primary["status"] = "REAL"
        continue
    seen[key] = e
    deduped.append(e)

print(f"After exact-dup pass: {len(deduped)} (from {len(entries)})")

# near-dup pass within same company-group + topic, using difflib ratio
by_group = collections.defaultdict(list)
for i, e in enumerate(deduped):
    gkey = (tuple(sorted(e["companies"])), e["topic"])
    by_group[gkey].append(i)

to_drop = set()
for gkey, idxs in by_group.items():
    if len(idxs) < 2 or len(idxs) > 400:
        continue
    for a in range(len(idxs)):
        ia = idxs[a]
        if ia in to_drop:
            continue
        for b in range(a+1, len(idxs)):
            ib = idxs[b]
            if ib in to_drop:
                continue
            na, nb = deduped[ia]["_norm"], deduped[ib]["_norm"]
            if abs(len(na) - len(nb)) > max(len(na), len(nb)) * 0.5:
                continue
            ratio = difflib.SequenceMatcher(None, na, nb).ratio()
            if ratio > 0.88:
                # merge ib into ia, keep the longer/more detailed one as primary
                keep, drop = (ia, ib) if len(deduped[ia]["answer"]) >= len(deduped[ib]["answer"]) else (ib, ia)
                other = ib if keep == ia else ia
                if deduped[other]["source_url"] and deduped[other]["source_url"] != deduped[keep]["source_url"]:
                    deduped[keep].setdefault("_extra_sources", []).append(
                        (deduped[other]["source_name"], deduped[other]["source_url"]))
                if deduped[other]["status"] == "REAL":
                    deduped[keep]["status"] = "REAL"
                to_drop.add(drop)

final = [e for i, e in enumerate(deduped) if i not in to_drop]
print(f"After near-dup pass: {len(final)} (dropped {len(to_drop)} near-duplicates)")

# clean up internal fields, build output records
output = []
for e in final:
    output.append({
        "q": e["question"],
        "companies": e["companies"],
        "role": e["role"],
        "type": e["type"],
        "round": e.get("round", ""),
        "status": e["status"],
        "topic": e["topic"],
        "source": e["source_name"],
        "url": e["source_url"],
        "answer": e["answer"],
        "extra": e.get("_extra_sources", []),
    })

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=1)

# ---------- Stats ----------
stats = {
    "total_raw": len(entries),
    "total_final": len(output),
    "by_status": dict(collections.Counter(o["status"] for o in output)),
    "by_topic": dict(collections.Counter(o["topic"] for o in output)),
    "by_company": dict(collections.Counter(c for o in output for c in o["companies"])),
}
with open(STATS_PATH, "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=1)

print(json.dumps(stats, indent=1))
