# CLAUDE.md

Guidelines to reduce common coding mistakes. Bias toward caution over speed. For trivial tasks, use judgment.

## 1. Surface assumptions

- State your assumptions before coding.
- If several readings are plausible, name them and pick the most likely one. Ask only when a wrong guess would be costly to undo.
- If a simpler approach exists, say so.

## 2. Keep it simple

- Write the minimum code that solves the request. No extra features, configurability, or abstractions for single-use code.
- No error handling for cases that cannot happen.
- Ask: would a senior engineer call this overcomplicated? If yes, simplify.

## 3. Make surgical changes

- Touch only what the request requires. Don't reformat, rename, or "improve" adjacent code.
- Match the existing style, even if you would do it differently.
- Remove imports, variables, and functions that your own change left unused. Leave pre-existing dead code alone and mention it.
- Every changed line should trace back to the request.

## 4. Verify before you finish

- Turn the task into a check first:
  - Bug: write a test that reproduces it, then make it pass.
  - Validation: write tests for invalid inputs, then make them pass.
  - Refactor: run the tests before and after.
- For multi-step work, write a short plan where each step has a verification.
- Loop until the check passes. If you cannot run it, say so.
