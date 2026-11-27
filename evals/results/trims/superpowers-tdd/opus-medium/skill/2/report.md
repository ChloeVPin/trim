I saved the proposed version as `trimmed.md` and left `instructions.md` unchanged.

**Target model:** `claude-opus-5-5`, as you named it. The profile for this model has been tested at medium effort.

**Length:** roughly 1,550 words before and 830 after, about a 45% cut. These are estimates, because I don't have a word-count tool in this session.

## Changes

| Cut or merged | Reason |
|---|---|
| The diagram of the red-green-refactor cycle | It repeats the section headings below it. |
| The "Common Rationalizations" table and the "Red Flags" list | They argue for rules already stated in the Iron Law. The profile says this kind of persuasive emphasis makes Opus 5.5 over-apply rules. I kept the two rows that make real decisions: throw away exploration code, and add tests to existing untested code. |
| "Violating the letter…", "Thinking 'skip TDD just this once'? Stop." | These are emphasis lines that add no instruction. |
| The "Good Tests" table | I folded it into the RED requirements, and kept the "'and' in the name? Split it" rule. |
| The Good/Bad examples in GREEN (the over-engineered retry function) | The sentence "Don't add features or options…" already says this. I kept the RED examples because they show the no-mocks rule in practice. |
| "Example: Bug Fix" | It walks through the same cycle again. I kept its rule ("write a failing test that reproduces it") and merged it into "When to Use". |
| The "Debugging Integration" and "Final Rule" sections | Their content is now in "When to Use" and the Iron Law. "Never fix bugs without a test" and "No exceptions without your human partner's permission" stay word for word. |
| The "When Stuck" table | I cut it to one line: keep the "ask your human partner" choice and the point that a test that's hard to write signals bad design. The rest is general advice Opus already follows. |
| "**MANDATORY.**" in capitals | Changed to plain "Never skip this step." The profile says capitals now cause over-application. The step itself stays. |
| Bulleted lists in Verify RED, Verify GREEN and REFACTOR | Turned into sentences with nothing removed. |

## Kept exactly as written
- **The Iron Law and "Delete it. Start over"**, including all four "No exceptions" bullets. These rules make the model delete code, so I left them untouched.
- **The paragraph about running the full test suite.** It's a specific choice you made (run the repo's whole suite even if the task names only one file, and name every failure in the report), not a generic "double-check" line.
- **The list of exceptions where the model should ask its human partner first**, and the permission rule.
- **The link to `writing-good-tests.md` and its four bullets.** That file isn't in this sandbox, so check that it's still next to the skill where it's actually installed.
- **The frontmatter, the `npm test` command, and the RED examples.**

## Flagged for you to decide
- **Verification checklist (about 75 words).** Six of its eight items repeat earlier sections. The profile says self-check lines like these were cut for Opus 5, but it's unverified whether that holds for 5.5. The checklist also ends with "Start over", which leads to deleting code, so I kept it whole. If you agree to trim it to the two new items ("every new function/method has a test" and "edge cases and errors covered") plus the closing line, it saves about 50 words.
- **The RED Good/Bad examples (about 90 words).** They repeat the no-mocks requirement. Opus would probably manage without them, but examples steer it strongly, so I kept them.