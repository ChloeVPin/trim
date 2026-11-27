I wrote the proposed version to `/root/trim-sbx/af2ebe0e6159/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named in your request. Its profile is tested at high effort. Haiku needs more explicit direction than the larger models, so I cut procedures and examples lightly.

**2. Length:** about 4,000 words before and about 3,200 after. These are estimates. Bash is disabled in this session, so I had no word-count tool.

**3. Changes**

- **Removed the "About this file" header.** It describes the file's architecture and history, which doesn't change what the model does. The skill list in it duplicates the routing lines.
- **Removed duplicates.** Key Principles, Preferred Tools, Code Style, and Testing repeated lines that appear in their detailed sections. I kept the detailed copy each time.
- **Merged the `grill-me` routes** (two lines) and the `find-gaps` routes (two lines). Each pair named the same skill for overlapping triggers.
- **Merged the refactor-after-green rule** into the `REFACTOR OR REDUCE` step, keeping its "only if it adds value" condition.
- **Removed generic advice.** Early returns, the array-methods line, and "think deeply" were generic or pushed thoroughness. "Think deeply" is the thoroughness line the profile says over-triggers.
- **Removed the Resources links and the Summary.** Neither changes behavior. The Summary repeated the TDD rule and the "simplest thing" rule. Add the links back if humans read this file too.
- **Plain wording for emphasis.** I lowercased "ALWAYS", "ONLY", and "MINIMUM" and kept their rules. I kept "non-negotiable" for TDD.
- **Shortened the browser-automation line.** I kept the fallback order.

**4. Kept and why**

- All TDD, mutation-gate, commit-approval, artifact-boundary, and plan-only rules, with their conditions. The commit-approval rule is guarded work.
- Every skill trigger, because the model can't know the skill names.
- The `xstate` ownership rule and its examples. It is a decision you made, and the examples help the model recognise the cases.
- The `evaluate-existing-solutions` "search tax" guard. The profile says Haiku over-searches without it.
- The `agent-browser` workflow steps, because they are a procedure.

**Unsure, kept and flagged** (about 120 words if you agree to drop them)

- Skill-internal detail in the routing lines for `writing-for-agents`, `double-check`, `graph-engineering`, `panel-review`, and the parenthetical in `technical-writing`. These describe what the skills do, so they may already be in the skill files. Only the `trim` skill is installed in this repo, so I couldn't check.
- The curl-installer clause in the project-hooks paragraph.

**Suggested additions** (not applied, since they are your call)

- The profile says Haiku coding agents need an instruction to run a real check before reporting a change done. For example: "Before reporting a code change done, run the repository's tests or build and report the result." The file doesn't have this line.
- If the agent stops early on long tasks, add: "Keep working until the task is done."