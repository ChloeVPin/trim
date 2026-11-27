# CLAUDE.md

Coding guidelines. Project-specific instructions take precedence. These lean toward caution; on trivial tasks, use judgment.

## Before coding
State the assumptions that matter. If a request could reasonably mean different things and the choice changes the result, ask instead of picking one quietly. If a simpler approach exists, say so.

## Keep it minimal
Write only what the task needs: no extra features, configurability, or abstractions, and no error handling for cases that can't happen. If the solution feels bloated, simplify it.

## Change only what's needed
Every changed line should trace back to the request. Match the existing style. Don't reformat, refactor, or "improve" nearby code. Remove imports or code that your own change made unused. Mention unrelated dead code instead of deleting it.

## Verify
Turn the task into a check you can run, e.g. a failing test that reproduces the bug, or tests that pass before and after a refactor. Work until the check passes. For multi-step work, give a short plan with a verification step for each part.
