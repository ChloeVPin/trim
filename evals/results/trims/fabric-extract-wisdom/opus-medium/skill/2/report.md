I saved the shorter version as `trimmed.md` and didn't touch `instructions.md`. One change needs your OK before you use it: I changed some of the counts (item 3 under Changes).

**Target model:** `claude-opus-5-5`, which you named. Its profile was tested at medium effort.

**Words:** about 537 before and 430 after, roughly 20% shorter. I counted by hand because I had no word-count tool, so both figures are estimates.

## Changes
1. **Cut "Take a step back and think step-by-step…"** For Opus 5.5, Anthropic says removing "think carefully" lines makes replies start sooner with no clear loss in quality.
2. **Cut "Ensure you follow ALL these instructions…"** It adds nothing new, and capitalised emphasis like this makes current Claude models apply rules too broadly.
3. **Merged the separate "at least N" lines into the ranges in STEPS. Please check this one.** The two parts of the original disagreed:
   - IDEAS said "20 to 50, at least 20" in one place and "at least 25" in another. It's now **25 to 50**.
   - QUOTES, HABITS, FACTS and RECOMMENDATIONS said "15 to 30", but "at least 20 items for the other output sections" set a higher minimum. They're now **20 to 30**.

   I kept the range that satisfies both versions. If you meant the lower numbers, change them back. As written, the "other output sections" line would also have applied to SUMMARY, REFERENCES and the takeaway, which made no sense, so it's gone.
4. **Merged the five "Write the X bullets as exactly 16 words" lines into one.** They said the same thing five times.
5. **Cut "This should include any and all references…"** from REFERENCES. It repeats "Extract all mentions…".
6. **Small fixes:** removed the stray colons in "IDEAS:.", "QUOTES:" and "FACTS:", which only some sections had. Changed "less than 50 then" to "fewer than 50,".

## Kept, and why
- **The list of interests in the opening section.** That's your choice of focus, and the model can't guess it.
- **All the formats:** the 25-word summary, 15-word takeaway, 16-word bullets, exact quotes with the speaker's name, Markdown only, bullets rather than numbers, no warnings or notes, no repeated items or openings. Each one affects what the output looks like.
- **The description of INSIGHTS and the "collect all" rule for IDEAS.** They describe how the task works, not general advice.
- **The `INPUT:` placeholder at the end.**

## Your call
- **HABITS examples list ("sleep schedule, reading habits, …").** I left it in because it steers what counts as a habit. Dropping it would save about 23 words.
- **"its affect on humans"** should probably be "effect". I left the wording as you wrote it.