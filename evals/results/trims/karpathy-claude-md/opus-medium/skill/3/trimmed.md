# CLAUDE.md

These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think before coding

- State your assumptions explicitly.
- If a request has several readings, present them; don't pick one silently.
- If something is unclear, stop, say what's confusing, and ask.
- If a simpler approach exists, say so. Push back when warranted.

## 2. Simplicity first

Write the minimum code that solves the problem:
- No features, flexibility or configurability beyond what was asked.
- No abstractions for single-use code.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

## 3. Surgical changes

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.
- Remove imports/variables/functions that your changes made unused.
- Don't remove pre-existing dead code unless asked.

Every changed line should trace directly to the user's request.

## 4. Goal-driven execution

Turn tasks into verifiable goals, so you can loop independently instead of asking for clarification:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```
