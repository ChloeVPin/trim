I saved the shorter version as `trimmed.md`, about 40% the length of the original. I didn't modify `instructions.md`. Every rule from the original is still there; most of the cuts are repetition and examples.

**What I cut:**
- **Bold slogans under each heading** (e.g. "Don't assume. Don't hide confusion."). Each one repeated the bullet list below it.
- **Repeated rules.** "Don't refactor things that aren't broken" and "Don't improve adjacent code" said the same thing, so I merged them. The two separate dead-code rules became one line.
- **The `validation→tests` examples and the plan template block.** Opus 5.5 doesn't need worked examples for "turn the task into something you can check." I kept a single example inline.
- **The "guidelines are working if…" footer.** It describes how a person should judge the file, not how the model should behave, so it only takes up space.
- **"Would a senior engineer say this is overcomplicated?" phrased as a self-question.** I folded it into one sentence.

**What I changed in tone:**
- The original said "If uncertain, ask" and "If something is unclear, stop… Ask." With a capable model, that wording tends to produce too many clarifying questions. I narrowed it to "ambiguous in a way that changes the result." I also kept the "for trivial tasks, use judgment" exception near the top so the cautious tone doesn't apply to small tasks.
- I removed the all-caps "YOUR changes." Newer models follow plain instructions fine, and emphasis like this can make them over-apply a rule.

**What I kept:** asking before building when it matters, saying when there's a simpler approach, minimal code, edits that trace back to the request, cleaning up what your own change left unused, and verifying with something you can run.