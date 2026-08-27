import re, json, glob, os, hashlib

RAW_DIR = os.path.expanduser("~/quant-hft-interview-prep/raw-notes")
FIELD_RE = re.compile(r'^-\s*(Company|Role|Type|Round/Stage|Status|Source|Answer/Discussion|Topic)\s*:\s*(.*)$')

FILE_TOPIC_HINT = {
    "topic-algo-ds-oa.md": "Algorithms & Data Structures (Coding/OA)",
    "topic-concurrency-atomics.md": "Concurrency, Atomics & Lock-Free",
    "topic-cpp-core-modern.md": "C++ Core & Modern C++",
    "topic-os-networking-cpu.md": "OS, Linux, Networking & CPU/Cache/Performance",
    "topic-stl-memory-pointers.md": "STL, Memory Management & Pointers",
    "topic-system-design.md": "System Design (Trading/Low-Latency)",
}

def parse_file(path):
    fname = os.path.basename(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    blocks = re.split(r'(?m)^###\s+', text)
    entries = []
    for block in blocks[1:]:
        lines = block.split("\n")
        question = lines[0].strip()
        fields = {"Company": "", "Role": "", "Type": "", "Round/Stage": "", "Status": "",
                  "Source": "", "Answer/Discussion": "", "Topic": ""}
        current = None
        for line in lines[1:]:
            if line.startswith("## ") or line.startswith("# "):
                break
            m = FIELD_RE.match(line)
            if m:
                current = m.group(1)
                fields[current] = m.group(2).strip()
            elif current and line.strip():
                fields[current] += " " + line.strip()
        if not question or not fields["Company"]:
            continue
        # split source into name / url
        src = fields["Source"]
        url_match = re.search(r'(https?://\S+)', src)
        source_url = url_match.group(1).rstrip('.,;)') if url_match else ""
        source_name = src.split('—')[0].strip() if '—' in src else src[:src.find('http')].strip() if 'http' in src else src
        entries.append({
            "question": question,
            "company": fields["Company"],
            "role": fields["Role"] or "unknown",
            "type": fields["Type"] or "Unknown",
            "round": fields["Round/Stage"],
            "status": "REAL" if "REAL" in fields["Status"].upper() else "PRACTICE",
            "source_name": source_name,
            "source_url": source_url,
            "source_raw": src,
            "answer": fields["Answer/Discussion"],
            "topic_hint": FILE_TOPIC_HINT.get(fname, ""),
            "file": fname,
        })
    return entries

all_entries = []
for path in sorted(glob.glob(os.path.join(RAW_DIR, "*.md"))):
    entries = parse_file(path)
    print(f"{os.path.basename(path)}: {len(entries)} entries")
    all_entries.extend(entries)

print(f"\nTOTAL RAW ENTRIES: {len(all_entries)}")

out_path = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad/raw_entries.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_entries, f, indent=1)
print(f"Wrote {out_path}")
