#!/usr/bin/env python3
"""Run behaviour probes for instruction-file variants.

For every (file, task, arm, config, trial) this runs the task once with the
arm's version of the instructions and records which checks passed.

  arm = none      no instructions at all (control)
        original  the file as published
        <other>   a trimmed version from evals/results/trims/<file>/<config>/<arm>/<k>/trimmed.md

Trial i uses trim i (wrapping around the number of trims available), so three
trials of a trimmed arm cover three independent trims.

Usage:
  probe.py --files dev --arms none,original --configs haiku-high --trials 3
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

OUT = C.RESULTS / "probe_runs.jsonl"


def trims_available(file_id: str, config: str, arm: str) -> int:
    base = C.RESULTS / "trims" / file_id / config / arm
    if not base.exists():
        return 0
    return sum(1 for d in base.iterdir() if (d / "trimmed.md").exists())


def run_job(job: dict) -> dict:
    file_id, task, arm, config, trial = job["file"], job["task"], job["arm"], job["config"], job["trial"]
    spec = job["spec"]
    mode = spec["mode"]
    k = job["k"]
    text = C.variant_text(file_id, config, arm, k)
    sbx = C.make_sandbox(spec.get("scaffold") if mode == "agent" else None)
    rec = {"file": file_id, "task": task["id"], "arm": arm, "config": config, "trial": trial, "trim_k": k,
           "mode": mode, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        if mode == "agent":
            if text is not None:
                (sbx / "CLAUDE.md").write_text(text)
            C.git_init(sbx)
            before = C.snapshot(sbx)
            tools = C.AGENT_TOOLS
            allowed = C.AGENT_TOOLS
            if spec.get("allowed_bash"):
                tools += ",Bash"
                allowed += "," + ",".join(f"Bash({b})" for b in spec["allowed_bash"])
            res = C.run_claude(task["prompt"], config, sbx, tools=tools, allowed_tools=allowed,
                               permission_mode="acceptEdits", budget=job["budget"], timeout=job["timeout"])
            changed = C.changed_files(sbx, before)
            ctx = {"text": res.get("text", ""), "changed": changed, "tool_calls": res.get("tool_calls", []),
                   "git_branch": C.git_branch(sbx), "git_commits_main": C.git_commit_count(sbx, "main")}
        else:
            sp = sbx / "system_prompt.txt"
            sp.write_text(text if text is not None else C.NEUTRAL_SYSTEM)
            run_dir = sbx / "cwd"
            run_dir.mkdir()
            res = C.run_claude(task["prompt"], config, run_dir, system_prompt_file=sp, tools="",
                               budget=job["budget"], timeout=job["timeout"])
            ctx = {"text": res.get("text", ""), "changed": {}, "tool_calls": []}

        checks = {}
        for chk in task["checks"]:
            checks[chk["id"]] = C.eval_check(chk, ctx)["pass"] if not res.get("is_error") else False
        rec.update({
            "checks": checks, "is_error": res.get("is_error", False), "error": res.get("error"),
            "cost_usd": res.get("cost_usd", 0.0), "usage": res.get("usage", {}),
            "num_turns": res.get("num_turns", 0), "duration_ms": res.get("duration_ms", 0),
            "attempts": res.get("attempts", 1), "limit_hit": res.get("limit_hit", False),
            "text": (res.get("text") or "")[:6000],
            "changed": {p: c[:6000] for p, c in list(ctx["changed"].items())[:12]},
            "tool_calls": [{"name": c["name"], "path": c.get("path"), "command": (c.get("command") or "")[:300] or None}
                           for c in ctx["tool_calls"]][:60],
            "git_branch": ctx.get("git_branch"),
        })
    except Exception as e:  # keep the batch alive; the record says what happened
        rec.update({"checks": {c["id"]: False for c in task["checks"]}, "is_error": True,
                    "error": f"{type(e).__name__}: {e}", "cost_usd": 0.0, "usage": {}})
    finally:
        shutil.rmtree(sbx, ignore_errors=True)
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", default="dev", help="dev | heldout | all | comma-separated ids")
    ap.add_argument("--arms", default="none,original")
    ap.add_argument("--configs", default="haiku-high")
    ap.add_argument("--trials", type=int, default=3)
    ap.add_argument("--tasks", default="", help="optional comma-separated task ids")
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--budget", type=float, default=1.0, help="per-run spend cap in USD")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--max-total-usd", type=float, default=60.0, help="stop launching runs past this spend")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--rerun-errors", action="store_true")
    args = ap.parse_args()

    out = Path(args.out)
    files = C.corpus_ids(args.files) if args.files in ("dev", "heldout", "all") else args.files.split(",")
    arms = args.arms.split(",")
    configs = args.configs.split(",")
    only = set(filter(None, args.tasks.split(",")))

    done = set()
    for r in C.read_jsonl(out):
        if args.rerun_errors and r.get("is_error"):
            continue
        done.add((r["file"], r["task"], r["arm"], r["config"], r["trial"]))

    jobs = []
    for f in files:
        spec = C.load_probe(f)
        for config in configs:
            for arm in arms:
                n = 1 if arm in ("none", "original") else trims_available(f, config, arm)
                if n == 0:
                    print(f"skip {f}/{config}/{arm}: no trims yet", flush=True)
                    continue
                for task in spec["tasks"]:
                    if only and task["id"] not in only:
                        continue
                    for trial in range(1, args.trials + 1):
                        key = (f, task["id"], arm, config, trial)
                        if key in done:
                            continue
                        jobs.append({"file": f, "task": task, "arm": arm, "config": config, "trial": trial,
                                     "k": ((trial - 1) % n) + 1, "spec": spec,
                                     "budget": args.budget, "timeout": args.timeout})

    print(f"{len(jobs)} runs to do ({len(done)} already recorded)", flush=True)
    spent, finished, errors, t0 = 0.0, 0, 0, time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        pending = iter(jobs)
        futures = set()

        def submit_next() -> bool:
            if spent >= args.max_total_usd:
                return False
            job = next(pending, None)
            if job is None:
                return False
            futures.add(pool.submit(run_job, job))
            return True

        for _ in range(args.concurrency):
            submit_next()
        while futures:
            fut = next(as_completed(futures))
            futures.discard(fut)
            rec = fut.result()
            if rec.get("limit_hit") or C.limit_hit():
                print("usage limit reached: stopping; rerun the same command later to resume", flush=True)
                pending = iter(())
                if rec.get("limit_hit"):
                    continue
            C.append_jsonl(out, rec)
            spent += rec.get("cost_usd", 0.0)
            finished += 1
            errors += 1 if rec.get("is_error") else 0
            if finished % 10 == 0 or finished == len(jobs):
                rate = finished / max(time.time() - t0, 1)
                eta = (len(jobs) - finished) / max(rate, 1e-6)
                print(f"[{finished}/{len(jobs)}] spent=${spent:.2f} errors={errors} eta={eta/60:.1f}min", flush=True)
            submit_next()
    if spent >= args.max_total_usd:
        print(f"stopped at spend cap ${args.max_total_usd}", flush=True)
    print(f"done: {finished} runs, ${spent:.2f}, {errors} errors, {(time.time()-t0)/60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
