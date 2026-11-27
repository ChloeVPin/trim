# CLAUDE.md

Guidelines to reduce common coding mistakes. Bias toward caution over speed on non-trivial work. For trivial tasks, use judgment.

## 1. Understand before coding
- State your assumptions.
- If the request has more than one reasonable reading, name them and pick the most likely one.
- Ask only when the answer depends on something you cannot find out yourself, such as a file, access, or a decision only the user can make.
- If a simpler approach exists, say so.

## 2. Keep it simple
- Write the minimum code that solves the request. No extra features, options, or abstractions that were not asked for.
- No error handling for cases that cannot happen.
- If the solution is much longer than it needs to be, rewrite it shorter.

## 3. Make surgical changes
- Change only what the request requires. Do not reformat, rename, or "improve" nearby code or comments.
- Match the existing style, even if you would do it differently.
- Remove imports, variables, and functions that your own change made unused. Leave pre-existing dead code alone.
- Mention unrelated problems you notice. Do not fix them unasked.
- Test: every changed line should trace back to the request.

## 4. Verify before done
- Turn each task into a check you can run:
  - Bug: write a test that reproduces it, then make it pass.
  - New validation: write tests for invalid inputs, then make them pass.
  - Refactor: run the tests before and after.
- For multi-step work, write a short numbered plan, and give each step its check.
- Run the checks and report the results. If one fails, say so and include the output.
