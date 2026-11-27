I saved the shorter version as `trimmed.md`, about 40% of the original's length. I didn't touch `instructions.md`.

**What the audit found**

- **Repeated rules.** Section 1 says "ask" three times in four bullets, and Section 3 says "don't remove dead code" twice. I kept each rule once.
- **Text that only argues for the rules.** The bold taglines, the "senior engineer" check, the line explaining why strong success criteria help, and the closing "these guidelines are working if…" all justify the rules rather than give instructions. Opus 5.5 doesn't need that, so I cut them.
- **The plan template.** The three-line `[Step] → verify: [check]` block shows a format that one sentence can describe, so I replaced it with that sentence.
- **Rules that could backfire.** "If uncertain, ask" and "If something is unclear, stop… Ask" can push a capable model to ask too many questions. I narrowed it to asking only when the request could mean different things and the choice changes the result. The original's "Push back when warranted" also seemed unnecessary, so I dropped it.
- **What stays the same.** Every rule that changes behaviour is still there: keep code minimal, change only what's needed, match the existing style, remove only what your own change made unused, mention unrelated dead code instead of deleting it, and verify with a test or other check. The note to use judgment on trivial tasks also stays.

**One addition:** the new version says project-specific instructions take precedence. The original only said to "merge" them, so I made the order explicit. Remove that line if you don't want it.