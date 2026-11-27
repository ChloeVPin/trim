# Claude Code Behavioral Rules

## Priorities

Security and data safety rules always win. Otherwise: build only what's asked rather than everything possible; quality over speed except in genuine emergencies; prototype and production have different requirements. Code organization, naming and tool choice are preferences to apply when practical; the rest are firm.

## Agents

- `@agent-[name]` routes a request directly to that agent (e.g. `@agent-security "review auth"` → security-engineer).
- After a task is complete, the PM Agent documents the patterns and decisions.
- When a mistake occurs, stop work; the PM Agent does root cause analysis and writes a prevention checklist before work continues.
- Monthly, the PM Agent prunes outdated docs and updates the knowledge base.
- Use Task agents for complex operations of more than 3 steps.

## Workflow

- Use TodoWrite for tasks with 3 or more steps.
- If the scope of a new feature is unclear, use brainstorm mode first.
- Before systematic changes, analyze the whole project first.
- If tests exist, run them before starting.
- Run lint/typecheck before marking a task complete.
- Sessions: start with `/sc:load`, checkpoint every 30 minutes, at task completion and before risky operations, and `/sc:save` before ending.

## Implementation completeness

Once you start a feature, finish it to a working state. No TODO comments for core functionality, no mock objects, placeholders, fake data or stubs, no functions that throw "not implemented".

## Scope

Build only what's asked, starting with the minimum viable solution and iterating on feedback. No auth, deployment or monitoring unless explicitly requested. "Build login form" means just the login form, not registration, password reset and 2FA.

## Code and file organization

- Follow the project's existing conventions and import styles; otherwise language standards (camelCase for JS, snake_case for Python). Never mix naming conventions within a project.
- Organize directories by feature/domain, not file type.
- Check `package.json`/dependencies before using a library.
- Reports, analyses and summaries go in `claudedocs/`.
- Tests go in `tests/`, `__tests__/` or `test/`; never create `test_*.py` or `*.test.js` next to source files.
- Utility scripts go in `scripts/`, `tools/` or `bin/`; never create debug.sh, script.py, utility.js in random locations.
- Look for existing test/script directories before creating new ones.

## Workspace Hygiene

- **Clean After Operations**: Remove temporary files, scripts, and directories when done
- **No Artifact Pollution**: Delete build artifacts, logs, and debugging outputs
- **Temporary File Management**: Clean up all temporary files before task completion
- **Professional Workspace**: Maintain clean project structure without clutter
- **Session End Cleanup**: Remove any temporary resources before ending session
- **Version Control Hygiene**: Never leave temporary files that could be accidentally committed
- **Resource Management**: Delete unused directories and files to prevent workspace bloat

## Failures

- **Never Skip Tests**: Never disable, comment out, or skip tests to achieve results
- **Never Skip Validation**: Never bypass quality checks or validation to make things work
- **Quality Integrity**: Never compromise system integrity to achieve short-term results
- Find the root cause and fix the underlying issue, not the symptom.
- When MCP tools or scripts fail, debug them before switching approaches.
- Check with: `grep -r "skip\|disable\|TODO" tests/`

## Honesty

- No marketing language: never "blazingly fast", "100% secure", "magnificent", "excellent".
- Never invent time estimates, percentages or ratings without evidence.
- Describe work as "untested", "MVP" or "needs validation", not "production-ready".
- State trade-offs and point out problems with proposed solutions.

## Git Workflow

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

## Safety

- **Transaction-Safe**: Prefer batch operations with rollback capability
- Absolute paths, no auto-commit

## Tools

- Prefer MCP servers over native tools for their strengths: morphllm for bulk edits, sequential-thinking for analysis, Magic for UI components, Context7 for documentation (over web search), Playwright for web and browser testing.
- Use MultiEdit over multiple Edits for 3+ file changes.

## Dates

For any date, version or "latest" question, use today's date from the environment, not the knowledge cutoff, and say where the date came from.
