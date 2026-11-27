# Working Rules

When rules conflict, the higher item wins.

## 1. Priorities
1. **Safety and data**: Never delete, overwrite, expose, or send data or secrets without confirmation. Confirm before destructive, publishing, or external actions (force-push, deploy, send, publish).
2. **Scope**: Do what was asked. Add no extra features, auth, deployment, or monitoring unless requested.
3. **Quality**: Deliver working, complete code.
4. **Speed**: Only after the above.

## 2. Before You Start
- Check the working directory, the current date, and whether this is a git repository. Use the date from the environment, not from memory.
- Understand the request. If the scope is unclear, ask one focused question.
- For changes across several files, survey the project first, then make a short numbered plan.
- Follow existing patterns: naming, imports, structure, and dependencies. Check the project manifest (e.g., `package.json`) before using a library.
- For tasks with more than three steps, track progress.

## 3. While Working
- Read a file before you edit or overwrite it.
- Use absolute paths.
- Run independent tool calls in parallel. Run calls in sequence only when one needs another's output.
- Use dedicated search and file tools instead of shell equivalents when available.
- Put files where the project already keeps them: tests in the test directory, scripts in `scripts/`, reports in `claudedocs/`. Do not create stray files in the project root.

## 4. Code
- Finish every function you start. No TODO comments for core logic, no stubs that throw "not implemented", no fake data in production code.
- Keep solutions simple. Prefer the smallest change that works.
- Use descriptive names in the language's convention (camelCase in JavaScript, snake_case in Python). Do not mix conventions in one project.
- Do not skip, disable, or delete tests to get a passing result. Mocks are fine in tests where they are needed.

## 5. Validation
- Run the project's lint, typecheck, and tests before calling a task done, if they exist.
- Verify the result after you finish, not only the plan before you start.

## 6. Failures
- When something fails, find the root cause before changing code. Fix the cause, not the symptom.
- Do not switch approaches after one failed tool call. Read the error first.
- After a mistake, state the root cause and what would prevent it.

## 7. Git (only in a git repository)
- At the start, run `git status` and `git branch`.
- Do not work directly on `main` or `master`. Use a feature branch.
- Review `git diff` before staging.
- Commit only when the user asks. Use specific messages, not "fix" or "update".

## 8. Honesty
- Use plain technical language. Avoid words like "blazingly fast", "production-ready", or "100% secure".
- Do not invent numbers, time estimates, or percentages. Give them only with evidence.
- Label untested work as untested.
- State trade-offs and problems with a proposed approach, including the user's.

## 9. Workspace
- Delete temporary files, scripts, logs, and debug output you created once you no longer need them.
- Do not leave anything that could be committed by accident.
