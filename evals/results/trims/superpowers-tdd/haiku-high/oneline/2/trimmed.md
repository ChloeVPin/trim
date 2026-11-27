---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

## The Rule

Do not write production code unless a failing test requires it. If you wrote production code before its test, delete that code and start over from the test. Do not keep it for reference or adapt it.

If you did not watch the test fail, you do not know that it tests the right thing.

Applies to: new features, bug fixes, refactors, behavior changes.

Exceptions need the user's permission: throwaway prototypes, generated code, configuration files.

## The Cycle

1. **RED.** Write one minimal test for one behavior. Give it a clear name that describes the behavior. Use real code; mock only when unavoidable.
2. **Verify RED.** Run the test. It must fail, and fail because the feature is missing, not because of a typo or setup error.
   - If it passes, it tests existing behavior. Fix the test.
   - If it errors, fix the error and run again.
3. **GREEN.** Write the simplest code that makes the test pass. Do not add features, options, or unrelated changes.
4. **Verify GREEN.** Run the test. It must pass with no errors or warnings in the output. If it fails, fix the code, not the test.
5. **Run the full project suite.** Use the repo's own test command (for example `npm test`, `pytest`, or `cargo test`), even if the task named one test file. Fix any failure your change caused. Report any other failure by name.
6. **REFACTOR.** Only after green: remove duplication, improve names, extract helpers. Keep tests green and add no behavior.
7. Repeat with the next failing test.

## Writing Good Tests

- One behavior per test. If the name contains "and", split the test.
- Name the behavior. Not `test1` or `retry works`.
- Assert on real behavior, not on mock calls.
- Before writing a test, name the production change that would make it fail.
- Keep test-only helpers in test utilities, not in production classes.
- Before mocking a dependency, understand its side effects.
- If a test is hard to write, simplify the design instead of adding mocks.

Example of a good test:

```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };

  expect(await retryOperation(operation)).toBe('success');
  expect(attempts).toBe(3);
});
```

## Bugs

Write a failing test that reproduces the bug. Then follow the cycle. Never fix a bug without a test.

## Before Reporting Done

Check every item:

- [ ] Every new function or method has a test
- [ ] Each test was seen failing for the expected reason before its code was written
- [ ] Only minimal code was written for each test
- [ ] The full project suite passes, with no errors or warnings in the output
- [ ] Tests use real code; mocks only where unavoidable
- [ ] Edge cases and error paths are covered

If any box is unchecked, TDD was skipped. Go back and fix that.

In the final report, name every failing test, including failures you did not cause. Do not leave them out.

## Rationalizations to Reject

If you catch yourself thinking any of these, stop. Delete the untested code and restart at RED:

- "It's too simple to test."
- "I'll write the tests after." Tests written after pass immediately, so they prove nothing.
- "I already tested it manually." Manual checks are not repeatable.
- "I'll keep the code as reference." You will end up adapting it.
- "Deleting it wastes the time I already spent." Keeping untested code is the bigger waste.
- "TDD is too slow here" or "this case is different."
