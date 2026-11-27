#!/usr/bin/env python3
"""Score trims against the output contract, without running any task.

Deterministic part (always):
  produced            a trimmed.md was written
  original_untouched  instructions.md was left as it was
  reduction           words removed, as a share of the original
  facts_kept          share of the probe file's `facts` entries still present
  protected_kept      share of the probe file's `protected` entries still present

Judged part (--judge, one model call per trim): whether the report
  states the size before and after, gives a reason for each change,
  lists what was kept and why, names the target model, and whether any
  substantive instruction was removed without being mentioned.

Usage:
  rubric.py --arms oneline,skill --files dev --configs haiku-high,opus-medium [--judge]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

OUT = C.RESULTS / "rubric.jsonl"
JUDGE_CONFIG = "sonnet-medium"

JUDGE_SYSTEM = """You are checking a report that proposes a shorter version of an instruction file.
You get three blocks: ORIGINAL (the file), TRIMMED (the proposed version) and REPORT (what the author of the trim told the user).
Answer only with a JSON object with these keys:
- "states_size": true if REPORT gives the size before and the size after (words, tokens, lines or characters), else false.
- "size_before": the before figure REPORT states, as a number, or null.
- "size_after": the after figure REPORT states, as a number, or null.
- "size_unit": "words", "tokens", "lines", "characters" or null.
- "change_reasons": "all" if every change REPORT lists has its own reason, "most", "some", or "none" (also "none" if REPORT lists no individual changes).
- "lists_kept": true if REPORT says what was deliberately kept and why, else false.
- "names_target_model": true if REPORT names the model the trimmed version is for, else false.
- "silent_removals": up to 6 short strings, each naming an instruction that is in ORIGINAL, is absent from TRIMMED in substance, and is not mentioned anywhere in REPORT. Ignore wording changes, merged duplicates and formatting. Use [] if there are none.
Judge only what is written. Do not reward length."""

SCHEMA = {"type": "object", "properties": {
    "states_size": {"type": "boolean"}, "size_before": {"type": ["number", "null"]},
    "size_after": {"type": ["number", "null"]}, "size_unit": {"type": ["string", "null"]},
    "change_reasons": {"type": "string", "enum": ["all", "most", "some", "none"]},
    "lists_kept": {"type": "boolean"}, "names_target_model": {"type": "boolean"},
    "silent_removals": {"type": "array", "items": {"type": "string"}}},
    "required": ["states_size", "change_reasons", "lists_kept", "names_target_model", "silent_removals"]}


def entries_kept(entries: list[dict], text: str) -> tuple[int, list[str]]:
    missing = [e["id"] for e in entries if not all(re.search(p, text, re.S) for p in e["patterns"])]
    return len(entries) - len(missing), missing


def deterministic(file_id: str, config: str, arm: str, k: int) -> dict | None:
    d = C.trim_dir(file_id, config, arm, k)
    meta_p = d / "meta.json"
    if not meta_p.exists():
        return None
    meta = json.loads(meta_p.read_text())
    spec = C.load_probe(file_id)
    trimmed = (d / "trimmed.md").read_text() if (d / "trimmed.md").exists() else ""
    facts_n, facts_missing = entries_kept(spec.get("facts", []), trimmed)
    prot_n, prot_missing = entries_kept(spec.get("protected", []), trimmed)
    ow, tw = meta.get("original_words", 0), meta.get("trimmed_words", 0)
    return {"file": file_id, "config": config, "arm": arm, "k": k,
            "produced": bool(trimmed.strip()), "original_untouched": not meta.get("original_modified", False),
            "original_words": ow, "trimmed_words": tw,
            "reduction": round((ow - tw) / ow, 3) if ow and tw else None,
            "facts_total": len(spec.get("facts", [])), "facts_kept": facts_n, "facts_missing": facts_missing,
            "protected_total": len(spec.get("protected", [])), "protected_kept": prot_n, "protected_missing": prot_missing,
            "trim_cost_usd": meta.get("cost_usd", 0.0), "trim_seconds": round(meta.get("duration_ms", 0) / 1000),
            "skill_invoked": meta.get("skill_invoked"), "read_profiles": meta.get("read_profiles")}


def judge(row: dict) -> dict:
    d = C.trim_dir(row["file"], row["config"], row["arm"], row["k"])
    report = (d / "report.md").read_text() if (d / "report.md").exists() else ""
    trimmed = (d / "trimmed.md").read_text() if (d / "trimmed.md").exists() else ""
    sbx = C.make_sandbox()
    try:
        sp = sbx / "system.txt"
        sp.write_text(JUDGE_SYSTEM)
        (sbx / "cwd").mkdir()
        prompt = (f"<ORIGINAL>\n{C.original_text(row['file'])}\n</ORIGINAL>\n\n<TRIMMED>\n{trimmed}\n</TRIMMED>\n\n"
                  f"<REPORT>\n{report}\n</REPORT>\n\nReturn the JSON object now.")
        res = C.run_claude(prompt, JUDGE_CONFIG, sbx / "cwd", system_prompt_file=sp, tools="", budget=1.0, timeout=300)
        m = re.search(r"\{.*\}", res.get("text", ""), re.S)
        verdict = json.loads(m.group(0)) if m else {}
    except Exception as e:  # a failed judgement is recorded as such, never guessed
        verdict = {"judge_error": f"{type(e).__name__}: {e}"}
        res = {}
    finally:
        import shutil
        shutil.rmtree(sbx, ignore_errors=True)
    out = dict(row)
    out["judge"] = verdict
    out["judge_cost_usd"] = res.get("cost_usd", 0.0)
    # is the stated size right? compare against the real count in the stated unit
    unit, sb, sa = verdict.get("size_unit"), verdict.get("size_before"), verdict.get("size_after")
    if verdict.get("states_size") and unit in ("words", "characters", "lines") and sb and sa:
        orig, trim = C.original_text(row["file"]), trimmed
        real = {"words": (C.words(orig), C.words(trim)), "characters": (len(orig), len(trim)),
                "lines": (orig.count("\n") + 1, trim.count("\n") + 1)}[unit]
        out["size_error_before"] = round(abs(sb - real[0]) / max(real[0], 1), 3)
        out["size_error_after"] = round(abs(sa - real[1]) / max(real[1], 1), 3)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", default="oneline")
    ap.add_argument("--files", default="dev")
    ap.add_argument("--configs", default="haiku-high,opus-medium")
    ap.add_argument("--judge", action="store_true")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    files = C.corpus_ids(args.files) if args.files in ("dev", "heldout", "all") else args.files.split(",")
    out = Path(args.out)
    done = {(r["file"], r["config"], r["arm"], r["k"]) for r in C.read_jsonl(out) if ("judge" in r) == args.judge}
    rows = []
    for f in files:
        for config in args.configs.split(","):
            for arm in args.arms.split(","):
                for k in range(1, 10):
                    row = deterministic(f, config, arm, k)
                    if row and (f, config, arm, k) not in done:
                        rows.append(row)
    if args.judge:
        with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
            rows = list(pool.map(judge, rows))
    for r in rows:
        if args.judge and (not r.get("judge") or "judge_error" in r["judge"]):
            continue  # a failed judgement is rerun, never recorded
        C.append_jsonl(out, r)
    print(f"scored {len(rows)} trims -> {out}")


if __name__ == "__main__":
    main()
