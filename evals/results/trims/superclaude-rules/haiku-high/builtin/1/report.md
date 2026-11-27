The audit is done and the edits are applied to a copy. `instructions.md` is unchanged.

**Scope and target:** `instructions.md` is the only prompt-surface file in the working directory. It is a coding-agent configuration file, so I audited it against `claude-haiku-5-5` (named in the request). There is no git history, so the provenance step (Step 2) was skipped. No non-Anthropic provider markers. Groups 3 and 4 do not apply: there are no tool definitions and no request-building code.

**Highest-impact findings**

1. **Planning scaffold plus a contradiction.** The "Planning Efficiency" section asks for expected parallelization gains with examples like "60% time saving" (`instructions.md:70`). Line 151 says "Never invent … percentages … without evidence." Haiku 5.5 plans with adaptive thinking on by default, so the scaffold mostly adds over-planning. I removed the section and the plan-first lines.
2. **Commit conflict (flagged, not edited).** Lines 167 and 169 say to commit frequently and to commit before risky operations. Lines 243 and 274 say "no auto-commit." Both are in the same file, and with no git history I can't tell which is current. You need to decide which one holds.
3. **Git rules assume a repository that isn't here.** Lines 165–176 and 270–272 require `git status` and feature branches every session. This directory is not a git repo. This is proposed only, not applied, per the audit rules for volatile specifics.

**Counts by group**
- Group 1 (dated prompt text): 14 findings. 10 are in the diff, 4 are flagged.
- Group 2 (instruction-file cruft): 7 findings. 1 is in the diff, 1 is proposed only, 5 are flagged.
- Group 3 (tool descriptions): not applicable.
- Group 4 (request config): not applicable.

**Applied to `trimmed.md`** (`/root/trim-sbx/7cdec8c8eecc/trimmed.md`, one hunk per finding)

| # | Location (in instructions.md) | Pattern | Change | Confidence |
|---|---|---|---|---|
| 1 | Lines 63–73 | 1b, plan-before-acting | Remove the "Planning Efficiency" section | High |
| 2 | Line 49 | 1b | Drop the "Plan" step from the task pattern | High |
| 3 | Lines 60–61 | 1b | Remove the plan-first ✅/❌ pair | High |
| 4 | Line 53 | 1d, unenforced fake metric | Remove "Maintain ≥90% understanding" | Medium |
| 5 | Line 50 | 1a, caps | "ALWAYS … ONLY" → plain sentence with the same rule | Medium |
| 6 | Line 78 | 1a, caps | "you MUST complete" → "complete it to a working state" | Medium |
| 7 | Line 92 | 1a, caps | "Build ONLY" → "Build only" | Medium |
| 8 | Line 181 | 1a, caps | "Always use the most powerful tool" → "Prefer the most capable tool" | Medium |
| 9 | Line 150 | 1e, banned-phrase list | Rewrite as a positive style rule; the examples stay | Medium |
| 10 | Line 184 | 1b, thinking scaffold via tool | Drop the "sequential-thinking" example | Medium |
| 11 | Line 224 | Group 2, dated fact | Remove "January 2025"; use the environment's date | Medium |

**Proposed only, not applied** (Group 2 volatile row)
- Lines 165–176 and 270–272: make git checks conditional, e.g. "If the project is a git repository, check `git status` and the current branch before changing files." This needs your decision.

**Flagged, not edited**
- **Commit conflict:** lines 167/169 against 243/274 (see above).
- **External commands and agents:** `/sc:load`, `/sc:save`, the 30-minute checkpoint trigger (lines 56–58), the PM Agent layer (lines 27–44), `@agent-security`, and the MCP and skill names on lines 184, 249 and 265–266. These belong to an installed framework I can't verify from this repo. The 30-minute checkpoint has no clock behind it.
- **"No Mock Objects" (line 80):** this rule reads as a ban on test doubles, which is probably not what you mean. Low confidence.
- **"Stop over-praising" (line 155):** low confidence.
- **"Discovery First" (line 55):** it is strategy coaching. Low confidence.
- **Tier markers:** six sections are marked 🔴 CRITICAL. Low confidence; the tiers work as a conflict-resolution frame.
- **Example date (line 229):** "Today is 2025-08-15" is an illustrative example. Low confidence.

**Not verified:** Step 7 was not run. There is no eval suite here, and a before/after probe would need paid Haiku calls. If you want the planning removal and the caps rewrites checked, I can run a small probe within the $4 budget.