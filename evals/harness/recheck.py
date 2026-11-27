#!/usr/bin/env python3
"""Re-evaluate stored probe runs against the current probe definitions.

Use after fixing a check (a regex that missed a correct reply, say) so that old
runs do not have to be repeated. Only the named checks are recomputed.

  recheck.py --file cursorrules-nextjs --checks uses-next-safe-action [--runs results/probe_runs.jsonl]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--checks", required=True, help="comma-separated check ids")
    ap.add_argument("--runs", default=str(C.RESULTS / "probe_runs.jsonl"))
    args = ap.parse_args()
    wanted = set(args.checks.split(","))
    spec = C.load_probe(args.file)
    checks = {c["id"]: c for t in spec["tasks"] for c in t["checks"] if c["id"] in wanted}
    path = Path(args.runs)
    out, changed = [], 0
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if r["file"] == args.file and not r.get("is_error"):
            ctx = {"text": r.get("text", ""), "changed": r.get("changed", {}),
                   "tool_calls": r.get("tool_calls", []), "git_branch": r.get("git_branch")}
            for cid, chk in checks.items():
                if cid in r["checks"]:
                    new = C.eval_check(chk, ctx)["pass"]
                    changed += new != r["checks"][cid]
                    r["checks"][cid] = new
        out.append(json.dumps(r, ensure_ascii=False))
    path.write_text("\n".join(out) + "\n")
    print(f"rechecked {sorted(checks)} in {args.file}: {changed} results changed")


if __name__ == "__main__":
    main()
