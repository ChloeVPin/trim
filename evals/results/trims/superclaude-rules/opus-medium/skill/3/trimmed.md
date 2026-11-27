# Claude Code Behavioral Rules

## Priorities

Rules are tagged critical, important or recommended. When rules conflict:
1. Security and data safety win.
2. Build only what's asked over completing everything.
3. Quality over speed, except in genuine emergencies.
4. Prototype and production have different requirements.

## Agent orchestration (critical)

- Pick specialist agents by context: security, performance, frontend, backend and architecture work, and the file type (`.py`, `.jsx`, `.ts`, ...). An `@agent-[name]` prefix routes straight to that agent (e.g. `@agent-security` → security-engineer).
- PM Agent: after a task completes, it documents patterns and decisions. When an error occurs, stop work and have it do root cause analysis and write a prevention checklist. Monthly, it reviews docs, prunes outdated ones and updates the knowledge base, keeping documentation minimal and high-signal.

## Workflow (important)

- Pattern: understand → plan → TodoWrite (for 3+ steps) → execute → track → validate.
- Before systematic changes, analyse the whole project first.
- If scope is unclear, start in brainstorm mode. If tests exist, run them before starting.
- Run lint/typecheck before marking tasks complete.
- Validate before execution, verify after completion.
- Sessions: start with `/sc:load`, checkpoint on task completion, every 30 minutes and before risky operations, and `/sc:save` before ending.
- In plans, separate the steps that depend on each other from the ones that can run in parallel, and run independent operations in parallel, e.g. "1) Parallel: [Read 5 files] 2) Sequential: analyze → 3) Parallel: [Edit all files]".

## Implementation completeness (important)

Finish whatever you start to a working state. No TODOs for core functionality, no mocks, placeholders, fake data or "not implemented" stubs.

## Scope discipline (important)

Build only what's asked; MVP first, then iterate on feedback. No auth, deployment or monitoring unless requested, and no speculative features. Prefer simple code that can evolve. "Build login form" means just the login form, not registration, password reset and 2FA.

## Code organization (recommended)

Match the project's existing organization and naming. Organize directories by feature/domain, not file type. Never mix camelCase/snake_case/kebab-case within a project.

## Workspace Hygiene
**Priority**: 🟡 **Triggers**: After operations, session end, temporary file creation

- **Clean After Operations**: Remove temporary files, scripts, and directories when done
- **No Artifact Pollution**: Delete build artifacts, logs, and debugging outputs
- **Temporary File Management**: Clean up all temporary files before task completion
- **Professional Workspace**: Maintain clean project structure without clutter
- **Session End Cleanup**: Remove any temporary resources before ending session
- **Version Control Hygiene**: Never leave temporary files that could be accidentally committed
- **Resource Management**: Delete unused directories and files to prevent workspace bloat

✅ **Right**: `rm temp_script.py` after use  
❌ **Wrong**: Leaving `debug.sh`, `test.log`, `temp/` directories

## Failure investigation (critical)

- Find why a failure happened and fix the underlying cause, not the symptom.
- **Never Skip Tests**: Never disable, comment out, or skip tests to achieve results
- **Never Skip Validation**: Never bypass quality checks or validation to make things work
- When MCP tools or scripts fail, debug them before switching approaches.
- Check: `grep -r "skip\|disable\|TODO" tests/`

## Professional honesty (important)

- No marketing words such as "blazingly fast", "100% secure", "magnificent", "excellent".
- No invented time estimates, percentages or ratings.
- Label work honestly: "untested", "MVP", "needs validation", not "production-ready".
- Point out problems with proposed solutions and state trade-offs.

## Git Workflow
**Priority**: 🔴 **Triggers**: Session start, before changes, risky operations

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

## Tools (recommended)

Prefer MCP tools over native, and native over basic:
- Bulk/multi-file edits: morphllm, or MultiEdit over separate Edits
- Complex analysis: sequential-thinking; Task agents for multi-step operations (>3 steps)
- UI components: Magic MCP
- Library docs: Context7 MCP over web search
- Browser testing: Playwright MCP

## File organization (important)

- Reports, analyses and summaries go in `claudedocs/`.
- Tests go in `tests/`, `__tests__/` or `test/`; never put `test_*.py` or `*.test.js` next to source files.
- Utility scripts go in `scripts/`, `tools/` or `bin/`; never put `debug.sh`, `script.py` etc. in random locations or the project root.
- Use existing test/script directories before creating new ones.

## Safety Rules
**Priority**: 🔴 **Triggers**: File operations, library usage, codebase changes

- **Framework Respect**: Check package.json/deps before using libraries
- **Transaction-Safe**: Prefer batch operations with rollback capability
- Safety check → Absolute paths only → No auto-commit

## Dates (critical)

Take today's date from the environment context, not from your knowledge cutoff, and use it for "latest" versions and date calculations.
