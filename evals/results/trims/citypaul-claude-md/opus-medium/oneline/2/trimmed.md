# Development Guidelines

Core working policy. Detailed patterns live in skills; load the matching skill before acting in its area.

## Behavior changes: TDD

- New or changed production behavior starts from a failing behavior test: RED → minimum code for GREEN → refactor while green → repeat. Each increment leaves the codebase working.
- Pure refactors and reductions start from passing preservation evidence and stay green. Don't fabricate a RED test to assert implementation shape.
- For configuration, contract, integration, CI, docs, dependency, or operational changes where a behavior test doesn't fit, record proportionate alternate evidence and mark mutation `N/A`.
- Before behavior-changing work, load `tdd`, `testing`, and any applicable refactoring skill. For pure reductions, load `refactoring` / `reduce-system-complexity` and say why other skills are `N/A`.

## Mutation testing gate

Run the mutation harness once per phase, at PR readiness, after implementation and refactoring are finished. Don't run it after each increment or commit. A phase is one PR review boundary: one mergeable slice, or one member/layer of a stack. It is not a whole feature and not the lifecycle phases in `README.md`. At the gate, address valuable survivors and re-run focused checks. Ask the human when a survivor's value is unclear. You can use the `mutation-testing` mutator rules earlier as cheap test-design guidance.

## Testing

- Test behavior through the public interface at the layer the claim names (an HTTP test can't prove a browser claim). Prefer real-browser evidence for browser claims when the cost is justified.
- Tests document business behavior. Cover changed and high-risk behavior proportionately; a coverage percentage proves nothing.
- Use factories for repeated or nested data. Clear one-off values and isolated hooks are fine.
- Organize tests by behavior and repository ownership.

## TypeScript and style

- Use strict mode. Don't use `any` without an explanation; use `unknown` at untrusted boundaries and contain interop. Justify every type assertion.
- Put schemas at runtime trust boundaries and derive types from them. Use plain types or smart constructors for trusted internal logic. Reuse an existing production schema rather than redefining the contract.
- Follow the repo's convention for `type` vs `interface`.
- Prefer immutable values and pure functions. Contain mutation where a boundary, library, or measured performance need requires it, and keep effects explicit.
- Compose small private functions behind cohesive, stable module contracts. Use an options object when positional parameters are ambiguous. Write comments for the non-obvious why.
- Favor simplicity and readability over cleverness.

## Front-end state (`xstate`)

Load `xstate` before reaching for `useState`. State belongs in a machine if an external answer changes it (request, response, error, retry, timeout, cancellation, stream message) or the interaction has an interruptible middle (drag with pointer capture, closing animation, document listeners). It stays in React only when one event sets it completely and there's nothing to interrupt or dispose. `isLoading`/`submitting` flags, double-submit guards, effects that need ignore flags, and timers that must be cleared are hand-rolled statecharts. If an actor already owns that lifecycle, the state goes in that actor. Check the repo's convention for where machines live, and ask on a genuine tie.

## React performance

Load `react-performance`. Baseline first, attribute the cost with evidence, apply one rule at a time, then re-measure. Revert optimizations you didn't measure. Never trade away behavior tests, immutability, or typing for speed.

## New mechanisms and dependencies

Before adding bespoke generic machinery or a durable new dependency, load `evaluate-existing-solutions` and scale the effort to the stakes. Skip it for domain logic, small glue, tools already adopted, and ordinary fixes.

## Skill routing where it isn't obvious

- Fuzzy decisions: `grill-me` if installed, otherwise `specification`. Broad stories: `story-splitting`, then `planning`. Use the repo's declared plan location, and `plans/` only as a fallback. Slices too big for one PR: `stack-pull-requests`.
- Domain terms: `ubiquitous-language`. Never coin terms silently.
- Prose: `technical-writing` for human readers, `writing-for-agents` for agent-consumed docs (choose by audience, not file type). `clarity` for voice and sentences, `simple-english` for plain-English/STE requests (Strict mode only when STE is named).
- Skills: `skill-creator` to author and evaluate, `skill-doctor` for retrospective grading, `find-skills` to discover.
- Review: `panel-review` for any change boundary and the pre-PR evidence gate. `acceptance-review` for read-only checks against requirements. `double-check` for a second opinion.

## Workflow guardrails

- Wait for approval before every commit.
- When asked for a plan, design, or document, produce only that. Don't make code changes. Write it to a file only if asked or if the repo declares a durable home for it. Otherwise answer in chat.
- When exploring, produce a first draft within 3–4 tool calls and refine from there.
- Run `/setup` or add project hooks only when the user explicitly authorizes project configuration.
- After significant changes, ask "What do I wish I'd known at the start?" Route durable learnings through `expectations` to their real owner (code/tests, glossary, decisions, docs, plan). Edit this file only for working policy it owns, and only when authorized.

## Browser automation

Try `agent-browser` first: `open <url>`, then `snapshot -i` for refs, then `click @e1` / `fill @e2 "text"`, and re-snapshot after page changes. See `--help` for more. If it isn't installed, fall back to WebFetch, curl, or MCP browser tools.
