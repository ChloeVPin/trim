I saved the shorter version as `trimmed.md`. It's about 330 lines shorter than the original's ~60 lines, and I didn't change `instructions.md`.

**Most of the length came from repetition and emphatic wording:**
- **The same rule appears in several forms.** "No code before a failing test, delete it if you did" shows up as the Iron Law, the Red Flags list, the rationalizations table, the checklist, the Final Rule and "When to Use." I kept it once, with the reason behind it.
- **Lists of excuses to argue against.** The 10-row rationalizations table and 13-item Red Flags list are written to stop a model from talking itself out of the rule. Opus 5.5 follows a rule with a stated reason more reliably, so one paragraph on why test-first matters does that job. Lines like "Violating the letter of the rules…", "Delete means delete", "MANDATORY. Never skip." and "Period." add pressure but no information.
- **Content that repeats the text.** The Graphviz diagram restates the cycle, the "Good Tests" table repeats the test requirements, and the checklist repeats the cycle steps.
- **Examples.** The original had four example blocks, two good and two bad. I kept one short red/green example.

**Kept as-is in substance:**
- The frontmatter (`name` and `description`), so the skill still triggers the same way.
- The red → verify red → green → verify green → refactor cycle, including what counts as failing correctly: it must fail rather than error, for the expected reason, and not because of a typo.
- Deleting code written before its test, and that spikes are fine if you throw them away.
- Running the full suite before calling the work done, and reporting every failure by name, including ones you didn't cause. This is the most specific instruction in the file, so I didn't shorten it.
- The exceptions that need your human partner's approval.
- Bug fixes start with a test that reproduces the bug.
- The link to `writing-good-tests.md` and its key rules.
- The "when stuck" advice, rewritten as a short list.

**Dropped:**
- The checklist item "every new function/method has a test" and the explicit "edge cases and errors covered" item.
- The table rows "existing code has no tests → add tests" and "TDD will slow me down."

If you want any of these back, each is a one-line addition.