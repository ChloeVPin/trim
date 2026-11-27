# Development Guidelines

Write clean, testable, functional TypeScript that evolves through small increments, each leaving the codebase working. When in doubt, choose simplicity and readability over cleverness. Detailed patterns live in skills; load the one that matches the task before starting it.

## Test-driven development

- Every new or changed production behavior starts from a failing behavior test (RED), gets the minimum code to pass (GREEN), then a refactor if it adds value. Repeat.
- Pure refactors and complexity reductions don't need a new failing test. Start from passing tests that preserve the behavior and keep them green.
- Test behavior through the public interface at the layer the claim is about. For example, an HTTP endpoint is the wrong interface for a claim about browser behavior. Tests should describe business behavior. Cover changed and high-risk paths in proportion to risk; a coverage percentage doesn't prove anything.
- Use factories for repeated or nested test data. One-off inline values and isolated lifecycle hooks are fine.
- Reuse an existing production schema in tests when it adds evidence instead of redefining the contract.
- For documentation, configuration, dependency, generated, CI, or operational changes, use evidence that fits the claim instead of a made-up RED test.

**Mutation testing** runs once per phase, at the PR-readiness gate after implementation and refactoring are done. Don't run it after every increment or commit. A phase is one PR review boundary: one mergeable slice, one member of a cross-slice stack, or one layer of an intra-slice stack. At the gate, run it on the accumulated scope, deal with survivors that matter, and re-run focused checks. Ask the user when it's unclear whether a survivor matters. Where mutation testing doesn't fit, record `N/A` with alternative evidence (reachability, config, contract, integration, operational). You can use the mutator rules from the `mutation-testing` skill earlier as test-design guidance without running the harness.

**Wait for my approval before every commit.**

## TypeScript and code style

- Strict mode always. Don't use `any` without an explanation; use `unknown` at untrusted boundaries and keep unavoidable interop contained. Every type assertion needs a justification.
- Define schemas at runtime trust boundaries and derive types from them. For trusted internal logic, use plain types, smart constructors, or domain values.
- Follow the repository's convention for `type` vs `interface`.
- Prefer immutable values and pure functions. Keep mutation and effects explicit and contained, and use them only where a boundary, a library, or a measured performance need calls for them.
- Compose small private functions behind cohesive, stable module contracts. A helper doesn't need to be its own public module.
- Use an options object when positional parameters would be ambiguous. Comments explain why, constraints, and safety context, not what the code does.

## Skill routing

Load the matching skill before starting the work. Most skills are named after their task. Rules that aren't obvious:

- **Behavior-changing slice:** load `tdd` and `testing`, plus `refactoring` if it applies, before changing code. **Pure refactor or reduction:** load `refactoring`, plus `reduce-system-complexity` when you claim to remove mechanism. Don't load the full RED workflow for that.
- **Upstream of code:** `grill-me` if installed (otherwise `specification`) for unclear decisions → `specification` for acceptance criteria → `story-splitting` for broad items → `planning` for one selected slice. Save plans where the repo declares; use `plans/` only as a fallback. Add `stack-pull-requests` when a slice is too big to review as one PR. Use `find-gaps` to tighten an existing story or plan, writing the answers back into it.
- **Domain terms:** any new or changed term goes through `ubiquitous-language`. Never coin terms silently.
- **Front-end state:** load `xstate` *before* reaching for `useState`. State belongs in a machine if (a) something external changes it (request, response, error, retry, timeout, cancellation, stream message), or (b) the interaction has a middle that can be interrupted (pointer capture, a closing animation, document listeners). Flags like `isLoading`, double-submit guards, `useEffect` ignore flags, and timers that need clearing are hand-rolled statecharts. Check the repo's conventions for where machines live. If two options are genuinely tied, ask.
- **React performance:** with `react-performance`, measure a baseline first, change one thing at a time, measure again, and revert optimizations that weren't measured. Don't trade away immutability or typing for speed.
- **New generic mechanism or lasting dependency:** run `evaluate-existing-solutions` in proportion to the decision. Skip it for domain logic, small glue code, tools already in use, and ordinary fixes.
- **Writing:** `technical-writing` for human-facing docs; `writing-for-agents` for docs an agent reads (SKILL.md, CLAUDE.md); `clarity` for sentence-level prose quality; `simple-english` for plain-language requests (Strict mode only if STE is named).
- **Review:** `acceptance-review` for a read-only verdict against requirements, `double-check` for a second opinion, `panel-review` for reviewing a change or for the PR-readiness gate.

Other skills (each named after its task): `debugging`, `ci-debugging`, `finding-seams`, `characterisation-tests`, `functional`, `typescript-strict`, `api-design`, `secure-oauth-oidc`, `hexagonal-architecture`, `domain-driven-design`, `event-sourcing`, `twelve-factor`, `observability`, `cli-design`, `bff-design`, `bff-entry-points`, `codebase-design`, `structure-codebase`, `improve-codebase-architecture`, `render-code-shape` (read-only; it never authorizes an edit), `production-parity-skill-builder`, `storyboard`, `expectations`, `skill-creator`, `skill-doctor`, `find-skills`, `graph-engineering`, `/teach-me`.

## Scope and output

- When asked for a plan, design, or document, produce only that. Don't change code unless asked.
- Save a plan or document to a file only if I ask for one or the repository declares where it belongs. Otherwise answer in chat.
- When exploring a codebase, show a first draft within a few tool calls and refine it from there.
- Run `/setup` or add project hooks only when I ask for onboarding and authorize the generated files.
- After significant changes, ask "What do I wish I'd known at the start?" Route lasting, non-obvious learnings through `expectations` to where they belong. Edit CLAUDE.md only for the local working policy it owns, and only when authorized.

## Browser automation

Try `agent-browser` first; fall back to `WebFetch`, `curl`, or MCP browser tools. Workflow: `open <url>` → `snapshot -i` (gives refs like `@e1`) → `click @e1` / `fill @e2 "text"` → snapshot again after the page changes. Run `agent-browser --help` for everything else.
