Target model is **claude-haiku-5-5**, named by you. It has a tested profile (high effort). The proposed version is saved at `/root/trim-sbx/b9afdd4dc0ad/trimmed.md`. `instructions.md` is unchanged.

**Words:** about 335 before and about 295 after, roughly 12% shorter. These are estimates because I had no word-count tool.

**Changes**

- **Removed the bold summary under "1. Think Before Coding."** Its three phrases are each covered by the bullets beneath it.
- **Merged two "ask" lines in section 1.** "If uncertain, ask" and "If something is unclear, stop... Ask" said the same thing. The merged line keeps "name what's confusing," which only the second line had.
- **Merged the two "flexibility/features" bullets in section 2.** Both forbid unrequested extras.
- **Merged the two dead-code rules in section 3.** "Mention it, don't delete it" and "don't remove pre-existing dead code unless asked" conflicted in form and repeated each other.
- **Changed "YOUR" to "your own"** in the orphans rule. The profile says capitalised emphasis causes over-application on Anthropic models, and plain wording works.
- **Removed the closing paragraph** ("These guidelines are working if..."). It describes how you judge the file, not something the model does.

**Kept, and why**

- The tradeoff line, including "for trivial tasks, use judgment." Without it, Haiku is likely to over-apply the rules.
- All concrete rules (no abstractions for single-use code, the 200-to-50 line rule, match existing style) and the "test" line.
- Section 4 in full. Its examples and the plan template carry the task procedure, which the profile says to keep for Haiku.

**Flagged, kept (drop if you agree)**

- "Merge with project-specific instructions as needed." Dropping it saves about 9 words. It is a note for whoever merges files, but it also tells the model that other instructions may apply.
- "Ask yourself: 'Would a senior engineer say this is overcomplicated?'" Dropping it saves about 13 words. It repeats section 2's point, but it is a usable self-check.

**Suggested additions (not applied)**

- **A line to run a real check before reporting a change done.** The profile recommends this for coding agents. Section 4's "loop until verified" implies it but doesn't say it.
- **A line to keep working until the task is done.** The profile recommends this only if the agent stops early. Section 1 says to stop and ask when something is unclear, so the two lines would pull against each other. Add it only if you see early stops.