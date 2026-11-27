#!/usr/bin/env python3
"""Generate trimmed versions of corpus files, one arm at a time.

Arms
  oneline   a one-line request, no skill installed
  builtin   Claude Code's bundled `/claude-api prompt-audit`, asked to apply its edits to a copy
  skill     a skill directory installed as a project skill and invoked by name

Each run happens in a fresh sandbox that holds only `instructions.md` (plus the
skill for the skill arm). The trimmer runs on the same model and effort the
trimmed file is meant for. Output lands in
evals/results/trims/<file>/<config>/<arm>/<k>/{trimmed.md,report.md,meta.json}.

Usage:
  trim.py --arm oneline --files dev --configs haiku-high,opus-medium --k 3
  trim.py --arm skill --skill-dir ../skills/trim --files dev --configs haiku-high --k 3
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

MECHANICS = "Save the proposed version as trimmed.md and leave instructions.md unchanged."

PROMPTS = {
    "oneline": "Audit instructions.md and propose a shorter version suited to {model}. " + MECHANICS,
    "builtin": "/claude-api prompt-audit instructions.md -- the target model is {model}. "
               "Apply your proposed edits to a copy saved as trimmed.md and leave instructions.md unchanged.",
    "skill": "/{skill} instructions.md for {model}. " + MECHANICS,
}


def run_one(job: dict) -> dict:
    file_id, config, arm, k = job["file"], job["config"], job["arm"], job["k"]
    out_dir = C.trim_dir(file_id, config, arm, k)
    model = C.CONFIGS[config]["model"]
    original = C.original_text(file_id)
    sbx = C.make_sandbox()
    meta = {"file": file_id, "config": config, "arm": arm, "k": k, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        (sbx / "instructions.md").write_text(original)
        skill_name = None
        if job.get("skill_dir"):
            skill_src = Path(job["skill_dir"]).resolve()
            skill_name = skill_src.name
            shutil.copytree(skill_src, sbx / ".claude" / "skills" / skill_name)
            meta["skill_sha"] = C.sha256("".join(p.read_text() for p in sorted(skill_src.rglob("*")) if p.is_file()))
        kind = job["prompt_kind"]
        prompt = PROMPTS[kind].format(model=model, skill=skill_name)
        res = C.run_claude(prompt, config, sbx, tools=C.AGENT_TOOLS, allowed_tools=C.AGENT_TOOLS,
                           permission_mode="acceptEdits", slash=True, budget=job["budget"], timeout=job["timeout"])
        if res.get("limit_hit"):
            meta.update({"is_error": True, "limit_hit": True, "produced": False, "cost_usd": 0.0, "error": "usage limit"})
            return meta
        trimmed_path = sbx / "trimmed.md"
        trimmed = trimmed_path.read_text() if trimmed_path.exists() else ""
        after = (sbx / "instructions.md").read_text() if (sbx / "instructions.md").exists() else ""
        calls = res.get("tool_calls", [])
        meta.update({
            "prompt": prompt, "produced": bool(trimmed.strip()), "original_modified": after != original,
            "original_words": C.words(original), "original_chars": len(original),
            "trimmed_words": C.words(trimmed), "trimmed_chars": len(trimmed),
            "is_error": res.get("is_error", False), "error": res.get("error"),
            "cost_usd": res.get("cost_usd", 0.0), "usage": res.get("usage", {}),
            "num_turns": res.get("num_turns", 0), "duration_ms": res.get("duration_ms", 0),
            "skill_invoked": any(c["name"] == "Skill" for c in calls),
            "read_profiles": any(c["name"] == "Read" and "profiles" in (c.get("path") or "") for c in calls),
            "tools": [c["name"] for c in calls],
        })
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)
        if trimmed.strip():
            (out_dir / "trimmed.md").write_text(trimmed)
        (out_dir / "report.md").write_text(res.get("text") or "")
        (out_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    except Exception as e:
        meta.update({"is_error": True, "error": f"{type(e).__name__}: {e}", "produced": False, "cost_usd": 0.0})
    finally:
        shutil.rmtree(sbx, ignore_errors=True)
    return meta


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, help="name to store results under")
    ap.add_argument("--prompt-kind", default=None, help="oneline | builtin | skill (defaults from --arm)")
    ap.add_argument("--skill-dir", default=None)
    ap.add_argument("--files", default="dev")
    ap.add_argument("--configs", default="haiku-high")
    ap.add_argument("--k", type=int, default=3, help="independent trims per file and config")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--budget", type=float, default=3.0)
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    kind = args.prompt_kind or ("skill" if args.skill_dir else args.arm if args.arm in PROMPTS else "oneline")
    files = C.corpus_ids(args.files) if args.files in ("dev", "heldout", "all") else args.files.split(",")
    jobs = []
    for f in files:
        for config in args.configs.split(","):
            for k in range(1, args.k + 1):
                d = C.trim_dir(f, config, args.arm, k)
                if (d / "trimmed.md").exists() and not args.force:
                    continue
                jobs.append({"file": f, "config": config, "arm": args.arm, "k": k, "prompt_kind": kind,
                             "skill_dir": args.skill_dir, "budget": args.budget, "timeout": args.timeout})
    print(f"{len(jobs)} trims to generate for arm '{args.arm}' ({kind})", flush=True)
    spent, t0 = 0.0, time.time()
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        for i, fut in enumerate(as_completed([pool.submit(run_one, j) for j in jobs]), 1):
            m = fut.result()
            spent += m.get("cost_usd", 0.0)
            flag = "" if m.get("produced") else "  NO OUTPUT"
            flag += "  ORIGINAL MODIFIED" if m.get("original_modified") else ""
            flag += f"  ERROR {m.get('error')}" if m.get("is_error") else ""
            ow, tw = m.get("original_words", 0), m.get("trimmed_words", 0)
            pct = f"{100 * (ow - tw) / ow:.0f}%" if ow and tw else "-"
            print(f"[{i}/{len(jobs)}] {m['file']} {m['config']} {m['arm']}#{m['k']}: {ow}->{tw} words (-{pct}) "
                  f"${m.get('cost_usd', 0):.3f} {m.get('duration_ms', 0) / 1000:.0f}s{flag}", flush=True)
    print(f"done: ${spent:.2f}, {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
