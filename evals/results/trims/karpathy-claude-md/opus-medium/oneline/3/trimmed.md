# CLAUDE.md

Coding guidelines. These favor care over speed; for trivial tasks, use judgment.

## Before coding
- State assumptions that matter. If the request is ambiguous in a way that changes the result, ask, or name the readings, before picking one.
- If a simpler approach exists, say so, and push back when it's warranted.

## Keep it simple
Write the least code that solves the problem. Don't add unrequested features, single-use abstractions, configurability, or handling for cases that can't happen. If a senior engineer would call it overcomplicated, simplify it.

## Make surgical changes
- Every changed line should trace back to the request. Don't reformat, refactor, or "improve" nearby code, and match the existing style.
- Remove imports, variables, and functions that your change left unused. Mention any dead code that was already there, but don't delete it.

## Verify
Turn the task into a check you can run, such as a failing test that reproduces the bug or tests that pass before and after a refactor. Iterate until it passes. For multi-step work, give a short plan with a verification for each step.
