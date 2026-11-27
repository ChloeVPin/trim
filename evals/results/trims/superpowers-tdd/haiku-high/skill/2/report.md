Saved the proposed version to `/root/trim-sbx/1787bf0e5e39/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named in your request. The profile is tested at high effort. For Haiku, the profile says to cut generic advice and repeated emphasis, and to keep procedures, examples, and the coding-agent "run a real check" line.

**2. Words:** about 1,850 before and about 1,450 after, roughly 20% shorter. These are estimates because I had no shell to count with.

**3. Changes**

- **Removed the Graphviz diagram** (Red-Green-Refactor). It repeats the RED, GREEN, REFACTOR and Repeat sections. This is the largest cut. Restore it if you want a visual.
- **Removed the "Requirements" list under RED.** It restates the Good Tests table and the checklist.
- **Removed the intro line "Thinking 'skip TDD just this once'? Stop."** The Red Flags list already has "Rationalizing 'just this once'".
- **Removed four Red Flags that duplicate table rows:** "I already manually tested it", "Tests after achieve the same purpose", "It's about spirit not ritual", "Tests added 'later'".
- **Removed two rationalization rows.** "Test hard = design unclear" repeats When Stuck. "Manual test faster" repeats "Already manually tested".
- **Shortened the "I'll test after" reality cell.** The meaning is the same.
- **Replaced "MANDATORY" with "Never skip this step."** Your profile says capitals over-trigger on Claude models. This is the same rule in plain wording.
- **Shortened the "other tests" paragraph.** I kept the rule and the reason that a task's scope does not limit verification. I dropped the "falsified by omission" line and reworded it to "Leaving out a failure you saw makes the report false."
- **Removed the Final Rule code block.** It repeats the Iron Law. I kept the sentence "No exceptions without your human partner's permission."

**4. Kept on purpose**

- **Deletion rules, unchanged.** The Iron Law block, the "Deleting X hours" row, and the "Keep as reference" row and Red Flag all guard deleting code. Your rules say those stay as written.
- **Examples and procedures:** the RED and GREEN Good/Bad examples, the Bug Fix walkthrough, the verify steps and their commands, and the When Stuck table.
- **The "run the full suite before reporting done" paragraph.** It is the coding-agent check your profile says to keep.
- **Verification Checklist.** It repeats earlier steps, but it is the done-gate. Cut it if you want a shorter file.

**Flags for you to decide**

- **`writing-good-tests.md` was not found** anywhere under `/root/trim-sbx`. The link and its four bullets are kept as written. If the file exists in your repo, it is not reachable from here. If it is gone, the link and bullets need fixing.
- **"Violating the letter of the rules is violating the spirit of the rules."** I kept this but it is unsure. It is generic, and cutting it would save one line.