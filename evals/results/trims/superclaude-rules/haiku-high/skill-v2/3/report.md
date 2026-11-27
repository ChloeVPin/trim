Proposed version saved to `/root/trim-sbx/31723ed3c64a/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. Haiku needs more explicit direction than the larger models, so I cut only duplicates, generic virtues, and emphasis, and kept every procedure.

**2. Size:** about 2,700 words before, about 1,900 after. These are estimates, since I have no word-count tool in this session.

**3. Changes**
- **Quick Reference and Decision Trees removed.** They repeated the rules above them. Their unique rules moved to their sections: read before write/edit and absolute paths/no auto-commit to Safety Rules, "run tests before starting" to Workflow, "brainstorm mode" to Scope, Magic MCP to Tool Optimization.
- **Duplicates merged:** parallel-execution lines (Workflow, Tool Optimization, Planning Efficiency), the two marketing-language lines, the two evidence-based lines, the file-placement rules.
- **Generic virtues cut:** "descriptive names", "elegant organization", "hierarchical logic", "single responsibility", "simple solutions", "quality integrity", "YAGNI" acronym, the "Start it = Finish it" slogan, the intro sentence.
- **Restated rules cut:** the Orchestration Flow and its Right/Wrong examples, the Planning Efficiency section (folded into Workflow), "Think Before Build".
- **Capitals lowered** (ALWAYS, NEVER, MUST) to plain wording, as Anthropic's guidance for Claude 5 models recommends. "Never" and "must not" in the guarded rules keep their force.

**4. Kept as written**
- **Git Workflow** and **Workspace Hygiene**, verbatim. Both guard committing and deleting, which I treat as hard-to-reverse. Both have near-duplicate lines you may want to merge. That is your call.
- **Safety Rules** and the "never skip tests" rules, with their conditions.
- Every ✅/❌ example that pins a format or placement.
- Lines I could not judge, flagged below.

**5. Flags for you to decide**
- **Conflict:** "Plans should state expected parallelization gains (e.g., '3 parallel ops = 60% time saving')" contradicts "No invented ... percentages". The example also invites invented numbers.
- **Conflict:** "No auto-commit" (Safety) against "Incremental Commits" and "Create Restore Points: commit before risky operations". Haiku has to guess which wins.
- **Possibly missing tools or commands:** `/sc:load`, `/sc:save`, the PM Agent, TodoWrite, MultiEdit, brainstorm mode, and the MCP servers (morphllm, sequential-thinking, Magic, Context7, Playwright). In this session I have Read, Write, Edit, Glob and Grep only. If those names don't exist where Haiku runs, it will try to call them.
- **Can't be followed:** "30-minute intervals", "monthly" maintenance, and "≥90% understanding". The model has no clock or way to measure this. Dropping them saves about 50 words.
- **Stale dates:** the examples use January 2025 and 2025-08-15. Replacing them would change wording, so I left them.
- **Tension:** "Start it = finish it" and "MVP first" pull in different directions. Also, "No mock objects" may be meant for production code only, or it may ban test mocks too. Clarify which.
- **Blanket search risk:** "Discovery first: complete project-wide analysis" is the kind of blanket search instruction the Haiku profile warns about. I kept it, but scoping it to the files a change touches would reduce that risk.
- **Git assumptions:** the Git rules only apply inside a repository. This folder is not one.
- **Vague priority:** "Context matters: prototype vs production" doesn't say how the model should tell which applies.
- **Harness descriptions:** the auto-selection and PM Agent lines describe behaviour the model doesn't control. Their use is unclear.

**6. Suggestion, not added:** if Haiku stops early on long tasks, add a line that it should keep working until the task is done. The profile recommends this for agents that stop early. I did not add it, because I can't see how your agent behaves.