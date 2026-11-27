---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first. Watch it fail. Write minimal code to pass. If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

Applies to new features, bug fixes, refactoring and behavior changes.

**Exceptions (ask your human partner):**
- Throwaway prototypes
- Generated code
- Configuration files

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

Why: tests written after the code pass immediately, which proves nothing; they check the cases you remembered, not the ones you would have found. Time already spent on untested code is sunk cost. Exploring first is fine, but throw the exploration away and start with TDD. When touching existing code that has no tests, add tests for it.

## Red-Green-Refactor

### RED: write a failing test

One minimal test showing what should happen: one behavior, a clear name, real code (no mocks unless unavoidable).

<Good>
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
Clear name, tests real behavior, one thing
</Good>

<Bad>
```typescript
test('retry works', async () => {
  const mock = jest.fn()
    .mockRejectedValueOnce(new Error())
    .mockRejectedValueOnce(new Error())
    .mockResolvedValueOnce('success');
  await retryOperation(mock);
  expect(mock).toHaveBeenCalledTimes(3);
});
```
Vague name, tests mock not code
</Bad>

### Verify RED: watch it fail

Always run it. Confirm the test fails (not errors), the failure message is the expected one, and it fails because the feature is missing (not a typo).

- Test passes? You're testing existing behavior. Fix the test.
- Test errors? Fix the error and re-run until it fails correctly.

### GREEN: minimal code

Write the simplest code that passes the test. Don't add options, features or refactors beyond what the test requires.

### Verify GREEN: watch it pass

Confirm the test passes, other tests still pass, and output is pristine (no errors, warnings).

- Test fails? Fix the code, not the test.
- Other tests fail? Fix now.

**"Other tests" means the project's suite, not just your file.** A
green run of the test you wrote is not a green suite. Before you call
the change done, run the project's test command (bare `pytest`,
`npm test`, `cargo test` — whatever the repo uses) even when your task
named only one test file. A scope statement in your task bounds the
deliverable, not your verification. Any failure that run shows —
including one you didn't cause — goes in your report by name; a red
test you watched scroll past and didn't mention is a report falsified
by omission.

### REFACTOR

Only after green: remove duplication, improve names, extract helpers. Keep tests green; don't add behavior. Then write the next failing test.

## Good Tests

- Minimal: one thing. "and" in the name? Split it.
- Clear: the name describes the behavior.
- Shows intent: demonstrates the desired API.
- Every new function/method has a test; edge cases and errors are covered.

When writing or changing any test, read [writing-good-tests.md](writing-good-tests.md) for the rules that keep tests honest:
- Name the production change that would make the test fail — before writing it
- Assert on real behavior, never on mock behavior
- Keep test-only code in test utilities, out of production classes
- Understand a dependency's side effects before mocking it

## Bugs

Never fix a bug without a test. Write a failing test that reproduces it, then follow the cycle.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write wished-for API. Write assertion first. Ask your human partner. |
| Test too complicated | Design too complicated. Simplify interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify design. |

No exceptions without your human partner's permission.
