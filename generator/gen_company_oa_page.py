import json, sys, os, hashlib, collections
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import site_nav, esc

SCRATCH = os.path.dirname(__file__)
DATA_PATH = f"{SCRATCH}/whatsapp_entries.json"
TEMPLATE = f"{SCRATCH}/company_oa_template.html"
OUT = "/Users/pushpakumar/quant-hft-interview-prep/docs/company-oa-questions.html"
URL_MAP_LOCAL = f"{SCRATCH}/url_map_local.json"

TOPIC_ORDER = [
    "Algorithms & Data Structures (Coding/OA)",
    "Quantitative & Probability Puzzles",
    "General Technical / Company-Specific",
    "System Design (Trading/Low-Latency)",
    "Concurrency, Atomics & Lock-Free",
    "STL, Memory Management & Pointers",
    "C++ Core & Modern C++",
    "OS, Linux, Networking & CPU/Cache/Performance",
    "HFT & Trading Domain Concepts",
    "Interview Process, Format & Behavioral",
]

TOPIC_DESC = {
    "Algorithms & Data Structures (Coding/OA)": "Coding-round and OA problems — array/string/graph/DP algorithms and data-structure tasks, reported verbatim from real assessments.",
    "Quantitative & Probability Puzzles": "Expected-value, probability, and combinatorics puzzles — concentrated at the prop-trading firms in this set (Ebullient Securities, Graviton, Squarepoint, IMC, Plutus Research, AlgoQuant).",
    "General Technical / Company-Specific": "MCQ/aptitude sections, SQL/Python questions, system-design case studies, and other company-specific format that doesn't fit a single DSA topic.",
    "System Design (Trading/Low-Latency)": "Architecture / whiteboard-design questions.",
    "Concurrency, Atomics & Lock-Free": "Threads, semaphores, and parallel-execution questions.",
    "STL, Memory Management & Pointers": "Smart pointers, move semantics, STL container questions.",
    "C++ Core & Modern C++": "Language-mechanics and output-prediction questions.",
    "OS, Linux, Networking & CPU/Cache/Performance": "OS/networking/performance questions.",
    "HFT & Trading Domain Concepts": "Market-structure and trading-domain questions.",
    "Interview Process, Format & Behavioral": "Round-structure and behavioral questions.",
}


def stable_id(prefix, *parts):
    h = hashlib.sha1("||".join(str(p) for p in parts).encode("utf-8")).hexdigest()[:12]
    return f"{prefix}-{h}"


def build_insights_html(data):
    topic_counts = collections.Counter(e["topic"] for e in data)
    total = len(data)
    bars = []
    for t in TOPIC_ORDER:
        n = topic_counts.get(t, 0)
        if not n:
            continue
        pct = round(100 * n / total)
        bars.append(
            f'<div class="bar-row"><span class="bar-label">{esc(t)}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{pct}%"></span></span>'
            f'<span class="bar-n">{n}</span></div>'
        )
    bars_html = "".join(bars)

    company_counts = collections.Counter(c for e in data for c in e["companies"])
    top_companies = ", ".join(f"{c} ({n})" for c, n in company_counts.most_common(8) if c != "Unknown")

    return f'''<section class="insights">
    <h2>Topic priority &amp; company patterns (auto-computed from this dataset)</h2>
    <div class="insights-grid">
      <div>
        <h3>Where the questions cluster</h3>
        {bars_html}
      </div>
      <div>
        <h3>Study priority</h3>
        <ul>
          <li><strong>Core DSA first</strong> — over half of everything here is a straight algorithms/data-structures problem; this is the highest-leverage prep, and overlaps directly with the site's CP/DSA Guide.</li>
          <li><strong>Quant/probability puzzles second</strong> if targeting prop-trading firms — they make up roughly a fifth of this set and are almost entirely concentrated at a handful of companies (see below).</li>
          <li><strong>MCQ/SQL/aptitude sections</strong> are a real gatekeeping stage at some companies (notably American Express) even though they carry little algorithmic depth — don't skip practicing them just because they're "easy."</li>
        </ul>
      </div>
      <div>
        <h3>Company patterns</h3>
        <ul>
          <li><strong>Prop-trading / quant cluster</strong> (Ebullient Securities, Squarepoint Capital, Graviton Research Capital, IMC Trading, Plutus Research, AlgoQuant): hard Codeforces/AtCoder-difficulty DSA plus expected-value/probability puzzles — this cluster looks the most like the rest of this site's HFT-focused content.</li>
          <li><strong>American Express</strong>: dominated by MCQ/numerical-reasoning + Python/SQL sections rather than hard DSA — a screening filter more than a coding test.</li>
          <li><strong>NatWest</strong>: mostly hands-on custom array/string/graph coding problems with few MCQs.</li>
          <li><strong>Mid-tier product/bank OAs</strong> (Wells Fargo, Oracle, Deutsche Bank, Meesho, Microsoft): standard LeetCode-medium-equivalent DSA sets.</li>
          <li><strong>Gap this surfaced</strong>: Convex Hull / computational geometry (LeetCode "Erect the Fence" asked independently at two companies, plus "Rectangle Area II") had zero coverage in the CP/DSA Guide's 14 topics — a new Computational Geometry page was added to close that gap.</li>
        </ul>
        <p style="margin-top:8px;">Top companies by question count: {esc(top_companies)}.</p>
      </div>
    </div>
  </section>'''


def main():
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)

    for e in data:
        if "id" not in e or not e["id"]:
            e["id"] = stable_id("wa", e["q"], e.get("topic"), e.get("source"), tuple(sorted(e.get("companies", []))))

    with open(URL_MAP_LOCAL, encoding="utf-8") as f:
        url_map_local = json.load(f)

    nav_urls = {
        "cpguide": url_map_local.get("cpguide-hub", "#"),
        "concepts": url_map_local.get("concepts-hub", "#"),
        "index": url_map_local.get("index", "#"),
        "companyoa": "company-oa-questions.html",
    }
    nav_html = site_nav(nav_urls, "companyoa")

    total = len(data)
    company_count = len(set(c for e in data for c in e["companies"]))
    with_link_count = sum(1 for e in data if e.get("url"))
    tagline = (
        "325 real online-assessment and interview questions collected from campus placement drives at ~30 "
        "companies (NatWest, American Express, Ebullient Securities, Squarepoint Capital, Graviton Research "
        "Capital, Wells Fargo, Oracle, Microsoft, Visa, Stripe, D.E. Shaw, and more) &mdash; every question that "
        "is verbatim a known LeetCode / Codeforces / AtCoder / GfG / HackerRank problem links straight to it so "
        "you can submit and check your solution."
    )
    insights_html = build_insights_html(data)

    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()

    html = (
        tpl.replace("__SITE_NAV__", nav_html)
        .replace("__TAGLINE__", tagline)
        .replace("__TOTAL__", str(total))
        .replace("__COMPANY_COUNT__", str(company_count))
        .replace("__WITH_LINK_COUNT__", str(with_link_count))
        .replace("__INSIGHTS_HTML__", insights_html)
        .replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
        .replace("__TOPIC_ORDER_JSON__", json.dumps(TOPIC_ORDER, ensure_ascii=False))
        .replace("__TOPIC_DESC_JSON__", json.dumps(TOPIC_DESC, ensure_ascii=False))
        .replace("__GENERATED_DATE__", "September 1, 2026")
        .replace("__INSIGHTS_URL__", url_map_local.get("oa-insights", "#"))
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {OUT}  ({len(html):,} bytes, {total} entries, {company_count} companies)")


if __name__ == "__main__":
    main()
