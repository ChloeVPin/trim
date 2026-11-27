# Development Guidelines

Core rules live here. Detailed patterns live in skills; load the matching skill before starting the work it covers.

## Test-driven development

Every new or changed production behavior starts from a failing behavior test (RED), gets the minimum code to pass (GREEN), then a refactor only if it adds value. Keep the codebase working after each increment.

- Test behavior through the public interface at the layer the claim names. An HTTP endpoint test does not prove a browser claim.
- Pure refactors and reductions start from passing tests and stay green. Do not invent a RED test to assert implementation shape.
- For config, contract, integration, operational, or unreachable changes, record proportionate alternate evidence and `N/A` instead of a fake RED or fake mutants.
- Coverage percentage is not proof. Use factories for repeated or nested test data. Reuse an existing production schema in tests instead of redefining it.
- **Ask for approval before every commit.**

**Mutation testing runs once per phase, at PR readiness.** A phase is one PR review boundary: one independently mergeable slice, or one member of a stack. Do not run the mutation harness after each increment, refactor, or commit. At the gate, address valuable survivors and re-run focused checks; ask me when a survivor's value is unclear. Earlier, you may use the `mutation-testing` mutator rules as cheap test-design guidance.

Before a behavior-changing slice, load `tdd`, `testing`, and the relevant refactoring skill. For a pure refactor, load only the testing/refactoring skills that apply, plus `reduce-system-complexity` when claiming net removal of mechanisms.

## TypeScript and code style

- Strict mode. No unexplained `any`; use `unknown` at untrusted boundaries. Justify every type assertion.
- Define schemas at runtime trust boundaries and derive types from them; use plain types or smart constructors internally.
- Follow repository convention for `type` vs `interface`.
- Prefer immutable values and pure functions; keep necessary mutation and effects explicit and contained.
- Comments explain non-obvious why, constraints, and safety context.
- Small private functions behind cohesive, stable module contracts. One helper is not one public module.

## Front-end state (xstate)

Load `xstate` before reaching for `useState`, not only when a file already imports xstate. State belongs in a machine when an external answer changes it (request, response, error, retry, timeout, cancellation, stream message) or the interaction has an interruptible middle (drag with pointer capture, closing animation, gesture with document listeners). It stays in React only when one event sets it completely and nothing needs interrupting or disposing. A `submitting`/`isLoading` flag, a double-submit guard, a `useEffect` with an ignore flag, or a timer that must be cleared is a hand-rolled statechart. Check repository conventions for which layer owns machines; ask on a genuine tie.

For React performance, load `react-performance`: measure first, change one thing at a time, re-measure, and revert optimizations that don't measurably help. Behavior tests stay unchanged.

## New dependencies and generic mechanisms

Before adding a durable dependency or bespoke generic machinery, load `evaluate-existing-solutions`, scaled to the stakes. Skip it for domain logic, small glue, already-adopted tools, and ordinary fixes.

## Skill routing where descriptions overlap

- Fuzzy product decisions: `grill-me` if installed; otherwise `specification`.
- Writing: `technical-writing` for human-facing docs (structure, claims); `clarity` for sentence-level voice; `simple-english` for plain-English/STE requests (Plain mode unless STE is named); `writing-for-agents` for agent-facing docs such as SKILL.md or CLAUDE.md.
- Skills: `skill-creator` to author or eval a skill; `skill-doctor` to grade installed skills against past conversations.
- Review: `panel-review` for reviewing a change boundary and the PR-readiness gate; `double-check` for a second opinion on finished work; `acceptance-review` for a read-only verdict on whether work meets a requirement.
- `render-code-shape` is read-only and never authorizes an edit.
- Planning: `story-splitting` before `planning` for broad items; add `stack-pull-requests` when a slice is too large for one review. Use `plans/` only when the repository declares no planning location.

## Scope and output

- When asked for a plan, design, or document, produce only that. No code or implementation changes unless asked.
- Write a file only when I ask for one or the repository declares that location as the owner; otherwise answer in chat.
- When exploring a codebase, produce a first draft within 3–4 tool calls and refine from there.
- Run `/setup` only when I ask to onboard a project and authorize the generated files.
- Route durable, non-obvious learnings through `expectations` to their real owner (code, tests, glossary, docs, plan). Edit CLAUDE.md only for policy it owns, and only when authorized.

## Browser automation

Use `agent-browser` first; fall back to `WebFetch`, `curl`, or MCP browser tools if it isn't installed. Workflow: `open <url>`, `snapshot -i` for element refs, `click @e1` / `fill @e2 "text"`, re-snapshot after page changes. See `agent-browser --help`.
