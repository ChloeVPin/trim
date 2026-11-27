I saved the proposed version as `trimmed.md`. I didn't change `instructions.md`.

**Target model:** `claude-opus-5-5`, as you named it. Its profile has been tested at medium effort.

**Words:** about 1,700 before and about 900 after. These are estimates, because I had no tool to count words in this session.

## Changes and reasons

| Cut or changed | Reason |
|---|---|
| "Overview" and "When to Use" headings; the four "Always" bullets became one line | Same content, shorter. |
| "Thinking 'skip TDD just this once'? Stop. That's rationalization." | The Iron Law right below says the same thing. |
| The Graphviz `dot` diagram of the cycle | It repeats the RED / Verify / GREEN / REFACTOR text under it. |
| "**MANDATORY. Never skip.**" and "**MANDATORY.**" | The profile says capitals and forceful emphasis now make this model over-apply rules, and plain wording works. The step itself stays ("Always run it"). |
| The two `npm test path/to/test.test.ts` snippets | They're placeholders, not real project commands. The suite paragraph you kept already says to use whatever command the repo uses. |
| GREEN's Good/Bad code examples | One line now covers them: "simplest code… no options, features or refactors beyond what the test requires." I kept the RED Good/Bad pair, which shows what a good test looks like. |
| "Common Rationalizations" table (10 rows) | Shrunk to one "Why" paragraph with the reasons that add something: tests written after pass at once and prove nothing, sunk cost, explore and then throw it away, add tests to untested code. The profile says a rule with its reason works better than repeated argument. |
| "Red Flags" list and "All of these mean: Delete code. Start over" | It repeats the Iron Law. It also clashed with Verify RED: "Test passes immediately" said delete the code here, but fix the test there. The Iron Law's delete rule stays word for word. |
| "Example: Bug Fix" | It walks through the same cycle again. Its one rule ("never fix bugs without a test") is in the new short "Bugs" section. |
| Verification Checklist and "Can't check all boxes? … Start over." | Six of the eight items repeat earlier steps. The two new ones ("every new function/method has a test", "edge cases and errors covered") moved to Good Tests. |
| "Final Rule" block | It repeats the Iron Law. Its last line about permission is kept. |
| Good Tests table | Became bullets. The Bad-column examples are dropped. |

## Kept as written, and why

- **Rules about deleting code and getting approval:** the Iron Law, its "No exceptions" list, "Exceptions (ask your human partner)" and "No exceptions without your human partner's permission." These cover deleting work and approvals, so I didn't touch them.
- **The full-suite paragraph, word for word:** it says to run the whole suite, not just your test file, and to name every failure in your report, including ones you didn't cause. That's your own choice about reporting.
- **The link to `writing-good-tests.md` and its four bullets**, the frontmatter `name`/`description` (Claude uses the description to decide when to apply the skill), and the When Stuck table.
- **The watch-it-fail and watch-it-pass checks.** The profile says self-check lines can go for Opus 5, but it hasn't confirmed that for 5.5. These checks are also the core of TDD, not a general reminder to double-check.

## Your call

- **"Violating the letter of the rules is violating the spirit of the rules."** I kept it. Opus 5.5 already follows wording closely, so it may not change anything, but it's your stated position on strictness. Cutting it saves about 12 words.
- **The "Why" paragraph.** If the Iron Law alone is enough for you, cutting it saves about 75 more words. Without it, the model loses the reasons behind the rule, and the profile says rules with reasons generalise better.