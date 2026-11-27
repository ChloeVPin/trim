# Development Guidelines

## Core Rules

- **TDD for behavior changes.** Before changing production behavior, write a failing behavior test. Then write the minimum code that makes it pass. Then refactor while the tests stay green.
- **Refactors and reductions that do not change behavior** start from passing tests. Keep them green. Do not invent a failing test for them.
- **Non-behavior changes** (config, docs, dependencies, CI, generated code, operations) use evidence that fits the claim. If TDD does not apply, record `N/A` and the evidence you used instead.
- **Small steps.** Every increment leaves the codebase in a working state.
- **Wait for user approval before every commit.**
- **Test behavior, not implementation.** Test through the public interface of the layer the claim is about. Tests should describe expected business behavior.
- **Use factories** for repeated or nested test data.

## Mutation Testing

- Do not run the mutation harness after each increment, refactor, or commit.
- Run it once, at the PR-readiness gate: after implementation and refactoring are complete, when the phase is otherwise ready for review.
- A phase is one PR-sized, independently mergeable slice. In a stack, it is one stack member. It is not the whole feature.
- If mutation testing is not meaningful, record `N/A` with proportionate evidence (reachability, configuration, contract, integration, or operational checks).
- At the gate, address valuable surviving mutants and re-run focused checks. If the value of a survivor is unclear, ask the user.
- Before the gate, you may use the `mutation-testing` skill's mutator rules as test-design guidance only.

## TypeScript

- Strict mode, always.
- No `any` without a written justification. Use `unknown` at untrusted boundaries.
- No type assertions without a written justification.
- At runtime trust boundaries (input, network, storage), define a schema and derive the type from it.
- Reuse an existing production schema. Do not redefine the same contract.
- Follow the repository's convention for `type` vs `interface`.

## Code Style

- Prefer immutable values and pure functions. Isolate necessary mutation and side effects.
- Use early returns when they make branching clearer.
- Use an options object when positional parameters are ambiguous.
- Comments explain *why*, constraints, or safety context. Do not comment *what* the code does.
- Compose small private functions behind stable module contracts.

## Skills

Skills hold detailed patterns. Load a skill before starting work that matches its trigger. Do not load skills for work that does not match. If a skill is marked "when installed" and is not installed, use the fallback named.

| Trigger | Skill |
|---|---|
| Behavior-changing slice | `tdd`, `testing` |
| Refactoring | `refactoring` (add `reduce-system-complexity` if removing mechanism) |
| Removing branches, states, dependencies, layers, flags, retries, or jobs | `reduce-system-complexity` |
| Mutation check at the PR gate | `mutation-testing` |
| CI failure | `ci-debugging` |
| Local or runtime failure | `debugging` |
| Read-only check of finished work against a requirement | `acceptance-review` |
| Significant implementation | `planning` |
| Change too large for one review | `stack-pull-requests` with `planning` |
| Broad story, epic, or feature | `story-splitting` |
| Fuzzy product or design decision | `grill-me` (fallback: `specification` or one question at a time) |
| Fuzzy intent needing shared acceptance criteria | `specification` |
| New or changed domain term | `ubiquitous-language` |
| Tightening a story, plan, or acceptance criteria | `find-gaps` |
| Front-end flow with requests, retries, timeouts, or async state | `xstate` (check this before using `useState` for async state) |
| React or Next.js performance | `react-performance` |
| Making untestable code testable | `finding-seams` |
| Documenting existing behavior before a change | `characterisation-tests` |
| Reviewing a change, branch, or PR | `panel-review` |
| Second opinion on finished work | `double-check` |
| Adding a durable dependency or generic mechanism | `evaluate-existing-solutions` |
| Understanding or pseudocoding a code path (read-only) | `render-code-shape` |
| API design | `api-design` |
| OAuth or OpenID Connect | `secure-oauth-oidc` |
| Hexagonal architecture | `hexagonal-architecture` |
| Domain-Driven Design | `domain-driven-design` |
| Event-sourced system | `event-sourcing` |
| 12-factor service | `twelve-factor` |
| Production observability | `observability` |
| Backend-for-frontend (whether to adopt, responsibilities) | `bff-design` |
| Browser-facing BFF entry points, auth, cookies, CSRF | `bff-entry-points` |
| CLI tool design | `cli-design` |
| Module responsibility and caller-facing contract | `codebase-design` |
| Source tree or folder structure | `structure-codebase` |
| Architecture improvement across a repo | `improve-codebase-architecture` |
| Environment parity (works locally, not in production) | `production-parity-skill-builder` |
| Developer-facing docs (READMEs, guides, reference) | `technical-writing` |
| Agent-facing docs (SKILL.md, CLAUDE.md, pointer docs) | `writing-for-agents` (when installed) |
| Reader-facing prose that feels generic | `clarity` (when installed) |
| Plain-English or translation-ready prose | `simple-english` (when installed) |
| Authoring or evaluating a skill | `skill-creator` (when installed) |
| Installing skills from the open ecosystem | `find-skills` |

## Workflow Boundaries

- **Plan-only request:** produce only the plan or document. Make no code or test changes.
- **Files:** write a plan or document to disk only when the user asks for a file or the repository declares that location. Otherwise answer in chat.
- **Codebase exploration:** give a first draft within 3-4 tool calls, then refine it.
- **Onboarding (`/setup`) and project hooks:** only when the user asks to onboard or configure the project and authorizes the generated files.
- **CLAUDE.md:** edit it only when the user authorizes that write.
- **Learnings:** after significant changes, ask "What do I wish I'd known at the start?" Record durable learnings in their owner: code, tests, glossary, maintained docs, or the active plan.

## Browser Automation

- Use `agent-browser` first: `open <url>`, then `snapshot -i` to get element refs (`@e1`, `@e2`), then `click @e1` or `fill @e2 "text"`. Re-snapshot after each page change. Run `agent-browser --help` for all commands.
- If `agent-browser` is not installed, use WebFetch, curl, or an MCP browser tool.
- When a claim depends on browser behavior and the cost is justified, prefer real-browser evidence.

## Summary

Drive behavior changes with a test that describes the desired behavior. Write clean, testable code in small, safe steps. The simplest code that passes the test or check is the right code.
