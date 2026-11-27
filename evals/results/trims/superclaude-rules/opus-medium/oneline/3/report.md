I saved the proposed version as `trimmed.md`. It's about 40 lines, down from 287, and `instructions.md` is unchanged.

## What I removed and why

- **Repeated rules.** The original says most things three times: once in a section, again in the "Quick Reference" decision trees, and again in the priority lists. Each rule now appears once.
- **The 🔴/🟡/🟢 labels and "Triggers:" lines.** They took up space without changing behaviour. A one-line note on how to resolve conflicts does the same job. The labels were also inconsistent: "Planning Efficiency" was marked critical while "Implementation Completeness" was only marked important.
- **Things Opus 5.5 and Claude Code already do by default:**
  - parallel tool calls
  - using Grep instead of bash grep
  - reading a file before editing it
  - absolute paths
  - checking today's date from the environment
  - planning before coding
  - using a todo list for multi-step work
- **Instructions that were unclear, couldn't be checked, or worked against each other:**
  - "Maintain ≥90% understanding"
  - "Complex analysis → Task agent > native reasoning"
  - "Playwright > unit tests"
  - the monthly PM Agent maintenance
  - "Plan should specify expected parallelization gains (e.g. 60% time saving)". This directly contradicted "No Fake Metrics."
- **Outdated tool references.** The instruction to prefer MultiEdit over separate edits is gone, since that tool may not exist in current Claude Code. Remove the other tool references too if your setup doesn't have them.
- **Shouting.** Words like ALWAYS, NEVER and MUST were rewritten in a normal tone. Current models follow plain instructions, and heavy emphasis tends to make them overcorrect.

## What I kept

These are the rules the model can't infer by itself:

- staying in scope
- not leaving stubs or TODOs
- not skipping tests or validation
- no marketing language
- feature branches and the git habits that go with them
- the `claudedocs/`, `tests/` and `scripts/` locations
- checking dependencies before using a library
- cleaning up temp files

The setup-specific tools (`@agent-`, `/sc:load` and `/sc:save`, the MCP servers, the PM Agent learning notes) are now a short "use these when they're available" list.

## Decisions for you to check

1. **Commits:** the original says "no auto-commit" but also "commit frequently" and "commit before risky operations." I kept frequent commits on the feature branch. If you want commits only when you ask for them, swap that line.
2. **Mocks:** "No Mock Objects" as written would ban mocks in tests too. I limited it to production code.
3. **TodoWrite:** the original asks for it at 3+ tasks in one place and above 3 steps in another. I dropped it because Claude Code already uses it by default. Add one line back if you want a fixed threshold.