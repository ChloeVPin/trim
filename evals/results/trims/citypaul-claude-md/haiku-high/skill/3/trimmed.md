# Development Guidelines for Claude

Skills available on demand: specification, ubiquitous-language, planning, story-splitting, stack-pull-requests, acceptance-review, debugging, ci-debugging, tdd, testing, mutation-testing, test-design-reviewer, typescript-strict, functional, refactoring, reduce-system-complexity, expectations, front-end-testing, react-testing, react-performance, xstate, render-code-shape, hexagonal-architecture, domain-driven-design, event-sourcing, twelve-factor, api-design, secure-oauth-oidc, bff-design, bff-entry-points, cli-design, codebase-design, improve-codebase-architecture, structure-codebase, evaluate-existing-solutions, finding-seams, characterisation-tests, production-parity-skill-builder, storyboard, teach-me, diagrams, technical-writing, find-skills, find-gaps, double-check, graph-engineering, review.

External skills: impeccable (with 17 steering commands), seo-audit, web quality and clarity (Addy Osmani), simple-english, Next.js and React skills (Vercel), grill-me, writing-for-agents, skill-creator, skill-doctor.

## Core Philosophy

Follow test-driven development (TDD) with a behavior focus and functional programming. Make small, incremental changes that keep the codebase working.

- Behavior changes require a failing behavior test first. Pure behavior-preserving refactoring and mechanism reduction start from passing preservation evidence and stay green.
- For documentation, configuration, dependency, generated, CI, and operational changes, use claim-appropriate evidence instead of a test-first cycle.
- Use mutation evidence where it is meaningful. For unreachable, configuration, contract, integration, or operational changes, record proportionate alternate evidence and `N/A` instead of fabricating RED tests or structural mutants.
- A **phase of work** is one PR review boundary: normally one PR-sized, independently mergeable slice; in a cross-slice stack, one whole-slice member; in an intra-slice stack, one focused dependent layer. It is not a multi-PR feature or stack, nor the numbered lifecycle phases in `README.md`.

## Testing

- Follow the repository's test harness.
- Test behavior, not implementation. Test through the subject's public interface at the layer the claim names (an HTTP endpoint is the wrong interface for a browser claim).
- Tests must document expected business behavior.
- Use factories for repeated or nested test data. Isolated lifecycle hooks and clear one-off values are valid.
- Organize tests around behavior and repository ownership, not a fixed file-count rule.
- Cover changed and high-risk behavior proportionately. A coverage percentage is not proof.
- Prefer real-browser evidence when the claim depends on browser behavior and the cost is justified.
- Load `testing` for detailed patterns. Load `mutation-testing` at the end-of-phase PR-readiness gate; before that, use its mutator rules for test design only, without running the harness.

## TypeScript

- Strict mode always. No unexplained `any`. Use `unknown` at untrusted boundaries and contain unavoidable interop.
- No type assertions without justification.
- Follow repository convention for `type` vs `interface`, then language semantics.
- Define schemas at runtime trust boundaries and derive types from them. Use plain types, smart constructors, or domain values for trusted internal logic.
- Reuse an existing production schema when it adds test evidence. Do not redefine the same contract.
- Load `typescript-strict` for detailed patterns, `api-design` for API and interface design, and `secure-oauth-oidc` for any OAuth 2.0 or OpenID Connect design, implementation, review, testing, incident analysis, or migration.

## Code Style

- Prefer immutable values. Contain mutation where a boundary, library, or measured performance need requires it.
- Use pure functions wherever possible. Use early returns or composition when they make branching clearer.
- Comments explain non-obvious why, constraints, and safety context.
- Use an options object when positional parameters are ambiguous or unstable.
- Choose array methods or loops by clarity, control flow, and measured needs.
- Compose small private functions behind cohesive, stable module contracts. Do not equate one helper with one public module.
- Load `functional` for detailed patterns.

## Development Workflow

- **RED**: write a failing behavior test before new or changed behavior.
- **GREEN**: write the minimum code that passes the test.
- **REFACTOR OR REDUCE**: assess applicable improvements while ordinary behavior tests stay green. Refactor after a green step only if it adds value.
- **REPEAT**: continue the inner cycle. Do not run the automated mutation harness after each increment, refactor, or commit.
- **PRE-PR MUTATION GATE**: when the phase is otherwise ready for a PR, run mutation testing once for the accumulated scope, where meaningful. Otherwise record `N/A` with proportionate reachability, configuration, contract, integration, or operational evidence.
- **KILL MUTANTS**: at that gate, address valuable survivors and re-run focused or diff mutation checks. Ask the human when the value is ambiguous.
- **Wait for commit approval before every commit.**
- Each increment leaves the codebase in a working state.
- Load `tdd` for the detailed TDD workflow. For a behavior-changing planned slice, load `tdd`, `testing`, and applicable refactoring guidance before code changes begin. Do not load the full RED workflow just to assert implementation shape.
- For a pure behavior-preserving refactor or reduction, load only the applicable testing, refactoring, and reduction skills during implementation, then apply mutation testing or alternate evidence at the PR gate. Record why any other skill is `N/A`.
- Load `refactoring` for refactoring methodology.
- Load `reduce-system-complexity` when removing branches, states, dependencies, layers, flags, retries, jobs, or operational parts from an existing path while conserving behavior, or when net mechanism removal is claimed. Pure reductions use the REFACTOR path, not a fabricated structural RED test.

