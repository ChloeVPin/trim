I saved the proposed version as `trimmed.md`. `instructions.md` hasn't been changed.

**1. Target model:** `claude-opus-5-5`. You named it, and it has a profile that was tested at medium effort.

**2. Word count:** about 1,650 words before and 560 after, so roughly a third of the original. These are estimates: I had no word-count tool here, only line counts (331 lines before, about 115 after).

**3. Changes and reasons**

| Cut or changed | Why |
|---|---|
| The dot diagram of the cycle | It repeats the RED, GREEN and REFACTOR sections step by step. |
| All the TypeScript Good/Bad examples and the "Bug Fix" walkthrough | They illustrate rules the prose already states ("one behavior, clear name, real code" and "don't add features beyond the test"). None of them sets a required output format, which is the one kind of example the profile says to keep. Examples also steer this model strongly toward copying them. |
| "Violating the letter…", "Thinking 'skip TDD just this once'? Stop.", "MANDATORY." | Opus 5.5 follows wording closely. Pressure language written to push older models into complying now makes it apply rules too broadly. "Never skip" stays, written plainly. |
| The "Common Rationalizations" table and the "Red Flags" list | These argue the case for TDD to a model that might resist it. Opus 5.5 doesn't need persuading, and a rule with its reason works better than a list of rebuttals. I kept the reason in one sentence under the core principle ("tests written after pass immediately, which proves nothing"). The two rows that were real decisions became rules: "add tests for existing code" and "throw away exploration". |
| The "Verification Checklist" | Most items repeat the Verify RED/GREEN steps. I kept the two new ones (every new function has a test; edge cases and errors covered). |
| "When Stuck" table | This is generic design advice the model already knows. I kept "write the wished-for API first" and "ask your human partner". |
| "Debugging Integration" and "Final Rule" diagram | "Debugging Integration" is folded into "Bug fixes" under When to Use. The "Final Rule" diagram repeats the Iron Law. I kept its permission line word for word. |
| Second `npm test` block and the REFACTOR bullet list | Duplicates. The full-suite paragraph already covers what to run at GREEN. |

**4. What I kept and why**
- **The frontmatter, unchanged.** The description decides when the skill gets triggered.
- **The Iron Law and the delete-and-start-over rules, word for word.** They tell the model to delete code, so they stay as you wrote them.
- **The exceptions and permission lines.** "Ask your human partner" and "No exceptions without your human partner's permission" are approval rules, kept with their conditions.
- **The "Other tests means the project's suite" paragraph, word for word.** It sets your rule for what to verify and how to report failures, including ones the model didn't cause.
- **The Verify RED/GREEN steps.** The profile does say to delete self-check lines, but that advice was written for Opus 5, isn't confirmed for 5.5, and only covers generic "double-check" reminders. Watching the test fail is the method itself, not a reminder to check.
- **The `writing-good-tests.md` reference and its four rules.** They point to a file and say what it's for.

**Flag:** the Rationalizations and Red Flags sections are the biggest single cut, about 400 words. If you've seen agents argue their way out of TDD in practice, add back a short Red Flags list, since that's cheaper than the full table.