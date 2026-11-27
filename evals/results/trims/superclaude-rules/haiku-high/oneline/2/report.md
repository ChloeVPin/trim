I wrote the shorter version to `/root/trim-sbx/d768efe111f5/trimmed.md`. `instructions.md` is unchanged. The file went from 287 lines to about 75, and I did not test it against claude-haiku-5-5, so the Haiku suitability is a judgment based on keeping rules short, concrete, and non-conflicting.

**Audit of instructions.md**

- **Things the agent can't do or that don't exist here:** the PM Agent, automatic specialist-agent selection, `@agent-` routing, `/sc:load` and `/sc:save`, MCP servers (Magic, Context7, Playwright, morphllm, sequential-thinking), 30-minute checkpoints, monthly maintenance, and "≥90% context retention." A model can't schedule or measure these, so they add noise.
- **Invented metrics:** "3 parallel ops = 60% time saving" breaks the file's own "No Fake Metrics" rule.
- **Contradictions:**
  - "Incremental commits" and "commit before risky operations" conflict with the decision tree's "No auto-commit."
  - "Feature branches only" assumes a git repo, but this workspace is not one.
  - "No mock objects" conflicts with normal test doubles.
- **Redundancy:** the parallel-calls rule appears in four sections, the priority tiers are restated three times, and the right/wrong examples repeat.
- **Vague phrasing:** "Elegant Organization," "Think before build," and "Quality > Speed" are hard to act on.
- **Kept:** read-before-edit, never skipping tests, root-cause analysis, no stubs in production code, scope limits, honest reporting, file placement, and cleanup of temp files.

**Choices I made that you may want to change**

1. **Git:** I made commits and pushes happen only when you ask, and made the git section apply only if the project is a repo. This resolves the auto-commit conflict in favor of not committing. If you want the agent to commit restore points on its own, tell me and I'll adjust.
2. **Test doubles:** allowed in tests, banned in production code.
3. **Folder conventions:** I kept `tests/`, `scripts/`, and `claudedocs/` as the placement rules.
4. **Dropped:** the tiered priority scheme, the decision trees, and the Haiku-irrelevant agent and MCP references.