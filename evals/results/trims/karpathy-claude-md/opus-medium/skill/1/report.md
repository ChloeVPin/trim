I've saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile was tested at medium effort.

**Word count:** about 327 before and 237 after, roughly 27% shorter. I counted by hand because I had no word-count tool, so treat these as estimates. Bullets, arrows and code fences aren't counted, so a tool like `wc` would give somewhat higher numbers for both.

## Changes
1. **Cut the intro line** ("Behavioral guidelines to reduce common LLM coding mistakes. Merge with…"). It tells a human what the file is for and doesn't change what the model does.
2. **Cut the four bold slogans under the headings** ("Don't assume…", "Minimum code…", "Touch only what you must…", "Define success criteria. Loop until verified."). Each one repeats the bullets below it. "Think Before Coding" and "Loop until verified" are also the kind of think-carefully and self-check wording the Opus profile says to drop.
3. **Merged two bullets in section 1.** "If uncertain, ask" and "If something is unclear, stop. Name what's confusing. Ask." now read: "If something is unclear, name what's confusing and ask."
4. **Cut "Ask yourself: would a senior engineer say this is overcomplicated?"** The "200 lines → 50" bullet and the section heading already say this.
5. **Cut "The test:"** before "Every changed line should trace…". The sentence itself stays.
6. **Cut the closing "These guidelines are working if…" line and the `---` above it.** It's a measure for you to judge the file by, not an instruction, and it repeats sections 1–3.
7. **Shortened "Tradeoff:"** to a plain sentence with the same content.

## Kept, and why
- **The deletion rules in section 3 are word for word**, including "YOUR". "Mention it – don't delete it" and "Don't remove pre-existing dead code unless asked" overlap, but they cover deleting code, so I didn't merge or reword them.
- **All the specific rules** in sections 2 and 3 (no unrequested features, abstractions or configurability, match existing style, and so on). These are choices you made, not things the model does on its own.
- **The test-first examples in section 4.** They set a specific way of working that the model wouldn't follow by default.

## Flagged: kept for now, your call
- **The plan template with `→ verify:` steps** (about 19 words). For Opus 5, Anthropic says to drop prompts to verify because the model checks its own work anyway. Whether that holds for 5.5 is unconfirmed, and the template also sets a format, so I kept it. Cutting it would bring the file to about 218 words.
- **"Strong success criteria let you loop independently…"** (15 words). It explains why section 4 exists, and rules with reasons tend to generalise better, but it adds no new instruction. Cutting it would bring the file to about 222 words, or about 203 if you cut both flagged items.