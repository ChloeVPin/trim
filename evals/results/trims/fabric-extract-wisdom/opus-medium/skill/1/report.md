I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Words:** about 537 before and about 438 after, roughly 18% shorter. I had no word-count tool here, so I counted by hand and these are estimates.

## What I changed

1. **Cut "Take a step back and think step-by-step…"** For Opus 5.5, the model's maker says instructions to think carefully before answering can be removed. Replies start sooner with no clear quality loss.
2. **Combined the five "Write the X bullets as exactly 16 words" lines into one.** The rule is the same and so are the sections.
3. **Cut "Extract at least 10 INSIGHTS."** It repeats the "10 to 20" already in the INSIGHTS step.
4. **Cut "Make sure you extract at least 20" from the IDEAS step.** It repeats the "20 to 50" in the same line.
5. **Cut "This should include any and all references…" from REFERENCES.** "Extract all mentions" already says this.
6. **Cut "Ensure you follow ALL these instructions."** It adds nothing new, and the profile says capitalised emphasis now makes this model over-apply rules.
7. **Shortened two lines without changing their meaning:**
   - INSIGHTS now says "drawing on the raw input and the IDEAS above" instead of "from the input and from a combination of the raw input and the IDEAS above."
   - The TAKEAWAY line now uses a colon instead of "This should be…"

## What I kept and why

- **All counts, ranges and word limits** (25-word summary, 15-word takeaway, 16-word bullets, exact quote text with the speaker's name). These are format choices you made.
- **The list of interests in IDENTITY.** It decides what gets picked, and the model can't guess it.
- **The rules on output and style:** Markdown only, bullets rather than numbers, no warnings, no repeats, no repeated opening words.
- **The section headings exactly as written, including the colons in `IDEAS:.`, `QUOTES:.` and `FACTS:.`** The output headings may depend on them.
- **The `INPUT:` template slot.**

## For you to decide

- **Conflicting minimums.** The trimmed file still has these conflicts, because only you can say which number you want. Opus 5.5 follows wording closely, so conflicting numbers will make output vary between runs.
  - IDEAS says "20 to 50" in STEPS but "at least 25" under OUTPUT INSTRUCTIONS.
  - "At least 20 items for the other output sections" conflicts with the "15 to 30" ranges for QUOTES, HABITS, FACTS and RECOMMENDATIONS. Read literally, it also applies to SUMMARY and the one-sentence TAKEAWAY, which can't have 20 items.

  If you put the minimums you want into the ranges in STEPS (for example "25 to 50", "20 to 30") and delete both "at least" lines, the file gets about 19 words shorter and the conflict goes away.
- **Small text issues I left alone:** "its affect on humans" should be "effect", and "less than 50" would normally be "fewer than 50". Neither changes behaviour much.