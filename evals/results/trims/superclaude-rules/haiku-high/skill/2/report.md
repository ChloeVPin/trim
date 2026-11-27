**Target model:** `claude-haiku-5-5`, as you named it. It has a profile in the skill (tested at high effort).

**Words:** about 2,500 before and about 1,200 after. I have no word-count tool in this session, so both figures are my estimates (roughly ±10%).

**Saved to:** `/root/trim-sbx/6431a859558c/trimmed.md`. `instructions.md` is unchanged.

## Changes and reasons

- **Removed the Quick Reference section (~330 words).** Its quick actions repeat rules above, and its decision trees restate them. I kept the four facts that appeared only there: absolute paths, no auto-commit, run existing tests before starting, and clarify unclear scope.
- **Removed most ✅/❌ examples.** Each restated its rule. I kept two that pin format or scope: the plan example and the login-form scope example.
- **Removed things Haiku can't act on:** "Context retention ≥90%", "monthly maintenance", "30-min checkpoint intervals", "execution time" estimates, and the Temporal "Detection" line.
- **Removed duplicates and generic virtues.** "Always parallel" appeared in four places and is now one line. Also cut: "evidence-based" (repeated), "validation gates" (covered by the task pattern), "single responsibility", "YAGNI", "elegant organization", and "think before write".
- **Removed the "Efficiency Metrics" line.** It asks for invented figures such as "60% time saving", which contradicts "No Fake Metrics" in Professional Honesty. See the flags below.
- **Removed the agent auto-selection bullets.** They describe harness behaviour the model does not act on.
- **Lowered emphasis** in non-protected sections: "ALWAYS", "MUST", and "ONLY" are now plain. The maker says capitals over-apply on Claude 5 models. Meaning is unchanged.
- **Narrowed "complete project-wide analysis"** to "survey the affected code". The profile warns that blanket search instructions make Haiku search when it doesn't need to. This changes your wording, so it's your call.
- **Reworded "always use the most powerful tool"** to "prefer … when they fit the task", to avoid over-triggering tool use.
- **Removed stale dates** ("January 2025", "Today is 2025-08-15") from Temporal Awareness. The rule stays.
- **Removed Triggers lines** from non-protected sections. Priority labels stay.

## Kept, and why

- **Verbatim:** Workspace Hygiene, Git Workflow, and Failure Investigation. Workspace Hygiene covers deletion, Git Workflow covers commits, and both fall under the skill's protected list. Failure Investigation is 🔴 and governs skipping tests and validation, so I left it whole.
- **Priority tiers and conflict order:** these are the author's choices.
- **Lint and typecheck before marking done:** this is the real check the profile asks for on coding agents.

## Flags for you to decide

1. **Metrics conflict:** "No Fake Metrics" versus the efficiency-metrics line. I removed the metrics line. Tell me if you want it back.
2. **Commit conflict:** Git Workflow says "commit frequently", but the Quick Reference said "no auto-commit". I kept "Do not auto-commit" in Safety Rules and left Git Workflow untouched. Tell me which rule holds.
3. **"No Mock Objects"** may be read as banning test doubles. I kept it as written.
4. **References that may not exist in your setup:** PM Agent, `@agent-`, `/sc:load`, `/sc:save`, MultiEdit, Task agents, and the named MCP servers. If they are not installed, cutting them saves about 120 words.
5. **Merge candidates in protected sections:** the seven Workspace Hygiene bullets say much the same thing (about 60 words). "Quality Integrity" overlaps two Failure Investigation bullets (about 15 words).

## Suggested addition (not applied)

- For Haiku, if the agent stops early on long tasks, add "Keep working until the task is done." The profile recommends this.