## Loading Skills by Task

- **Fuzzy product or design decision**: load `grill-me` when installed. Otherwise use the host's one-question mechanism or `specification` to pressure-test the decision tree before writing stories or plans.
- **Turning fuzzy intent into shared understanding and acceptance criteria** (agent draft, then human review proportionate to risk): `specification`.
- **Domain concepts, glossary work, or any new or changed domain term**: `ubiquitous-language`, which follows a five-step protocol and never coins terms silently.
- **Broad story, epic, feature, or backlog item**: `story-splitting` before planning.
- **Tightening an existing story, plan, acceptance criteria, or mock spec**: `find-gaps`, writing confirmed answers back into the artifact.
- **Significant implementation**: `planning`, for the repository's declared planning workflow and location. Use `plans/` only as the documented fallback.
- **A planned vertical slice too large for review, or later slices that should start on the same evolving baseline**: `stack-pull-requests` with `planning`. Choose independent PRs or an explicit hard- or flow-lineage stack. Do not turn technical layers into stories or slices.
- **CI failure**: `ci-debugging`.
- **Local or runtime failure**: `debugging`. Preserve evidence, localize one causal hypothesis at a time, and fix the earliest shared owning boundary when a fix is requested.
- **Read-only decision on whether finished work satisfies an authoritative requirement**: `acceptance-review`. Report every criterion with its evidence and an exact verdict.
- **Hexagonal architecture**: `hexagonal-architecture`. **Domain-Driven Design**: `domain-driven-design`.
- **Event-sourced systems or bounded contexts** (events as source of truth, Decider write model, event stores, projections, read models, versioning, snapshots): `event-sourcing`.
- **12-factor service**: `twelve-factor`. **Production observability** (wide events, OpenTelemetry, SLOs and alerting, telemetry testing): `observability`.
- **CLI tool design** (stream separation, format flags, exit codes, composability): `cli-design`.
- **Whether to adopt a backend-for-frontend, how many, what each may own, upstream aggregation and partial failure, or mediating user identity toward upstream services**: `bff-design`.
- **Browser-facing BFF or backend HTTP entry points** (public/protected classification, auth middleware, session cookies, CSRF/Origin policy, protected SSE/WebSocket registration, endpoint-protection enforcement): `bff-entry-points`.
- **A selected module's responsibility, caller-facing contract, information hiding, depth, leverage, or justified seams**: `codebase-design`.
- **Read-only render of how code composes** (entry points, module boundaries, types crossing them, signatures, cited call graph; `[NEW]` marks unbuilt work), to understand a path or pseudocode a change before implementing it: `render-code-shape`. It never authorizes an edit.
- **Architecture improvements across a repository or subsystem**, with a self-contained visual HTML report: `improve-codebase-architecture`.
- **Designing or auditing source trees**: route or feature ownership, state or design-system ownership, package boundaries, visible hexagonal layouts, feature folders, BFF route organization, composition roots, or folder migrations: `structure-codebase`.
- **Front-end flow logic**: load `xstate` before reaching for `useState`. Two tests decide ownership, not how a value renders:
  1. An external answer changed it (request, response, error, retry, timeout, cancellation, stream message, anything sent to a BFF), or
  2. The interaction has an interruptible middle (a drag holding pointer capture, a closing animation, a gesture binding document listeners).

  A disabled button or spinner presents temporal state; it does not own it. State stays in React only when both tests are empty: one event sets it completely, and nothing needs interrupting or disposing. A `submitting` or `isLoading` flag, a promise chain setting state in sequence, a double-submit guard, an error cleared before a retry, a `useEffect` needing an ignore flag, or a timer something must clear is a hand-rolled statechart. If an actor already owns that lifecycle, the state belongs in it. Check the repository's conventions for which layer owns machines before creating one. Ask rather than guess on a genuine tie.
