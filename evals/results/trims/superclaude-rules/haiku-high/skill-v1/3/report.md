I saved the proposed version to `/root/trim-sbx/3e165bfee23f/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. The cut is conservative because the profile says Haiku needs more detail than the larger models.

**2. Words:** about 1,750 before and about 1,500 after, roughly 14% less. These are estimates because this session has no word-count tool.

**3. Changes**
- **Removed the "Priority-Based Quick Actions" list.** Every item restates a rule that appears in full elsewhere in the file. The decision trees stay.
- **Merged duplicate bullets** in Professional Honesty ("No marketing language" and "Professional language") and in Implementation Completeness ("No partial features" and "Completion mindset").
- **Merged the three session lines** in Workflow Rules (lifecycle, pattern, checkpoint triggers) into one.
- **Removed "Parallel Everything"** from Tool Optimization. Workflow Rules already says the same thing.
- **Lowered emphasis:** "ALWAYS parallel" became "Run independent calls in parallel", and "you MUST" became plain wording. The meaning stays.

**4. Kept as written**
- The guard rules: Git Workflow, Safety Rules, Failure Investigation (including "Never skip tests"), and Workspace Hygiene. Workspace Hygiene covers deletion, which is in the protected category.
- Temporal Awareness and the three decision trees, which carry the procedures.
- All examples, file paths, commands, and the priority tags.

**5. Flags for you to decide**
- **Tools and commands that may not exist in your setup:** `/sc:load`, `/sc:save`, TodoWrite, MultiEdit, Task agents, PM Agent, `@agent-[name]`, and the MCP servers (morphllm, sequential-thinking, Magic, Context7, Playwright). I can't confirm they're available, and Haiku will try to use them if they're named. I kept them.
- **Conflict:** "Efficiency metrics" asks for example figures such as "60% time saving", but Professional Honesty says "No fake metrics". I kept both.
- **Threshold mismatch:** Workflow Rules says TodoWrite at "3+ tasks", but the decision tree says ">3 steps".
- **Can't be measured or acted on:** "Maintain ≥90% understanding", checkpoints every 30 minutes (an agent has no clock), and PM Agent's monthly maintenance (nothing schedules it).
- **Possible over-search:** "Complete project-wide analysis before systematic changes". Blanket search instructions made Haiku search when it didn't need to. Scoping it to the files a change touches and their callers would be safer.
- **No project commands:** the lint/typecheck gate names no commands for this project.

**6. Suggestions (not added to the text)**
- **Real check before "done":** the profile recommends this for coding agents. The file has lint and typecheck gates but no line requiring a test or build run before reporting a change finished. Naming your project's test command would make it concrete.
- **Keep working until done:** if the agent stops early, add "Keep working until the task is done or you are blocked; say what is blocking you."
- **Reasons beside rules:** the profile says rules with a reason generalise better. For example, why main/master is off-limits.