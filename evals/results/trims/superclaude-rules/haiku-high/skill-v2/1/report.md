I saved the proposed version to `/root/trim-sbx/64fa1742710c/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile (tested at high effort). If you run Haiku at a different effort level, the cuts may need re-checking.

**2. Size:** I have no shell tool here, so these are estimates. Before is roughly 1,800 words; after is roughly 900, about half.

**3. Changes and reasons**
- **Removed the Quick Reference section.** It repeats rules that appear earlier, so it adds nothing for the model.
- **Removed blanket tool-push lines.** "Always use the most powerful tool" and "Efficiency first: use the fastest method" push tool use on every task. The profile says to cut blanket search and tool instructions for Haiku. I kept the specific preferences (Grep over bash grep, Glob over find).
- **Removed repeated lines.** Examples: "Evidence-based" appeared twice, "non-destructive workflow" repeated "create restore points", and "think before build" repeated the workflow section. Each now appears once.
- **Lowered emphasis.** I removed ALWAYS, MUST, and CRITICAL from ordinary rules. Guards keep "never": never work on main, never skip tests, never bypass validation.
- **Dropped the "Right" examples** that restated their rule, and some "Wrong" examples that restated theirs.
- **Merged the file-organization sections** into one, keeping every location rule.

**4. Kept as written, and why**
- The priority levels and conflict order: these tell the model how to weigh rules.
- Deletion and cleanup rules in Workspace Hygiene: deletion rules stay in substance. I merged repeats but kept the wording close.
- Git rules: the main and master guard, the `git status` and `git branch` checks, and the `git diff` review.
- The test-skipping ban, the validation-bypass ban, and the lint and typecheck step.
- Temporal rules, the banned marketing words, and the scope limits.
- Concrete commands, paths, and the grep detection line.

**5. Flags for you to decide**
- **Conflict: "No auto-commit" vs "Commit frequently."** The Safety section says no auto-commit, and the Git section says commit in small increments and before risky operations. I kept both. Pick one; the Git line is the one to change.
- **Conflict: parallelization gains vs "no fake metrics."** The Workflow section asks the plan to state gains like "60% time saving," but Professional Honesty forbids invented percentages. The example invites invented numbers. Dropping that clause saves about 20 words.
- **Possibly stale names.** These may not exist in your setup: `/sc:load`, `/sc:save`, TodoWrite, MultiEdit, and the named MCP servers. The whole Agent Orchestration section assumes a PM Agent and automatic specialist selection. If these are not real in your environment, dropping the orchestration section saves about 110 words, and dropping the MCP line saves about 40.
- **Things the model can't act on.** "Checkpoint every 30 minutes" needs a clock. "Monthly" PM Agent maintenance can't happen inside a session. "Maintain at least 90% context retention" can't be measured. Dropping the 90% line saves about 8 words.
- **Possible over-triggering.** The "use Task agents for more than 3 steps" line may make Haiku delegate more than needed. I kept it because it's a deliberate choice; consider it if you see extra sub-agent calls.

**6. Suggestions (not added to the text)**
- If this agent ever stops early on long tasks, add a line to keep working until the task is done. The profile recommends this for agents that stop early.