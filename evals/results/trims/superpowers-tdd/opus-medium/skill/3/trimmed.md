---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing. Tests written after the code pass immediately, which proves nothing.

## When to Use

**Always:**
- New features
- Bug fixes (write a failing test that reproduces the bug first)
- Refactoring
- Behavior changes
- Changes to existing code with no tests: add tests for it

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

Exploratory code is fine, but throw it away and start with TDD.

## Red-Green-Refactor

### RED - Write Failing Test

Write one minimal test showing what should happen:
- One behavior ("and" in the name? Split it.)
- Clear name that describes the behavior
- Real code (no mocks unless unavoidable)

### Verify RED - Watch It Fail

Never skip this.

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test fails (not errors)
- Failure message is expected
- Fails because feature missing (not typos)

**Test passes?** You're testing existing behavior. Fix test.

**Test errors?** Fix error, re-run until it fails correctly.

### GREEN - Minimal Code

Write the simplest code that passes the test. Don't add features, refactor other code, or "improve" beyond the test.

### Verify GREEN - Watch It Pass

Confirm:
- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

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

After green only. Keep tests green. Don't add behavior.

Then write the next failing test for the next behavior.

## Good Tests

When writing or changing any test, read [writing-good-tests.md](writing-good-tests.md) for the rules that keep tests honest:
- Name the production change that would make the test fail — before writing it
- Assert on real behavior, never on mock behavior
- Keep test-only code in test utilities, out of production classes
- Understand a dependency's side effects before mocking it

Before marking work complete, every new function/method has a test, and edge cases and errors are covered.

Don't know how to test something? Write the wished-for API and the assertion first, or ask your human partner. Hard to test usually means the design is too complicated or too coupled; simplify it.

No exceptions without your human partner's permission.
