import json, glob, subprocess, os, sys

SCRATCH = "/private/tmp/claude-502/-Users-pushpakumar/c8e85676-8f01-4b43-b788-3703f3293634/scratchpad"
GXX = "/opt/homebrew/bin/g++-16"
tmpdir = f"{SCRATCH}/verify_tmp"
os.makedirs(tmpdir, exist_ok=True)

total = 0
failed = []
for path in sorted(glob.glob(f"{SCRATCH}/page_*.json")):
    d = json.load(open(path))
    fname = os.path.basename(path)
    for sub in d["subtopics"]:
        for ex in sub["examples"]:
            total += 1
            src = f"{tmpdir}/t.cpp"
            with open(src, "w") as f:
                f.write(ex["code"])
            binpath = f"{tmpdir}/t.out"
            comp = subprocess.run([GXX, "-std=c++17", "-O2", "-w", src, "-o", binpath],
                                   capture_output=True, text=True, timeout=60)
            if comp.returncode != 0:
                failed.append((fname, sub["name"], ex["title"], "COMPILE ERROR", comp.stderr[:500]))
                continue
            try:
                run = subprocess.run([binpath], input=ex["sample_input"], capture_output=True,
                                      text=True, timeout=10)
            except subprocess.TimeoutExpired:
                failed.append((fname, sub["name"], ex["title"], "TIMEOUT", ""))
                continue
            actual = run.stdout.rstrip("\n")
            expected = ex["expected_output"].rstrip("\n")
            if actual != expected:
                failed.append((fname, sub["name"], ex["title"], "OUTPUT MISMATCH",
                                f"expected={expected!r} actual={actual!r}"))

print(f"TOTAL EXAMPLES: {total}")
print(f"FAILED: {len(failed)}")
for fname, sub, title, kind, detail in failed:
    print(f"\n--- {fname} / {sub} / {title} ---")
    print(kind)
    print(detail)
