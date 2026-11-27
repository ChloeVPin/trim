I wrote the proposed version to `/root/trim-sbx/16f3f707ef73/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. For Haiku the profile calls for keeping procedures and examples and cutting only repeats and generic advice, so the cuts here are modest.

**2. Length:** about 1,500 words before and about 1,300 after, roughly 13% shorter. These are estimates because I have no word-count tool in this session.

**3. Changes**
- **Removed** "Thinking 'skip TDD just this once'? Stop. That's rationalization." It repeats the rationalizations table and the Red Flags list.
- **Removed the "Good Tests" table.** Its "Minimal" and "Clear" rows repeat the Requirements list and the Good/Bad examples. The "Shows intent" row is dropped, which is a small content change. Say if you want it back.
- **Removed the "MANDATORY." labels** (two). "Never skip." stays under Verify RED.
- **Tightened the "Other tests" paragraph.** Removed the "report falsified by omission" sentence. The rule to report every failure by name stays.
- **Red Flags:** removed the quoted excuses that the table already covers. Kept the state triggers and added a pointer to the table.
- **Removed the Final Rule code block,** which repeats the Iron Law. Kept the sentence "No exceptions without your human partner's permission."

**4. Kept, and why**
- **Iron Law, including "Delete it" and the no-exceptions list.** It is a deletion rule, so it stays exactly as written.
- **"Ask your human partner" exceptions and the permission sentence.** These are approval rules.
- **Good/Bad code examples and the Bug Fix walkthrough.** These carry the task procedure, which the profile says Haiku needs.
- **Run-the-whole-suite rule and the verification checklist.** These are the "run a real check before reporting done" line the profile asks for in coding agents. I added nothing new.

**Unsure, kept and flagged.** Dropping any of these would save the following:
- **Common Rationalizations table,** about 330 words. This is the largest cut available. It guards against skipping TDD, so I kept it.
- **Dot diagram,** about 120 words. It duplicates the RED/GREEN/REFACTOR text.
- **Verification checklist,** about 70 words. It repeats the Verify steps.

**Missing file.** The Good Tests section links to `writing-good-tests.md`, which is not in this workspace. I kept the link and its four rules. Check that the file exists in the real skill before you ship this, or the link is dead.