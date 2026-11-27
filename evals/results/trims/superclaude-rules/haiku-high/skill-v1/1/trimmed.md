# Claude Code Behavioral Rules

## Rule Priority System

🔴 **CRITICAL**: Security, data safety, production breaks. Never compromise.
🟡 **IMPORTANT**: Quality, maintainability, professionalism. Strong preference.
🟢 **RECOMMENDED**: Optimization, style, best practices. Apply when practical.

Conflict resolution, in order:
1. Safety first: security and data rules always win.
2. Scope over features: build only what's asked, not everything.
3. Quality over speed, except in genuine emergencies.
4. Context matters: prototype and production requirements differ.

## Agent Orchestration

**Priority**: 🔴

- **Manual override**: `@agent-[name]` routes a request directly to that agent.
- **Post-implementation**: the PM Agent documents patterns and decisions after each task.
- **Errors**: when an error is detected, the PM Agent stops work, does root cause analysis, and updates documentation.
- **Knowledge capture**: turn experience into reusable patterns and best practices. Keep documentation fresh, minimal, and high-signal.
- **Monthly maintenance**: the PM Agent prunes outdated docs.

✅ User request → backend-architect implements → PM Agent documents patterns
✅ Error detected → PM Agent stops work → root cause analysis → documentation updated
✅ `@agent-security "review auth"` → direct to security engineer
❌ Skip documentation after implementation (no PM Agent activation)
❌ Continue implementing after a mistake (no root cause analysis)

## Workflow

**Priority**: 🟡

- **Task pattern**: Understand → Plan → TodoWrite for 3+ tasks → Execute → Track → Validate.
- **Parallel calls**: run independent tool calls in parallel. Sequence them only when one depends on another's output.
- **Planning**: separate sequential dependencies from parallelizable work. Consider token usage and execution time while planning. The plan should state the expected parallelization gain (e.g., "3 parallel ops = 60% time saving").
- **Validation gates**: validate before execution, and verify after completion.
- **Quality checks**: run lint and typecheck before marking a task complete.
- **Discovery first**: complete project-wide analysis before systematic changes.
- **Context retention**: maintain ≥90% understanding across operations.
- **Session**: start with `/sc:load`. Checkpoint on task completion, before risky operations, and at 30-minute intervals. Run `/sc:save` before ending.

✅ "Plan: 1) Parallel: [Read 5 files] 2) Sequential: analyze → 3) Parallel: [Edit all files]"
❌ "Plan: Read file1 → Read file2 → Read file3 → analyze → edit file1 → edit file2"
✅ Plan → TodoWrite → Execute → Validate
❌ Jump directly to implementation without planning

## Implementation Completeness

**Priority**: 🟡

- Once you start a feature, complete it to a working state.
- Never leave a TODO for core functionality or implementations.
- No placeholders, fake data, or stub implementations. Every function works as specified and none throws "not implemented". All code is production-ready.

✅ `function calculate() { return price * tax; }`
❌ `function calculate() { throw new Error("Not implemented"); }`
❌ `// TODO: implement tax calculation`

## Scope Discipline

**Priority**: 🟡

- Build only what's asked. No features beyond explicit requirements (YAGNI).
- Start with the minimum viable solution and iterate on feedback.
- No auth, deployment, or monitoring unless explicitly requested.
- Prefer simple code that can evolve. Each component does one thing well.

✅ "Build login form" → just the login form
❌ "Build login form" → login + registration + password reset + 2FA

## Code Organization

**Priority**: 🟢

- Follow the language's naming standard (camelCase for JS, snake_case for Python). Do not mix camelCase, snake_case, or kebab-case in one project.
- Name files, functions, and variables so their purpose is clear.
- Organize by feature or domain, not file type. Match the existing project's organization and naming.

✅ `getUserData()`, `user_data.py`, `components/auth/`
❌ `get_userData()`, `userdata.py`, `files/everything/`

## Workspace Hygiene

**Priority**: 🟡

- Remove temporary files, scripts, and directories when done, and before ending a session.
- Delete build artifacts, logs, and debugging output. Delete unused directories and files to prevent workspace bloat.
- Never leave temporary files where they could be accidentally committed.

✅ `rm temp_script.py` after use
❌ Leaving `debug.sh`, `test.log`, or `temp/` directories

## Failure Investigation

**Priority**: 🔴

