I saved the proposed version to `/root/trim-sbx/86c800fd9de7/trimmed.md`. `instructions.md` is unchanged. The original is 331 lines and the new file is about 85.

**Audit of instructions.md**

- **Dangling reference.** It points to `writing-good-tests.md`, which does not exist in this directory. The four rules from that section are now inline.
- **Repetition.** The Iron Law, the Final Rule, the Red Flags list, and the "All of these mean" line all restate the same rule. The trimmed version states it once.
- **Rationalization table.** It has 14 rows. A smaller model follows explicit rules better than a list of excuses to reject, so I dropped the table.
- **Graphviz diagram.** The DOT graph repeats the numbered cycle. I replaced it with a numbered list.
- **Examples.** The two good/bad code pairs and the bug-fix walkthrough are long. The rules they illustrate are kept in plain text.
- **"Ask your human partner."** This appears several times. For an agent working autonomously, I changed it to "ask the user only if still blocked."
- **Verification.** The rule to run the full project suite and report every failing test by name is the most important operational rule, so it is kept and stated clearly.

**Choices you may want to change**

- **Deletion.** I kept "Delete it" for code written before its test, as the original says. In a real repo this discards work. If you would rather have it set aside, for example with `git stash`, change that line.
- **Exceptions.** I kept the original exception list but added "confirm with the user before skipping."
- **Length.** I cut about 75%. If Haiku misses a rule, the first place to look is the "Test Quality" section.

I have not tested the trimmed file against Haiku 5.5 on a real task. That would show whether the shorter version still produces red-then-green behavior.