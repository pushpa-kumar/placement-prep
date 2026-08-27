import json, re, difflib, collections

SCRATCH = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad"

def load(name):
    with open(f"{SCRATCH}/{name}", encoding="utf-8") as f:
        return json.load(f)

generated_files = ["mcq_cpp.json", "mcq_stl.json", "mcq_concurrency.json", "mcq_os_net_cpu.json", "mcq_algo_ds.json"]

mcqs = []
for fname in generated_files:
    for e in load(fname):
        mcqs.append({
            "question": e["question"],
            "code": e.get("code"),
            "options": e["options"],
            "correctIndex": e["correctIndex"],
            "explanation": e["explanation"],
            "topic": e["topic"],
            "status": "GENERATED",
            "company": "General / Unspecified",
            "source": "Self-generated for this question bank",
            "url": "",
        })

n_generated = len(mcqs)

wave3 = load("mcq_wave3_parsed.json")
for e in wave3:
    company = e.get("company", "").strip()
    if not company or company.lower() in ("unknown", "unknown/general", "general"):
        company = "General / Unspecified"
    elif "(" in company:
        company = company.split("(")[0].strip()
    mcqs.append({
        "question": e["question"],
        "code": e.get("code"),
        "options": e["options"],
        "correctIndex": e["correctIndex"],
        "explanation": e["explanation"],
        "topic": e["topic"],
        "status": e["status"],
        "company": company,
        "source": e["source"],
        "url": e["url"],
    })

n_wave3 = len(mcqs) - n_generated
print(f"self-generated: {n_generated}, wave3-sourced: {n_wave3}, total before dedup: {len(mcqs)}")

def norm(s):
    s = (s or "").lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

for m in mcqs:
    m["_norm"] = norm(m["question"] + " " + (m["code"] or ""))[:400]

# exact dedup
seen = {}
deduped = []
for m in mcqs:
    key = m["_norm"]
    if key in seen:
        continue
    seen[key] = m
    deduped.append(m)
print(f"after exact dedup: {len(deduped)}")

# near-dup within same topic
by_topic = collections.defaultdict(list)
for i, m in enumerate(deduped):
    by_topic[m["topic"]].append(i)

to_drop = set()
for topic, idxs in by_topic.items():
    for a in range(len(idxs)):
        ia = idxs[a]
        if ia in to_drop: continue
        for b in range(a+1, len(idxs)):
            ib = idxs[b]
            if ib in to_drop: continue
            na, nb = deduped[ia]["_norm"], deduped[ib]["_norm"]
            if not na or not nb: continue
            if abs(len(na)-len(nb)) > max(len(na),len(nb))*0.4: continue
            ratio = difflib.SequenceMatcher(None, na, nb).ratio()
            if ratio > 0.87:
                # keep the one with a real source (REAL/PRACTICE) over GENERATED; else keep longer explanation
                ma, mb = deduped[ia], deduped[ib]
                if ma["status"] != "GENERATED" and mb["status"] == "GENERATED":
                    to_drop.add(ib)
                elif mb["status"] != "GENERATED" and ma["status"] == "GENERATED":
                    to_drop.add(ia)
                else:
                    drop = ib if len(mb["explanation"]) <= len(ma["explanation"]) else ia
                    to_drop.add(drop)

final = [m for i, m in enumerate(deduped) if i not in to_drop]
for m in final:
    del m["_norm"]
print(f"after near-dup: {len(final)} (dropped {len(to_drop)})")

stats = {
    "total": len(final),
    "by_status": dict(collections.Counter(m["status"] for m in final)),
    "by_topic": dict(collections.Counter(m["topic"] for m in final)),
}
print(json.dumps(stats, indent=1))

with open(f"{SCRATCH}/final_mcqs.json", "w", encoding="utf-8") as f:
    json.dump(final, f, ensure_ascii=False, indent=1)
print(f"wrote final_mcqs.json ({len(final)} entries)")

concepts = load("concepts.json")
with open(f"{SCRATCH}/final_concepts.json", "w", encoding="utf-8") as f:
    json.dump(concepts, f, ensure_ascii=False, indent=1)
print(f"wrote final_concepts.json ({len(concepts)} entries)")
