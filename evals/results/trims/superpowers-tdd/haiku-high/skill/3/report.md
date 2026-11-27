The proposed version is in `/root/trim-sbx/a0b5fe5c5acb/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile (tested at high effort). I did not run any evals, so the cuts rest on the profile and the maker's guidance, not on a test against this file.

**2. Length:** about 1,850 words before and about 850 after. These are estimates, since I have no word-count tool here.

**3. Changes**

- **Removed the Common Rationalizations table and the Red Flags list (about 450 words).** Most rows repeat the Iron Law, Verify RED and the Final Rule. This is the cut I'd most like you to look at. If the model has skipped tests under pressure, restore the table.
- **Removed the Red-Green-Refactor graphviz diagram (about 140 words).** The section text already gives every branch: passes, fails, errors, stay green.
- **Removed the Good Tests table.** Its rows restate the RED requirements. The four rules under it are kept as a short "Writing Tests" list.
- **Removed the Bad examples for RED and GREEN.** The requirements lists and the "Don't add features" line already say what they show.
- **Removed "MANDATORY" and "Never skip", and the "Violating the letter…" line.** Emphasis like this over-applies on Haiku, and the Iron Law already covers the point.
- **Shortened Verify GREEN** to the same instruction: run the project's full test command before reporting done, and name every failure in the report. This is the check the Haiku profile asks coding agents to keep. I dropped the extra rhetoric around it.
- **Merged Repeat, Debugging Integration and the Bug Fix example** into shorter lines. The example keeps the full RED/GREEN/REFACTOR flow.
- **Turned the Verification Checklist into a few lines.** The checks are the same. "Can't check all boxes? You skipped TDD. Start over." is kept as written.
- **Changed "Think 'skip TDD' → Stop" to a single sentence** that merges into the exceptions line.

**Kept as written:**
- The frontmatter, which is the skill's trigger.
- The Iron Law, including its "No exceptions" list (delete, don't adapt, don't look at it, "Period"). Deletion rules stay exactly as written.
- The Final Rule, including "without your human partner's permission". This is an approval condition.
- The "ask your human partner" exceptions and the "start over" remedy.
- The RED and GREEN Good examples, which set the style.
- The Verify RED and Verify GREEN commands and their confirmation steps.
- The "When Stuck" guidance, compressed to four lines.

**Things to check:**

- **Unsure, cut anyway:** the two retryOperation Good examples (about 100 words). The Bug Fix example also shows the procedure, so they could go too.
- **Missing file:** the original points to `writing-good-tests.md`, which is not in this workspace. I inlined its four rules so the skill does not depend on that file. If the file exists in your skill bundle, you can point back to it instead.
- **Wording:** I kept "your human partner" as you wrote it, even though a model may read it as "the user".