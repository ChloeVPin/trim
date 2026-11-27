#!/usr/bin/env python3
"""Measure the size in tokens of every instruction version, on the model it is for.

Each text is sent once as a system prompt with a trivial user message; the
input-token count the API reports, minus the count for a one-character system
prompt, is the text's size on that model's tokenizer.

Usage:
  tokens.py --files all --arms original,oneline,builtin,skill --configs haiku-high,opus-medium
"""
from __future__ import annotations

import argparse
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

OUT = C.RESULTS / "tokens.jsonl"


def count(text: str, config: str) -> int:
    sbx = C.make_sandbox()
    try:
        sp = sbx / "sp.txt"
        sp.write_text(text)
        (sbx / "cwd").mkdir()
        res = C.run_claude("Reply with OK.", config, sbx / "cwd", system_prompt_file=sp, tools="", budget=0.5, timeout=180)
        u = res.get("usage", {})
        return u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
    finally:
        shutil.rmtree(sbx, ignore_errors=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", default="all")
    ap.add_argument("--arms", default="original,oneline,builtin,skill")
    ap.add_argument("--configs", default="haiku-high,opus-medium")
    ap.add_argument("--concurrency", type=int, default=6)
    args = ap.parse_args()
    files = C.corpus_ids(args.files) if args.files in ("dev", "heldout", "all") else args.files.split(",")
    done = {(r["file"], r["config"], r["arm"], r["k"]) for r in C.read_jsonl(OUT)}
    base = {}
    for config in args.configs.split(","):
        prior = [r for r in C.read_jsonl(OUT) if r["file"] == "_baseline" and r["config"] == config]
        base[config] = prior[0]["tokens"] if prior else count("x", config)
        if not prior:
            C.append_jsonl(OUT, {"file": "_baseline", "config": config, "arm": "-", "k": 0, "tokens": base[config]})
    jobs = []
    for f in files:
        for config in args.configs.split(","):
            for arm in args.arms.split(","):
                ks = [1] if arm == "original" else [k for k in range(1, 10) if (C.trim_dir(f, config, arm, k) / "trimmed.md").exists()]
                for k in ks:
                    if (f, config, arm, k) not in done:
                        jobs.append((f, config, arm, k))

    def work(job):
        f, config, arm, k = job
        text = C.variant_text(f, config, arm, k)
        return {"file": f, "config": config, "arm": arm, "k": k, "words": C.words(text), "chars": len(text),
                "tokens": max(count(text, config) - base[config], 0)}

    print(f"{len(jobs)} texts to measure", flush=True)
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        for rec in pool.map(work, jobs):
            C.append_jsonl(OUT, rec)
    print("done")


if __name__ == "__main__":
    main()
