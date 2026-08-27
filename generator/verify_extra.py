import json, subprocess, os, sys, glob

HERE = os.path.dirname(__file__)
WORK = "/tmp/verify_extra_work"
os.makedirs(WORK, exist_ok=True)
GXX = "/opt/homebrew/bin/g++-16" if os.path.exists("/opt/homebrew/bin/g++-16") else "g++"

files = sorted(glob.glob(f"{HERE}/page_*_extra.json"))
total = 0
failed = []

for path in files:
    fname = os.path.basename(path)
    d = json.load(open(path))
    for sub in d["subtopics"]:
        for ex in sub["examples"]:
            total += 1
            src = f"{WORK}/t.cpp"
            binp = f"{WORK}/t.out"
            with open(src, "w") as f:
                f.write(ex["code"])
            comp = subprocess.run([GXX, "-std=c++17", "-O2", "-w", src, "-o", binp],
                                   capture_output=True, text=True, timeout=60)
            if comp.returncode != 0:
                failed.append((fname, sub["name"], ex["title"], "COMPILE ERROR", comp.stderr[:400]))
                continue
            try:
                run = subprocess.run([binp], input=ex["sample_input"], capture_output=True,
                                      text=True, timeout=10)
            except subprocess.TimeoutExpired:
                failed.append((fname, sub["name"], ex["title"], "TIMEOUT", ""))
                continue
            actual = run.stdout.rstrip("\n")
            expected = ex["expected_output"].rstrip("\n")
            if actual != expected:
                failed.append((fname, sub["name"], ex["title"], "OUTPUT MISMATCH",
                                f"expected={expected!r}\n    actual=  {actual!r}"))

print(f"TOTAL NEW EXAMPLES: {total}")
print(f"FAILED: {len(failed)}")
for fname, sub, title, kind, detail in failed:
    print(f"\n--- {fname} / {sub} / {title} ---")
    print(kind)
    print(detail)
