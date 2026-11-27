---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first, watch it fail, then write the minimal code that makes it pass. If you never saw the test fail, you don't know whether it can catch the bug it's meant to catch.

## When to use

Use it for new features, bug fixes, refactoring, and behavior changes. For throwaway prototypes, generated code, or configuration files, ask your human partner whether TDD applies.

If production code was written before its test, delete it and start again from the test. Don't keep it as a reference and adapt it. Tests written to fit existing code pass right away and check the cases you remembered, not the ones the code should handle. Exploratory spikes are fine, but throw them away before starting the TDD cycle.

## The cycle

### 1. RED: write one failing test

Each test covers one behavior, has a name that describes that behavior, and runs real code. Use mocks only when there's no way around them.

```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };
  const result = await retryOperation(operation);
  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```

Avoid vague names like `'retry works'`, and avoid tests that only check a mock, such as `expect(mock).toHaveBeenCalledTimes(3)`.

### 2. Verify RED (never skip this)

Run the test and confirm that:
- it fails rather than errors,
- the failure message is the one you expected,
- it fails because the feature is missing, not because of a typo or setup problem.

If it passes, it's testing behavior that already exists, so fix the test. If it errors, fix the error and run it again until it fails for the right reason.

### 3. GREEN: write minimal code

Write the simplest code that makes the test pass. Don't add options, features, or refactors the test doesn't require. For example, if the test only covers three retries, don't add configurable backoff.

### 4. Verify GREEN (never skip this)

Run the test and confirm that it passes and the output is clean, with no errors or warnings. If it fails, fix the code, not the test.

Then run the whole project suite with the repo's test command (bare `pytest`, `npm test`, `cargo test`, and so on), even if your task named only one test file. The scope of your task limits what you deliver, not what you verify. Fix any failures you caused. Report every failure by name, including ones you didn't cause. Leaving a red test out of your report makes the report false.

### 5. REFACTOR

Only once everything is green: remove duplication, improve names, and extract helpers. Keep the tests green and don't add behavior. Then write the next failing test.

## Writing good tests

Before writing or changing any test, read [writing-good-tests.md](writing-good-tests.md). In short:
- Before you write a test, name the production change that would make it fail.
- Assert on real behavior, never on mock behavior.
- Keep test-only code in test utilities, not in production classes.
- Understand a dependency's side effects before you mock it.

If a test name contains "and", split it into separate tests.

## Bugs

Before fixing a bug, write a failing test that reproduces it, then follow the cycle. The test proves the fix works and guards against regression.

## When stuck

| Problem | Response |
|---|---|
| Don't know how to test it | Write the API you wish you had, and write the assertion first. Ask your human partner. |
| Test is complicated or setup is huge | The design is probably too complicated. Simplify the interface or extract helpers. |
| You have to mock everything | The code is too tightly coupled. Use dependency injection. |

## Before marking work complete

- [ ] Every new function or method has a test that you watched fail for the expected reason.
- [ ] Each piece of implementation is the minimal code needed to pass its test.
- [ ] Edge cases and error paths are covered.
- [ ] The full project suite passes with clean output, or every failure is named in your report.
