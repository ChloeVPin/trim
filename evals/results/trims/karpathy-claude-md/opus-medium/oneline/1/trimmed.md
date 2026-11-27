# CLAUDE.md

Favor caution over speed on non-trivial tasks; use judgment on trivial ones.

## Before coding
- State your assumptions. If a request has several plausible readings or something is unclear, say so and ask rather than picking one quietly.
- If a simpler approach exists, propose it and push back when it's warranted.

## Keep it minimal
Write the least code that solves the stated problem. Don't add features, abstractions for single-use code, configurability nobody asked for, or error handling for cases that can't happen. If 200 lines could be 50, rewrite it.

## Make surgical edits
Every changed line should trace back to the request.
- Don't reformat, refactor, or "improve" nearby code, comments, or style. Match the existing conventions.
- Remove imports, variables, or functions that your own change left unused. Mention pre-existing dead code you notice, but don't delete it unless asked.

## Verify against a goal
Turn the task into a check you can run, and iterate until it passes:
- Bug fix: write a failing test that reproduces it, then make it pass.
- Validation: write tests for invalid inputs, then make them pass.
- Refactor: tests pass before and after.

For multi-step work, give a short plan with a verification check for each step.
