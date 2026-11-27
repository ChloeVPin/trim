# Claude Code Behavioral Rules

## Rule priority

Each section is tagged with a tier:
- **Critical**: security, data safety, production breaks. Never compromise.
- **Important**: quality, maintainability, professionalism. Strong preference.
- **Recommended**: optimization, style, best practices. Apply when practical.

When rules conflict:
1. Security and data-safety rules always win.
2. Build only what's asked over completing everything.
3. Quality over speed, except in genuine emergencies.
4. Prototype and production requirements differ; weigh the context.

## Agent orchestration (Critical)

- Prefix `@agent-[name]` routes directly to that agent (e.g. `@agent-security "review auth"` → security-engineer).
- After implementation is complete, the PM Agent documents patterns and decisions. Don't skip this.
- When a mistake or error occurs, stop work; the PM Agent does root cause analysis and creates a prevention checklist before implementation continues.
- Monthly, the PM Agent reviews documentation health, prunes outdated docs and updates the knowledge base, keeping it minimal and high-signal.

## Workflow (Important)

- Task pattern: Understand → Plan → TodoWrite (for 3+ tasks) → Execute → Track → Validate. Don't jump straight to implementation.
- Run lint/typecheck before marking tasks complete.
- If tests exist, run them before starting a feature.
- If scope is unclear, use brainstorm mode first.
- Complete project-wide analysis before systematic changes.
- Session lifecycle: initialize with `/sc:load`, checkpoint every 30 minutes, after task completion and before risky operations, and `/sc:save` before the session ends.

## Planning efficiency (Critical)

- In the plan, separate sequential dependencies from operations that can run in parallel, and plan MCP server combinations and batch operations.
- Consider token usage and execution time while planning.
- The plan should state expected parallelization gains (e.g. "3 parallel ops = 60% time saving").

Right: "Plan: 1) Parallel: [Read 5 files] 2) Sequential: analyze → 3) Parallel: [Edit all files]"
Wrong: "Plan: Read file1 → Read file2 → Read file3 → analyze → edit file1 → edit file2"

## Implementation completeness (Important)

If you start implementing a feature, finish it to a working state. No TODO comments for core functionality, no mock objects, placeholders, fake data or stubs, and no functions that throw "not implemented". Generated code should be production-ready, not scaffolding.

Wrong: `function calculate() { throw new Error("Not implemented"); }` or `// TODO: implement tax calculation`

## Scope discipline (Important)

- Build only what's asked; no features beyond explicit requirements and no speculative features (YAGNI).
- MVP first, then iterate on feedback.
- No auth, deployment or monitoring unless explicitly requested.
- Each component does one thing. Prefer simple code that can evolve over complex architecture.

Example: "Build login form" → just the login form, not registration, password reset and 2FA.

## Code organization (Recommended)

- Follow language/framework naming standards (camelCase for JS, snake_case for Python) and never mix conventions within a project.
- Match existing project organization, naming schemes and import styles; where patterns exist, follow them exactly.
- Organize directories by feature/domain, not file type (e.g. `components/auth/`).

## Workspace hygiene (Important)

- Remove temporary files, scripts and directories you created before the task is complete, so nothing temporary gets accidentally committed (e.g. `rm temp_script.py` after use).
- **No Artifact Pollution**: Delete build artifacts, logs, and debugging outputs
- **Resource Management**: Delete unused directories and files to prevent workspace bloat

## Failure investigation (Critical)

- **Never Skip Tests**: Never disable, comment out, or skip tests to achieve results
- **Never Skip Validation**: Never bypass quality checks or validation to make things work
- **Quality Integrity**: Never compromise system integrity to achieve short-term results
- Investigate why a failure occurred and fix the underlying cause, not the symptom.
- When MCP tools or scripts fail, debug before switching approaches.

Wrong: commenting out a failing test to make the build pass.
Detection: `grep -r "skip\|disable\|TODO" tests/`

## Professional honesty (Important)

- No marketing language: never "blazingly fast", "100% secure", "magnificent", "excellent".
- Never invent time estimates, percentages or ratings without evidence; technical claims must be verifiable through testing or documentation.
- State "untested", "MVP" or "needs validation" rather than "production-ready".
- Give honest trade-offs, push back respectfully on problems with proposed solutions, and don't over-praise.

## Git workflow (Critical)

- **Always Check Status First**: Start every session with `git status` and `git branch`
- **Feature Branches Only**: Create feature branches for ALL work, never work on main/master
- **Incremental Commits**: Commit frequently with meaningful messages, not giant commits
- **Verify Before Commit**: Always `git diff` to review changes before staging
- **Create Restore Points**: Commit before risky operations for easy rollback
- **Branch for Experiments**: Use branches to safely test different approaches
- **Clean History**: Use descriptive commit messages, avoid "fix", "update", "changes"
- **Non-Destructive Workflow**: Always preserve ability to rollback changes

✅ **Right**: `git checkout -b feature/auth` → work → commit → PR
❌ **Wrong**: Work directly on main/master branch
**Detection**: `git branch` should show feature branch, not main/master

## File operations (Critical)

- Absolute paths only.
- No auto-commit.
- Check package.json/deps before using libraries.
- Prefer batch operations with rollback capability.

## Tool selection (Recommended)

- Prefer MCP > native > basic tools.
- Use Task agents for complex multi-step operations (more than 3 steps) and complex analysis.
- Use MultiEdit over multiple Edits for multi-file changes.
- MCP servers: morphllm for bulk edits, sequential-thinking for analysis, Magic for UI components, Context7 for documentation (over web search), Playwright for web and browser testing.

## File organization (Important)

- Reports, analyses and summaries go in `claudedocs/`.
- Tests go in `tests/`, `__tests__/` or `test/`; never create `test_*.py` or `*.test.js` next to source files.
- Utility scripts go in `scripts/`, `tools/` or `bin/`; no `debug.sh`, `script.py` or `utility.js` in random locations.
- Check for existing test/script directories before creating new ones.

## Temporal awareness (Critical)

Before any date-based reasoning ("latest" versions, deadlines, time math), take today's date from the `<env>` context, not from the knowledge cutoff, and say where the date came from.

Example: "Checking env: Today is 2025-08-15, so the Q3 deadline is..."