- **React or Next.js performance**: `react-performance`. Baseline the symptom, attribute the cost with evidence, apply one rule at a time from the pinned `vercel-react-best-practices` catalogue, then re-measure. Behavior tests stay unchanged and green. Do not trade immutability or typing rules for speed. Revert unmeasured optimizations.
- **Before a material generic mechanism or durable new dependency**: `evaluate-existing-solutions`, proportionately. Run a lightweight local or platform preflight before bespoke generic machinery. For a named dependency already introduced, run due diligence without reopening alternatives. Use the full comparison only for consequential unresolved choices. Do not apply it to domain-specific logic, small glue, routine use of an adopted tool, or ordinary fixes and refactors.
- **Environment parity** (works locally but not in production or staging; config or auth drift): `production-parity-skill-builder`.
- **Untestable code**: `finding-seams`. **Documenting existing behavior before changes**: `characterisation-tests`.
- **Multi-surface design audit before code** (every mock in a scope on one page, with a flow diagram, gap cards, and per-mock checklists): `storyboard`.
- **Structured learning of any topic**: `/teach-me [topic]`.
- **Developer-facing prose** (READMEs, guides, tutorials, reference docs, proposals, release notes): `technical-writing`.
- **Reader-facing prose that feels generic, hollow, or AI-shaped**, needing sentence-level co-writing, rewriting, or review: `clarity` when installed. `technical-writing` owns the document's reader job, structure, and verifiable claims. `clarity` owns substance, voice, and sentences.
- **Technical prose in plain English, layman's terms, ASD-STE100, or for non-native readers or translation**: `simple-english` when installed. Use Plain mode by default and Strict mode only when the user names STE or compliance. Leave marketing and brand voice to `clarity`.
- **Documents an agent consumes** (SKILL.md, CLAUDE.md, AGENTS.md, docs reached by a pointer): `writing-for-agents` when installed. Route by audience: `technical-writing` for human-facing prose, `writing-for-agents` for agent-facing instruction.
- **Authoring, restructuring, evaluating, or benchmarking a skill**: `skill-creator` when installed. For how the words read, use `writing-for-agents`.
- **Grading installed skills against recent agent conversations**: `skill-doctor` when installed. Authoring and controlled evals belong to `skill-creator`.
- **Discovering or installing agent skills** (`npx skills`): `find-skills`.
- **Adversarial review of plans, acceptance criteria, stories, or mock designs**: `find-gaps`, one question at a time, with answers written back to the source of truth.
- **Decision-tree interrogation before splitting, planning, or implementing**: `grill-me` when installed; otherwise `specification` or the host's one-question mechanism.
- **Rigorous second opinion on finished work**: `double-check`.
- **Composing several skills into one multi-agent run**: `graph-engineering`.
- **Review of any change boundary** (uncommitted work, branch, stacked layer, diff, or pull request), or the PR-readiness evidence gate before creating a PR: `panel-review`.

**Project onboarding:** Run `/setup` only when the user asks to onboard or configure a project and authorizes the generated project files. Ordinary read-only or narrowly scoped work does not trigger setup.

**Project-level hooks:** When the repository supports hooks and the user authorizes project configuration, consider a PostToolUse typecheck/format hook using the repository's existing toolchain. `/setup` may generate one only within that explicit onboarding scope. The curl installer does not install settings.json.

## Output Guardrails

- **Honor the requested artifact boundary.** Persist a plan or document only when the user asks for a file or the repository declares that durable owner. Otherwise answer in chat without creating a new source of truth.
- **Plan-only mode.** When asked for a plan, design, or document only, produce ONLY that artifact. Do not write production code, test code, or make any implementation changes unless explicitly asked.
- **Incremental output.** When exploring a codebase, produce a first draft within 3-4 tool calls. Refine iteratively rather than exploring everything before writing anything.

## Working with Claude

- After significant changes, ask: "What do I wish I'd known at the start?"
- Route durable, non-obvious learnings through `expectations` to their owner: source or tests, glossary, accepted decision mechanism, maintained docs, active plan, or repository working policy. Load `expectations` for detail.
- Update CLAUDE.md only for local working policy it is declared to own, and only when the request or repository workflow authorizes that write.

## Browser Automation

Prefer `agent-browser` for web automation. Always try it first. If it is not installed, fall back to other available tools (e.g. `WebFetch`, `curl`, or MCP browser tools).

Core workflow:
1. `agent-browser open <url>`: navigate to the page.
2. `agent-browser snapshot -i`: get interactive elements with refs (@e1, @e2).
3. `agent-browser click @e1` / `fill @e2 "text"`: interact using refs.
4. Re-snapshot after any page change.

Run `agent-browser --help` for all commands.

## Summary

Drive production-behavior changes with a test that describes the desired behavior. Write the simplest code that makes the test or other governing check pass. Prefer simplicity and readability over cleverness.
