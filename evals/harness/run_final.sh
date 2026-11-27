#!/usr/bin/env bash
# Final evaluation of the frozen skill. Cheapest work first, so that a usage
# limit cuts off the most expensive runs and not the whole table.
# Every step is resumable: rerun this script to pick up where it stopped.
set -u
cd "$(dirname "$0")/.."
SKILL=../skills/trim
LOG=results/logs
mkdir -p "$LOG"
NONFABRIC_HELDOUT="citypaul-claude-md,openai-agents-agents-md,karpathy-claude-md,daveshap-slide-deck,beast-mode,superpowers-tdd"

step() { echo "=== $(date -u +%H:%M:%S) $*"; }
stop_if_limited() { if [ -f results/.limit_hit ]; then echo "usage limit reached at $(cat results/.limit_hit); stopping"; exit 3; fi; }

step "trims: skill, Haiku, all files";            python3 harness/trim.py --arm skill --skill-dir "$SKILL" --files all --configs haiku-high --k 3 --concurrency 4 > "$LOG/final_trim_skill_haiku.log" 2>&1; stop_if_limited
step "probes: Haiku, dev, skill";                 python3 harness/probe.py --files dev --arms skill --configs haiku-high --trials 3 --concurrency 6 > "$LOG/final_probe_haiku_dev.log" 2>&1; stop_if_limited
step "probes: Haiku, held-out, all trimmed arms"; python3 harness/probe.py --files heldout --arms oneline,builtin,skill --configs haiku-high --trials 3 --concurrency 8 --timeout 900 > "$LOG/final_probe_haiku_heldout.log" 2>&1; stop_if_limited
step "trims: skill, Opus, all files";             python3 harness/trim.py --arm skill --skill-dir "$SKILL" --files all --configs opus-medium --k 3 --concurrency 4 > "$LOG/final_trim_skill_opus.log" 2>&1; stop_if_limited
step "probes: Opus, dev, skill";                  python3 harness/probe.py --files dev --arms skill --configs opus-medium --trials 3 --concurrency 6 --max-total-usd 15 > "$LOG/final_probe_opus_dev.log" 2>&1; stop_if_limited
step "probes: Opus, held-out except fabric";      python3 harness/probe.py --files "$NONFABRIC_HELDOUT" --arms oneline,skill --configs opus-medium --trials 3 --concurrency 6 --max-total-usd 30 > "$LOG/final_probe_opus_heldout.log" 2>&1; stop_if_limited
step "probes: Opus, fabric (2 trials)";           python3 harness/probe.py --files fabric-extract-wisdom --arms oneline,skill --configs opus-medium --trials 2 --concurrency 6 --budget 3 --timeout 900 --max-total-usd 15 > "$LOG/final_probe_opus_fabric.log" 2>&1; stop_if_limited
step "judge the reports";                         python3 harness/rubric.py --arms oneline,builtin,skill --files all --configs haiku-high,opus-medium --judge --concurrency 4 > "$LOG/final_rubric.log" 2>&1; stop_if_limited
step "token counts (Haiku tokenizer)";            python3 harness/tokens.py --files all --arms original,oneline,builtin,skill --configs haiku-high > "$LOG/final_tokens.log" 2>&1; stop_if_limited
step "done"
