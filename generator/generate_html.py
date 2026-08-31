import json, argparse, hashlib

def stable_id(prefix, *parts):
    h = hashlib.sha1("||".join(str(p) for p in parts).encode("utf-8")).hexdigest()[:12]
    return f"{prefix}-{h}"

SCRATCH = "/Users/pushpakumar/quant-hft-interview-prep/generator"
FINAL = f"{SCRATCH}/final_entries.json"
FINAL_MCQS = f"{SCRATCH}/final_mcqs.json"
TEMPLATE = f"{SCRATCH}/template.html"

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="/Users/pushpakumar/quant-hft-interview-prep/index.html")
ap.add_argument("--cpguide-url", default="https://claude.ai/code/artifact/e932bf7a-2fde-4f1b-86f5-0637b417d9b2")
ap.add_argument("--concepts-url", default="https://claude.ai/code/artifact/eed48dca-cc19-4727-bbed-c7112580de54")
ap.add_argument("--companyoa-url", default="#", help="URL/relative path to the gated Company OA Bank page (docs build only)")
ap.add_argument("--enable-progress", action="store_true", help="include login/progress-tracking (GitHub Pages build only)")
args = ap.parse_args()

OUT = args.out
CPGUIDE_URL = args.cpguide_url
CONCEPTS_URL = args.concepts_url
COMPANYOA_URL = args.companyoa_url
PROGRESS_ENABLED = args.enable_progress
PROGRESS_SCRIPT = '<script type="module" src="progress.js"></script>' if PROGRESS_ENABLED else ""
AUTH_SLOT = '<span id="authSlot" class="auth-slot"></span>' if PROGRESS_ENABLED else ""

MCQ_TOPIC_ORDER = [
    "C++ Core & Modern C++",
    "STL, Memory Management & Pointers",
    "Concurrency, Atomics & Lock-Free",
    "OS, Linux, Networking & CPU/Cache/Performance",
    "Algorithms & Data Structures (Coding/OA)",
]

TOPIC_ORDER = [
    "System Design (Trading/Low-Latency)",
    "Algorithms & Data Structures (Coding/OA)",
    "Concurrency, Atomics & Lock-Free",
    "STL, Memory Management & Pointers",
    "C++ Core & Modern C++",
    "OS, Linux, Networking & CPU/Cache/Performance",
    "HFT & Trading Domain Concepts",
    "Quantitative & Probability Puzzles",
    "Interview Process, Format & Behavioral",
    "General Technical / Company-Specific",
]

TOPIC_DESC = {
    "System Design (Trading/Low-Latency)": "Architecture and whiteboard-design questions — order books, matching engines, market-data feed handlers, and other low-latency system design asked at trading firms.",
    "Algorithms & Data Structures (Coding/OA)": "Coding-round and online-assessment problems — graph/array/string algorithms, complexity analysis, and classic data-structure implementation tasks reported from real OAs.",
    "Concurrency, Atomics & Lock-Free": "Threads, mutexes, atomics, memory ordering, and lock-free/wait-free programming — a staple of HFT technical rounds.",
    "STL, Memory Management & Pointers": "STL containers/iterators, smart pointers, RAII, manual memory management, and pointer/reference fundamentals — including many \"implement shared_ptr\" style tasks.",
    "C++ Core & Modern C++": "Language mechanics — templates, value categories, move semantics, virtual dispatch, output-prediction and debugging trick questions, and modern (C++11–20) features.",
    "OS, Linux, Networking & CPU/Cache/Performance": "Operating-system internals, Linux, TCP/UDP and kernel-bypass networking, CPU architecture, caches, false sharing, and general low-latency performance engineering.",
    "HFT & Trading Domain Concepts": "Market-structure and trading-domain questions — order flow, matching logic, FIX connectivity, and market-making concepts — as distinct from pure system-design or algorithm questions.",
    "Quantitative & Probability Puzzles": "Probability, expected-value, and brainteaser-style questions that showed up alongside the engineering rounds at several firms.",
    "Interview Process, Format & Behavioral": "Reports describing the shape of the process itself — round structure, OA format, timing, and behavioral questions — rather than a single technical question.",
    "General Technical / Company-Specific": "Real and practice technical questions that didn't cleanly fit one of the categories above — still worth reviewing, especially the company-specific ones.",
}

with open(FINAL, encoding="utf-8") as f:
    data = json.load(f)

# sort: REAL first, then topic (fixed order handled client-side), then company, then question
topic_rank = {t: i for i, t in enumerate(TOPIC_ORDER)}
data.sort(key=lambda e: (
    topic_rank.get(e["topic"], 99),
    0 if e["status"] == "REAL" else 1,
    ",".join(sorted(e["companies"])),
    e["q"][:80],
))
for e in data:
    e["id"] = stable_id("qa", e["q"], e.get("topic"), e.get("source"), tuple(sorted(e.get("companies", []))))

with open(FINAL_MCQS, encoding="utf-8") as f:
    mcqs = json.load(f)
mcq_topic_rank = {t: i for i, t in enumerate(MCQ_TOPIC_ORDER)}
mcqs.sort(key=lambda m: (
    mcq_topic_rank.get(m["topic"], 99),
    {"REAL": 0, "PRACTICE": 1, "GENERATED": 2}.get(m["status"], 3),
    m["question"][:80],
))
for m in mcqs:
    m["id"] = stable_id("mcq", m["question"], m.get("topic"), tuple(m.get("options", [])))
    m["companies"] = [m.pop("company")]

with open(TEMPLATE, encoding="utf-8") as f:
    tpl = f.read()

html = (tpl
    .replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
    .replace("__TOPIC_ORDER_JSON__", json.dumps(TOPIC_ORDER, ensure_ascii=False))
    .replace("__TOPIC_DESC_JSON__", json.dumps(TOPIC_DESC, ensure_ascii=False))
    .replace("__MCQS_JSON__", json.dumps(mcqs, ensure_ascii=False))
    .replace("__MCQ_TOPIC_ORDER_JSON__", json.dumps(MCQ_TOPIC_ORDER, ensure_ascii=False))
    .replace("__CPGUIDE_URL__", CPGUIDE_URL)
    .replace("__CONCEPTS_URL__", CONCEPTS_URL)
    .replace("__COMPANYOA_URL__", COMPANYOA_URL)
    .replace("__GENERATED_DATE__", "August 28, 2026")
    .replace("__PROGRESS_SCRIPT__", PROGRESS_SCRIPT)
    .replace("__AUTH_SLOT__", AUTH_SLOT)
    .replace("__PROGRESS_ENABLED_JS__", "true" if PROGRESS_ENABLED else "false")
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Wrote {OUT}  ({len(html):,} bytes, {len(data):,} QA entries, {len(mcqs):,} MCQs)")
