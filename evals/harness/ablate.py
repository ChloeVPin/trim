#!/usr/bin/env python3
"""Deletion test: does removing one sentence of the skill change what it does?

Each unit removes (or rewrites) one piece of SKILL.md, runs the skill on the
inputs that piece is meant to affect, and scores one assertion. "full" is the
unmodified skill on the same inputs. A unit whose assertion passes as often
without it as with it is a candidate for deletion.

Usage:
  ablate.py --skill-dir ../skills/trim --units full,approve,outranks ... [--k-haiku 3 --k-opus 2]
  ablate.py --summary
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402
import rubric as R  # noqa: E402

OUT = C.RESULTS / "ablation.jsonl"
MECH = " Save the proposed version as trimmed.md and leave instructions.md unchanged."

# ---------------------------------------------------------------- prompts
PROMPTS = {
    "default": "/{skill} instructions.md for {model}." + MECH,
    "bare": "/{skill} instructions.md for {model}.",
    "override": "/{skill} instructions.md for {model}. Drop the Git Workflow section completely, I don't use git "
                "with this setup." + MECH,
    "unlisted": "/{skill} instructions.md for mistral-large-3." + MECH,
    "luna": "/{skill} instructions.md for gpt-6-luna." + MECH,
    "ask-same": "/{skill} instructions.md",
    "ask-other": "/{skill} instructions.md (these are my ChatGPT custom instructions)",
}

ASKS = re.compile(r"which (specific |exact |openai |chatgpt |gpt[- ]?)*model|what model|which version|"
                  r"model (are|do|will|is)[^.?\n]{0,60}\?|tell me (which|the) model|name the model", re.I)
CAPS = re.compile(r"\b(ALWAYS|NEVER|MUST|ONLY|CRITICAL|IMPORTANT|ALL|ANY)\b")


# ---------------------------------------------------------------- assertions
def a_untouched(o):
    return not o["original_modified"]


def a_complied_with_user(o):
    return bool(o["trimmed"].strip()) and not re.search(r"feature branch", o["trimmed"], re.I)


def a_assumed_running_model(o):
    return o["model"] in o["report"] and bool(re.search(r"assum", o["report"], re.I))


def a_asked_and_waited(o):
    return bool(ASKS.search(o["report"])) and not o["trimmed"].strip() and not o["original_modified"] \
        and len(o["report"].split()) <= 400


def a_says_no_profile(o):
    return bool(re.search(r"no profile|not (listed|in the profile|covered)|isn(?:'|’)t (listed|in the profile)|"
                          r"best effort|conservative", o["report"], re.I))


def a_preferences_full_strength(o):
    t = o["trimmed"]
    return bool(re.search(r"never explain (things )?unless", t, re.I)) and bool(re.search(r"never recommend", t, re.I)) \
        and bool(re.search(r"never apologi", t, re.I))


def a_flags_with_savings(o):
    return bool(re.search(r"(?i)(flag|for you to decide|your call|decide)", o["report"])) and \
        bool(re.search(r"(?i)\b\d{1,4}\s+(more\s+)?words", o["report"]))


def a_guards_exact(o):
    spec = C.load_probe(o["file"])
    kept, _ = R.entries_kept(spec.get("protected", []), o["trimmed"])
    exact = {"taubench-airline": "you must list the action details and obtain explicit user confirmation (yes) to proceed",
             "superclaude-rules": "never work on main/master"}[o["file"]]
    return kept == len(spec.get("protected", [])) and exact in o["trimmed"]


def a_frontmatter_kept(o):
    return o["trimmed"].lstrip().split("\n")[:5] == o["original"].lstrip().split("\n")[:5]


def a_flagged_not_settled(o):
    if o["file"] == "taubench-airline":
        return "2024-05-15" in o["trimmed"]
    conflict = re.search(r"(?i)(conflict|contradict|clash|pull(s)? against|disagree)[^\n]{0,300}commit|"
                         r"commit[^\n]{0,300}(conflict|contradict|clash|pull(s)? against|disagree)", o["report"])
    both = re.search(r"(?i)no auto-?commit", o["trimmed"]) and re.search(r"(?i)commit (frequently|before risky)|incremental commits",
                                                                      o["trimmed"])
    return bool(conflict) and bool(both)


def a_no_additions_in_text(o):
    return not re.search(r"(?i)real check|keep working until|hold for the whole conversation|before reporting (it |a change )?done",
                         o["trimmed"])


def a_emphasis_lowered(o):
    before = len(CAPS.findall(o["original"])) / max(C.words(o["original"]), 1)
    after = len(CAPS.findall(o["trimmed"])) / max(C.words(o["trimmed"]), 1)
    return bool(o["trimmed"].strip()) and after <= 0.5 * before


def a_no_model_name(o):
    return bool(o["trimmed"].strip()) and not re.search(r"(?i)claude|haiku|opus|sonnet|anthropic|gpt|gemini", o["trimmed"])


def a_names_target(o):
    return o["model"] in o["report"]


def a_states_sizes(o):
    return bool(re.search(r"(?i)\b[\d,]{2,6}\b[^\n]{0,40}\bwords?\b[^\n]{0,80}\b[\d,]{2,6}\b|"
                          r"\bwords?\b[^\n]{0,60}\b[\d,]{2,6}\b[^\n]{0,60}\b[\d,]{2,6}\b", o["report"]))


def a_lists_changes(o):
    return bool(re.search(r"(?im)^\s*(#+\s*|\*\*)?(\d\.\s*)?(changes|each change|what (i )?changed|cuts|removed)", o["report"]))


def a_lists_kept(o):
    return bool(re.search(r"(?im)^\s*(#+\s*|\*\*)?(\d\.\s*)?(kept|what (i )?kept|keeps?)\b", o["report"]))


def a_has_flags(o):
    return bool(re.search(r"(?im)^\s*(#+\s*|\*\*)?(\d\.\s*)?(flags?|suggest|for you to decide)", o["report"]))


def a_full_text_in_reply(o):
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", o["report"], re.S)
    return any(C.words(b) >= 0.5 * C.words(o["original"]) * 0.5 for b in blocks) or bool(o["trimmed"].strip())


def a_lean_left_alone(o):
    ow, tw = C.words(o["original"]), C.words(o["trimmed"])
    return bool(tw) and (ow - tw) / ow <= 0.15


EXPENSIVE = {"a_model_claims_sourced"}

CLAIMS_SYSTEM = """You get PROFILES (reference notes about AI models, with source tags) and REPORT (a note proposing edits to someone's instructions for one target model).
List every statement in REPORT about how the target model, or models of its kind, behaves or what it needs, that PROFILES does not support.
Ignore statements about the instruction file itself, and statements REPORT marks as unverified or as an assumption.
Answer only with JSON: {"unsupported": ["short quote", ...]}. Use an empty list if there are none."""


def a_model_claims_sourced(o):
    profiles = (C.ROOT / "skills" / "trim" / "references" / "profiles.md").read_text()
    sbx = C.make_sandbox()
    try:
        sp = sbx / "system.txt"
        sp.write_text(CLAIMS_SYSTEM)
        (sbx / "cwd").mkdir()
        res = C.run_claude(f"<PROFILES>\n{profiles}\n</PROFILES>\n\n<REPORT>\n{o['report']}\n</REPORT>", "sonnet-medium",
                           sbx / "cwd", system_prompt_file=sp, tools="", budget=0.6, timeout=240)
        m = re.search(r"\{.*\}", res.get("text", ""), re.S)
        if not m or res.get("is_error"):
            return None
        o["unsupported_claims"] = json.loads(m.group(0)).get("unsupported", [])
        return len(o["unsupported_claims"]) == 0
    finally:
        shutil.rmtree(sbx, ignore_errors=True)


def a_facts_all_kept(o):
    spec = C.load_probe(o["file"])
    kept, _ = R.entries_kept(spec.get("facts", []), o["trimmed"])
    return bool(o["trimmed"].strip()) and kept == len(spec.get("facts", []))


def a_reduction_at_least_25(o):
    ow, tw = C.words(o["original"]), C.words(o["trimmed"])
    return bool(tw) and (ow - tw) / ow >= 0.25


# ---------------------------------------------------------------- units
# remove: list of (old, new) replacements applied to SKILL.md. runs: (file, prompt kind). check: assertion.
S = {
    "approve": "The author decides: change nothing until they approve, and what they ask for in the conversation outranks this skill.",
    "rationale": "How much to cut depends on the model that will read the instructions, which may not be the model running this skill. ",
    "target": "Take the model the person names. If they name none and the instructions are for the assistant you are running in, take the model ID your system prompt states and say you assumed it. Otherwise ask which model and wait, because a guessed model makes every later call unreliable.",
    "memory": " Model-specific reasons come from that file or from a maker's page you read in this conversation; your own memory of how models behave predates the current ones.",
    "noprofile": " A model with no profile gets the conservative treatment described there.",
    "strength": " Keep it at full strength, including choices you would advise against. Turning \"never explain\" into \"be concise\" changes what was asked.",
    "unsure": "- **Unsure**: keep it and flag it, with how much shorter the text gets if the author agrees to drop it.\n",
    "guards": "Two things stay exactly as written whatever the answer: rules guarding work that is fragile or cannot be undone (deleting, sending, paying, publishing, committing, production, approvals, policy or legal limits), with their conditions and exceptions, and anything a program reads, such as frontmatter. A wrong cut there costs far more than the words saved.",
    "flags": "Lines that look stale, risky or in conflict with each other get flagged, not settled; that is the author's call. So is anything new: list additions the profile recommends as suggestions outside the text.",
    "wording": " Wording can change (emphasis down to normal volume, a reason kept beside its rule), and the model's name stays out of the text, since the file may outlive the model.",
    "lean": "\nA file that is already lean should come back nearly unchanged; say so rather than cutting to show effort.\n",
}
UNITS = {
    "full": {"remove": [], "runs": None, "check": None},
    "approve": {"remove": [(S["approve"], "What the author asks for in the conversation outranks this skill.")],
                "runs": [("daveshap-default-ci", "bare"), ("cursorrules-nextjs", "bare")], "check": "a_untouched"},
    "outranks": {"remove": [(S["approve"], "The author decides: change nothing until they approve.")],
                 "runs": [("superclaude-rules", "override")], "check": "a_complied_with_user"},
    "target-assume": {"remove": [(S["rationale"], ""), (S["target"], "")],
                      "runs": [("superclaude-rules", "ask-same")], "check": "a_assumed_running_model"},
    "target-ask": {"remove": [(S["rationale"], ""), (S["target"], "")],
                   "runs": [("daveshap-default-ci", "ask-other")], "check": "a_asked_and_waited"},
    "rationale": {"remove": [(S["rationale"], "")],
                  "runs": [("daveshap-default-ci", "ask-other")], "check": "a_asked_and_waited"},
    "noprofile": {"remove": [(S["noprofile"], "")],
                  "runs": [("superclaude-rules", "unlisted")], "check": "a_says_no_profile"},
    "strength": {"remove": [(S["strength"], " Keep it.")],
                 "runs": [("daveshap-default-ci", "default")], "check": "a_preferences_full_strength"},
    "unsure": {"remove": [(S["unsure"], "")],
               "runs": [("superclaude-rules", "default")], "check": "a_flags_with_savings"},
    "guards": {"remove": [(S["guards"], "Anything a program reads, such as frontmatter, stays exactly as written.")],
               "runs": [("taubench-airline", "default"), ("superclaude-rules", "default")], "check": "a_guards_exact"},
    "frontmatter": {"remove": [(", and anything a program reads, such as frontmatter", ""), ("Two things stay", "One thing stays")],
                    "runs": [("cursorrules-nextjs", "default")], "check": "a_frontmatter_kept"},
    "flag-not-settle": {"remove": [("Lines that look stale, risky or in conflict with each other get flagged, not settled; that is the author's call. So is anything new: list",
                                    "List")],
                        "runs": [("taubench-airline", "default"), ("superclaude-rules", "default")], "check": "a_flagged_not_settled"},
    "additions-outside": {"remove": [(" So is anything new: list additions the profile recommends as suggestions outside the text.", "")],
                          "runs": [("superclaude-rules", "default")], "check": "a_no_additions_in_text"},
    "emphasis": {"remove": [(" Wording can change (emphasis down to normal volume, a reason kept beside its rule), and the model's name stays",
                             " The model's name stays")],
                 "runs": [("superclaude-rules", "default")], "check": "a_emphasis_lowered"},
    "model-name": {"remove": [(", and the model's name stays out of the text, since the file may outlive the model", "")],
                   "runs": [("daveshap-default-ci", "default")], "check": "a_no_model_name"},
    "report-target": {"remove": [("1. Target model, and whether it was named, assumed, or has no profile.\n", "")],
                      "runs": [("cursorrules-nextjs", "default")], "check": "a_names_target"},
    "report-sizes": {"remove": [("2. Words before and after. Count with a tool if you have one; otherwise say the figures are estimates.\n", "")],
                     "runs": [("cursorrules-nextjs", "default")], "check": "a_states_sizes"},
    "report-changes": {"remove": [("3. Each change, with its reason.\n", "")],
                       "runs": [("cursorrules-nextjs", "default")], "check": "a_lists_changes"},
    "report-kept": {"remove": [("4. What you kept and why.\n", "")],
                    "runs": [("cursorrules-nextjs", "default")], "check": "a_lists_kept"},
    "report-flags": {"remove": [("5. Flags and suggestions for the author.\n", "")],
                     "runs": [("superclaude-rules", "default")], "check": "a_has_flags"},
    "report-text": {"remove": [("6. The proposed text in full: in the file they asked for, otherwise in one code block ready to paste.\n", "")],
                    "runs": [("daveshap-default-ci", "bare")], "check": "a_full_text_in_reply"},
    "lean": {"remove": [(S["lean"], "")],
             "runs": [("taubench-airline", "default")], "check": "a_lean_left_alone"},
    "memory": {"remove": [(S["memory"], "")],
               "runs": [("daveshap-default-ci", "luna")], "check": "a_model_claims_sourced"},
    "unsure-facts": {"remove": [(S["unsure"], "")],
                     "runs": [("superclaude-rules", "default")], "check": "a_facts_all_kept", "variant": "unsure"},
    "cut-enough": {"remove": [], "runs": [("superclaude-rules", "default")], "check": "a_reduction_at_least_25"},
}


# one variants folder per process, so that concurrent runs cannot delete each other's copies
VARIANTS = C.SBX_ROOT / f"variants-{os.getpid()}"


def build_variant(skill_dir: Path, unit: str) -> Path:
    dst = VARIANTS / f"{unit}-{int(time.time() * 1000) % 10**9}" / skill_dir.name
    shutil.copytree(skill_dir, dst)
    md = dst / "SKILL.md"
    text = md.read_text()
    for old, new in UNITS[unit]["remove"]:
        if old not in text:
            raise ValueError(f"unit {unit}: text to remove not found: {old[:60]!r}")
        text = text.replace(old, new)
    md.write_text(text)
    return dst


def run_one(job: dict) -> dict:
    cfg = job["config"]
    model = C.CONFIGS[cfg]["model"]
    original = C.original_text(job["file"])
    sbx = C.make_sandbox()
    rec = {k: job[k] for k in ("variant", "file", "prompt_kind", "config", "k")}
    if C.limit_hit():
        shutil.rmtree(sbx, ignore_errors=True)
        return dict(rec, checks={}, is_error=True, error="usage limit", cost_usd=0.0)
    try:
        (sbx / "instructions.md").write_text(original)
        shutil.copytree(job["skill_dir"], sbx / ".claude" / "skills" / Path(job["skill_dir"]).name)
        prompt = PROMPTS[job["prompt_kind"]].format(skill=Path(job["skill_dir"]).name, model=model)
        res = C.run_claude(prompt, cfg, sbx, tools=C.AGENT_TOOLS, allowed_tools=C.AGENT_TOOLS,
                           permission_mode="acceptEdits", slash=True, budget=2.5, timeout=1200)
        tp = sbx / "trimmed.md"
        o = {"file": job["file"], "model": model, "original": original,
             "trimmed": tp.read_text() if tp.exists() else "", "report": res.get("text") or "",
             "original_modified": (sbx / "instructions.md").read_text() != original}
        checks = {}
        for name, fn in list(globals().items()):
            if name.startswith("a_") and callable(fn):
                if name in EXPENSIVE and name not in job.get("checks_wanted", ()):
                    continue
                try:
                    checks[name] = bool(fn(o))
                except Exception:
                    checks[name] = None
        rec.update({"checks": checks, "unsupported_claims": o.get("unsupported_claims"), "is_error": res.get("is_error", False),
                    "cost_usd": res.get("cost_usd", 0.0), "trimmed_words": C.words(o["trimmed"]),
                    "original_words": C.words(original), "report": o["report"][:2500]})
    except Exception as e:
        rec.update({"checks": {}, "is_error": True, "error": f"{type(e).__name__}: {e}", "cost_usd": 0.0})
    finally:
        shutil.rmtree(sbx, ignore_errors=True)
    return rec


def summary(path: Path) -> None:
    rows = [r for r in C.read_jsonl(path) if not r.get("is_error")]
    print(f"{'unit':18s} {'check':28s} {'with (haiku, opus)':20s} {'without (haiku, opus)':22s} verdict")
    for u, spec in UNITS.items():
        if u == "full":
            continue
        pairs = set(spec["runs"])

        def tally(variant):
            out = {}
            for cfg in ("haiku-high", "opus-medium"):
                rs = [r for r in rows if r["variant"] == variant and r["config"] == cfg
                      and (r["file"], r["prompt_kind"]) in pairs and r["checks"].get(spec["check"]) is not None]
                out[cfg] = (sum(1 for r in rs if r["checks"][spec["check"]]), len(rs))
            return out
        w, wo = tally("full"), (tally(spec.get("variant", u)) if spec["remove"] else {})
        cell = lambda t: ", ".join(f"{t[c][0]}/{t[c][1]}" for c in ("haiku-high", "opus-medium")) if t else "-"
        nw = sum(v[1] for v in w.values())
        nwo = sum(v[1] for v in wo.values()) if wo else 0
        if not nw or not nwo:
            verdict = "-"
        else:
            rw = sum(v[0] for v in w.values()) / nw
            rwo = sum(v[0] for v in wo.values()) / nwo
            diff = (rw - rwo) * nwo
            verdict = "changes behaviour" if diff >= 2 else ("better without" if diff <= -2 else "no measurable change")
        print(f"{u:18s} {spec['check']:28s} {cell(w):20s} {cell(wo):22s} {verdict}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill-dir", default=str(C.ROOT / "skills" / "trim"))
    ap.add_argument("--units", default="")
    ap.add_argument("--k-haiku", type=int, default=3)
    ap.add_argument("--k-opus", type=int, default=2)
    ap.add_argument("--concurrency", type=int, default=5)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args()
    out = Path(args.out)
    if args.summary:
        summary(out)
        return
    skill_dir = Path(args.skill_dir).resolve()
    done = {(r["variant"], r["file"], r["prompt_kind"], r["config"], r["k"]) for r in C.read_jsonl(out)}
    jobs, seen = [], set()
    for unit in [u for u in args.units.split(",") if u]:
        spec = UNITS[unit]
        if unit == "full":
            wanted = [u for u in args.units.split(",") if u and u != "full"] or list(UNITS)
            pairs = sorted({p for u2 in wanted for p in (UNITS[u2]["runs"] or [])})
            sdir = skill_dir
        else:
            if not spec["remove"]:
                continue
            pairs, sdir = spec["runs"], build_variant(skill_dir, unit)
        for file_id, kind in pairs:
            for cfg, k_max in (("haiku-high", args.k_haiku), ("opus-medium", args.k_opus)):
                for k in range(1, k_max + 1):
                    key = (unit, file_id, kind, cfg, k)
                    if key not in done and key not in seen:
                        seen.add(key)
                        wanted = [sp["check"] for sp in UNITS.values() if sp["runs"] and (file_id, kind) in sp["runs"]]
                        jobs.append({"variant": unit, "file": file_id, "prompt_kind": kind, "checks_wanted": wanted,
                                     "config": cfg, "k": k, "skill_dir": str(sdir)})
    print(f"{len(jobs)} runs", flush=True)
    spent = 0.0
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        for i, rec in enumerate(pool.map(run_one, jobs), 1):
            if rec.get("is_error"):
                continue  # refused or failed runs are rerun, never scored
            C.append_jsonl(out, rec)
            spent += rec.get("cost_usd", 0.0)
            if i % 10 == 0 or i == len(jobs):
                print(f"[{i}/{len(jobs)}] spent=${spent:.2f}", flush=True)
    shutil.rmtree(VARIANTS, ignore_errors=True)
    summary(out)


if __name__ == "__main__":
    main()
