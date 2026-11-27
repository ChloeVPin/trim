I've saved the shorter version as `/root/trim-sbx/35f898d1fe12/trimmed.md`. It's about 35 lines, down from 287, and `instructions.md` is unchanged.

## What I cut and why

**1. Things Opus 5.5 already does by default.** These were removed:
- Running independent tool calls in parallel, and the "Planning Efficiency" section.
- Reading a file before editing it.
- Preferring Grep and Glob over bash `grep` and `find`.
- Checking today's date from the environment.
- Using absolute paths.
- Generic advice like "think before you build", "use descriptive names" and "plan, execute, verify".

Repeating these mostly adds noise. Strong wording like "ALWAYS" and "never sequentially" can also make the model apply a rule where it doesn't fit.

**2. The 🔴🟡🟢 priority system and capital-letter emphasis.** These rank and shout every section, which makes the model treat everything as top priority. They're replaced with plain, direct wording.

**3. Repetition.** The same rules appeared up to four times: in their own section, in the Quick Reference, in the decision trees and in the "Right/Wrong" examples. For example, "parallel" appears 6+ times and "build only what's asked" 4 times. Each rule now appears once.

**4. Rules that contradicted each other or couldn't be checked:**
- The planning section asked for figures like "3 parallel ops = 60% time saving", while "Professional Honesty" forbids made-up metrics. I kept the ban.
- "Commit frequently" clashed with "no auto-commit". I resolved this as "commit only when asked or at agreed checkpoints".
- "Maintain ≥90% understanding" and "monthly maintenance" can't be measured or acted on by the model in a session, so I removed them.
- The timed checkpoints ("every 30 minutes") had the same problem, so the trimmed file ties checkpoints to finished tasks and risky operations instead.

**5. Tool preferences that could cause harm:**
- "Magic MCP > manual coding", "Playwright > unit tests" and "Task agent > native reasoning" would send even simple work to heavier tools.
- References to MultiEdit, morphllm and sequential-thinking assume tools that may not be installed.

I removed all of these.

## What I kept
The trimmed file keeps the rules specific to your setup that the model can't guess:
- **Scope and completeness:** no stubs, mocks or extra features.
- **Failures:** never skip tests or checks; find the cause first.
- **Honesty:** no marketing language or made-up numbers.
- **Git:** feature branches and reviewing `git diff` before committing.
- **File locations:** `claudedocs/`, `tests/` and `scripts/`.
- **Framework:** `/sc:load` and `/sc:save`, `@agent-<name>`, and the PM agent recording lessons.

## Check before you adopt it
- **PM agent and `/sc:*` commands:** I kept these short on the assumption that they really exist in your framework. If not, delete the "Framework specifics" section.
- **Feature branches:** "Never work on main" stays a firm rule. Soften it if you sometimes want small fixes made directly on main.