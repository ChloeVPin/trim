# Development Guidelines (trimmed for claude-haiku-5-5)

Follow the core rules in sections 1-5. Use the skill routing table in section 6 to decide which skill to load before doing that kind of work.

## 1. Core rules

- **TDD for changed behavior.** Before any production behavior change:
  1. RED: write a failing behavior test.
  2. GREEN: write the minimum code that passes it.
  3. REFACTOR: improve the code while tests stay green.
- **Behavior-preserving refactors and reductions** start from passing tests and stay green. Never write a fake RED test to make a refactor look like TDD.
- **Config, docs, dependency, CI, generated, or operational changes:** use evidence that fits the claim, such as running the config or checking reachability. If TDD or mutation testing does not apply, record `N/A` and the reason. Do not invent failing tests or artificial mutants.
- **Keep every increment working.** Tests pass after each step.
- **Test behavior, not implementation.** Test through the public interface of the layer the claim is about. Tests describe business behavior.
- **Mutation testing runs once per phase**, at the PR-readiness gate, after implementation and refactoring are done. Do not run the mutation harness between increments. You may use the mutator rules from the `mutation-testing` skill as a cheap design check.
  - A *phase* is one PR review boundary: usually one PR-sized, independently mergeable slice. It is not a whole feature, and not the lifecycle phases in `README.md`.
  - At the gate, kill valuable surviving mutants. Ask the user when the value of a survivor is unclear.
- **Wait for approval before every commit.**

## 2. Code rules

- TypeScript `strict` mode, always.
- No `any` unless a comment explains why. Use `unknown` at untrusted boundaries and narrow it.
- No type assertions (`as`) without a justification comment.
- Validate untrusted input with a runtime schema, and derive the type from it. If a production schema already defines the contract, reuse it. Do not define it again.
- Follow the repo's convention for `type` vs `interface`. If there is none, follow language semantics.
- Prefer immutable values and pure functions. Keep mutation and side effects in a small, explicit boundary.
- Use an options object when positional parameters are ambiguous.
- Use early returns when they make branches clearer.
- Comment only the non-obvious *why*: constraints and safety context.
- Choose simple and readable over clever.
- Tests: use factories for repeated or nested data. Clear one-off values can be inline. Organize tests by behavior and repo ownership.

## 3. Workflow

1. Read the relevant code. Give a first draft of the answer within 3-4 tool calls, then refine it.
2. For a planned behavior change, load `tdd` and `testing` before editing.
3. Implement the smallest change that makes the test pass.
4. Refactor only if it adds value, and only while tests are green.
5. When the phase is ready for PR, run the gate in section 1.
6. Report results honestly. If a test fails, show the output. If a step was skipped, say so.

## 4. Output and file boundaries

- Write a plan, design, or document file only if the user asks for it or the repo declares that location. Otherwise answer in chat.
- If the user asks for a plan, design, or document *only*, produce only that. Make no code changes.
- Do not edit `CLAUDE.md` or other local policy files unless the user asks. Route durable learnings through the `expectations` skill to their owner: code/tests, glossary, maintained docs, active plan, or repo policy.
- Run `/setup` only when the user asks to onboard or configure a project and approves the generated files.
- Add a PostToolUse typecheck/format hook only when the user authorizes project configuration.
- For planning files, use the repo's declared location. Use `plans/` only when the repo declares none.

## 5. Browser automation

- Try `agent-browser` first:
  1. `agent-browser open <url>`
  2. `agent-browser snapshot -i` to get element refs (`@e1`, `@e2`, ...)
  3. `agent-browser click @e1` or `agent-browser fill @e2 "text"`
  4. Run `snapshot` again after any page change.
- Run `agent-browser --help` for more commands.
- If `agent-browser` is not installed, use WebFetch, curl, or an MCP browser tool.
- When a claim depends on real browser behavior and the cost is justified, get real-browser evidence.

