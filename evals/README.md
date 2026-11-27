# Evals

This folder holds everything behind the numbers in the top-level README: the instruction files, the tasks, the harness and the raw results.

## What is being measured

A trim is only worth having if the shorter file still makes the model do what the original made it do. So the main measurement is behavioural:

1. Take a real instruction file.
2. Write small tasks whose outcome depends on specific rules in it, each with a deterministic check.
3. Run each task several times with five versions of the instructions ("arms"):

| Arm | What the model is given |
|---|---|
| `none` | no instructions (control) |
| `original` | the file as published |
| `oneline` | a version produced by a one-line request with no skill |
| `builtin` | a version produced by Claude Code's bundled `/claude-api prompt-audit` |
| `skill` | a version produced by this skill |

The trimmed arms are produced by the same model, at the same effort, that then runs the tasks. Each trimmed arm has three independent trims per file and model; trial *i* of a task uses trim *i*.

## Definitions

These were fixed before any trimmed arm was run.

- **Valid check**: the original file gets it right in at least two of three trials. A check the original itself fails cannot show whether a trim kept anything.
- **Instruction-dependent check**: a valid check that fails in at least two of three trials with no instructions. These are the behaviours the file is responsible for.
- **Default check**: a valid check that also passes with no instructions. Removing the rule behind it should change nothing.
- **Kept**: an arm's pass count on instruction-dependent checks.
- **Regression**: a valid check where an arm passes at least two fewer trials (of three) than the original.

Pass counts are small. A check run three times can swing by one from run to run, so read single-check differences as noise and look at totals.

## Corpus

Eleven real files, each pinned to a commit, under `corpus/<id>/` with a `source.json` giving the repository, path, commit, licence and checksum. Four were used while the skill was being written (`dev`); seven were held out and run only after the skill text was frozen (`heldout`). The held-out probes were written by separate agent sessions that never saw the skill. Before the freeze, the only held-out results looked at were the original and no-instruction runs used to validate the probes, and the sizes of the one-line trims.

| id | split | kind | words | licence |
|---|---|---|---|---|
| cursorrules-nextjs | dev | Cursor rules file | 578 | CC0-1.0 |
| superclaude-rules | dev | Claude Code behaviour rules | 2,127 | MIT |
| taubench-airline | dev | customer-service policy prompt | 1,051 | MIT |
| daveshap-default-ci | dev | ChatGPT custom instructions | 242 | MIT |
| citypaul-claude-md | heldout | personal CLAUDE.md | 2,933 | MIT |
| openai-agents-agents-md | heldout | repository AGENTS.md | 2,103 | MIT |
| karpathy-claude-md | heldout | short principles card | 358 | MIT |
| fabric-extract-wisdom | heldout | system prompt with a strict output format | 539 | MIT |
| daveshap-slide-deck | heldout | custom instructions with a strict format | 200 | MIT |
| beast-mode | heldout | agent prompt written for GPT-4.1 | 2,657 | MIT |
| superpowers-tdd | heldout | installed skill (test-driven development) | 1,475 | MIT |

## How a task runs

`PROBES.md` describes the probe format and the check primitives. In short:

- **agent mode**: a fresh sandbox is copied from `scaffolds/<name>`, the arm's text is written to `CLAUDE.md`, the sandbox becomes a one-commit git repository, and the task runs in headless Claude Code with file tools only (plus Bash for the few command patterns a probe allows).
- **chat mode**: the arm's text is the system prompt, there are no tools, and the task is one user message.

Two things about the harness matter when reading results:

- Tasks run inside Claude Code, whose own system prompt already carries general coding guidance. "No instructions" therefore means "Claude Code defaults", not a bare model.
- Claude Code tells the model its own model ID in every session, so the case "the app does not say which model this is" cannot be produced. The skill's ask-first path is tested another way (see `harness/asktest.py`).

## Other measurements

- `harness/rubric.py`: for each trim, whether the non-derivable facts and hard rules listed in the probe file are still in the text, and (with a judge model) whether the report states sizes, gives reasons, lists what was kept and names the target. The judge is `claude-sonnet-5-5`, which is neither trimmer.
- `harness/asktest.py`: what the trimmer does when no target model is named.
- `harness/ablate.py`: the deletion test on the skill's own sentences.
- `harness/check.py`: mechanical checks on any contribution; no model calls.
- `harness/tokens.py`: token counts for every version, as reported by the API for `claude-haiku-5-5`.
- `harness/triggertest.py`: whether the skill loads when it should, with `trigger_queries.json`.

## Running it

Requirements: Python 3.10+, the `claude` CLI signed in, and no other dependencies.

```bash
python3 harness/trim.py  --arm oneline --files all --configs haiku-high,opus-medium --k 3
python3 harness/trim.py  --arm builtin --files all --configs haiku-high,opus-medium --k 1
python3 harness/trim.py  --arm skill --skill-dir ../skills/trim --files all --configs haiku-high,opus-medium --k 3
python3 harness/probe.py --files all --arms none,original,oneline,builtin,skill --configs haiku-high,opus-medium --trials 3
python3 harness/rubric.py --arms oneline,builtin,skill --files all --judge
python3 harness/report.py summary --files all --configs haiku-high,opus-medium --arms original,oneline,builtin,skill
```

Runs are resumable: finished runs are skipped. Sandboxes are created under `~/trim-sbx` because Claude Code does not load `CLAUDE.md` from its own temp directory.

## Running on other providers

Only Claude models have been run. To add another provider:

1. Add an entry to `CONFIGS` in `harness/common.py`, for example `"astra-medium": {"provider": "openai", "model": "gpt-6.2-astra", "effort": "medium"}`.
2. Replace the placeholder for that provider in `PROVIDERS` with a function that takes the same arguments as `run_claude` and returns the same record: `text`, `tool_calls`, `cost_usd`, `usage`, `num_turns`, `duration_ms`, `is_error`.
3. For agent-mode files the adapter must run an agent that reads the instruction file from the sandbox the way that product does (`AGENTS.md` for Codex, `GEMINI.md` for Gemini CLI) and exposes file tools. Chat-mode files need only a system prompt and one user message.

Until that is done the profiles for those models stay "from documentation, untested".

## Results

Raw records are in `results/`: `probe_runs.jsonl` (one line per task run), `trims/` (every trimmed file with its report and metadata), `rubric.jsonl`, `asktest.jsonl` and `ablation.jsonl`. `probe_runs.jsonl` is stored gzipped; the harness reads it as it is, and `gunzip` it before adding runs. The per-model tables in `RESULTS.md` are generated from these files by `harness/report.py full`; the summary above them is written by hand from those tables.
