I saved the proposed version as `trimmed.md`. I didn't change `instructions.md`.

## 1. Target model
I used `claude-opus-5-5`, the model you named. Its profile was tested at medium effort.

## 2. Length
I had no shell to count words, so these are estimates: about **2,000 words before and 1,050 after**, roughly 47% shorter.

## 3. Changes and why
- **The emoji priority system and the "Priority/Triggers" line on every section are gone.** For this model, loud emphasis makes it apply rules too broadly, and plain wording works. Your three strength levels are still there, as a one-line legend and a "(critical)" or "(recommended)" tag on each section heading.
- **"Quick Reference & Decision Trees" is cut.** It repeated the sections above it. I moved the lines that appeared only there into the main sections: brainstorm mode, running existing tests before starting, absolute paths, no auto-commit, and the Magic/Context7/Playwright tool picks.
- **Agent Orchestration is shorter.** The bullets describing how Claude Code picks specialist agents automatically (keywords, file types, complexity) described the system rather than telling the model what to do. I kept the `@agent-` override and every PM Agent duty.
- **Repeated bullets are merged.** Workspace Hygiene had three bullets about temp-file cleanup. Implementation Completeness had six that said the same thing. Scope Discipline, Workflow ("Session Lifecycle" and "Session Pattern"), and Safety versus Code Organization ("follow existing conventions") also overlapped.
- **Lines with no effect are cut.** These are "Context Retention: maintain ≥90% understanding", "Elegant Organization", "Professional Workspace", "Descriptive Names", "Think Before Write", "Methodical Problem-Solving" and "Separation of Concerns".
- **"Grep over bash grep, Glob over find" is cut.** Claude Code's own system prompt already tells the model this.
- **Most ✅/❌ examples are cut or folded into the bullets.** I kept the planning example because it pins the plan format, and the Git example as part of that section.
- **The Temporal Awareness example and the "January 2025" line are replaced** by one rule: use the date from the environment and say where it came from.
- **"ALWAYS", "ONLY" and "MUST" are lowercased** everywhere except the Git section.

## 4. What I kept and why
- **Git Workflow is word for word, including its emphasis and examples.** It covers commits and branches, and rules like that stay exactly as written.
- **These Failure Investigation lines are word for word:** "Never Skip Tests", "Never Skip Validation" and "Quality Integrity". They protect quality checks.
- **The three deletion rules in Workspace Hygiene are word for word.** I only merged the duplicate temp-file bullets.
- **All concrete facts are kept.** That includes `/sc:load`, `/sc:save`, the 30-minute checkpoints, `claudedocs/`, the test and script folders, the TodoWrite threshold, the lint/typecheck step, the banned marketing words, the grep check, the MCP server names, the `@agent-` syntax and the PM Agent schedule.
- **Rules that are your own choices are kept at full strength.** Examples: organize by feature rather than file type, no auth/deployment/monitoring unless asked, Playwright over unit tests for browser testing.

## 5. Flags and suggestions
1. **Conflicts with no-auto-commit.** "Incremental Commits" and "Create Restore Points" (commit often, commit before risky operations) conflict with "No auto-commit". Which one wins?
2. **Made-up metrics.** Planning Efficiency asks for estimates like "3 parallel ops = 60% time saving", but Professional Honesty says "never invent… percentages… without evidence". I kept both.
3. **"Production-ready".** Implementation Completeness says code must be "production-ready", while Professional Honesty says to describe work as "MVP", not "production-ready". The first is probably about the code and the second about how it's described, but you may want to make that explicit.
4. **The "3" threshold is inconsistent.** The original says both "TodoWrite (3+ tasks)" and "TodoWrite for >3 step tasks". I kept 3+, and the Task-agent rule still says ">3 steps". Which number do you mean?
5. **The deletion rules are risky.** "Delete unused directories and files" and "Delete build artifacts, logs" could remove the user's files. Consider limiting them to files the agent created this session, or asking before deleting.
6. **Self-check lines may not be needed (I left them in).** "Validate before execution, verify after completion" and the planning bullet to consider token use and time are the kind of lines the maker said to delete for Opus 5, because the model checks its work unprompted. Whether that holds for 5.5 is unverified. Removing them would save about 25 words.
7. **Two lines push thoroughness and tool use, which this model tends to overdo (I left them in).** They are "Complete project-wide analysis before systematic changes" and "Prefer MCP > native > basic" / "Task agent > native reasoning". They may cause too much analysis and delegation. Narrowing or removing them would save about 30 words.
8. **These may be out of date.** MultiEdit may no longer exist in your Claude Code version, and sequential-thinking MCP for analysis overlaps with the model's own reasoning. Please confirm which tools and MCP servers are still installed.
9. **Suggestion: you could add reasons.** This model follows a rule better when its reason sits beside it. Good candidates are "feature branches only" and "tests in `tests/`, not next to source".

## 6. Proposed text
The full text is in `/root/trim-sbx/8ad7e7f6e381/trimmed.md`.