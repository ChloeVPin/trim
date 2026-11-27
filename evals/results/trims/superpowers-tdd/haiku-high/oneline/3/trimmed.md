---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development

## Rule

Do not write production code without a failing test written first.

If you wrote production code before its test, delete it and start over from the test. Do not keep it as reference and do not adapt it.

## When This Applies

- Always: new features, bug fixes, refactors, behavior changes.
- Exceptions (ask the user first): throwaway prototypes, generated code, configuration files.

Do not skip TDD on your own judgment, even "just this once."

## The Cycle

1. **RED: write one failing test.** Test one behavior, with a clear name. Use real code. Mock only when unavoidable.
2. **Verify RED: run the test.**
   - It passes: you are testing existing behavior. Fix the test.
   - It errors (typo, bad import, syntax error): fix the error and rerun.
   - It fails with the expected message because the feature is missing: continue.
3. **GREEN: write the simplest code that passes.** Do not add features, options, or unrelated changes.
4. **Verify GREEN: run the full project test suite**, not just your test file. Use the repo's command (for example `pytest`, `npm test`, or `cargo test`).
   - Your test fails: fix the code, not the test.
   - Any other test fails: fix it now, even if you did not cause it.
   - The output must be clean, with no errors or warnings.
5. **REFACTOR: only when green.** Remove duplication, improve names, extract helpers. Do not add behavior. Rerun the tests.
6. Repeat for the next behavior.

## Good Tests

- One behavior per test. If the name contains "and," split the test.
- The name describes the behavior. Avoid names like `test1` or `retry works`.
- Assert on real results, not on mock calls.
- Before writing a test, name the production change that would make it fail.

Good:

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

Bad: a test named `retry works` that only checks that a jest mock was called 3 times.

## Bugs

Write a failing test that reproduces the bug. Then fix the code. Never fix a bug without a test.

## Red Flags: Stop and Restart With a Failing Test

- Code written before its test
- A new test passes immediately
- You cannot explain why the test failed
- "I'll add tests later"
- "I already tested it manually"
- "Keep it as reference" or "adapt the existing code"

## Completion Checklist

- [ ] Every new function or method has a test
- [ ] I saw each test fail for the expected reason before implementing
- [ ] I wrote minimal code to pass each test
- [ ] The full project test suite passes
- [ ] The output has no errors or warnings
- [ ] Edge cases and error paths are tested
- [ ] Mocks are used only where unavoidable

If any box is unchecked, the work is not done.

## When Stuck

- Do not know how to test it: write the assertion for the API you wish existed, then build toward it. If still unclear, ask the user.
- Test needs heavy setup or many mocks: the design is too coupled. Simplify the interface or inject dependencies.

## Reporting

In your final report, name every failing test from the full-suite run, including failures you did not cause. Do not leave out failures you saw.
