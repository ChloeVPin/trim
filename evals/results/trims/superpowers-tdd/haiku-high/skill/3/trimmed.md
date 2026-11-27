---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

## When to Use

**Always:** new features, bug fixes, refactoring, behavior changes.

**Exceptions (ask your human partner):** throwaway prototypes, generated code, configuration files. Thinking "skip TDD just this once"? Stop.

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

## Red-Green-Refactor

For each behavior: RED, then GREEN, then REFACTOR. Then start the next failing test.

### RED - Write Failing Test

Write one minimal test showing what should happen.

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

Requirements:
- One behavior
- Clear name
- Real code (no mocks unless unavoidable)

### Verify RED - Watch It Fail

Run the test:

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test fails (not errors)
- Failure message is expected
- Fails because feature missing (not typos)

Test passes? You're testing existing behavior. Fix the test.
Test errors? Fix the error and re-run until it fails correctly.

### GREEN - Minimal Code

Write the simplest code that passes the test.

<Good>
```typescript
async function retryOperation<T>(fn: () => Promise<T>): Promise<T> {
  for (let i = 0; i < 3; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === 2) throw e;
    }
  }
  throw new Error('unreachable');
}
```
Just enough to pass
</Good>

Don't add features, refactor other code, or "improve" beyond the test.

### Verify GREEN - Watch It Pass

Run the same command. Confirm:
- Test passes
- Other tests still pass
- Output is clean (no errors, warnings)

Test fails? Fix the code, not the test. Other tests fail? Fix now.

"Other tests" means the project's whole suite. Before you call the change done, run the project's test command (bare `pytest`, `npm test`, `cargo test`, whatever the repo uses), even when your task named only one test file. Name every failure that run shows in your report, including ones you did not cause. A red test left out of the report makes the report false.

### REFACTOR - Clean Up

After green only: remove duplication, improve names, extract helpers. Keep tests green. Don't add behavior.

## Writing Tests

Before writing or changing any test:
- Name the production change that would make the test fail, before writing the test.
- Assert on real behavior, never on mock behavior.
- Keep test-only code in test utilities, out of production classes.
- Understand a dependency's side effects before mocking it.

## Example: Bug Fix

Bugs get a failing test that reproduces them before any fix. Never fix a bug without a test.

**Bug:** Empty email accepted

**RED**
```typescript
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});
```

**Verify RED**
```bash
$ npm test
FAIL: expected 'Email required', got undefined
```

**GREEN**
```typescript
function submitForm(data: FormData) {
  if (!data.email?.trim()) {
    return { error: 'Email required' };
  }
  // ...
}
```

**Verify GREEN**
```bash
$ npm test
PASS
```

**REFACTOR**
Extract validation for multiple fields if needed.

## When Stuck

- Don't know how to test: write the wished-for API and the assertion first, then ask your human partner.
- Test too complicated: simplify the interface.
- Must mock everything: inject dependencies.
- Test setup huge: extract helpers; if it is still complex, simplify the design.

## Verification Checklist

Before marking work complete, confirm:
- every new function or method has a test, and you watched each one fail for the expected reason (feature missing, not a typo);
- you wrote minimal code to pass each test;
- the project's test run passes with clean output;
- tests use real code (mocks only if unavoidable), and edge cases and errors are covered.

Can't confirm all of these? You skipped TDD. Start over.

## Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without your human partner's permission.
