#!/usr/bin/env python3
"""Does the skill load when it should, and stay out of the way when it should not?

Each query runs in a small project that has the skill installed next to Claude
Code's own bundled skills. A run counts as "triggered" when the model calls the
Skill tool for this skill. Queries are in evals/trigger_queries.json: half
should trigger (some never name the skill's subject directly), half are
near-misses that share words with it.

Usage:
  triggertest.py --skill-dir ../skills/trim --configs haiku-high,opus-medium --n 3
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

OUT = C.RESULTS / "triggertest.jsonl"
QUERIES = C.EVALS / "trigger_queries.json"


def project(sbx: Path) -> None:
    """A plausible project so that the paths the queries mention exist."""
    (sbx / "CLAUDE.md").write_text(C.original_text("superclaude-rules"))
    (sbx / "AGENTS.md").write_text(C.original_text("openai-agents-agents-md"))
    (sbx / ".cursor" / "rules").mkdir(parents=True)
    (sbx / ".cursor" / "rules" / "frontend.mdc").write_text(C.original_text("cursorrules-nextjs"))
    (sbx / ".claude" / "skills" / "deploy").mkdir(parents=True)
    (sbx / ".claude" / "skills" / "deploy" / "SKILL.md").write_text(C.original_text("superpowers-tdd"))
    (sbx / "src" / "utils").mkdir(parents=True)
    (sbx / "src" / "utils" / "strings.py").write_text("def slug(s):\n    return s.lower().replace(' ', '-')\n")
    (sbx / "orders.py").write_text("def process_orders(orders):\n    return [o for o in orders if o]\n")


def run(job: dict) -> dict:
    sbx = C.make_sandbox()
    rec = {k: job[k] for k in ("qid", "should_trigger", "kind", "config", "trial")}
    try:
        project(sbx)
        src = Path(job["skill_dir"]).resolve()
        shutil.copytree(src, sbx / ".claude" / "skills" / src.name)
        tools = "Read,Glob,Grep,Skill"
        res = C.run_claude(job["query"], job["config"], sbx, tools=tools, allowed_tools=tools, slash=True,
                           budget=0.6, timeout=420, retries=1)
        calls = res.get("tool_calls", [])
        skills = [c.get("skill") for c in calls if c["name"] == "Skill"]
        rec.update({"triggered": any(s and s.split(":")[-1] == src.name for s in skills), "skills_called": skills,
                    "cost_usd": res.get("cost_usd", 0.0), "is_error": res.get("is_error", False),
                    "text": (res.get("text") or "")[:600]})
    except Exception as e:
        rec.update({"triggered": False, "is_error": True, "error": f"{type(e).__name__}: {e}"})
    finally:
        shutil.rmtree(sbx, ignore_errors=True)
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill-dir", default=str(C.ROOT / "skills" / "trim"))
    ap.add_argument("--configs", default="haiku-high,opus-medium")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    queries = json.loads(QUERIES.read_text())
    done = {(r["qid"], r["config"], r["trial"]) for r in C.read_jsonl(Path(args.out))}
    jobs = [dict(q, config=cfg, trial=t, skill_dir=args.skill_dir)
            for q in queries for cfg in args.configs.split(",") for t in range(1, args.n + 1)
            if (q["qid"], cfg, t) not in done]
    print(f"{len(jobs)} runs", flush=True)
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        for rec in pool.map(run, jobs):
            if rec.get("is_error"):
                continue
            C.append_jsonl(Path(args.out), rec)
    rows = [r for r in C.read_jsonl(Path(args.out)) if not r.get("is_error")]
    for cfg in args.configs.split(","):
        for kind in ("direct", "indirect", "near-miss"):
            rs = [r for r in rows if r["config"] == cfg and r["kind"] == kind]
            if rs:
                print(f"{cfg:12s} {kind:10s} triggered {sum(r['triggered'] for r in rs)}/{len(rs)}")


if __name__ == "__main__":
    main()
