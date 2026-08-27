import re, json, glob, os

RAW_DIR = os.path.expanduser("~/quant-hft-interview-prep/raw-notes")
FIELD_RE = re.compile(r'^-\s*(Options|Correct|Company|Type|Topic|Status|Source|Explanation)\s*:\s*(.*)$')

def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    blocks = re.split(r'(?m)^###\s+', text)
    entries = []
    for block in blocks[1:]:
        lines = block.split("\n")
        # question text = everything up to the first "- Options:" line
        q_lines = []
        i = 0
        fields = {"Options": "", "Correct": "", "Company": "", "Type": "", "Topic": "",
                  "Status": "", "Source": "", "Explanation": ""}
        current = None
        started_fields = False
        for line in lines:
            if not started_fields:
                m = FIELD_RE.match(line)
                if m:
                    started_fields = True
                    current = m.group(1)
                    fields[current] = m.group(2).strip()
                    continue
                if line.startswith("## ") or line.startswith("---"):
                    continue
                q_lines.append(line)
            else:
                m = FIELD_RE.match(line)
                if m:
                    current = m.group(1)
                    fields[current] = m.group(2).strip()
                elif current and line.strip():
                    fields[current] += " " + line.strip()
        question_raw = "\n".join(q_lines).strip()
        if not question_raw or not fields["Options"]:
            continue

        # extract fenced code block if present
        code = None
        code_m = re.search(r'```[a-zA-Z]*\n(.*?)```', question_raw, re.S)
        if code_m:
            code = code_m.group(1).rstrip("\n")
            question_text = (question_raw[:code_m.start()] + question_raw[code_m.end():]).strip()
        else:
            question_text = question_raw

        # parse options: "A) foo B) bar C) baz D) qux"
        opt_matches = re.findall(r'([A-D])\)\s*(.*?)(?=\s+[A-D]\)|$)', fields["Options"])
        if len(opt_matches) < 2:
            continue
        letters = [m[0] for m in opt_matches]
        options = [m[1].strip() for m in opt_matches]
        correct_letter = fields["Correct"].strip()[:1].upper()
        if correct_letter not in letters:
            continue
        correct_index = letters.index(correct_letter)

        status = "REAL" if "REAL" in fields["Status"].upper() else "PRACTICE"
        src = fields["Source"]
        url_m = re.search(r'(https?://\S+)', src)
        source_url = url_m.group(1).rstrip('.,;)') if url_m else ""
        source_name = src.split('—')[0].strip() if '—' in src else src

        topic_field = fields["Topic"].strip().lower()
        topic_map = {
            "cpu/cache": "OS, Linux, Networking & CPU/Cache/Performance",
            "stl/ds": "STL, Memory Management & Pointers",
        }
        default_topic = {
            "mcq-wave3-cpp.md": "C++ Core & Modern C++",
            "mcq-wave3-os.md": "OS, Linux, Networking & CPU/Cache/Performance",
            "mcq-wave3-networking.md": "OS, Linux, Networking & CPU/Cache/Performance",
        }
        fname = os.path.basename(path)
        topic = topic_map.get(topic_field, default_topic.get(fname, "OS, Linux, Networking & CPU/Cache/Performance"))

        entries.append({
            "question": question_text,
            "code": code,
            "options": options,
            "correctIndex": correct_index,
            "explanation": fields["Explanation"],
            "topic": topic,
            "status": status,
            "company": fields["Company"],
            "source": source_name,
            "url": source_url,
        })
    return entries

all_entries = []
for path in sorted(glob.glob(os.path.join(RAW_DIR, "mcq-wave3-*.md"))):
    entries = parse_file(path)
    print(f"{os.path.basename(path)}: {len(entries)} parsed")
    all_entries.extend(entries)

print(f"TOTAL: {len(all_entries)}")
out = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad/mcq_wave3_parsed.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(all_entries, f, indent=1)
print("wrote", out)
