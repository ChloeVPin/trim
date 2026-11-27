I've saved the shorter version as `trimmed.md` and left `instructions.md` unchanged.

## 1. Target model
`claude-opus-5-5`, which you named. Its profile is marked as tested at medium effort.

## 2. Length
These are estimates. I only had a search tool, and it counts non-empty lines rather than words.

| | Non-empty lines (measured) | Words (estimated) |
|---|---|---|
| `instructions.md` | 229 | ~2,000 |
| `trimmed.md` | 78 | ~950 |

## 3. Changes and why
- **Removed the capitals, "MUST" and emoji emphasis outside the sections I protected.** Older models needed this kind of emphasis. Opus 5.5 follows wording closely, so it now makes the model apply rules too broadly. I kept the critical, important and recommended tiers as plain labels, and I kept your conflict order.
- **Merged duplicates.** The original says to run things in parallel four times and to plan first three times. It states "Evidence-based" in two places and "follow existing patterns" in three. The "Quick Reference" section and the "Priority-Based Quick Actions" lists repeat the whole file. Each of these now appears once. I moved the facts found only in the quick reference into the main sections: brainstorm mode when scope is unclear, run tests before starting, absolute paths, no auto-commit, and the Magic, Context7 and Playwright mappings.
- **Cut lines that describe what Opus 5.5 already does:** "debug systematically", "methodical problem-solving", "descriptive names", "think before write", "no sycophantic behavior", "professional language", "elegant organization", and "use Grep over bash grep" (Claude Code's own prompt already says this).
- **Cut lines that give the model nothing to act on:** "Maintain ≥90% understanding" and the preamble that only describes the file.
- **Cut "Efficiency Metrics: Plan should specify expected parallelization gains (e.g. '60% time saving')".** It conflicts with your own "No Fake Metrics" rule. Put it back if you want plans to include those numbers.
- **Cut "Resource Estimation: consider token usage".** The effort setting controls that, not a line in the prompt.
- **Cut most of the ✅/❌ examples.** Examples strongly steer what the model produces. I kept the ones that set a format or define scope: the parallel-plan template, the login-form scope example, and the git and cleanup examples inside the protected sections.
- **Shortened "Temporal Awareness" to one line.** The reference to "January 2025" is outdated.

## 4. What I kept and why
- **Kept word for word:** the whole Git Workflow section (commits, branches, rollback), the whole Workspace Hygiene section (it tells the model to delete files), "Never Skip Tests" and "Never Skip Validation", the "Framework Respect" and "Transaction-Safe" rules, and "Absolute paths only → No auto-commit". These guard actions that are hard to undo, so I didn't change them.
- **Kept:** every specific fact. That includes `/sc:load`, `/sc:save`, the 30-minute checkpoints, `@agent-[name]`, the PM Agent duties, `claudedocs/`, the test and script folders, the MCP server names, the banned marketing words, the detection `grep`, and lint/typecheck before marking work done.
- **Kept:** your own choices, such as feature-based folders, no mocks or TODOs, and no auth or deployment unless asked.

### Decisions for you
I kept each of these for now. Dropping any one would make the file a little shorter.
1. **Commits contradict each other.** "No auto-commit" clashes with "Commit frequently" and "Commit before risky operations". I didn't change either because both are protected, but you should decide which one wins. Dropping one saves about 10 words.
2. **"Delete unused directories and files" is very broad.** It's protected, so I didn't edit it. You may want to narrow it to files the model created itself, or have it ask first.
3. **"Validate before execution, verify after completion".** Opus 5 checks its own work without being asked, and Anthropic says to remove lines like this for Opus 5. Whether that holds for 5.5 hasn't been confirmed. Dropping it saves about 6 words.
4. **"Task agents for >3 steps" and "MCP > native > basic".** Lines that push tool or agent use can make newer Claude models overuse them. Dropping the agent part saves about 8 words.
5. **MultiEdit.** Check that this tool still exists in your setup. If it doesn't, the reference does nothing.
6. **The Dates section.** Claude Code already puts today's date in its prompt. Dropping the section saves about 25 words.
7. **The rules on picking specialist agents by keyword and file type.** These may describe what your framework does automatically rather than something the model decides. If so, cutting them saves about 30 words.