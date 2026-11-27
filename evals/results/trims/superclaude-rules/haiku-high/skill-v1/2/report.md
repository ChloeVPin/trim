Proposed version saved to `/root/trim-sbx/8e8b85fe1ac1/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile in the skill's `profiles.md`, tested at high effort. Haiku needs more explicit direction than the larger models, so I cut less.

**2. Words:** about 2,200 before and about 2,000 after. These are estimates, since I have no word-count tool in this session.

**3. Changes**
- **Removed the "Priority-Based Quick Actions" section.** Every item restates a rule that appears earlier in the file.
- **Removed duplicate lines:** "Session Lifecycle" (repeats "Session Pattern"), "Evidence-Based" in Workflow Rules (repeats "Evidence-Based Claims" in Professional Honesty), "Parallel Everything" (repeats "Batch Operations" in Workflow Rules), "Temporary File Management" and "Professional Workspace" (both repeat "Clean After Operations"), and "Quality Integrity" (repeats "Never Skip Validation").
- **Removed generic virtues:** "Efficiency First" (restates "Best Tool Selection") and "Elegant Organization."
- **Lowered capitals** on ALWAYS, ONLY, MUST, ONE, ANY and ALL to normal case. Meaning is unchanged, and "never" is kept.

**4. Kept**
- All guard rules, with their conditions: no auto-commit, feature branches only, never skip tests or validation, no TODO for core functionality.
- Every example and decision tree. The profile says to keep procedures for Haiku.
- All of your stated preferences, including the ones I would not pick myself, such as the marketing-language ban and the naming conventions.
- The file has no blanket search instructions, so there was nothing for the profile's search cut to apply to.

**5. Flags for you to decide**
- **Commit conflict:** the "Before Any File Operations" tree says "No auto-commit," but "Create Restore Points" says to commit before risky operations, and "Incremental Commits" says to commit frequently. I kept all three.
- **Metrics conflict:** Planning Efficiency asks for time and percentage savings, while Professional Honesty says never to invent time estimates or percentages. I kept both.
- **Scope conflict:** "Start it = Finish it, no exceptions" pulls against "MVP First" and "Build only what's asked."
- **"No Mock Objects"** could be read as banning mocks in tests. If it only covers production code, say so.
- **"Context Retention: ≥90% understanding"** cannot be measured. Kept.
- **References that may not exist here:** `/sc:load` and `/sc:save`, TodoWrite, Task agents, MultiEdit, the MCP servers named, PM Agent, and `@agent-security`. This session has only Read, Edit, Write, Glob and Grep. Haiku may try to call tools that are not present. I kept them in case the file is used where they exist.
- **Checkpoint "30min" intervals:** the model has no clock. "After each completed task" is already a trigger in the same line, so the interval is probably redundant.
- **"Monthly Maintenance" for PM Agent:** nothing in a session can run on a monthly schedule.
- **Git status check:** this directory is not a git repo, so "Always check git status first" will fail here.

**6. Suggested additions** (outside the text; the profile recommends these for Haiku)
- For coding agents: "Before reporting a code change done, run the project's tests or build and report the result."
- For agents that stop early: "Keep working until the task is done."