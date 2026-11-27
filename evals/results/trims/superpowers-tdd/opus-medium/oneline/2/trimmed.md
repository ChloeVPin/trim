---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first, watch it fail, then write the minimal code that makes it pass. The reason: a test you never saw fail hasn't shown it can catch the bug. Tests written after the code tend to pass right away, check the cases you remembered instead of the ones you'd have found, and end up testing the implementation instead of the behavior.

Use this for new features, bug fixes, refactoring, and behavior changes. Throwaway prototypes, generated code, and configuration files may be exceptions; ask your human partner before skipping TDD for them.

If you wrote production code before its test, delete it and rebuild it from the tests. Don't keep it as a reference or adapt it, because that turns into writing tests after the code. Exploratory spikes are fine; throw them away before you start the TDD cycle.

## The cycle

1. **Red: write one failing test.** Test one behavior, give it a name that describes that behavior, and exercise real code. Use mocks only when you can't avoid them.
2. **Verify red.** Run the test. It must *fail* (not error), with the failure message you expected, because the feature is missing and not because of a typo. If it passes, it's testing existing behavior, so fix the test. If it errors, fix the error and rerun.
3. **Green: write the simplest code that passes.** Don't add options, features, or unrelated refactors the test doesn't require.
4. **Verify green.** The new test passes and the output has no errors or warnings. If it fails, fix the code, not the test.
5. **Refactor** only while green: remove duplication, improve names, extract helpers. Don't add behavior, and keep the tests green.
6. Repeat for the next behavior.

Before calling the work done, run the project's full test command (`pytest`, `npm test`, `cargo test`, or whatever the repo uses), even if your task named only one test file. The task's scope limits what you deliver, not what you verify. Report every failure from that run by name, including failures you didn't cause.

Bug fixes follow the same cycle: first write a test that reproduces the bug and watch it fail, then fix the code. The test proves the fix and guards against the bug coming back.

## Example

```typescript
// Red: write the test; it fails with "expected 'Email required', got undefined"
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});

// Green: minimal fix
function submitForm(data: FormData) {
  if (!data.email?.trim()) return { error: 'Email required' };
  // ...
}
```

## Test quality

Before writing or changing any test, read [writing-good-tests.md](writing-good-tests.md). In short:
- Before you write the test, name the production change that would make it fail.
- Assert on real behavior, never on what a mock did.
- Keep test-only code in test utilities, not in production classes.
- Understand a dependency's side effects before you mock it.
- If a test name contains "and", split it into separate tests.

## When testing is hard

A test that's hard to write usually points to a design problem:
- If you don't know how to test something, write the API you wish you had, starting with the assertion, or ask your human partner.
- If you'd have to mock everything, the code is too coupled; use dependency injection.
- If the setup is huge, extract helpers. If it's still complex after that, simplify the design.
