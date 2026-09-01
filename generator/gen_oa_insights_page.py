import json, sys, os, collections
sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import site_nav, esc
from dsa_classify import classify_technique, dsa_technique_counts, dsa_company_top_techniques, UNCLASSIFIED_TECHNIQUE_LABEL

SCRATCH = os.path.dirname(__file__)
DATA_PATH = f"{SCRATCH}/whatsapp_entries.json"
TEMPLATE = f"{SCRATCH}/oa_insights_template.html"
OUT = "/Users/pushpakumar/quant-hft-interview-prep/docs/company-oa-insights.html"
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

TOPIC_SHORT = {
    "Algorithms & Data Structures (Coding/OA)": "DSA",
    "Quantitative & Probability Puzzles": "Quant/Aptitude",
    "General Technical / Company-Specific": "General/MCQ/SQL",
}

def build_topic_bars(data):
    total = len(data)
    counts = collections.Counter(e["topic"] for e in data)
    rows = []
    for t in TOPIC_ORDER:
        n = counts.get(t, 0)
        if not n:
            continue
        pct = round(100 * n / total)
        rows.append(
            f'<div class="bar-row"><span class="bar-label">{esc(t)}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{pct}%"></span></span>'
            f'<span class="bar-n">{n} ({pct}%)</span></div>'
        )
    return "".join(rows)


def build_company_rows(data):
    by_company = collections.defaultdict(list)
    for e in data:
        for c in e["companies"]:
            if c == "Unknown":
                continue
            by_company[c].append(e)

    rows = []
    for c, items in by_company.items():
        n = len(items)
        if n < 2:
            continue
        topic_counts = collections.Counter(e["topic"] for e in items)
        pct_dsa = round(100 * topic_counts.get("Algorithms & Data Structures (Coding/OA)", 0) / n)
        pct_quant = round(100 * topic_counts.get("Quantitative & Probability Puzzles", 0) / n)
        pct_general = round(100 * topic_counts.get("General Technical / Company-Specific", 0) / n)
        with_link = round(100 * sum(1 for e in items if e.get("url")) / n)
        rows.append((c, n, pct_dsa, pct_quant, pct_general, with_link))

    rows.sort(key=lambda r: -r[1])
    html_rows = []
    for c, n, dsa, quant, general, link in rows:
        html_rows.append(
            f"<tr><td class='company'>{esc(c)}</td><td>{n}</td>"
            f"<td class='pct-dsa'>{dsa}%</td><td>{quant}%</td><td>{general}%</td><td>{link}%</td></tr>"
        )
    return "".join(html_rows)


def build_dsa_bars(dsa_entries):
    total = len(dsa_entries)
    counts = dsa_technique_counts(dsa_entries)
    # Unclassified (bare contest references) last, everything else by frequency.
    ordered = [(t, n) for t, n in counts.most_common() if t != UNCLASSIFIED_TECHNIQUE_LABEL]
    if counts.get(UNCLASSIFIED_TECHNIQUE_LABEL):
        ordered.append((UNCLASSIFIED_TECHNIQUE_LABEL, counts[UNCLASSIFIED_TECHNIQUE_LABEL]))
    rows = []
    for label, n in ordered:
        pct = round(100 * n / total)
        rows.append(
            f'<div class="bar-row"><span class="bar-label">{esc(label)}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{pct}%"></span></span>'
            f'<span class="bar-n">{n} ({pct}%)</span></div>'
        )
    return "".join(rows)


def build_dsa_company_rows(dsa_entries):
    rows = dsa_company_top_techniques(dsa_entries, min_count=3, top_n=3)
    html_rows = []
    for c, n, top in rows:
        top_str = ", ".join(f"{esc(s)} ({k})" for s, k in top) if top else "mostly unclassified/contest references"
        html_rows.append(f"<tr><td class='company'>{esc(c)}</td><td>{n}</td><td style='text-align:left;'>{top_str}</td></tr>")
    return "".join(html_rows)


def main():
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)
    dsa_entries = [e for e in data if e["topic"] == "Algorithms & Data Structures (Coding/OA)"]

    with open(URL_MAP_LOCAL, encoding="utf-8") as f:
        url_map_local = json.load(f)

    nav_urls = {
        "cpguide": url_map_local.get("cpguide-hub", "#"),
        "concepts": url_map_local.get("concepts-hub", "#"),
        "index": url_map_local.get("index", "#"),
        "companyoa": url_map_local.get("companyoa", "#"),
    }
    nav_html = site_nav(nav_urls, "companyoa")

    total = len(data)
    company_count = len(set(c for e in data for c in e["companies"] if c != "Unknown"))
    with_link_count = sum(1 for e in data if e.get("url"))
    stats_html = "".join(
        f'<div class="stat-tile"><div class="n">{n}</div><div class="l">{l}</div></div>'
        for l, n in [
            ("Questions analyzed", total),
            ("Named companies", company_count),
            ("With a practice link", with_link_count),
        ]
    )

    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()

    html = (
        tpl.replace("__SITE_NAV__", nav_html)
        .replace("__STATS_HTML__", stats_html)
        .replace("__TOPIC_BARS_HTML__", build_topic_bars(data))
        .replace("__COMPANY_ROWS_HTML__", build_company_rows(data))
        .replace("__DSA_COUNT__", str(len(dsa_entries)))
        .replace("__DSA_BARS_HTML__", build_dsa_bars(dsa_entries))
        .replace("__DSA_COMPANY_ROWS_HTML__", build_dsa_company_rows(dsa_entries))
        .replace("__BANK_URL__", url_map_local.get("companyoa", "#"))
        .replace("__CPGUIDE_URL__", url_map_local.get("cpguide-hub", "#"))
        .replace("__GEOMETRY_URL__", url_map_local.get("computational-geometry", "#"))
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {OUT}  ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
