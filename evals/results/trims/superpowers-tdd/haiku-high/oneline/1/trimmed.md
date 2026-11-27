---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

**Rule:** Write production code only after a test for it has failed. If you did not see the test fail, you do not know it tests the right thing.

## When to Use

- Always: new features, bug fixes, refactors, behavior changes.
- Exceptions (confirm with the user before skipping): throwaway prototypes, generated code, configuration files.

## The Cycle

1. **RED: write one failing test.** Test one behavior, with a clear name. Use real code. Mock only when unavoidable.
2. **Run it and confirm it fails for the right reason.** The failure must be because the feature is missing, not a typo, import error, or syntax error.
   - It passes: it tests existing behavior. Fix the test.
   - It errors: fix the error and re-run until it fails correctly.
3. **GREEN: write the simplest code that passes.** Do not add features, options, or changes outside the test.
4. **Run it and confirm it passes.** Other tests must still pass, and the output must have no errors or warnings.
   - If the test fails, fix the code, not the test.
5. **REFACTOR (only when green):** remove duplication, improve names, extract helpers. Keep tests green and add no behavior.
6. Repeat for the next behavior.

## Code Written Before Its Test

Delete it. Do not keep it as reference or adapt it while writing the test. Re-implement from the test.

## Test Quality

- One behavior per test. If the name contains "and", split the test.
- Name describes the behavior. Not `test1` or `retry works`.
- Assert on real behavior, not on mock calls.
- Before writing a test, name the production change that would make it fail.
- Before mocking a dependency, check its side effects.
- Keep test-only helpers in test utilities, not in production classes.
- If setup is huge or mocking is needed everywhere, the design is too coupled. Simplify the interface or inject the dependency.

## Bugs

Write a failing test that reproduces the bug. Then fix the bug. Never fix a bug without a test.

## Unsure How to Test Something?

Write the assertion for the API you wish existed, then build toward it. Ask the user only if you remain blocked.

## Before Reporting Done

- [ ] Every new function or method has a test.
- [ ] You saw each test fail for the expected reason before implementing.
- [ ] Each test was made to pass with minimal code.
- [ ] You ran the project's full test command (for example `npm test`, `pytest`, `cargo test`), not only the new test file.
- [ ] All tests pass, and the output has no errors or warnings.
- [ ] Edge cases and error paths are covered.

Report every failing test by name, including failures you did not cause. If any box is unchecked, the work is not done. Go back and add the missing test.
