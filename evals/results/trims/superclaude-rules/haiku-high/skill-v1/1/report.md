I saved the proposed version to `/root/trim-sbx/70736b212f85/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. Haiku needs more detail than the larger models, so I cut only duplicates, descriptions of platform behaviour, and slogans. Every ✅/❌ example and every procedure step is kept.

**2. Length:** about 2,700 words before, about 1,800 after. These are estimates, since I had no word counter in this session.

**3. Changes and reasons:**
- **Removed duplicates:** the same rule appeared in two to four sections (parallel calls, git branches, cleanup, "no mock/placeholder code", tool choice). Each now appears once.
- **Quick Reference:** the "Priority-Based Quick Actions" list repeated the sections above, so I dropped it. Its unique items (read before editing, absolute paths, no auto-commit) now sit in the decision trees. The three decision trees and the tool matrix are kept.
- **Agent Orchestration:** I removed the auto-selection, keyword, file-type and complexity bullets, because they describe what Claude Code does, not what the model should do. I also removed the four-step "Orchestration Flow", which restated the layer bullets.
- **Generic lines:** "Professional workspace", "Elegant organization", "Hierarchical logic", "Efficiency First", "Separation of concerns" and "Quality integrity" were either unmeasurable or repeated something else.
- **Emphasis:** I lowered capitals on non-guard rules ("ALWAYS parallel" became "run independent calls in parallel"). Guard rules keep their original wording, including "Never", "never work on main/master", and "no auto-commit".

**4. Kept on purpose:** all deletion, commit, branch and test-skipping rules; all ✅/❌ examples; all paths, commands and tool names; the priority hierarchy; and the author's preferences, including the ones I would not choose.

**5. Flags for you to decide (none applied):**
- **Conflict, commits:** "no auto-commit" (Safety, Quick Reference) vs "commit frequently" and "commit before risky operations" (Git Workflow).
- **Conflict, metrics:** "Do not invent time estimates, percentages" (Professional Honesty) vs the planning line asking for expected gains, whose example is itself an invented "60% time saving".
- **Conflict, threshold:** TodoWrite at "3+ tasks" (Workflow) vs "more than 3 steps" (Quick Reference). Pick one.
- **Ambiguity:** "No mock objects" could be read as banning test mocks.
- **Stale or unverifiable:** PM Agent, backend-architect, `@agent-security`, `/sc:load`, `/sc:save`, and "monthly maintenance". The model cannot run a monthly job. The 30-minute checkpoint has no clock to rely on. Check that each exists in your setup.
- **Tools that may be absent:** Magic MCP, Context7, Playwright, morphllm, sequential-thinking, and MultiEdit. If they are not installed, "debug before switching approaches" could make the agent loop.
- **Risky deletion:** "Delete unused directories and files" has no scope and could remove your own files. You could limit it to files created in the session.
- **Dated examples:** "Today is 2025-08-15" and "January 2025" are out of date (today is 2026-11-27) and could anchor the model to old dates.
- **Broad search:** "complete project-wide analysis before systematic changes" is the kind of blanket search instruction that made Haiku search when it did not need to. I kept it and did not scope it.
- **Unmeasurable:** "maintain ≥90% understanding" cannot be checked.

**6. Suggestions, not added to the text:**
- Haiku guidance for coding agents says to run a real check before reporting a change done. "Run lint and typecheck" is there, but no test run is. Consider adding "run the relevant tests".
- If the agent stops early on long tasks, add "keep working until the task is done".
- Add a one-line reason to each rule (e.g., why no auto-commit). Rules with reasons generalise better.