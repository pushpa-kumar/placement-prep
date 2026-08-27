import re, json, glob, os

RAW_DIR = os.path.expanduser("~/quant-hft-interview-prep/raw-notes")
FIELD_RE = re.compile(r'^-\s*(Judge|Link|Difficulty|Topic|Subtopic|One-line description|Why it\'s a good hard problem|Company|Status|Source|Explanation)\s*:\s*(.*)$')

def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    blocks = re.split(r'(?m)^###\s+', text)
    entries = []
    for block in blocks[1:]:
        lines = block.split("\n")
        name = lines[0].strip()
        fields = {}
        current = None
        for line in lines[1:]:
            if line.startswith("## ") or line.startswith("# "):
                continue
            m = FIELD_RE.match(line)
            if m:
                current = m.group(1)
                fields[current] = m.group(2).strip()
            elif current and line.strip():
                fields[current] += " " + line.strip()
        if not name or "Judge" not in fields:
            continue
        entries.append({
            "name": name,
            "judge": fields.get("Judge", ""),
            "link": fields.get("Link", ""),
            "difficulty": fields.get("Difficulty", ""),
            "subtopic": fields.get("Subtopic", ""),
            "description": fields.get("One-line description", ""),
            "why_hard": fields.get("Why it's a good hard problem", ""),
        })
    return entries

TOPIC_FILES = {
    "arrays-strings": "cp-guide-arrays-strings.md",
    "sorting-searching": "cp-guide-sorting-searching.md",
    "recursion-backtracking": "cp-guide-recursion-backtracking.md",
    "dynamic-programming": ["cp-guide-dp-core.md", "cp-guide-dp-advanced.md"],
    "greedy": "cp-guide-greedy.md",
    "graphs": "cp-guide-graphs.md",
    "trees": "cp-guide-trees.md",
    "data-structures": "cp-guide-data-structures.md",
    "number-theory": "cp-guide-number-theory.md",
    "string-algorithms": "cp-guide-string-algorithms.md",
    "bit-manipulation": "cp-guide-bit-manipulation.md",
    "game-theory": "cp-guide-game-theory.md",
    "network-flow": "cp-guide-network-flow.md",
    "fft-ntt": "cp-guide-fft.md",
}

out_dir = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad/problems"
os.makedirs(out_dir, exist_ok=True)

total = 0
for slug, fnames in TOPIC_FILES.items():
    if isinstance(fnames, str):
        fnames = [fnames]
    entries = []
    for fname in fnames:
        path = os.path.join(RAW_DIR, fname)
        entries.extend(parse_file(path))
    print(f"{slug}: {len(entries)} problems")
    total += len(entries)
    with open(f"{out_dir}/{slug}.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)

print(f"TOTAL: {total}")
