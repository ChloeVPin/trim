I saved the shorter version to `/root/trim-sbx/f7bb871553fd/trimmed.md`. `instructions.md` is unchanged.

**Audit of instructions.md**

- **Broken reference:** It points to `writing-good-tests.md`, which is not in the directory. I inlined those four rules so the file works on its own.
- **Repetition:** The Iron Law appears in four places. The red-flags list, the rationalizations table, and the checklist overlap heavily.
- **Redundant diagram:** The GraphViz diagram repeats the prose cycle. Haiku follows a numbered list more reliably anyway.
- **Duplicate examples:** The retry example and the empty-email bug example teach the same pattern. I kept one.
- **Rhetoric:** Lines like "Period." and "Stop." add length without adding rules. I kept the rules and dropped the emphasis.
- **Stack-specific:** `npm test` is hard-coded. I replaced it with "the repo's own test command" and listed examples.
- **Wording:** "your human partner" is now "the user," which fits this setting.

**What the trimmed version keeps**

- The Iron Law and the rule to delete code written before its test.
- The RED → GREEN → REFACTOR steps, each with its verify step.
- The full-suite requirement, and the rule to report failures by name, including ones you did not cause.
- The bug-fix rule and the pre-completion checklist.
- The list of rationalizations to reject.

It is about 105 lines, down from 331.

**Choices I made that you may want to change**

- I kept the rule that code written before its test must be deleted. The original is strict on this, and I did not soften it.
- The exceptions (prototypes, generated code, config) are still listed and still need the user's permission.