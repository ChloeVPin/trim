I wrote the proposed version to `/root/trim-sbx/1963759fbd87/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. Its profile was tested at high effort.

**2. Words:** about 334 before and 275 after, roughly 18% shorter. These are estimates, since I had no word-count tool.

**3. Changes**
- Removed "Merge with project-specific instructions as needed." It's a note to the reader, not something the model acts on. Keep it if this file is loaded alongside other rules.
- Removed "If uncertain, ask." It duplicates "If something is unclear, stop... Ask."
- Removed the bold summary under section 1. It restates the bullets below it.
- Removed "Nothing speculative." It repeats the "No features beyond what was asked" rule.
- Removed "Don't refactor things that aren't broken." It's covered by "Don't 'improve' adjacent code."
- Removed "Don't remove pre-existing dead code unless asked." It repeats "mention it - don't delete it."
- Removed the closing "These guidelines are working if..." It's a success measure for the author, not an instruction, and it restates the ask-first rule.

**4. Kept**
- All three examples and the plan template. They carry the task procedure, which the Haiku profile says to keep.
- The ask-before-implementing rule and the tradeoff line. Both are your choices.
- The surgical-change rules, the 200-line check, and the "test" line.
- The one-line reason after the examples. It explains why strong criteria matter.

**5. Unsure, kept and flagged**
- "Ask yourself: 'Would a senior engineer say this is overcomplicated?'" (13 words) overlaps with the 200-line rule. Dropping it saves 13 words if you agree.

**6. Suggested additions, not in the file**
- For a coding agent, add: "Run the tests or build before reporting a task done." The profile recommends this for Haiku. "Loop until verified" implies it but doesn't say it.
- If this agent tends to stop early, add: "Keep working until the task is done." Note that section 1 tells it to stop and ask when something is unclear. Together, those two lines could make it stop early, so decide which one should win.