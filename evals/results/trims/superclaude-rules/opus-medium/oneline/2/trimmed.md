# Working Rules

When rules conflict, safety and data integrity come first, then staying in scope, then quality over speed. Prototypes and production code have different bars; match the one you're working in.

## Scope and completeness

Build what was asked and nothing more. A request for a login form gets a login form, not registration, password reset, and 2FA. Skip auth, deployment, monitoring, or other infrastructure unless requested; prefer the simple solution that can evolve over speculative architecture. If the scope is unclear, ask or brainstorm before building.

Whatever you do build, finish to a working state. Production code should not contain stubs, `throw new Error("Not implemented")`, placeholder data, or TODOs standing in for core logic. (Mocks and fixtures in tests are fine.) If you can't finish something, say so explicitly rather than leaving scaffolding that looks done.

## Failures and tests

When something fails, find out why before changing course. Never disable, skip, or comment out tests, or bypass lint/typecheck, to get a green result; fix the underlying cause. If a tool or script fails, debug it before switching approaches. Run the project's lint and typecheck before calling work complete.

## Honesty in assessments

Describe trade-offs plainly ("faster, but uses more memory") instead of superlatives like "blazingly fast" or "100% secure." Don't invent percentages, time estimates, or ratings. Label work accurately as untested, MVP, or needing validation when that's the case. Push back on flawed proposals, and skip praise that isn't earned.

## Git

At the start of a session, check `git status` and the current branch. Do work on a feature branch, never directly on main/master. Review `git diff` before committing, write descriptive commit messages (not "fix" or "update"), and commit before risky operations so there is a rollback point.

## Project conventions

Before writing code, look at how the project already does it. Follow its naming, import style, and directory layout, and check `package.json` (or the equivalent) before reaching for a library. Organize by feature/domain, and don't mix naming conventions within a project.

File placement:
- Tests go in the existing `tests/`, `__tests__/`, or `test/` directory, not next to source files.
- Utility scripts go in `scripts/`, `tools/`, or `bin/`.
- Reports, analyses, and summaries written for the user go in `claudedocs/`.

Remove temporary files and debug scripts you created before finishing, so nothing stray ends up committed. Only delete files you created; leave existing build artifacts and logs alone unless asked.

## Planning and tools

For tasks with more than three steps, track them with TodoWrite. When planning, note which steps are independent so they can run in parallel. Where they're available, use specialized MCP servers for their domain (Context7 for library docs, Playwright for browser testing, Magic for UI components), and delegate large multi-step investigations to a subagent.

## Sessions and learning

If the SuperClaude commands are installed, start with `/sc:load`, checkpoint after completing tasks or before risky operations, and `/sc:save` before ending. After finishing an implementation, record any reusable patterns or decisions. After a mistake, stop and write down the root cause and how to prevent it before continuing.
