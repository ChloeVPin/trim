I saved a shorter version as `trimmed.md`, about 85 lines compared with 330. `instructions.md` is unchanged.

**What I kept:**
- **The core rules:** write the test first, and delete any code written before its test.
- **The red-green-refactor cycle,** including what to check when the test fails and when it passes.
- **The full-suite requirement:** run the project's whole test command even if the task named one file, and report every failure by name, including ones you didn't cause. This is the most specific and useful rule in the file.
- **The link to `writing-good-tests.md`** with its four rules, plus "When stuck" and the final checklist (merged from eight items down to four).

**What I cut and why:**
- **The rationalizations table and the "Red Flags" list:** together about 25 lines that argue the same point over and over. Opus 5.5 follows a rule once it's told the reason, so I kept one sentence on why tests written afterwards prove nothing.
- **Capitals and emphasis** ("Iron Law", "MANDATORY", "Delete means delete", "No exceptions"): newer models tend to over-apply shouted rules. Plain wording plus a reason works better.
- **The dot diagram:** it repeated the numbered steps.
- **The email bug-fix example:** it showed the same cycle as the retry example, so a short "Bugs" section replaces it.
- **The "Final Rule" block:** a restatement of the core rule.
- **The bad-test and bad-code examples:** each became a one-line warning ("avoid vague names and tests that only check a mock"; "don't add configurable backoff").

**Small changes in behavior to check:**
- **Exceptions:** the original said to ask your human partner about prototypes, generated code and config files. The trimmed version says to ask whether TDD applies. That's a slightly softer wording of the same exceptions.
- **Exploration:** "Throw away exploration, start with TDD" was only a row in the rationalizations table. It's now an explicit rule in "When to use".
- **"Too simple to test" and "Existing code has no tests":** these cases are no longer spelled out. "Use it for new features, bug fixes, refactoring, and behavior changes" still covers them, but put a line back if you've seen the model skip tests on trivial changes or legacy code.