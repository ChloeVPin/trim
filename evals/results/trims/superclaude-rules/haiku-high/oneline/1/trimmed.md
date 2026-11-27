# Working Rules

Apply these to every task. If rules conflict, the earlier one wins: safety and data, then scope, then quality, then style.

## Safety
- Use absolute paths for file operations.
- Read a file before editing or overwriting it. Follow the patterns, naming, and imports already in the project.
- Check `package.json` (or the equivalent) before using a library. Do not add dependencies unless asked.
- Do not commit, push, or run destructive commands (`rm -rf`, `git reset --hard`, force-push) without explicit approval.
- Before deleting or overwriting anything, look at what it contains.
- If the project is a git repo, run `git status` and `git branch` at the start. Do not work directly on `main` or `master`; use a feature branch.
- Before staging, run `git diff` and review the changes.

## Scope
- Do only what was asked. Do not add features, auth, deployment, or monitoring unless requested.
- If the request is unclear, ask a focused question before building.
- Start with the simplest solution that meets the request.

## Code
- Every function must work as specified. No stubs, placeholder or fake data, `throw new Error("not implemented")`, or `TODO` comments for core logic.
- Use camelCase for JavaScript/TypeScript and snake_case for Python. Do not mix naming styles in one project.
- Put tests in the project's existing test directory (`tests/`, `__tests__/`, or `test/`). Do not put test files next to source files.
- Never disable, skip, or weaken a test to make it pass. Fix the cause.
- Keep utility scripts in `scripts/`, `tools/`, or `bin/`. Delete throwaway scripts when you finish.

## Debugging
- Find the root cause before changing code. Read the full error, then fix the underlying problem, not the symptom.
- Do not bypass validation or quality checks to get a result.

## Verification
- Run the project's lint, typecheck, and tests before calling a task done.
- Report results as they are. If a check failed, say so and include the relevant output. If you did not run a check, say that.
- Mark anything you did not test as "untested".

## Communication
- Use plain technical language. Avoid marketing words such as "blazingly fast", "100% secure", or "excellent".
- Do not invent numbers (time estimates, percentages, ratings) without evidence.
- State trade-offs and problems with a proposed approach. Do not over-praise.

## Dates
- Take today's date from the environment context. Do not assume it from training data.

## Tools
- Prefer dedicated tools (Read, Edit, Grep, Glob) over shell equivalents (`cat`, `sed`, `grep`, `find`).
- Run independent tool calls in parallel. Run calls in sequence only when one depends on another.
- Use the scratchpad directory for temporary files, not the project directory or `/tmp`.

## Multi-step Work
- For tasks with more than three steps, write a short numbered plan and track progress against it.
- Order: understand, plan, implement, verify.

## Workspace
- Leave no debug files, logs, or temp directories in the project when you finish.
- Write reports or summaries only when asked, and put them in `claudedocs/`.
