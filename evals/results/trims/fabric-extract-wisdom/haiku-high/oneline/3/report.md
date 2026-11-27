I saved the proposed version to `/root/trim-sbx/65eba5f9435d/trimmed.md`. `instructions.md` is unchanged. I haven't run either prompt through claude-haiku-5-5, so the Haiku-specific changes are based on reading the prompt, not on testing its output.

**Audit of instructions.md**

- **Conflicting counts.** IDEAS says 20 to 50, then "at least 25", then "at least 20". QUOTES, HABITS, FACTS and RECOMMENDATIONS say 15 to 30, but the output rules say "at least 20".
- **Blanket minimum.** "At least 20 items for the other output sections" can't apply to REFERENCES, which asks for every mention, and it conflicts with the 15-item ranges.
- **Exact word counts.** Five sections require exactly 16 words per bullet, plus 25 and 15 words for SUMMARY and the takeaway. This is the most fragile part for a small model. A script could check it if you want to keep it.
- **Filler.** "Take a step back and think step-by-step" adds nothing for this task.
- **Typos and unclear wording.** "affect" should be "effects", and the INSIGHTS sentence repeats "from input and from a combination of the raw input".
- **Inconsistent headers.** Some headers have colons (IDEAS:, QUOTES:, FACTS:) and others don't.

**Choices in trimmed.md**

- I resolved each count conflict in favor of the range that satisfies all the rules: IDEAS 25 to 50, INSIGHTS 10 to 20, and 20 to 30 for QUOTES, HABITS, FACTS and RECOMMENDATIONS.
- REFERENCES has no minimum, since it asks for all mentions.
- I added "include all that the input contains" for when the input is too thin to meet a minimum. The original only said this for IDEAS.
- I kept the section order, the Markdown-only output, the no-notes rule, the verbatim quotes, and the exact word counts.
- I replaced the colon-style headers with consistent `##` headers and cut the prompt by roughly a third.