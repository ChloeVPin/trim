I saved the shorter version as `trimmed.md`. It's about 40 lines, down from 287, and `instructions.md` is unchanged.

## What the audit found

**Removed because Opus 5.5 already does it or the tool setup handles it:**
- **Temporal Awareness:** the model is given today's date and uses it. The original example dates ("2025-08-15", "January 2025") are out of date themselves.
- **Basic tool habits:** "Grep over bash grep", "read before edit", "use absolute paths" and "make independent tool calls in parallel" are already built-in behaviour.
- **The Quick Reference and decision trees** (lines 234–287) repeated rules that appear earlier in the file.
- **Repeated rules:** "Plan → Execute → Verify" appeared in about five sections, and most sections said the same thing 3–4 times in different words (e.g., Workspace Hygiene's seven bullets).
- **The 🔴/🟡/🟢 labels and ALWAYS/NEVER/MUST capitals.** Heavy emphasis tends to make Opus 5.5 apply rules too rigidly. A short conflict-ordering sentence replaces the label system.
- **Rules with no practical effect,** such as "Maintain ≥90% understanding across operations".
- **The automatic routing to specialist agents** (lines 20–25): this describes how the system works rather than giving the model instructions.

**Contradictions or risks I fixed:**
- **Made-up speed figures:** Planning Efficiency asked for numbers like "3 parallel ops = 60% time saving", but Professional Honesty says "never invent percentages". I dropped the speed figures.
- **Mocks:** "No Mock Objects" as written would rule out normal test mocks. I limited it to production code.
- **Cleanup:** "Delete build artifacts, logs" could destroy files you want to keep. I limited it to temporary files the model created.
- **"Most powerful tool, MCP > Native":** I changed this to "use a specialised MCP server for its own domain, where available".
- **MultiEdit:** I removed the requirement because that tool may not exist in your setup.

## Needs your decision
- **When to commit:** the Git section says "commit frequently" and "commit before risky operations", but the Quick Reference says "no auto-commit". I kept the Git section's approach (feature-branch commits). If you meant "only commit when asked", change that paragraph.
- **SuperClaude features:** `/sc:load`, the PM Agent and `claudedocs/` look specific to SuperClaude. I couldn't confirm they exist in your setup. I made the `/sc:*` steps apply only if the commands are installed, and turned the PM Agent behaviour into plain instructions. If you don't use SuperClaude, delete the last section.