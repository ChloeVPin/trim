#!/usr/bin/env python3
"""Summarise probe runs.

Definitions (fixed before any trimmed arm was run):

  valid check           the original file gets it right in at least 2 of 3 trials
  instruction-dependent a valid check that fails in at least 2 of 3 trials with no instructions
  default               a valid check that passes in at least 2 of 3 trials with no instructions
  retention             pass rate of an arm on valid, instruction-dependent checks
  regression            a valid check where an arm passes at least 2 fewer trials than the original

Usage:
  report.py matrix  [--configs haiku-high] [--files dev]       per-check pass counts
  report.py summary [--configs ...] [--arms ...]               per-file and overall tables (markdown)
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

RUNS = C.RESULTS / "probe_runs.jsonl"


def load(paths=None):
    """-> counts[config][file][check][arm] = [passes, trials], costs[config][file][arm] = [usd...]"""
    counts = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [0, 0]))))
    costs = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    toks = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    seen = {}
    for path in (paths or [RUNS]):
        for r in C.read_jsonl(Path(path)):
            seen[(r["file"], r["task"], r["arm"], r["config"], r["trial"])] = r  # last record wins
    current = {}
    for r in seen.values():
        if r.get("is_error"):
            continue
        if r["file"] not in current:  # only checks that still exist in the probe file count
            try:
                current[r["file"]] = {c["id"] for t in C.load_probe(r["file"])["tasks"] for c in t["checks"]}
            except FileNotFoundError:
                current[r["file"]] = set()
        for chk, ok in r["checks"].items():
            if chk not in current[r["file"]]:
                continue
            cell = counts[r["config"]][r["file"]][chk][r["arm"]]
            cell[0] += 1 if ok else 0
            cell[1] += 1
        costs[r["config"]][r["file"]][r["arm"]].append(r.get("cost_usd", 0.0))
        u = r.get("usage", {})
        toks[r["config"]][r["file"]][r["arm"]].append(
            (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0),
             u.get("output_tokens", 0)))
    return counts, costs, toks


def check_meta(file_id: str) -> dict:
    spec = C.load_probe(file_id)
    return {c["id"]: {"kind": c.get("kind", "?"), "task": t["id"], "rule": c.get("rule", "")}
            for t in spec["tasks"] for c in t["checks"]}


def classify(cell: dict) -> str:
    """valid/dependence class of one check from its none and original cells."""
    o, n = cell.get("original"), cell.get("none")
    if not o or o[1] == 0:
        return "unknown"
    if o[0] * 3 < o[1] * 2:           # original passes fewer than 2/3
        return "invalid"
    if not n or n[1] == 0:
        return "valid"
    if n[0] * 3 <= n[1]:              # none passes at most 1/3
        return "dependent"
    if n[0] * 3 >= n[1] * 2:
        return "default"
    return "mixed"


def cmd_matrix(args):
    counts, _, _ = load(args.runs.split(",") if args.runs else None)
    files = C.corpus_ids(args.files) if args.files in ("dev", "heldout", "all") else args.files.split(",")
    for config in args.configs.split(","):
        print(f"\n## {config}")
        for f in files:
            if f not in counts[config]:
                continue
            meta = check_meta(f)
            arms = sorted({a for chk in counts[config][f].values() for a in chk},
                          key=lambda a: (a not in ("none", "original"), a))
            print(f"\n{f}")
            print(f"  {'check':34s} {'kind':11s} {'class':10s} " + " ".join(f"{a:>9s}" for a in arms))
            for chk, m in meta.items():
                cell = counts[config][f].get(chk, {})
                row = " ".join(f"{(str(cell[a][0])+'/'+str(cell[a][1])) if a in cell else '-':>9s}" for a in arms)
                print(f"  {chk:34s} {m['kind']:11s} {classify(cell):10s} {row}")


def cmd_summary(args):
    counts, costs, toks = load(args.runs.split(",") if args.runs else None)
    files = C.corpus_ids(args.files) if args.files in ("dev", "heldout", "all") else args.files.split(",")
    arms = args.arms.split(",")
    out = []
    for config in args.configs.split(","):
        out.append(f"\n### {config}\n")
        out.append("| File | Split | Dependent checks | " + " | ".join(f"{a} kept" for a in arms) + " | Regressions |")
        out.append("|---|---|---|" + "---|" * len(arms) + "---|")
        tot = {a: [0, 0] for a in arms}
        for f in files:
            if f not in counts[config]:
                continue
            split = C.source_meta(f)["split"]
            dep = [chk for chk, cell in counts[config][f].items() if classify(cell) == "dependent"]
            cells, regs = [], []
            for a in arms:
                p = sum(counts[config][f][c][a][0] for c in dep if a in counts[config][f][c])
                n = sum(counts[config][f][c][a][1] for c in dep if a in counts[config][f][c])
                tot[a][0] += p
                tot[a][1] += n
                cells.append(f"{p}/{n}" if n else "-")
            for chk, cell in counts[config][f].items():
                if classify(cell) in ("invalid", "unknown"):
                    continue
                o = cell["original"]
                for a in arms:
                    if a in ("none", "original") or a not in cell or cell[a][1] == 0:
                        continue
                    if o[0] / o[1] * 3 - cell[a][0] / cell[a][1] * 3 >= 2:
                        regs.append(f"{a}: {chk}")
            out.append(f"| {f} | {split} | {len(dep)} | " + " | ".join(cells) + f" | {'; '.join(regs) or 'none'} |")
        out.append("| **All** | | | " + " | ".join(f"**{p}/{n}**" if n else "-" for p, n in tot.values()) + " | |")
    print("\n".join(out))


def cmd_full(args):
    """Write the full results document (markdown) to stdout."""
    import statistics as st
    runs = args.runs.split(",") if args.runs else None
    counts, costs, toks = load(runs)
    arms = args.arms.split(",")
    label = dict(zip(arms, (args.labels.split(",") if args.labels else arms)))
    files_all = C.corpus_ids("all")
    rub = [r for r in C.read_jsonl(C.RESULTS / "rubric.jsonl") if "judge" in r]
    tok = {(r["file"], r["config"], r["arm"], r["k"]): r for r in C.read_jsonl(C.RESULTS / "tokens.jsonl")}
    out = []
    w = out.append

    def trims(f, config, arm):
        rows = []
        for k in range(1, 10):
            m = C.trim_dir(f, config, arm, k) / "meta.json"
            if m.exists():
                rows.append(json.loads(m.read_text()))
        return rows

    def rate(cell, a):
        return cell[a][0] / cell[a][1] if a in cell and cell[a][1] else None

    for config in args.configs.split(","):
        cfg = C.CONFIGS[config]
        w(f"\n## {cfg['model']} at {cfg['effort']} effort\n")

        # ---- size
        w("### Size\n")
        w("Words in the file, as a mean over the trims of each arm, with the cut against the original.\n")
        w("| File | Split | Original | " + " | ".join(label[a] for a in arms if a != "original") + " |")
        w("|---|---|---|" + "---|" * (len(arms) - 1))
        tot = {a: [0, 0] for a in arms}
        for f in files_all:
            meta = C.source_meta(f)
            ow = meta["words"]
            cells = []
            for a in arms:
                if a == "original":
                    continue
                ts = [t for t in trims(f, config, a) if t.get("produced")]
                if not ts:
                    cells.append("-")
                    continue
                mw = st.mean(t["trimmed_words"] for t in ts)
                tot[a][0] += mw
                tot[a][1] += ow
                cells.append(f"{mw:,.0f} ({100 * (mw - ow) / ow:+.0f}%)")
            w(f"| {f} | {meta['split']} | {ow:,} | " + " | ".join(cells) + " |")
        w("| **All files** | | | " + " | ".join(
            (f"**{100 * (tot[a][0] - tot[a][1]) / tot[a][1]:+.0f}%**" if tot[a][1] else "-") for a in arms if a != "original") + " |")

        # ---- tokens
        if any(k[1] == config for k in tok):
            w("\nThe same in tokens, measured on this model:\n")
            w("| File | Original | " + " | ".join(label[a] for a in arms if a != "original") + " |")
            w("|---|---|" + "---|" * (len(arms) - 1))
            for f in files_all:
                o = tok.get((f, config, "original", 1))
                if not o:
                    continue
                cells = []
                for a in arms:
                    if a == "original":
                        continue
                    vals = [v["tokens"] for (ff, cc, aa, kk), v in tok.items() if ff == f and cc == config and aa == a]
                    cells.append(f"{st.mean(vals):,.0f} ({100 * (st.mean(vals) - o['tokens']) / o['tokens']:+.0f}%)" if vals else "-")
                w(f"| {f} | {o['tokens']:,} | " + " | ".join(cells) + " |")

        # ---- behaviour
        w("\n### Behaviour\n")
        w("Passes on instruction-dependent checks (the behaviours the original file is responsible for).\n")
        barms = ["none"] + arms
        label.setdefault("none", "No instructions")
        w("| File | Split | Checks | " + " | ".join(label[a] for a in barms) + " |")
        w("|---|---|---|" + "---|" * len(barms))
        totals = {sp: {a: [0, 0] for a in barms} for sp in ("dev", "heldout")}
        dflt = {a: [0, 0] for a in barms}
        worse, better = [], []
        for f in files_all:
            if f not in counts[config]:
                continue
            split = C.source_meta(f)["split"]
            meta = check_meta(f)
            dep = [c for c, cell in counts[config][f].items() if classify(cell) == "dependent"]
            cells = []
            for a in barms:
                p = sum(counts[config][f][c][a][0] for c in dep if a in counts[config][f][c])
                n = sum(counts[config][f][c][a][1] for c in dep if a in counts[config][f][c])
                totals[split][a][0] += p
                totals[split][a][1] += n
                cells.append(f"{p}/{n}" if n else "-")
                for c, cell in counts[config][f].items():
                    if classify(cell) == "default" and a in cell:
                        dflt[a][0] += cell[a][0]
                        dflt[a][1] += cell[a][1]
            w(f"| {f} | {split} | {len(dep)} | " + " | ".join(cells) + " |")
            for c, cell in counts[config][f].items():
                if classify(cell) in ("invalid", "unknown"):
                    continue
                ro = rate(cell, "original")
                for a in arms:
                    ra = rate(cell, a)
                    if a == "original" or ra is None:
                        continue
                    if ro - ra >= 2 / 3 - 1e-9:
                        worse.append((a, f, c, meta.get(c, {}).get("kind", "?"), cell["original"], cell[a]))
                    if ra - ro >= 2 / 3 - 1e-9:
                        better.append((a, f, c, meta.get(c, {}).get("kind", "?"), cell["original"], cell[a]))
        for sp, name in (("dev", "Dev files"), ("heldout", "Held-out files")):
            w(f"| **{name}** | | | " + " | ".join(
                (f"**{totals[sp][a][0]}/{totals[sp][a][1]}**" if totals[sp][a][1] else "-") for a in barms) + " |")
        w("| **All** | | | " + " | ".join(
            f"**{totals['dev'][a][0] + totals['heldout'][a][0]}/{totals['dev'][a][1] + totals['heldout'][a][1]}**" for a in barms) + " |")
        w("\nChecks the model passes even with no instructions (so the rule behind them changes nothing): "
          + ", ".join(f"{label[a]} {dflt[a][0]}/{dflt[a][1]}" for a in arms if dflt[a][1]) + ".")

        w("\nChecks where an arm passed at least two-thirds less often than the original:\n")
        if worse:
            w("| Arm | File | Check | Kind | Original | Arm |")
            w("|---|---|---|---|---|---|")
            for a, f, c, kind, o, x in sorted(worse):
                w(f"| {label[a]} | {f} | {c} | {kind} | {o[0]}/{o[1]} | {x[0]}/{x[1]} |")
        else:
            w("None.")
        if better:
            w("\nChecks where an arm passed at least two-thirds more often than the original:\n")
            w("| Arm | File | Check | Kind | Original | Arm |")
            w("|---|---|---|---|---|---|")
            for a, f, c, kind, o, x in sorted(better):
                w(f"| {label[a]} | {f} | {c} | {kind} | {o[0]}/{o[1]} | {x[0]}/{x[1]} |")

        # ---- invalid checks
        inv = [(f, c) for f in files_all for c, cell in counts[config].get(f, {}).items() if classify(cell) == "invalid"]
        if inv:
            w("\nChecks left out because the original file itself fails them on this model: "
              + ", ".join(f"`{f}/{c}`" for f, c in inv) + ".")

        # ---- cost per task
        w("\n### Cost of running the tasks\n")
        w("Mean cost in US dollars of one task run with each version loaded.\n")
        w("| File | " + " | ".join(label[a] for a in arms) + " |")
        w("|---|" + "---|" * len(arms))
        nfiles = sum(1 for f in files_all if costs[config][f].get("original"))
        sums = {a: [] for a in arms}
        for f in files_all:
            cells = []
            for a in arms:
                v = costs[config][f].get(a)
                if v:
                    sums[a].append(st.mean(v))
                cells.append(f"{st.mean(v):.4f}" if v else "-")
            w(f"| {f} | " + " | ".join(cells) + " |")
        w("| **Mean of files** | " + " | ".join(
            (f"**{st.mean(sums[a]):.4f}**" if len(sums[a]) == nfiles else "-") for a in arms) + " |")

        # ---- the trims themselves
        w("\n### The trims themselves\n")
        w("| | " + " | ".join(label[a] for a in arms if a != "original") + " |")
        w("|---|" + "---|" * (len(arms) - 1))
        rows = {a: [r for r in rub if r["config"] == config and r["arm"] == a] for a in arms if a != "original"}

        def frac(a, fn):
            rs = rows[a]
            return f"{sum(1 for r in rs if fn(r))}/{len(rs)}" if rs else "-"

        def ratio(a, num, den):
            rs = rows[a]
            return f"{sum(r[num] for r in rs)}/{sum(r[den] for r in rs)}" if rs else "-"
        line = lambda name, fn: w(f"| {name} | " + " | ".join(fn(a) for a in rows) + " |")
        line("Trims scored", lambda a: str(len(rows[a])))
        line("Non-derivable facts still present", lambda a: ratio(a, "facts_kept", "facts_total"))
        line("Hard rules still present", lambda a: ratio(a, "protected_kept", "protected_total"))
        line("Original file left untouched", lambda a: frac(a, lambda r: r["original_untouched"]))
        line("Report states size before and after", lambda a: frac(a, lambda r: r["judge"].get("states_size")))
        line("Report gives a reason for every change", lambda a: frac(a, lambda r: r["judge"].get("change_reasons") in ("all", "most")))
        line("Report lists what was kept and why", lambda a: frac(a, lambda r: r["judge"].get("lists_kept")))
        line("Report names the target model", lambda a: frac(a, lambda r: r["judge"].get("names_target_model")))
        line("Removed instructions the report never mentions, per trim",
             lambda a: (f"{st.mean(len(r['judge'].get('silent_removals', [])) for r in rows[a]):.1f}" if rows[a] else "-"))
        line("Cost of producing one trim (USD)", lambda a: (f"{st.mean(r['trim_cost_usd'] for r in rows[a]):.3f}" if rows[a] else "-"))
        line("Time to produce one trim (seconds)", lambda a: (f"{st.mean(r['trim_seconds'] for r in rows[a]):.0f}" if rows[a] else "-"))
    print("\n".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["matrix", "summary", "full"])
    ap.add_argument("--configs", default="haiku-high")
    ap.add_argument("--files", default="dev")
    ap.add_argument("--arms", default="original,oneline,skill")
    ap.add_argument("--labels", default="", help="display names for --arms, comma-separated")
    ap.add_argument("--runs", default="", help="comma-separated run files (default: results/probe_runs.jsonl)")
    args = ap.parse_args()
    {"matrix": cmd_matrix, "summary": cmd_summary, "full": cmd_full}[args.cmd](args)


if __name__ == "__main__":
    main()
