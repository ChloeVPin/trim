# CLAUDE.md

Behavioral guidelines to reduce common coding mistakes. For trivial tasks, use judgment.

## 1. Think before coding

- State your assumptions. If the request has more than one reasonable reading, name the readings and say which one you chose.
- Ask before starting only when a wrong guess would be costly to undo.
- If something is unclear, name what is confusing before writing code.
- If a simpler approach exists, say so.

## 2. Simplicity first

- Write the minimum code that solves the stated problem.
- No features, options, or abstractions that were not requested.
- No abstraction for single-use code. No error handling for cases that cannot happen.
- If the solution is much longer than the problem needs, rewrite it shorter.

## 3. Surgical changes

- Change only what the request requires. Match the existing style.
- Do not reformat, rename, or refactor code the task does not touch.
- Remove imports, variables, and functions that your own change made unused.
- Leave pre-existing dead code alone. Mention it instead.
- Every changed line should trace back to the request.

## 4. Verify before finishing

- Turn the task into a check you can run first:
  - "Add validation" → write tests for invalid inputs, then make them pass.
  - "Fix the bug" → write a test that reproduces it, then make it pass.
  - "Refactor X" → run the tests before and after.
- For multi-step tasks, list each step with its check:
  1. [step] → verify: [check]
  2. [step] → verify: [check]
- Loop until the check passes. If you cannot run a check, say so.
