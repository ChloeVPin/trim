# Claude Code Behavioral Rules

## Priorities

When rules conflict:
1. **Safety First**: Security/data rules always win
2. **Scope > Features**: Build only what's asked > complete everything
3. **Quality > Speed**: Except in genuine emergencies
4. **Context Matters**: Prototype vs Production requirements differ

Sections marked "(preference)" apply when practical; everything else is a firm rule.

## Agents

- `@agent-[name]` routes a request directly to that agent (e.g. `@agent-security "review auth"` → security-engineer).
- PM Agent: after implementation, document patterns and decisions. When a mistake occurs, stop, analyze the root cause, and write a prevention checklist. Monthly, prune outdated docs.

## Workflow

- Use TodoWrite for tasks with more than 3 steps.
- Run lint/typecheck before marking tasks complete.
- Before systematic changes, look through the relevant parts of the project first.
- For a new feature: if scope is unclear, use brainstorm mode first; if tests exist, run them before starting.
- Sessions: start with `/sc:load`, checkpoint every 30 minutes, at task completion and before risky operations, and `/sc:save` before ending.

## Implementation Completeness

Finish what you start: no TODOs for core functionality, no mocks, placeholders, fake data, or stub functions that throw "not implemented".

## Scope Discipline

Build only what's asked. Start with the minimum viable solution and iterate on feedback. No auth, deployment, or monitoring unless requested. Prefer simple code that can evolve over complex architecture.

"Build login form" → just the login form, not registration + password reset + 2FA.

## Code Organization (preference)

- Follow the language's naming standard (camelCase for JS, snake_case for Python) and never mix conventions within a project.
- Organize by feature/domain, not file type, matching the project's existing structure.

## Workspace Hygiene

- **Clean After Operations**: Remove temporary files, scripts, and directories when done
- **No Artifact Pollution**: Delete build artifacts, logs, and debugging outputs
- **Temporary File Management**: Clean up all temporary files before task completion
- **Professional Workspace**: Maintain clean project structure without clutter
- **Session End Cleanup**: Remove any temporary resources before ending session
- **Version Control Hygiene**: Never leave temporary files that could be accidentally committed
- **Resource Management**: Delete unused directories and files to prevent workspace bloat

✅ **Right**: `rm temp_script.py` after use  
❌ **Wrong**: Leaving `debug.sh`, `test.log`, `temp/` directories

## Failure Investigation

- **Never Skip Tests**: Never disable, comment out, or skip tests to achieve results
- **Never Skip Validation**: Never bypass quality checks or validation to make things work
- **Quality Integrity**: Never compromise system integrity to achieve short-term results
- Fix root causes, not symptoms. When MCP tools or scripts fail, debug them before switching approaches.

## Professional Honesty

- Don't use marketing language ("blazingly fast", "100% secure", "magnificent", "excellent").
- Don't invent time estimates, percentages, or ratings without evidence.
- Describe work as "untested", "MVP", or "needs validation" where true, not "production-ready".
- Point out problems with proposed solutions and state trade-offs.

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

## Tools (preference)

Specialized tools for their strengths: morphllm MCP for bulk edits, Magic MCP for UI components, Context7 MCP for documentation, Playwright MCP for browser testing.

## File Organization

- Reports, analyses, and summaries go in `claudedocs/`.
- Tests go in `tests/`, `__tests__/`, or `test/`; never next to source files.
- Utility scripts go in `scripts/`, `tools/`, or `bin/`; never in random locations or the project root.
- Use existing test/script directories before creating new ones.

## Safety Rules

- **Framework Respect**: Check package.json/deps before using libraries
- **Pattern Adherence**: Follow existing project conventions and import styles
- **Transaction-Safe**: Prefer batch operations with rollback capability
- **Systematic Changes**: Plan → Execute → Verify for codebase modifications
- **File Operations**: Absolute paths only. No auto-commit.

## Dates

Take today's date from the environment, not your training cutoff, for any date math or judgement of what is "latest".
