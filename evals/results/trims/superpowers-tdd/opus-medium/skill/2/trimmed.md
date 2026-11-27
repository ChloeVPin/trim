---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first. Watch it fail. Write minimal code to pass. If you didn't watch the test fail, you don't know if it tests the right thing.

## When to Use

Always: new features, bug fixes, refactoring, behavior changes. When fixing a bug, first write a failing test that reproduces it. Never fix bugs without a test. Code with no existing tests is no exception: add tests for it.

Exceptions (ask your human partner): throwaway prototypes, generated code, configuration files.

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

Implement fresh from tests. Period. If you need to explore first, throw the exploration away and start with TDD.

No exceptions without your human partner's permission.

## Red-Green-Refactor

### RED - Write Failing Test

Write one minimal test showing what should happen: one behavior, a clear name that describes the behavior, real code (no mocks unless unavoidable). "and" in the name? Split it.

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

When writing or changing any test, read [writing-good-tests.md](writing-good-tests.md) for the rules that keep tests honest:
- Name the production change that would make the test fail — before writing it
- Assert on real behavior, never on mock behavior
- Keep test-only code in test utilities, out of production classes
- Understand a dependency's side effects before mocking it

### Verify RED - Watch It Fail

Never skip this step.

```bash
npm test path/to/test.test.ts
```

Confirm the test fails (not errors), with the expected message, because the feature is missing (not a typo).

**Test passes?** You're testing existing behavior. Fix test.

**Test errors?** Fix error, re-run until it fails correctly.

### GREEN - Minimal Code

Write the simplest code that passes the test. Don't add features or options, refactor other code, or "improve" beyond the test.

### Verify GREEN - Watch It Pass

Confirm the test passes, other tests still pass, and output is pristine (no errors, warnings).

**Test fails?** Fix code, not test.

**Other tests fail?** Fix now.

**"Other tests" means the project's suite, not just your file.** A
green run of the test you wrote is not a green suite. Before you call
the change done, run the project's test command (bare `pytest`,
`npm test`, `cargo test` — whatever the repo uses) even when your task
named only one test file. A scope statement in your task bounds the
deliverable, not your verification. Any failure that run shows —
including one you didn't cause — goes in your report by name; a red
test you watched scroll past and didn't mention is a report falsified
by omission.

### REFACTOR - Clean Up

After green only: remove duplication, improve names, extract helpers. Keep tests green. Don't add behavior.

Then write the next failing test for the next feature.

## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## When Stuck

Don't know how to test? Write the wished-for API and the assertion first, or ask your human partner. A test that is hard to write usually means the design is too complicated or too coupled; simplify the interface rather than the test.
