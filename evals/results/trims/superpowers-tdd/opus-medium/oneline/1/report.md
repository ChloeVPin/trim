I saved a shorter version as `trimmed.md`, about 50 lines compared with 330 in the original. `instructions.md` is unchanged.

**What I cut, and why:**
- **The rationalizations table, the "Red Flags" list and the "Final Rule".** All three say "don't skip writing the test first" a dozen times over. Opus 5.5 follows a rule that's stated once with its reason, so I folded that reason ("a test you never saw fail proves nothing") into the opening line.
- **The capitalised and emphatic phrasing.** Lines like "MANDATORY. Never skip.", "Delete means delete" and "Violating the letter…" tend to make a capable model apply the rule too rigidly. The rules are still there, written in a normal tone.
- **The diagram of the cycle.** It's replaced by a numbered list that carries the same steps and checks.
- **The code examples.** The good/bad pairs and the empty-email bug-fix walkthrough showed things the model already knows. Their lessons are kept as single lines: minimal code, no extra options, real behavior rather than mocks.
- **Duplicate sections.** "Debugging Integration" is now one sentence under Scope. "When Stuck" and the "Good Tests" table are merged into "Writing good tests". The checklist went from 8 items to 4 by combining overlapping ones.

**What I kept:**
- The core cycle (write the test, watch it fail, write minimal code, watch it pass, refactor), including checking that the test fails for the right reason.
- The rule to delete production code written before its test.
- The exceptions, which still require asking the user before skipping TDD.
- The pointer to `writing-good-tests.md` and its four key rules.
- The rule to run the whole test suite and report every failure by name, kept almost word for word. It's the most important part of the file because it stops a common mistake: running only the one test you wrote and reporting success.

**One thing to decide:** I left out the sample `npm test path/to/test.test.ts` commands. If you want the file to name a particular test runner, add that back.