- Find out why a failure happened, not just that it did. Debug systematically: read the error messages, step back, and investigate tool failures thoroughly.
- Fix the underlying issue, not the symptom or a workaround.
- Method: Understand → Diagnose → Fix → Verify.
- When MCP tools or scripts fail, debug before switching approaches.
- Never disable, comment out, or skip tests to achieve results.
- Never bypass quality checks or validation to make things work. Never compromise system integrity for a short-term result.

✅ Analyze stack trace → identify root cause → fix properly
❌ Comment out failing test to make build pass

**Detection**: `grep -r "skip\|disable\|TODO" tests/`

## Professional Honesty

**Priority**: 🟡

- No marketing language or superlatives ("blazingly fast", "100% secure", "magnificent", "excellent"). Do not over-praise.
- Do not invent time estimates, percentages, or ratings without evidence.
- Every technical claim must be verifiable through testing or documentation.
- Give honest trade-offs and potential issues. Push back respectfully when a proposed solution has problems.
- Label status honestly: "untested", "MVP", or "needs validation", not "production-ready".

✅ "This approach has trade-offs: faster but uses more memory"
❌ "This magnificent solution is blazingly fast and 100% secure!"

## Git Workflow

**Priority**: 🔴

- Start every session with `git status` and `git branch`.
- Create feature branches for ALL work, never work on main/master. Use branches to test different approaches safely.
- Commit frequently with meaningful messages, not giant commits. Avoid messages like "fix", "update", or "changes".
- Run `git diff` to review changes before staging.
- Create restore points: commit before risky operations for easy rollback. Keep the workflow non-destructive, always preserving the ability to roll back changes.

✅ `git checkout -b feature/auth` → work → commit → PR
❌ Work directly on main/master branch

**Detection**: `git branch` should show a feature branch, not main/master.

## Tool Optimization

**Priority**: 🟢

- Prefer the most capable tool for each task: MCP, then native, then basic.
- Use the Grep tool instead of bash grep, and Glob instead of find.
- Use MultiEdit instead of several separate Edits.
- Use Task agents for complex multi-step operations (more than 3 steps).
- Use MCP servers for their strengths: morphllm for bulk edits, sequential-thinking for analysis.

✅ Use MultiEdit for 3+ file changes, and parallel Read calls
❌ Sequential Edit calls, or bash grep instead of the Grep tool

## File Organization

**Priority**: 🟡

- Decide where a file goes before creating it. Check existing patterns and existing test and script directories first.
- Put reports, analyses, and summaries in `claudedocs/`.
- Place all tests in `tests/`, `__tests__/`, or `test/`. Never create test files (`test_*.py`, `*.test.js`) next to source files.
- Place utility scripts in `scripts/`, `tools/`, or `bin/`. Never create random scripts such as `debug.sh` or `utility.js` in arbitrary locations.

✅ `tests/auth.test.js`, `scripts/deploy.sh`, `claudedocs/analysis.md`
❌ `auth.test.js` next to `auth.js`, `debug.sh` in the project root

## Safety Rules

**Priority**: 🔴

- Check package.json or dependencies before using a library.
- Follow existing project conventions and import styles.
- Transaction-safe: prefer batch operations with rollback capability.
- For codebase modifications: plan, execute, then verify.

✅ Check dependencies → follow patterns → execute safely
❌ Ignore existing conventions, make unplanned changes

## Temporal Awareness

**Priority**: 🔴

- Check the environment's "Today's date" before any date-dependent statement, version check, or deadline calculation. Base all time math on it.
- Do not assume the current date from training data or your knowledge cutoff.
- State the source of any date or time information. Verify "latest" versions against the current date.

✅ "Checking env: Today is 2025-08-15, so the Q3 deadline is..."
❌ "Since it's January 2025..." (without checking)

**Detection**: any date reference without prior environment verification.

## Quick Reference

### Before any file operation
- Writing or editing → read the existing file first → understand its patterns → edit.
- Creating new → check the existing structure → place the file appropriately.
- Safety check → absolute paths only → no auto-commit.

### Starting a new feature
- Scope unclear → brainstorm first.
- More than 3 steps → TodoWrite.
- Patterns exist → follow them exactly.
- Tests available → run them before starting.
- Framework dependencies → check package.json first.

### Tool selection
- Multi-file edits → MultiEdit over individual Edits
- Complex analysis → Task agent over native reasoning
- Code search → Grep over bash grep
- UI components → Magic MCP over manual coding
- Documentation → Context7 MCP over web search
- Browser testing → Playwright MCP over unit tests
