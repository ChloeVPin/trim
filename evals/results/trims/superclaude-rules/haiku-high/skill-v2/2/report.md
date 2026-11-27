The proposed version is saved at `/root/trim-sbx/95f0743e6e71/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. Its profile is tested at high effort, so the cuts assume that setting.

**2. Length:** about 1,800 words before and about 1,300 after (estimates, since this session has no word counter). That is roughly 25–30% shorter.

**3. Changes and reasons**
- **Removed the Orchestration Flow, Quick Reference, Priority-Based Quick Actions and Tool Selection Matrix.** They restate rules above them. The matrix's unique entries (Magic MCP, context7 over web search) moved into Tool Optimization.
- **Merged repeated rules.** Parallel execution appeared in four places; it now lives in Planning Efficiency. "Read before write," "Parallel everything," and "Tool specialization" were duplicates and are gone.
- **Removed generic virtues** with no action attached: "elegant organization," "professional workspace," "start it = finish it," "purpose-based organization," "quality integrity," and "use technical terms."
- **Removed the Monthly-maintenance and knowledge-capture wording** from the orchestration bullets, reduced to one line each.
- **Kept the procedures and examples.** Haiku needs them, per its profile.

**4. Kept as written**
- **Git Workflow, in full.** Committing rules stay exactly as written.
- **Failure Investigation and Safety Rules.** They guard validation and fragile work.
- **Temporal Awareness,** including the `<env>` wording and the dated examples.
- **All ✅/❌ examples and detection commands** that show a procedure.
- **Lines I think are problematic but did not settle** (see flags).

**5. Flags for you to decide**
- **Tools and agents that may not exist here.** TodoWrite, MultiEdit, Task agents, the MCP servers (morphllm, sequential-thinking, playwright, context7, Magic MCP), the PM Agent, the specialist agents, and `/sc:load` / `/sc:save`. In this session I can see Read, Write, Edit, Glob and Grep, but not TodoWrite, MultiEdit or Task. If Haiku can't call a tool, these lines will send it to tools it doesn't have.
- **Conflict: "Absolute paths, no auto-commit" vs. "Commit frequently" and "Commit before risky operations."** I kept all three. You need to pick one.
- **Conflict with "No Fake Metrics":** "3 parallel ops = 60% time saving" and "Maintain ≥90% understanding." Haiku will likely produce made-up figures. Dropping both saves about 25 words.
- **Conflict: "Quality over speed" vs. "choose speed over familiarity."**
- **"No mock objects" vs. tests that use mocks.** Clarify whether test doubles are allowed.
- **"Delete build artifacts" may remove outputs someone needs.** Also unclear where debugging output ends and `claudedocs/` reports begin.
- **"Every 30 minutes" checkpoint.** The model can't measure elapsed time. "After each completed step" would work.
- **"Monthly" PM Agent maintenance** can't run inside a session.
- **Dated examples** ("January 2025", "2025-08-15") will age. The `<env>` label may not match this harness's wording, which puts the date in the system prompt as "Today's date."

**6. Suggestions (not added to the text)**
- **For coding work:** "Before reporting a change done, run the project's tests, lint or typecheck and report the actual output." This follows the Haiku profile. The current text says to run lint and typecheck, but not to report the result.
- **If Haiku stops early on long tasks:** "Keep working until the task is done."