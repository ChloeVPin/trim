I saved the proposed version as `trimmed.md`. I didn't change `instructions.md`.

**Target model:** `claude-opus-5-5`, which you named. Its profile was tested at medium effort.

**Length:** about 540 words before and about 435 after, roughly 20% shorter. I had no tool to count words here, so both figures are hand estimates.

## Changes

1. **Cut "Take a step back and think step-by-step…"** For Opus 5.5, removing "think carefully" lines made replies start sooner with no clear loss in quality.
2. **Cut "Ensure you follow ALL these instructions."** It adds nothing, and on current Claude models all-caps emphasis tends to make the model over-apply rules rather than follow them better.
3. **Combined the five "Write the X bullets as exactly 16 words" lines into one.** The rule is the same for all five sections, so this changes nothing.
4. **Cut lines that repeated another line:**
   - "Make sure you extract at least 20" (IDEAS)
   - "Extract at least 10 INSIGHTS" (the step already says 10 to 20)
   - "This should include any and all references…" (repeats "Extract all mentions…")
5. **Put the minimum counts into the steps.** Your file gave two counts for several sections that disagreed:
   - IDEAS said "20 to 50" in the steps and "at least 25" in the output rules. The new version says **25 to 50**.
   - QUOTES, HABITS, FACTS and RECOMMENDATIONS said "15 to 30" in the steps and "at least 20" in the output rules. The new version says **20 to 30**.

   Each new range is the only one that satisfies both of your lines, so the rules haven't changed. They just no longer contradict each other. **Please check these ranges match what you meant.**
6. **Small wording fixes:** "affect" to "effect", "less than" to "fewer than", and "You use bulleted lists for output" to "Use bulleted lists".

## Kept, and why

- **All the counts, word limits, section names, the 25-word summary and the 15-word takeaway.** The model can't guess these.
- **The list of topics, the HABITS examples and "valid facts about the greater world".** These set what the model looks for.
- **The output rules:** Markdown only, no warnings or notes, no repeats, no matching openings, exact quote text with the speaker's name.

## For you to decide

- **REFERENCES:** your file asked for "all" references and also for "at least 20 items" in the other sections. When a talk has fewer than 20 references, those two clash. I kept "all", so the model won't make up references to reach 20.
- **Colons in section names:** IDEAS:, QUOTES: and FACTS: include a colon, but the other section names don't. I kept them exactly as written because the model may copy the colons into its headings. Removing them would make the headings consistent.
- **The "IDENTITY and PURPOSE" heading:** you could drop it and save about 3 words. I kept it because it does no harm.