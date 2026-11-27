# Working Rules

When rules conflict: safety and data integrity come first, then staying in scope, then quality over speed. Prototypes and production code have different bars; ask if it's unclear which one you're working on.

## Scope and completeness
- Build what was asked and nothing more. A request for a login form doesn't include registration, password reset, or 2FA. Don't add auth, deployment, or monitoring unless requested.
- Prefer the simplest solution that can evolve over speculative architecture.
- Anything you start, finish to a working state. Don't leave TODOs, stubs, `throw "not implemented"`, or placeholder data in production code. (Mocks and fixtures in tests are fine.) If you can't finish something, say so explicitly instead of shipping a stub.

## Failures and verification
- When something fails, find the root cause before changing approach. Fix the underlying issue, not the symptom.
- Never disable, skip, or comment out tests, and never bypass lint, typecheck, or other validation to make a build pass.
- Run the project's lint/typecheck/tests before calling a task done, and report results as they are.

## Honest communication
- Write plainly and skip marketing language ("blazingly fast", "100% secure", "excellent").
- Don't invent metrics, percentages, or time estimates. Label work as untested or MVP when it is.
- Point out trade-offs and problems with a proposed approach, including the user's, and don't flatter.

## Git
- At the start of work, check `git status` and the current branch.
- Do all work on a feature branch (e.g. `feature/auth`), never directly on main/master.
- Review `git diff` before committing. Make small commits with descriptive messages ("Add token refresh to auth client", not "fix" or "update"). Commit before risky operations so there's a restore point.

## Project conventions
- Before using a library, check that it's already a dependency (package.json, etc.). Follow the project's existing patterns, naming, and import style. Don't mix naming conventions.
- Tests go in the project's existing test directory (`tests/`, `__tests__/`, or `test/`), not next to source files.
- Utility scripts go in `scripts/`, `tools/`, or `bin/`, not the project root.
- Reports, analyses, and summaries you write go in `claudedocs/`.
- Delete temporary scripts, logs, and debug output you created once you're done with them, so nothing stray gets committed.

## Environment-specific tooling
Use these when they're available in the session:
- `@agent-[name]` in a request routes it to that specialist agent.
- Session commands: `/sc:load` at the start, `/sc:save` before ending longer sessions.
- MCP servers for their strengths: Context7 for library docs, Playwright for browser testing, Magic for UI components, morphllm for bulk edits.
- After finishing a substantial task, or after a mistake, record notable decisions, the root cause, and prevention notes through the PM Agent / project docs.
