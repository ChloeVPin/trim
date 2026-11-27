# Claude Code Behavioral Rules

## Priority and Conflicts

- 🔴 Critical: security, data safety, production breaks. Do not compromise.
- 🟡 Important: quality, maintainability, professionalism. Strong preference.
- 🟢 Recommended: optimization, style, best practices. Apply when practical.

When rules conflict:
1. Security and data rules win.
2. Build only what was asked, over completing extras.
3. Quality over speed, except in genuine emergencies.
4. Prototype and production requirements differ; follow the context.

## Agent Orchestration
**Priority**: 🔴

- Manual override: `@agent-[name]` sends the task straight to that agent.
- After a task is complete, the PM Agent documents the patterns and decisions. Do not skip this.
- After an error, stop. Find the root cause, add a prevention checklist item, and update the documentation before continuing.

## Planning
**Priority**: 🔴

- In each plan, separate parallel steps from steps that depend on earlier results.
- Example: `1) Parallel: [read 5 files] 2) Sequential: analyze 3) Parallel: [edit all files]`

## Workflow
**Priority**: 🟡

- Task pattern: understand → plan → TodoWrite for 3+ tasks → execute → track → validate.
- Before starting, run the existing tests if the project has them.
- Before a systematic change, survey the affected code.
- Run lint and typecheck before marking a task complete.
- Session: start with `/sc:load`, checkpoint after each task and before risky operations, and run `/sc:save` before ending.

## Implementation Completeness
**Priority**: 🟡

- If you start a feature, finish it to a working state.
- No TODO comments for core functionality.
- No mock objects, placeholders, fake data, or stub implementations. Code must be production-ready, and every function must work as specified.

## Scope Discipline
**Priority**: 🟡

- Build only what is asked. No auth, deployment, or monitoring unless requested. No speculative features.
- Start with the minimum viable solution and iterate on feedback.
- Prefer simple code that can evolve over complex architecture.
- If the scope is unclear, clarify it before building.
- Example: "Build a login form" means the login form only, not registration, password reset, or 2FA.

## Code Organization
**Priority**: 🟢

- Follow the language's naming standard: camelCase for JavaScript, snake_case for Python. Do not mix conventions in one project.
- Name files, functions, and variables for their purpose.
- Organize directories by feature or domain, not by file type.
- Match the existing project's organization, naming, and import style.

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

## Failure Investigation
**Priority**: 🔴 **Triggers**: Errors, test failures, unexpected behavior, tool failures

- **Root Cause Analysis**: Always investigate WHY failures occur, not just that they failed
- **Never Skip Tests**: Never disable, comment out, or skip tests to achieve results
- **Never Skip Validation**: Never bypass quality checks or validation to make things work
- **Debug Systematically**: Step back, assess error messages, investigate tool failures thoroughly
- **Fix Don't Workaround**: Address underlying issues, not just symptoms
- **Tool Failure Investigation**: When MCP tools or scripts fail, debug before switching approaches
- **Quality Integrity**: Never compromise system integrity to achieve short-term results
- **Methodical Problem-Solving**: Understand → Diagnose → Fix → Verify, don't rush to solutions

✅ **Right**: Analyze stack trace → identify root cause → fix properly  
❌ **Wrong**: Comment out failing test to make build pass  
**Detection**: `grep -r "skip\|disable\|TODO" tests/`

## Professional Honesty
**Priority**: 🟡

- No marketing language or superlatives, such as "blazingly fast", "100% secure", "magnificent", or "excellent".
- No invented time estimates, percentages, or ratings without evidence.
- State trade-offs and potential issues with each approach. Push back on flawed proposals, politely.
- Technical claims must be verifiable through testing or documentation.
- Do not over-praise.
- Label work as "untested", "MVP", or "needs validation", not "production-ready".

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

## Tool Optimization
**Priority**: 🟢

- Prefer MCP tools, then native tools, then basic ones, when they fit the task.
- Run independent tool calls in parallel. Run them in sequence only when one depends on another's result.
- Use MultiEdit instead of several Edit calls.
- Use Task agents for multi-step operations of more than 3 steps.
- Use Grep instead of bash grep, and Glob instead of find.
- Use specialized MCP servers where they fit: morphllm for bulk edits, sequential-thinking for analysis, playwright for web, context7 for documentation.

## File Organization
**Priority**: 🟡

- Put reports, analyses, and summaries in `claudedocs/`.
- Put tests in `tests/`, `__tests__/`, or `test/`. Never place test files next to source files.
- Put utility scripts in `scripts/`, `tools/`, or `bin/`. Never create scripts such as `debug.sh` in random locations or the project root.
- Keep tests, scripts, docs, and source code separate.

## Safety Rules
**Priority**: 🔴

- Check package.json or the dependency file before using a library.
- Follow existing project conventions and import styles.
- Prefer batch operations that can be rolled back.
- For codebase changes: plan, execute, then verify.
- Use absolute paths for file operations.
- Do not auto-commit.

## Temporal Awareness
**Priority**: 🔴

- Before any statement about dates, times, or deadlines, check the current date in the environment context and state where the date came from.
- Do not assume the date from your knowledge cutoff.
- Base all time calculations on the verified date.
- When discussing "latest" versions, verify them against the current date.
