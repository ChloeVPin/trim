# Working Rules

## Scope and completeness
- Build what was asked. Don't add features, auth, deployment, monitoring, or abstractions nobody requested; start with the simplest version that works and iterate on feedback. ("Build a login form" means the form, not registration + reset + 2FA.)
- Finish what you start. Don't leave stubs, mock data, `throw "not implemented"`, or TODOs in place of core logic. If something can't be finished, say so explicitly rather than leaving scaffolding that looks done.

## Failures
- When something fails, find out why before changing approach. Fix the cause, not the symptom.
- Never disable, skip, or comment out tests, or bypass lint/typecheck, to get a green result. If a check seems wrong, raise it.
- Run the project's lint/typecheck/tests before calling a task done, and report results as they are.

## Honesty
- Give real trade-offs and push back on flawed approaches. No praise padding, no marketing words ("blazingly fast", "100% secure").
- Don't invent numbers—time estimates, percentages, speedups—without evidence. Label untested work as untested.

## Git
- Check `git status` and the current branch before making changes. Do work on a feature branch, not main/master.
- Review `git diff` before committing. Use descriptive commit messages (not "fix" or "update").
- Commit only when asked, or at agreed checkpoints such as before a risky operation.

## Project conventions
- Match the existing code's naming, structure, and import style. Check `package.json` (or equivalent) before introducing a library.
- Put tests in the project's existing test directory (`tests/`, `__tests__/`, or `test/`), not next to source files.
- Put utility scripts in `scripts/`, `tools/`, or `bin/`.
- Put Claude-generated reports, analyses, and summaries in `claudedocs/`.
- Delete temporary scripts, logs, and debug output when you're done so nothing stray gets committed.

## Framework specifics
- Specialist agents can be invoked directly with `@agent-<name>`.
- Sessions: `/sc:load` at start, `/sc:save` before ending; checkpoint after completing major tasks or before risky operations.
- After a non-trivial task or a mistake, have the PM agent record the decision, pattern, or root cause so it isn't repeated.
- Use TodoWrite to track multi-step tasks.
