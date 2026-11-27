I saved the shorter version as `trimmed.md`. I didn't change `instructions.md`.

**1. Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**2. Word count:** about 340 words before and about 245 after, roughly 28% shorter. These are estimates because I had no counting tool here.

**3. What I cut and why**

| Cut | Reason |
|---|---|
| Line 3: "Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions…" | It describes the file to a human reader and doesn't tell the model to do anything. |
| The bold one-line summary under each heading, such as "Don't assume. Don't hide confusion. Surface tradeoffs." | Each one repeats the bullets below it. The profile says Opus 5.5 follows wording closely, so saying the same thing twice adds weight without changing behaviour. |
| Line 27: "Ask yourself: Would a senior engineer say this is overcomplicated?" | It repeats line 25 ("If you write 200 lines and it could be 50, rewrite it.") and the section's minimum-code rule. |
| Line 15: "If something is unclear, stop. Name what's confusing. Ask." | I merged it into line 12, which already says "If uncertain, ask." Both behaviours are still there. |
| Line 65: "These guidelines are working if…" | It tells the author how to judge the file. The model can't act on it. |

**4. What I kept and why**

- **The dead-code rules (lines 37 and 41), word for word.** They overlap, but both protect against deletion, so I didn't merge or reword them.
- **"YOUR changes" in capitals.** The profile warns that capitals can make the model over-apply a rule. Here they mark which code the model may clean up, so the emphasis does real work.
- **The Tradeoff line, every Simplicity and Surgical Changes bullet, and "The test: every changed line should trace to the user's request."** These are choices you made and the model wouldn't follow them by default.
- **The test-first examples and the plan format block.** They set a specific workflow and an output format. The profile says to keep an example that sets a required format.

**Optional cuts for you to decide**

- **The "Think Before Coding" heading.** The profile says that for Opus 5.5, telling it to think before answering only slowed replies, with no clear quality gain. The bullets under this heading are about asking questions and surfacing assumptions, which is different, so I kept the section. You could drop or rename just the heading.
- **The self-check parts of section 4**, meaning the "→ verify: [check]" steps and line 61 ("Strong success criteria let you loop independently…"). For Opus 5, Anthropic says to delete self-check lines because the model checks its work anyway. Nobody has confirmed that this still holds for 5.5. Dropping line 61 would save about 14 more words. Dropping the verify steps would also change your plan format, so I left both in.