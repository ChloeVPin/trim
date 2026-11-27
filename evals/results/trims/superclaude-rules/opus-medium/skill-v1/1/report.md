I've saved the shorter version as `trimmed.md`. It is about 58% shorter, and `instructions.md` is unchanged.

**Target model:** claude-opus-5-5, which you named. Its profile has been tested at medium effort.

**Word count:** 2,126 before and 883 after. I counted with ripgrep, which counts every whitespace-separated token, so markdown symbols, arrows and emoji are included.

## Changes and reasons
- **I replaced the emoji priority tiers and the CRITICAL/🔴 labels with three plain tiers** in a short "Priorities" section. On current models, all-caps and "CRITICAL"-style emphasis makes rules get applied too widely. I kept the order of what wins in a conflict.
- **I removed the "Quick Reference & Decision Trees" section.** Nearly all of it repeated earlier sections. I moved the few unique items into the relevant sections: brainstorm mode when scope is unclear, running existing tests before starting, read before edit, absolute paths, no auto-commit, and the Magic, Context7 and Playwright tool mappings.
- **"Run independent operations in parallel" appeared four times.** It now appears once, without the "ALWAYS" emphasis.
- **I cut the "think first" lines:** "Think Before Build", "Methodical Problem-Solving", "Debug Systematically" and "Think Before Write". The model's maker says that removing instructions to think carefully gave faster replies with no clear quality loss.
- **I cut the general check-your-work lines:** "Validation Gates", "Systematic Changes" in the workflow section, and the `Detection:` grep and git commands. The maker says the previous version of this model checks its work without being told, so these lines add cost. That this holds for the current version hasn't been confirmed. I kept the concrete lint/typecheck step because it defines when a task counts as done.
- **I cut "most powerful tool", "Efficiency First" and "MCP > Native > Basic".** Lines that push tool use now make the model reach for tools more than it should. The specific tool mappings are still there.
- **I removed lines that state general virtues or can't be acted on:** "Context Retention ≥90%", "Elegant Organization", "Professional Workspace", "Quality Integrity", "Completion Mindset", and the Auto-Selection paragraph. That paragraph describes what the framework does, not what the model should do.
- **I condensed the sections that said one thing several ways:** Implementation Completeness, Scope, Professional Honesty, Code and File Organization, and Dates. Most ✅/❌ example pairs went. I kept the ones that set a format: the plan format, naming, and `feature/auth`.
- **I cut the "Don't default to January 2025" line and the 2025-08-15 example** from the dates section because they are out of date. The instruction to check today's date and say where it came from is still there.

## Kept, and why
- **These lines are word for word:** the Git Workflow bullets, the Safety Rules bullets, the four main Failure Investigation rules (never skip tests or validation, fix the cause rather than work around it, debug tool failures), and the deletion lines in Workspace Hygiene. They cover commits, branches, deletion and test integrity, where a wrong cut costs far more than the words saved.
- **Every fact the model can't work out alone is still in:** `claudedocs/`, the test and script folders, `/sc:load` and `/sc:save`, the 30-minute checkpoints, `@agent-[name]`, the PM Agent duties, the MCP server names and the naming conventions.
- **I kept all your preferences, even where I might have chosen differently:** no mocks or TODOs, YAGNI, no marketing words, feature-branch-only work, and Task agents for work of more than 3 steps.

## Flags and suggestions for you to decide
1. **Commit rules conflict.** "Commit frequently" and "commit before risky operations" clash with "no auto-commit" (which I moved into Git Workflow). Say which applies, for example "commit only when asked" or "commit freely on feature branches".
2. **The parallelization rule conflicts with the honesty rule.** "State the expected parallelization gain (e.g. 60% time saving)" asks for exactly the kind of made-up percentage that "No Fake Metrics" forbids. I kept both.
3. **The deletion lines are broad.** "Delete unused directories and files" and "delete build artifacts, logs" could remove things the model didn't create. Consider limiting them to files the model made, or adding "ask before deleting anything else".
4. **The TodoWrite threshold is inconsistent.** One place says "3+ tasks" and another says ">3 steps". I kept "3+".
5. **The folder rules pull against each other.** "Organize by feature/domain, not file type" sits awkwardly next to the dedicated `tests/` and `scripts/` folders.
6. **Some references may be out of date.** Check that MultiEdit, morphllm, Magic MCP and `/sc:load` still exist in your setup. "Monthly PM Agent maintenance" can't be triggered from inside one session.
7. **A possible addition, which I didn't put in the text:** for loosely defined work, a line telling the model to look through the relevant sources before acting. The maker recommends this for this model.

The full proposed text is in `/root/trim-sbx/794a2c345326/trimmed.md`.