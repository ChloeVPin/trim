The proposed version is saved at `/root/trim-sbx/f56dae585a97/trimmed.md`. `instructions.md` is unchanged. I only read it. I have not run either file against claude-haiku-5-5, so the shorter version is untested.

The original is about 290 lines and about 2,000 words. The proposal is about 600 words, with one ordered priority list instead of 15 sections with tiers and decision trees.

## Audit findings

**References to tools and systems that may not exist here**
- `TodoWrite`, `MultiEdit`, `/sc:load`, `/sc:save`, Magic MCP, Context7, Playwright, morphllm, sequential-thinking, PM Agent, and specialist agents. A smaller model may try to call these or get confused by them. I removed them.

**Rules that can't be enforced or checked**
- 30-minute checkpoints, monthly maintenance, "≥90% context retention", and automatic agent selection. I removed them.

**Contradictions**
- "No auto-commit" (Safety) conflicts with "commit frequently" and "commit before risky operations" (Git). The proposal says commit only when asked. This is a choice you may want to change.
- "Efficiency metrics: 3 parallel ops = 60% time saving" conflicts with the "No Fake Metrics" rule. I removed the example.
- "No Mock Objects" would block normal test writing. I limited the rule to production code and allowed mocks in tests.
- The Git section assumes a repository. This directory is not one, so I made that section conditional.

**Duplication**
- The parallel-operations rule appears about four times. The priority list is repeated in the quick reference. The decision trees restate rules that are already stated. I kept one copy of each.

**Haiku-specific changes**
- Short imperative bullets, one ordering, no nested trees, and fewer examples. The ✅/❌ examples are gone to save length. If you find the model drifts on a specific behavior, adding one example back for that rule is the first thing I would try.

## Choices I made that you can change
- **Added:** "Confirm before destructive, publishing, or external actions." The original only implied this. It sits at the top of the priority list.
- **Kept:** "Reports in `claudedocs/`" as a placement rule. It still lets the model write reports you didn't ask for, which conflicts with the scope rule. You may want to remove it.
- **Dropped:** the agent-orchestration section. Its one useful idea, documenting a mistake's root cause, is now one line under Failures.