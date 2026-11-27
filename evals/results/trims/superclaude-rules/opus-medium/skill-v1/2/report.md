I've saved a shorter version as `trimmed.md` and left `instructions.md` unchanged.

**Target model:** claude-opus-5-5, which you named. Its profile was tested at medium effort.

**Word count:** about 2,200 before and about 1,300 after, roughly 40% shorter. These are estimates: I had no tool that counts words, only lines.

## What changed and why

- **Emoji priority labels and "CRITICAL" / "ALWAYS" / "MUST" capitals:** turned into plain tags such as "(critical)". The priority order and the conflict rules stay. Current Claude models follow wording closely, and shouted emphasis makes them apply a rule too broadly.
- **The ✅/❌ example pairs:** cut down to the ones that set a format or make a rule concrete. The plan-format pair, the naming pair, the `calculate()` pair and the login-form example are kept.
- **Lines asking it to think first:** cut. These were "Think Before Build", "Think Before Write", "Methodical Problem-Solving", "Debug Systematically" and "Context Retention ≥90%". Anthropic's guidance for this model is that removing think-carefully lines loses no quality, and "≥90%" can't be measured anyway.
- **"Validation Gates: always validate before, verify after":** cut. The model checks its own work without being told. Anthropic said this for Opus 5, and it hasn't been confirmed for 5.5. The concrete check, "run lint/typecheck before marking tasks complete", stays.
- **Lines pushing for more tool use:** cut. These were "Best Tool Selection: most powerful tool", "Efficiency First" and "Parallel Everything… never sequentially". Lines like these now make the model overuse tools. Every specific tool fact stays.
- **Repeats merged:**
  - The parallelism advice appeared in Workflow, Planning and Tools; it now lives in Planning and Tools.
  - "Evidence-based" appeared twice.
  - Code Organization and File Organization are now one section.
  - The Quick Reference and Decision Trees section mostly repeated earlier rules. Its unique items moved into short sections: "absolute paths only / no auto-commit", "brainstorm mode first if scope is unclear", "run tests before starting", and the tool-to-task list (Magic, Context7, Playwright).
- **Agent Orchestration:** the three-layer description and flow diagram are reduced to the concrete behaviours: how agents get selected, the `@agent-[name]` override, PM Agent documenting after each task, root-cause analysis on errors, and the monthly review.
- **Temporal Awareness:** the example dates "January 2025" and "2025-08-15" are replaced with `<date>`. The rule itself is unchanged.

## Kept word for word
- **Git Workflow**, **Workspace Hygiene** and **Safety Rules** are untouched, emoji included. They govern committing, branches and deleting files, where a wrong cut costs far more than the words saved.
- In Failure Investigation, the three "Never Skip Tests / Never Skip Validation / Quality Integrity" lines are verbatim.
- "Safety check → Absolute paths only → No auto-commit" is verbatim.

## Kept, but reworded
All the facts are still there: `/sc:load`, `/sc:save` and the 30-minute checkpoint; TodoWrite for 3+ tasks; `claudedocs/`, `tests/` and `scripts/`; the naming conventions; the banned marketing words; the MCP server roles; and the `grep` detection command. Your preferences are also kept even where I wouldn't have chosen them, such as organizing by feature and having PM Agent document every task.

## Things for you to decide (all left as they were)
1. **Commit rules conflict.** Git Workflow says to commit frequently and before risky operations, but the File Operations line says "No auto-commit". The model can't tell which wins.
2. **Made-up numbers conflict.** Planning asks for expected time savings like "3 parallel ops = 60% time saving", but Professional Honesty bans invented percentages.
3. **The step threshold doesn't match.** TodoWrite is triggered at "3+ tasks" but the old decision tree said ">3 steps", and Task agents also use ">3 steps". Pick one number.
4. **Deletion scope may be too wide.** Workspace Hygiene says to delete build artifacts, logs and "unused directories and files". That's broad, and deleting can't be undone. Consider limiting it to files the agent created itself, or asking before deleting anything else.
5. **Some lines may be out of date:**
   - MultiEdit may no longer exist as a tool.
   - The model can't do the monthly PM Agent review on its own unless something triggers it.
   - "Playwright MCP > unit tests" and "Task agent > native reasoning" may push the model to use those tools when it doesn't need to.
6. **Possible addition:** a line telling the model to look through the relevant sources before acting on loosely specified, multi-part work. That's what Anthropic recommends for this model.

The full proposed text is in `trimmed.md`.