I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Words:** about 356 before and 260 after, roughly 27% shorter. I had no tool to count with here, so I counted by hand by splitting on spaces. Treat both figures as estimates.

## Changes
| Cut or changed | Reason |
|---|---|
| The opening line ("Behavioral guidelines… Merge with project-specific instructions") | It's a note to the person setting the file up. The model wouldn't act differently without it. |
| All four bold slogans at the top of the sections ("Don't assume…", "Minimum code…", "Touch only what you must…", "Define success criteria…") | Each one repeats the bullets underneath it. |
| "If uncertain, ask" joined with "If something is unclear, stop… Ask" | They said the same thing. The joined line still says to stop, name what's confusing, and ask. |
| "No features…" joined with "No 'flexibility' or 'configurability'…" | Same rule, so one bullet now covers both. |
| "Ask yourself: would a senior engineer say this is overcomplicated?" | It repeats the 200-to-50-lines rule and the bullets above it. |
| "When your changes create orphans:" heading | The bullet under it already says "that your changes made unused". |
| "YOUR" changed to "your" | The profile says capitals now cause Opus models to over-apply a rule, and plain wording works. |
| The "Strong criteria vs weak criteria" sentence | I folded its reason into the line that introduces the examples ("so you can loop independently…"). Reasons help rules generalise, so I kept it rather than dropping it. |
| The closing "These guidelines are working if…" | It's a measure of success for you, the author. It doesn't give the model a new rule. |

## Kept, and why
- **The caution-over-speed line:** it's a choice you made.
- **The rules about asking first and pushing back:** they're about when to stop and ask, not about thinking harder. The profile only says to cut "think carefully" lines.
- **Both dead-code rules, word for word:** they're about deleting code. The second one adds the "unless asked" exception, so I didn't merge them.
- **The test-first examples and the plan block:** they set a method and a format you chose. The profile says to keep examples that set a required format.
- **"Every changed line should trace to the user's request":** it's the general test behind section 3.

## Unsure, so I kept them (you decide)
- **The `→ verify:` plan block (about 24 words).** For Opus 5, Anthropic says to drop self-check lines because the model checks its own work anyway. Whether that holds for Opus 5.5 hasn't been confirmed. If you drop it, the file gets about 9% shorter.
- **"If you write 200 lines and it could be 50, rewrite it" (13 words).** The other simplicity bullets mostly cover it. Dropping it saves about 5%.
- **Merging the two dead-code bullets into "Mention unrelated dead code; don't delete it unless asked" (about 12 words saved).** Only do this if you're happy with that exact wording.