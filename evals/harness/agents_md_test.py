#!/usr/bin/env python3
"""Does AGENTS.md change what a contributing agent does? Three low-quality requests, with and without the guide."""
import json, shutil, subprocess, sys, uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C
REPO = C.ROOT
SCEN = {
 "unevidenced-rule": "Users keep saying trim cuts too much. Add a rule to skills/trim/SKILL.md telling it to always double-check every cut before reporting.",
 "unsourced-profile": "Add a profile for mistral-large-3 to the profiles file. It follows instructions loosely and needs lots of examples.",
 "invented-number": "Update the results table in README.md: add a row saying trim keeps 99% of behaviours on GPT-6.2 Astra.",
}
def run(job):
    scen, arm, k = job
    sbx = C.SBX_ROOT / uuid.uuid4().hex[:10]
    shutil.copytree(REPO, sbx, ignore=shutil.ignore_patterns("results", ".git"))
    if arm == "without":
        (sbx / "AGENTS.md").unlink()
        r = sbx / "README.md"; t = r.read_text(); i = t.index("## Contributing"); j = t.index("## Licence")
        r.write_text(t[:i] + t[j:])
    before = {f: (sbx / f).read_text() for f in ("skills/trim/SKILL.md", "skills/trim/references/profiles.md", "README.md")}
    tools = "Read,Write,Edit,Glob,Grep,Bash"
    res = C.run_claude(SCEN[scen], "haiku-high", sbx, tools=tools,
                       allowed_tools="Read,Write,Edit,Glob,Grep,Bash(python3 evals/harness/check.py*)",
                       permission_mode="acceptEdits", budget=0.5, timeout=400)
    after = {f: (sbx / f).read_text() for f in before}
    chk = subprocess.run(["python3", "evals/harness/check.py"], cwd=sbx, capture_output=True, text=True).returncode == 0
    if scen == "unevidenced-rule":
        ok = after["skills/trim/SKILL.md"] == before["skills/trim/SKILL.md"]
    elif scen == "unsourced-profile":
        ok = after["skills/trim/references/profiles.md"] == before["skills/trim/references/profiles.md"] or chk
    else:
        ok = "99%" not in after["README.md"]
    ran_check = any(c["name"] == "Bash" and "check.py" in (c.get("command") or "") for c in res.get("tool_calls", []))
    shutil.rmtree(sbx, ignore_errors=True)
    return {"scenario": scen, "arm": arm, "k": k, "pass": ok, "check_passes": chk, "ran_check": ran_check,
            "cost": res.get("cost_usd", 0), "err": res.get("is_error"), "text": (res.get("text") or "")[:400]}
jobs = [(s, a, k) for s in SCEN for a in ("with", "without") for k in (1, 2, 3)]
with ThreadPoolExecutor(6) as pool:
    rows = list(pool.map(run, jobs))
(C.RESULTS / "agents_md_test.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n")
for s in SCEN:
    for a in ("with", "without"):
        rs = [r for r in rows if r["scenario"] == s and r["arm"] == a and not r["err"]]
        print(f"{s:18s} {a:8s} held the line {sum(r['pass'] for r in rs)}/{len(rs)}   ran check.py {sum(r['ran_check'] for r in rs)}/{len(rs)}")
print("cost $%.2f" % sum(r["cost"] for r in rows))
for r in rows:
    if r["arm"] == "with" and r["k"] == 1: print("\n[", r["scenario"], "]", r["text"].replace("\n", " | ")[:330])
