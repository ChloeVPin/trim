I've written `trimmed.md`. Here is the audit report; `instructions.md` is unchanged.

# Prompt audit: `instructions.md` → `trimmed.md`

**Assumptions**
- **Scope:** only `instructions.md`, the one file in the working directory. There is no git history, so I couldn't check when or why any line was added.
- **Target model:** `claude-opus-5-5`, as you named it. This file is a Claude Code configuration file, so I judged it against the model reading it, not against API request code.
- **Not checked:** the agents, MCP servers and `/sc:*` commands the file names aren't in this directory. They probably come from an installed framework, so I treated them as outside the repo rather than as broken references.

**Summary**
1. **Too much planning and "use a tool to think" text.** The planning rules (the "Planning Efficiency" section, plan scripts, "plan before you build") and the advice to use sequential-thinking or a Task agent for analysis were written for older models. On Opus 5.5, thinking is always on and it plans unprompted, so these lines push it to over-plan. The Planning Efficiency section also asks for made-up numbers like "60% time saving", which the file's own "No Fake Metrics" rule forbids.
2. **Volume markers on everything.** About a third of the sections were tagged 🔴 CRITICAL, including date-checking and planning. When that many things are critical, the tag stops meaning anything.
3. **The same rule said over and over.** Workspace Hygiene repeated "clean up temp files" in seven bullets. One bullet also said to delete *any* unused files, which could remove other people's work. I narrowed it to files the agent created.

**Findings by group:** Group 1 (dated prompt text): 10 · Group 2 (stale config): 2, both flags · Group 3 (tool descriptions): not applicable · Group 4 (request code): not applicable (no request code here).

## Findings (applied to `trimmed.md`)

| # | Location | Evidence | Pattern | Why it no longer fits | Conf. | Action |
|---|---|---|---|---|---|---|
| 1 | `:63-73` | "Planning Efficiency" section, "3 parallel ops = 60% time saving" | 1b plan-before-acting / 1c | Opus 5.5 plans unprompted, and this causes over-planning. It also asks for invented metrics, against `:151` | Medium | remove section |
| 2 | `:49`, `:60-61`, `:97`, `:215` | "Understand → Plan → TodoWrite → Execute…", "Jump directly… without planning", "Think Before Build", "Plan → Execute → Verify" | 1b / 1c choreography | Step-by-step scripts for judgment work make the model over-plan | Medium | remove (kept the TodoWrite threshold as its own line) |
| 3 | `:184`, `:260` | "sequential-thinking for analysis", "Complex analysis → Task agent > native reasoning" | 1b think-tool scaffold | Opus 5.5 always thinks, and `effort` controls how deeply | High | remove |
| 4 | `:5-9`, per-section `**Priority**` tags | 🔴/🟡/🟢 legend; 🔴 on Planning, Orchestration, Temporal | 1a pressure language | Too many critical tags and the tags carry no signal. The Conflict Resolution Hierarchy already ranks the rules | Medium | remove legend and tags; kept `Triggers` and the end recap (keep-list 10) |
| 5 | `:50`, `:182`, `:187` | "ALWAYS parallel…", "Parallel Everything… never sequentially", "Efficiency First" | 1a / 1c duplication | Said three times, and "never sequentially" contradicts "sequential ONLY for dependencies" | Medium | rewrite as one line: parallel when independent, in order when dependent |
| 6 | `:53` | "Maintain ≥90% understanding" | 1c padding | Nothing can measure it, so it means nothing | Medium | remove |
| 7 | `:78-83` | "you MUST complete…", "no exceptions", six overlapping bullets | 1a / 1c | Shouting plus repetition. The real rule is "no stubs" | Medium | rewrite as one sentence, plus "say so if it can't be finished" |
| 8 | `:106-112` | Code Organization bullets ("Elegant Organization", "Descriptive Names"…) | Group 2 verbose / 1c generic virtues | Mostly things the model already knows | Medium | rewrite as two sentences, keeping the author-specific preferences |
| 9 | `:120-126` | Seven cleanup bullets, including "Delete unused directories and files" | 1c repetition | Repeated, and the last bullet could delete files the agent didn't create | Medium | rewrite to cover files the agent created only |
| 10 | `:137`, `:140-141` | "Debug Systematically", "Quality Integrity", "Methodical Problem-Solving" | 1c padding | These repeat the root-cause and never-skip rules beside them | Medium | remove |
| 11 | `:150-157` | Banned words ("excellent", "magnificent"), "Stop over-praising", repeated evidence rule | 1e style prohibitions / 1c | A list of banned words with no stated reason. Rewritten as a positive statement of the goal | Medium | rewrite as one paragraph; push-back and realistic labels kept |
| 12 | `:181`, `:183`, `:186`, `:188` | "most powerful tool (MCP > Native > Basic)", "Task agents for >3 steps", "Grep over bash grep" | 1a / 1d tool steering | General tool-steering lines and a number-of-steps delegation rule. Claude Code's own instructions already cover choosing tools | Medium | remove; merged the MCP examples into one line |
| 13 | `:220-231` | "Never Assume… January 2025", "Today is 2025-08-15", "Always state the source" | 1d fossil / pinned dates | Written for an older model's training cutoff. It also made the model narrate "Checking env…" in replies | Medium | rewrite as one sentence |

## Flagged, not applied

| Location | Issue | Why it's a flag only |
|---|---|---|
| `:167`, `:169` vs `:243`, `:274` | "Commit frequently / commit before risky operations" contradicts "No auto-commit" | Fixing it would loosen a safety rule one way or the other. You decide which rule wins |
| `:17-44` | Describes automatic agent selection and a "monthly" PM Agent that nothing in this repo runs | The framework may supply these. If it doesn't, these rules aren't enforced by anything and can be deleted |
| `:185`, `:190`, `:259` | Refers to the `MultiEdit` tool | It belongs to an installed tool, so I can't check it from this repo. Confirm your Claude Code version still has it |
| `:264` | "Playwright MCP > unit tests" | Reads as preferring browser tests over unit tests, which is probably not what was meant |
| `:56-58` | `/sc:load`, `/sc:save`, and a 30-minute checkpoint routine | Commands from an installed tool. Kept as written |

**Deliberately kept:** the conflict hierarchy, Scope Discipline, never skipping tests or validation, feature-branch and `git diff` rules, File Organization, and the end-of-file recap (one recap at the end is fine). These are real constraints or context only you know.

These changes are hypotheses, not tested results. Try `trimmed.md` on a few typical tasks before replacing the original. If a removed rule turns out to matter, add it back as one short line.