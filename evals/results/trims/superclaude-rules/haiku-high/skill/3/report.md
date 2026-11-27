I saved the proposed version to `/root/trim-sbx/601e0e0b80bd/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is marked tested at high effort. If you run it at a different effort level, the cuts may need rechecking.

**2. Length:** about 2,900 words before and about 1,550 after, roughly 45% shorter. These are estimates because I had no word-count tool here.

**3. Changes**
- **Agent Orchestration:** removed the description of harness auto-selection and the `@agent` override, since the model can't act on them. Kept the Self-Improvement rules. Dropped "monthly maintenance", which the model can't schedule.
- **Quick Reference and Priority-Based Quick Actions:** removed as repeats of earlier sections. The Tool Selection Matrix and the Starting New Feature tree went with them. Kept the "Before Any File Operations" block, because it holds "No auto-commit" and "Absolute paths only", which appear nowhere else.
- **Duplicates merged:** the parallel-tool rule appeared in three sections and is now one line in Tool Optimization. Overlapping bullets in Implementation, Scope, Failure, Honesty, Temporal and File Organization are combined.
- **Cut as no-ops or unactionable:** "Context Retention ≥90%", "Resource Estimation" (the model can't measure time or tokens), "Efficiency First", "Think Before Build", "Single Responsibility", "Descriptive names", "Elegant Organization", "Professional Language" and similar generic advice.
- **Capitals removed** from non-safety bullets (ONLY, ALWAYS, MUST, ONE). The profile says emphasis causes over-application. "Never" in the test and validation rules is kept.
- **One substantive rewrite:** "Discovery First" was "Complete project-wide analysis before systematic changes". It is now conditional: before a change that spans files, search for every use. The blanket search wording is the pattern the profile says made Haiku over-search. Please check this one.
- **Kept verbatim:** Git Workflow, Workspace Hygiene, Safety Rules, the priority system and conflict hierarchy, and the File Operations block. These guard committing, deleting and file changes, so I did not edit their wording.

**4. Kept but flagged (your decision)**
- **Conflict:** "No auto-commit" (File Operations) contradicts "Commit frequently" (Git Workflow). I kept both. The model will have to pick one.
- **Conflict:** Efficiency Metrics asks for an estimated "60% time saving", while Professional Honesty says "No Fake Metrics". I kept both.
- **Possibly absent:** `/sc:load`, `/sc:save`, PM Agent, TodoWrite, MultiEdit and the named MCP servers. I can't verify them here. If they're not configured, dropping them saves about 120 words.
- **30-minute checkpoints:** the model has no clock, so "every 30 minutes" can go without loss.
- **Triggers lines:** one per section, about 150 words in total. Cut them if you think the section headings are enough.
- **Example date:** the Temporal example uses 2025-08-15, but today is 2026-11-27. The model could copy that date. A placeholder would be safer.

**5. Not added:** the Haiku profile suggests a line saying to keep working until the task is done, for agents that stop early. This file doesn't have one. I left it out. If you want it, it would go after the Workflow Rules, for example: "Keep working until the task is done."

Tell me which flags to apply and I'll update `trimmed.md`.