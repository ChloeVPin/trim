#!/usr/bin/env python3
"""Does the trimmer handle an unnamed target model correctly?

Two scenarios, each run with the one-line request and with the skill:

  same-assistant   the file is plainly for the assistant that is running (a
                   Claude Code rules file). Right behaviour: use the model ID
                   the app states and say it was assumed.
  other-product    the person says the instructions are for another product
                   (ChatGPT) and names no model. Right behaviour: ask which
                   model before proposing anything.

The headless CLI always tells the model its own ID, so the case "the app does
not state a model at all" cannot be produced here and is not tested.

Usage:
  asktest.py --skill-dir ../skills/trim --configs haiku-high,opus-medium --n 3
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

OUT = C.RESULTS / "asktest.jsonl"

SCENARIOS = {
    "same-assistant": {
        "file": "superclaude-rules",
        "oneline": "Audit instructions.md and propose a shorter version suited to the model that will use it.",
        "skill": "/{skill} instructions.md",
    },
    "other-product": {
        "file": "daveshap-default-ci",
        "oneline": "instructions.md holds my ChatGPT custom instructions. Audit them and propose a shorter version "
                   "suited to the model that will use them.",
        "skill": "/{skill} instructions.md (these are my ChatGPT custom instructions)",
    },
}

ASKS = re.compile(r"which (specific |exact |openai |chatgpt |gpt[- ]?)*model|what model|which version|"
                  r"model (are|do|will|is)[^.?\n]{0,60}\?|tell me (which|the) model|name the model", re.I)
ASSUMED = re.compile(r"assum", re.I)


def run(job: dict) -> dict:
    sc = SCENARIOS[job["scenario"]]
    model = C.CONFIGS[job["config"]]["model"]
    sbx = C.make_sandbox()
    rec = {"scenario": job["scenario"], "arm": job["arm"], "config": job["config"], "trial": job["trial"],
           "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        (sbx / "instructions.md").write_text(C.original_text(sc["file"]))
        skill_name = None
        if job["arm"] != "oneline":
            src = Path(job["skill_dir"]).resolve()
            skill_name = src.name
            shutil.copytree(src, sbx / ".claude" / "skills" / skill_name)
        prompt = sc["oneline" if job["arm"] == "oneline" else "skill"].format(skill=skill_name)
        res = C.run_claude(prompt, job["config"], sbx, tools=C.AGENT_TOOLS, allowed_tools=C.AGENT_TOOLS,
                           permission_mode="acceptEdits", slash=True, budget=2.0, timeout=900)
        text = res.get("text", "")
        new_files = [p.name for p in sbx.iterdir() if p.is_file() and p.name != "instructions.md"]
        untouched = (sbx / "instructions.md").read_text() == C.original_text(sc["file"])
        asked = bool(ASKS.search(text))
        proposed = bool(new_files) or not untouched or len(text.split()) > 400
        if job["scenario"] == "other-product":
            ok = asked and not proposed
        else:
            ok = (model in text) and bool(ASSUMED.search(text))
        rec.update({"pass": ok, "asked": asked, "proposed": proposed, "names_running_model": model in text,
                    "says_assumed": bool(ASSUMED.search(text)), "original_untouched": untouched,
                    "new_files": new_files, "cost_usd": res.get("cost_usd", 0.0), "is_error": res.get("is_error", False),
                    "text": text[:3000]})
    except Exception as e:
        rec.update({"pass": False, "is_error": True, "error": f"{type(e).__name__}: {e}"})
    finally:
        shutil.rmtree(sbx, ignore_errors=True)
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill-dir", required=True)
    ap.add_argument("--skill-arm", default="skill")
    ap.add_argument("--arms", default="oneline,skill")
    ap.add_argument("--configs", default="haiku-high,opus-medium")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    done = {(r["scenario"], r["arm"], r["config"], r["trial"]) for r in C.read_jsonl(Path(args.out))}
    jobs = []
    for scenario in SCENARIOS:
        for arm in args.arms.split(","):
            arm_name = "oneline" if arm == "oneline" else args.skill_arm
            for config in args.configs.split(","):
                for t in range(1, args.n + 1):
                    if (scenario, arm_name, config, t) not in done:
                        jobs.append({"scenario": scenario, "arm": arm_name, "config": config, "trial": t,
                                     "skill_dir": args.skill_dir})
    print(f"{len(jobs)} runs", flush=True)
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        for rec in pool.map(run, jobs):
            if rec.get("is_error"):
                continue
            C.append_jsonl(Path(args.out), rec)
    rows = C.read_jsonl(Path(args.out))
    agg = {}
    for r in rows:
        k = (r["scenario"], r["arm"], r["config"])
        agg.setdefault(k, [0, 0])
        agg[k][0] += 1 if r.get("pass") else 0
        agg[k][1] += 1
    for k in sorted(agg):
        print(f"{k[0]:16s} {k[1]:10s} {k[2]:12s} {agg[k][0]}/{agg[k][1]}")


if __name__ == "__main__":
    main()
