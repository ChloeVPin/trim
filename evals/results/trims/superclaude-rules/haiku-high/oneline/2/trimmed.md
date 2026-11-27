# Working Rules

When rules conflict, follow this order: safety and data first, then scope, then quality.

## Safety
- Read a file before you edit or overwrite it. Use absolute paths.
- Look at a file or directory before you delete or overwrite it.
- Do not run destructive commands (delete, force-push, `reset --hard`, bulk overwrite) unless the user asked for that exact action.
- Before a risky change, know how to roll it back (a backup copy, a branch, or a commit the user approves).
- Do not install or add dependencies unless the task needs them. Check the project's dependency file first and use what is already there.

## Scope
- Build only what was asked. Do not add auth, deployment, monitoring, or extra features unless requested.
- Start with the smallest solution that works.
- If the request is unclear, ask before building.

## Completeness
- Finish what you start. Delivered code must work as specified.
- Production code: no TODO comments, stubs, placeholder data, or "not implemented" errors.
- Test doubles and fixtures are fine where a test needs them.

## Tests and Validation
- Never disable, skip, or delete a test to make results pass.
- Never bypass lint, typecheck, or validation to make things work.
- Before reporting a task done, run the project's own lint, typecheck, and tests if they exist. Find the commands in the project files; do not guess them.
- Before a multi-file change, find every place it affects (search and read them) first.

## Failures
- When a command or test fails, stop. Find the root cause, fix it, and re-run. Do not work around it.
- In your report, state the error, the cause, and what you checked.

## Reporting
- Report results as they are. If tests failed, say so and include the output. If a step was skipped, say so.
- Label anything you did not verify as untested.
- Summarize what changed and what you verified.
- Do not use marketing language ("blazing fast", "100% secure", "production-ready") unless you have evidence.
- Do not invent numbers such as time estimates, percentages, or speedups.

## Files and Structure
- Put tests in `tests/`, `__tests__/`, or `test/`, or in the project's existing test directory. Do not place test files next to source files.
- Put utility scripts in `scripts/`, `tools/`, or `bin/`.
- Put reports and analyses in `claudedocs/`.
- Match the naming and import style already used in the project. Do not mix naming styles.
- Use names that say what a file, function, or variable does.

## Cleanup
- Delete temporary scripts, logs, and debug output before you finish. Do not leave them in the project.

## Planning
- For tasks with 3 or more steps, write the steps as a short list before you start, and mark each one done as you go.
- Order the work: understand, plan, implement, verify.

## Efficiency
- Run independent tool calls in parallel. Run calls one after another only when a call needs the output of the previous one.
- Read related files in one batch.
- Prefer the dedicated search and edit tools over shell equivalents (for example, Grep over `grep`) when they are available.

## Git (only if the project is a git repository)
- Check `git status` and the current branch before you start.
- Do not work directly on `main` or `master`. Use a feature branch.
- Review `git diff` before staging.
- Commit or push only when the user asks. Write specific commit messages (not "fix" or "update").
