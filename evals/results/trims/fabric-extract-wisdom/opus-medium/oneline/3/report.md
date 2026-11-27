I saved the shorter version as `/root/trim-sbx/3e9a27626c39/trimmed.md` and left `instructions.md` unchanged. It drops from about 60 lines to about 30 and keeps every section, the bullet word limits and the output rules.

**Problems I found in the original:**

1. **The counts contradict each other.** The steps and the output rules give different numbers for the same sections:
   - IDEAS: "20 to 50" in the steps, "at least 25" in the rules.
   - "At least 20 items for the other output sections" conflicts with QUOTES (15–30), HABITS, FACTS and RECOMMENDATIONS (15–30), and REFERENCES ("all mentions").
   - That same rule would also require at least 20 items in ONE-SENTENCE TAKEAWAY, which should be one sentence.

   I kept the higher minimums from the output rules: IDEAS 25–50, INSIGHTS 10–20, and 20–30 for QUOTES, HABITS, FACTS and RECOMMENDATIONS. REFERENCES stays "all" and the takeaway stays one sentence. **This is a real change to what the prompt asks for, so check that these are the numbers you want.**
2. **"Exactly 16 words" appeared five times**, once per section. I merged these into one rule.
3. **The IDEAS step was muddled.** "If there are less than 50 then collect all of them" sits right next to "at least 20." The new version says to pick the best when there are more than 50.
4. **I removed lines that add nothing for Opus 5.5.** These were "Take a step back and think step-by-step…" and "Ensure you follow ALL these instructions." Opus 5.5 follows clear instructions without them.
5. **Small fixes:**
   - "Its affect on humans" is now "its effect on people".
   - Section names had colons on some and not others; they're now consistent Markdown headings.
   - Each section's count and rules now sit in one bullet instead of being split between the steps and the output rules.
   - "Do not repeat" now explicitly covers items both within a section and across sections.

**What stays the same:**
- The list of preferred topics, because it guides what gets picked.
- The section order.
- Exact quotes with the speaker's name.
- The 25-word summary and 15-word takeaway.
- Bullets, not numbered lists.
- No warnings or notes in the output.
- The `INPUT:` placeholder.