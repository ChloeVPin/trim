# Development Guidelines for Claude

Write clean, testable code in small, safe steps. Each step leaves the code working.

## Core Rules

- **TDD for behavior changes.** Before changing production behavior, write a failing test that describes the desired behavior. Then write the minimum code that makes it pass. Then refactor while the tests stay green.
- **Behavior-preserving refactors** start from passing tests and stay green. They do not need a new failing test.
- **Non-behavior changes** (docs, config, dependencies, generated files, CI, operations) use proportionate evidence instead of a RED test. Record `N/A` and say what the evidence is. Do not invent failing tests or fake mutants.
- **Wait for approval before every commit.**
- **Ask when unsure.** Do not guess, especially when two options are genuinely tied.

## Mutation Testing

- A **phase** is one PR-sized, independently mergeable slice. In a stack, it is one layer or one slice member. It is not a whole multi-PR feature.
- Run mutation testing **once per phase**, at the PR-readiness gate, after implementation and refactoring are done. Do not run it after each increment.
- At the gate, fix valuable surviving mutants, then re-run the focused checks. If a survivor's value is unclear, ask.
- If mutation testing does not apply, record `N/A` with reachability, configuration, contract, integration, or operational evidence.
- Between increments, use the `mutation-testing` skill's mutator rules only as test-design advice.

## Testing

- Test behavior, not implementation.
- Test through the public interface at the layer the claim is about. An HTTP endpoint is the wrong interface for a browser claim.
- Tests document expected business behavior.
- Use factories for repeated or nested test data. Clear one-off values and isolated lifecycle hooks are fine.
- Coverage percentage is not proof. Cover changed and high-risk behavior.
- Follow the repository's test harness. Prefer real-browser evidence when a claim depends on browser behavior and the cost is justified.

## TypeScript

- Strict mode, always.
- No `any` unless it is explained and contained at an interop boundary.
- Use `unknown` for untrusted input. Validate it with a runtime schema at the boundary and derive the type from that schema.
- No type assertions without a justifying comment.
- Inside trusted internal logic, use plain types or domain values.
- Reuse an existing production schema. Do not redefine the same contract.
- Follow the repository's convention for `type` vs `interface`.

## Code Style

- Prefer immutable values and pure functions. Isolate necessary mutation and side effects.
- Use early returns when they make branching clearer.
- Use an options object when positional parameters are ambiguous.
- Keep modules cohesive behind stable contracts. Small private helpers are fine.
- Comment the *why*, constraints, and safety concerns. Do not comment the obvious *what*.
- Write the simplest code that passes the test. When in doubt, choose simplicity and readability.

## Front-End State

- If an external event changes the state (request, response, error, retry, timeout, cancellation, stream message, BFF call), or the interaction can be interrupted (drag, closing animation, document listeners), use an xstate machine. Do not hand-roll it.
- Hand-rolled red flags: `isLoading` or `submitting` flags, double-submit guards, chained promise state, `useEffect` ignore flags, manual timers.
- `useState` is fine only when one event sets the value completely and nothing needs cancelling.
- Check where the repository already keeps its machines. Ask on a genuine tie.

## Output and Scope

- **Artifact boundary:** Write a plan or document to a file only when the user asks for it or the repository declares that location. Otherwise, answer in chat.
- **Plan-only requests:** If asked only for a plan, design, or document, produce only that. Do not write production or test code.
- **Explore briefly:** Give a first draft within 3–4 tool calls, then refine.
- **Project setup:** Run `/setup` only when the user asks to onboard or configure the project and approves the generated files.
- **Hooks:** Add a PostToolUse typecheck or format hook only with explicit onboarding authorization, using the repository's existing toolchain.
- **Learnings:** After significant changes, ask "What do I wish I'd known at the start?" Record durable learnings with the `expectations` skill, in their proper owner (code or tests, glossary, docs, or plan).
- **CLAUDE.md:** Edit it only for local working policy it owns, and only when the request or repository workflow authorizes the edit.

## Browser Automation

1. Try `agent-browser` first: `agent-browser open <url>`.
2. Run `agent-browser snapshot -i` to get interactive elements with refs (`@e1`, `@e2`).
3. Interact with `agent-browser click @e1` or `agent-browser fill @e2 "text"`.
4. Re-snapshot after every page change. Run `agent-browser --help` for other commands.

If `agent-browser` is not installed, use WebFetch, curl, or an MCP browser tool.

## Skills (Load on Demand)

Load a skill only when the task matches its row. Do not load skills for tasks they do not cover.

| Task | Skill |
|---|---|
| Behavior change (TDD) | `tdd`, `testing` |
| Pure refactor | `refactoring` |
| Remove branches, states, deps, layers, flags, retries, or jobs | `reduce-system-complexity` |
| Mutation check at the PR gate | `mutation-testing` |
| TypeScript patterns | `typescript-strict` |
| Functional patterns | `functional` |
| API design | `api-design` |
| OAuth 2.0 or OIDC | `secure-oauth-oidc` |
| Fuzzy product or design decision | `grill-me` (or `specification`) |
| Turn fuzzy intent into acceptance criteria | `specification` |
| New or changed domain term, glossary | `ubiquitous-language` |
| Broad story, epic, or feature | `story-splitting` |
| Tighten a story, plan, or acceptance criteria | `find-gaps` |
| Significant implementation planning | `planning` |
| Split a slice into stacked PRs | `stack-pull-requests` |
| CI failure | `ci-debugging` |
| Local or runtime failure | `debugging` |
| Read-only check that work meets a requirement | `acceptance-review` |
| Review a diff, branch, or PR; PR-readiness gate | `panel-review` |
| Second opinion on finished work | `double-check` |
| Multi-agent orchestration | `graph-engineering` |
| Hexagonal architecture | `hexagonal-architecture` |
| Domain-Driven Design | `domain-driven-design` |
| Event-sourced systems | `event-sourcing` |
| 12-factor services | `twelve-factor` |
| Production observability | `observability` |
| CLI design | `cli-design` |
| Backend-for-frontend (whether and how) | `bff-design` |
| Browser-facing BFF entry points, auth, CSRF, SSE/WebSocket | `bff-entry-points` |
| A module's responsibility and contract | `codebase-design` |
| Source tree, folder, or route layout | `structure-codebase` |
| Architecture improvement report | `improve-codebase-architecture` |
| Read-only view of how code composes | `render-code-shape` |
| Front-end flow logic | `xstate` |
| React or Next.js performance | `react-performance` |
| React component tests | `react-testing`, `front-end-testing` |
| Make untestable code testable | `finding-seams` |
| Document existing behavior before changing it | `characterisation-tests` |
| Environment parity (works locally, not in prod) | `production-parity-skill-builder` |
| Multi-surface design audit | `storyboard` |
| Structured learning or tutoring | `teach-me` (`/teach-me [topic]`) |
| Developer-facing prose (READMEs, guides, reference) | `technical-writing` |
| Reader-facing prose that feels generic | `clarity` |
| Plain-English or translation-friendly prose | `simple-english` |
| Agent-facing docs (SKILL.md, CLAUDE.md, AGENTS.md) | `writing-for-agents` |
| Create or evaluate a skill | `skill-creator` |
| Grade installed skills against past conversations | `skill-doctor` |
| Install skills from the ecosystem | `find-skills` |
| Before adding a material mechanism or new dependency | `evaluate-existing-solutions` |

## Summary

Drive every production-behavior change with a test that describes the desired behavior. Use claim-appropriate evidence for everything else. Write the simplest code that passes. When in doubt, favor simplicity and readability.
