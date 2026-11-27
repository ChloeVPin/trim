---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

Write the test first, watch it fail, then write the minimal code that makes it pass. If you never saw a test fail, you don't know whether it can catch the bug it's meant to catch.

## Scope

Use TDD for new features, bug fixes, refactoring, and behavior changes. Bugs count too: before you fix one, write a failing test that reproduces it.

Throwaway prototypes, generated code, and configuration files may be exempt, but ask the user before you skip TDD.

If you wrote production code before its test, delete it and rebuild it from tests. Don't keep it as a reference or adapt it. A test written against existing code passes immediately, so it proves nothing. Exploratory spikes are fine as long as you throw them away afterwards.

## The cycle

1. **Red.** Write one minimal test for one behavior. Give it a name that describes the behavior. Use real code, and mock only when you can't avoid it.
2. **Verify red.** Run the test. It must *fail* (not error out), and it must fail for the expected reason: the feature is missing, not a typo or a setup problem. If it passes, it's testing behavior that already exists, so fix the test.
3. **Green.** Write the simplest code that passes. Don't add options, features, or unrelated refactors the test doesn't ask for.
4. **Verify green.** Run the test and confirm that it passes and the output is clean (no errors or warnings). If it fails, fix the code, not the test.
5. **Refactor.** Only once everything is green: remove duplication, improve names, extract helpers. Keep the tests green and add no behavior.
6. Repeat for the next behavior.

**Verification means the project's whole suite, not just your file.** Before you call the change done, run the project's test command (bare `pytest`, `npm test`, `cargo test`, or whatever the repo uses), even if your task named only one test file. The task's scope limits what you deliver, not what you verify. Name every failure in your report, including ones you didn't cause. Leaving out a failing test you saw makes the report false.

## Writing good tests

When writing or changing any test, read [writing-good-tests.md](writing-good-tests.md). Its key rules:
- Before writing a test, name the production change that would make it fail
- Assert on real behavior, not on mock behavior
- Keep test-only code in test utilities, not in production classes
- Understand a dependency's side effects before you mock it

If "and" appears in a test name, split the test. A test that's hard to write usually points to a design problem. Heavy mocking suggests coupling (try dependency injection), and a huge setup suggests the interface needs simplifying. When you're unsure how to test something, write the assertion for the API you wish you had first.

## Before marking work complete

- Every new function or method has a test that you watched fail for the expected reason
- Each test was passed by minimal code
- The full suite passes with clean output, or you reported each failure by name
- Edge cases and error paths are covered