## 6. Skill routing

Load a skill only when its task applies. If a skill is marked *(if installed)* and is missing, use the fallback in its row.

| Task | Load |
|---|---|
| New or changed behavior | `tdd`, `testing` |
| Pure refactor | `refactoring` |
| Remove branches, states, deps, layers, flags, retries, or jobs (net removal is claimed) | `reduce-system-complexity` |
| Mutation check at the PR gate | `mutation-testing` |
| TypeScript patterns | `typescript-strict` |
| Functional patterns | `functional` |
| API or interface design | `api-design` |
| OAuth 2.0 or OpenID Connect | `secure-oauth-oidc` |
| Front-end flow with async steps, retries, timers, cancellation, or an interruptible gesture | `xstate`. Load it before reaching for `useState`. |
| React or Next.js performance | `react-performance` |
| Read-only view of how code composes | `render-code-shape` |
| Hexagonal architecture project | `hexagonal-architecture` |
| Domain-Driven Design project | `domain-driven-design` |
| Event-sourced system or bounded context | `event-sourcing` |
| 12-factor service | `twelve-factor` |
| Production observability | `observability` |
| Whether to adopt a BFF, or its design | `bff-design` |
| Browser-facing BFF entry points, auth, CSRF, SSE/WebSocket | `bff-entry-points` |
| CLI tool design | `cli-design` |
| One module's responsibility and caller-facing contract | `codebase-design` |
| Source tree, folder layout, or migration | `structure-codebase` |
| Architecture improvement report across a repo | `improve-codebase-architecture` |
| Making untestable code testable | `finding-seams` |
| Documenting existing behavior before a change | `characterisation-tests` |
| Works locally but not in production or staging | `production-parity-skill-builder` |
| Before bespoke generic machinery: quick local/platform check. Before a named new dependency: due diligence only. For a consequential open choice: full comparison. Skip for domain logic, small glue, or routine use of an adopted tool. | `evaluate-existing-solutions` |
| Fuzzy product or design decision | `specification`. Also `grill-me` if installed. |
| New or changed domain term | `ubiquitous-language` |
| Broad story, epic, or feature | `story-splitting` |
| Significant implementation work | `planning` |
| Planned slice too large for one review, or stacked PRs | `stack-pull-requests` |
| Tighten an existing story, plan, or acceptance criteria | `find-gaps` |
| Read-only check that work meets a requirement | `acceptance-review` |
| Review a diff, branch, or PR; PR readiness | `panel-review` |
| Second opinion on finished work | `double-check` |
| Multi-surface design audit before code | `storyboard` |
| CI failure | `ci-debugging` |
| Local or runtime failure | `debugging` |
| Developer-facing docs | `technical-writing` |
| Plain-English or translation-ready prose | `simple-english` *(if installed)* |
| Reader-facing prose that feels generic | `clarity` *(if installed)* |
| Docs an agent reads (SKILL.md, CLAUDE.md, AGENTS.md) | `writing-for-agents` *(if installed)* |
| Create or evaluate a skill | `skill-creator` *(if installed)* |
| Grade installed skills | `skill-doctor` *(if installed)* |
| Find or install skills | `find-skills` |
| Multi-agent orchestrated run | `graph-engineering` |
| Learn a topic | `/teach-me [topic]` |

## 7. Before you report done

- [ ] Every behavior change has a test that failed first, or `N/A` is recorded with a reason.
- [ ] Tests pass. Any failure output is shown.
- [ ] No unexplained `any` or `as`.
- [ ] No commit was made without approval.
- [ ] No file was written that the user did not ask for.
- [ ] The mutation gate ran once at PR readiness, or `N/A` is recorded.
- [ ] Skipped steps are stated.

## 8. When a rule does not settle the choice

Pick the safest option that is easiest to reverse, state the choice in your reply, and ask the user one question. Ask first before any action that is hard to reverse or visible outside the workspace.
