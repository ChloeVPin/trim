I saved the proposed version to `/root/trim-sbx/02a9366a5a59/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. Its profile is tested at high effort, so these cuts are tested only at that setting.

**2. Length:** about 527 words before and about 451 after, a cut of roughly 14%. I have no shell tool to run `wc`, so these are my hand counts.

**3. Changes**

- **Cut** "Take a step back and think step-by-step about how to achieve the best possible results…" (20 words). It is generic advice that the STEPS already carry out. The Haiku profile says generic advice is not protected. If outputs start drifting from the procedure, this is the first line to restore.
- **Cut** "Ensure you follow ALL these instructions when creating your output." (10 words). It restates every other rule, and capitalised emphasis causes over-application on current Claude models.
- **Merged** the five separate "Write the X bullets as exactly 16 words" lines (IDEAS, INSIGHTS, RECOMMENDATIONS, HABITS, FACTS) into one line with the same rule (-31 words).
- **Cut** "Make sure you extract at least 20." from the IDEAS step (-7 words). The output section already requires at least 25, which satisfies it.
- **Cut** "Extract at least 10 INSIGHTS from the content." (-8 words). The INSIGHTS step already says 10 to 20.

**4. Kept, and why**

- Every STEPS entry, since they are the task procedure and the Haiku profile says to keep them.
- The HABITS examples, including "but aren't limited to" and "etc.", because they mark the list as open.
- All format rules (Markdown only, bullets not numbers, no notes, no repeats, no matching openings) and the INPUT header.
- I added nothing. The Haiku "keep or add" items (a check before reporting done, a rule that holds through a conversation, a line to keep working) apply to coding agents, chatbots and agents that stop early, and this is a single-pass extraction prompt.

**5. Needs your decision (I left these as written)**

- **Conflicting counts for non-IDEAS sections.** "Extract at least 20 items for the other output sections" clashes with the 15-to-30 ranges for QUOTES, HABITS, FACTS and RECOMMENDATIONS, where 15 is below 20. It also cannot apply to ONE-SENTENCE TAKEAWAY, which is a single sentence, or to REFERENCES, which has no count. Pick one range and name the sections the minimum applies to.
- **IDEAS range.** The step asks for 20 to 50 and the output section asks for at least 25. The 25 floor wins in practice, so you may want the step to say 25 to 50.
- **Typos, not changed:** "Extract the 15 to 30 of the most…" (RECOMMENDATIONS step, extra "the") and "its affect on humans" (should probably be "effect").