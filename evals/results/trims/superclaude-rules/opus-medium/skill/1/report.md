I saved the shorter version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`. You named it, and it has a profile that has been tested.

**Length:** about 2,250 words before and about 900 after, a cut of roughly 60%. These are estimates because I had no word-count tool in this session.

## What I changed and why

- **Removed the 🔴/🟡/🟢 labels, the capitals and words like "CRITICAL", "MUST" and "ALWAYS".** On Opus 5.5, heavy emphasis makes the model apply a rule too widely; plain wording works. I kept the two things the labels actually decided: which rule wins in a conflict, and that code organization and tool choice are preferences while the rest are firm.
- **Agent Orchestration:** I removed the description of how agents get picked automatically (keywords, file types, complexity). It describes the system rather than telling the model what to do. I kept the `@agent-` override and all four PM Agent duties.
- **Workflow and Planning Efficiency:**
  - Removed the "Understand → Plan → Execute" pattern, "always parallel tool calls", "≥90% understanding" and the resource-estimation lines. The model plans and runs independent calls in parallel without being told, and lines pushing thoroughness or tool use now make it overdo them.
  - **Removed a rule that contradicted another one.** "Efficiency Metrics" asks for figures like "60% time saving", which is exactly what "No Fake Metrics" forbids.
- **Implementation, Scope, Code Organization, Honesty:** I kept the concrete rules (no stubs or TODOs, no auth/deploy/monitoring unless asked, the list of banned words, "untested/MVP") and removed general advice like "Elegant Organization", YAGNI and "No Sycophantic Behavior", along with repeated lines.
- **Tools:** I removed "use the most powerful tool", "Parallel Everything" and "Grep over bash grep". The first two make the model overuse tools, and Claude Code's own system prompt already covers the third. I kept every server name and what each is for.
- **Removed the separate "think before you build" lines.** The profile says lines asking Opus 5.5 to think first now only slow its replies.
- **Dates:** I removed "Don't default to January 2025", which is out of date. The date is already given in the environment, so I shortened the section to one line and kept "say where the date came from".
- **Quick Reference and Decision Trees:** I removed this section because it only repeats rules from the body. The only item not found elsewhere, "no auto-commit", is now under Safety.
- **Examples:** I removed most ✅/❌ examples. None of them sets a required output format, and they steer the model's output strongly. I kept the login-form scope example as one sentence, plus the git example.

## What I left word for word

Rules about deleting, committing, tests and safety stay exactly as you wrote them: all of **Git Workflow**, all of **Workspace Hygiene**, the three "Never" rules under Failures, "Transaction-Safe" and "no auto-commit".

## For you to decide

1. **Commit rules contradict each other.** "Commit frequently" and "Commit before risky operations" conflict with "no auto-commit". I didn't resolve this; you should decide which applies.
2. **Workspace Hygiene says "Delete unused directories and files".** A model that follows wording closely may delete files it didn't create. Consider limiting it to files Claude created. I didn't change it.
3. **"Verify after completion" (removed).** Verification lines were found to be unneeded on Opus 5, but nobody has confirmed that for 5.5. Adding it back costs about 6 words.
4. **MultiEdit and the `/sc:` commands** are kept, but MultiEdit may not exist in current Claude Code. If it doesn't, drop that line (about 10 words).
5. **The PM Agent and Task-agent rules** are kept as your choices. If those agents aren't set up, removing them saves about 70 words.