# Development Guidelines for Claude

## Core Philosophy

Test-driven development is required for new or changed behavior. Every production behavior change starts from a failing behavior test. Pure behavior-preserving refactoring and mechanism reduction start from passing preservation evidence and stay behaviorally green. Use mutation evidence where meaningful. For unreachable, configuration, contract, integration, or operational changes, record proportionate alternate evidence and `N/A` instead of fabricating RED tests or structural mutants.

Make small, incremental changes that keep the codebase working after each step.

A **phase of work** is one PR review boundary: normally one PR-sized, independently mergeable slice; in a cross-slice stack, one whole-slice member; in an intra-slice stack, one focused dependent layer. It is not a whole multi-PR feature or stack, and not the numbered lifecycle phases in `README.md`. Use it to set mutation-testing cadence.

## Principles

**Testing**
- Write behavior tests first for new or changed behavior.
- Test behavior, not implementation, through the public interface at the layer the claim names. (An HTTP endpoint is the wrong interface for a browser claim.)
- Cover changed and high-risk behavior proportionately. A coverage percentage is not proof.
- Tests document expected business behavior. Organize them around behavior and repository ownership, not a fixed file-count rule.
- Use factories for repeated or nested test data. Isolated lifecycle hooks and clear one-off values are fine.
- Follow the repository's test harness. Prefer real-browser evidence when the claim depends on browser behavior and the cost is justified.

**TypeScript**
- Strict mode always.
- No unexplained `any`. Use `unknown` at untrusted boundaries and contain unavoidable interop.
- No type assertions without justification.
- Follow repository convention for `type` vs `interface`, then language semantics.
- Define schemas at runtime trust boundaries and derive types from them. Use plain types, smart constructors, or domain values for trusted internal logic.
- Reuse an existing production schema when it adds test evidence. Do not redefine the same contract.

**Code style**
- Prefer immutable values and pure functions. Isolate necessary mutation and effects, and contain mutation where a boundary, library, or measured performance need requires it.
- Use early returns or composition when they make branching clearer.
- Comment non-obvious why, constraints, and safety context.
- Use an options object when positional parameters are ambiguous or unstable.
- Choose array methods or loops by clarity, control flow, and measured need.
- Compose small private functions behind cohesive, stable module contracts. Do not equate one helper with one public module.

## Development Workflow

- **RED:** write a failing behavior test before new or changed behavior.
- **GREEN:** write the minimum code to pass it.
- **REFACTOR OR REDUCE:** assess improvements while behavior tests stay green. Skip this if it adds no value.
- **REPEAT:** continue the inner cycle. Do not run the mutation harness after each increment, refactor, or commit.
- **PRE-PR MUTATION GATE:** when a phase is otherwise ready for a PR, run mutation testing once for the accumulated scope where meaningful. Otherwise record `N/A` with proportionate reachability, configuration, contract, integration, or operational evidence.
- **KILL MUTANTS:** during that gate, address valuable survivors and re-run focused or diff mutation checks. Ask the human when value is ambiguous.
- **Wait for commit approval** before every commit.
- Each increment leaves the codebase in a working state.

Skills for this workflow:
- Behavior-changing slice: load `tdd`, `testing`, and applicable refactoring guidance before code changes begin.
- Pure behavior-preserving refactor or reduction: load only the applicable testing, refactoring, and reduction skills during implementation, and apply mutation testing or alternate evidence at the PR gate. Load `reduce-system-complexity` when net mechanism removal is claimed. Record why any other skill is `N/A`. Do not load the full RED workflow just to assert implementation shape.
- `mutation-testing`: run its harness only at the end-of-phase PR-readiness gate. Earlier, use its mutator rules for test-design guidance.
- Removing branches, states, dependencies, layers, flags, retries, jobs, or other operational parts while conserving behavior: `reduce-system-complexity`. Pure reductions use the verified REFACTOR path, not a fabricated structural RED test.
- Refactoring method: `refactoring`.

## Output Guardrails

- Persist a plan or document only when the user asks for a file or the repository declares that durable owner. Otherwise answer in chat without creating a new source of truth.
- Plan-only mode: when asked for a plan, design, or document only, produce only that artifact. Make no production code, test code, or implementation changes unless explicitly asked.
- When exploring a codebase, produce a first draft within 3-4 tool calls. Refine iteratively rather than front-loading exploration.

## Project Setup

- Run `/setup` only when the user asks to onboard or configure a project and authorizes the generated project files. Ordinary read-only or narrowly scoped work does not trigger setup.
- Consider a PostToolUse typecheck/format hook only when the repository supports hooks and the user authorizes project configuration. Use the repository's existing toolchain. `/setup` may generate one only within that onboarding scope. The curl installer does not install settings.json.

## Working with Claude

**Core principle:** think deeply, follow TDD strictly, capture learnings while context is fresh.

- After significant changes, ask: "What do I wish I'd known at the start?"
- Route durable, non-obvious learnings through `expectations` to their owner: source or tests, glossary, accepted decision mechanism, maintained docs, active plan, or repository working policy. Guidance on expectations and documentation: `expectations`.
- Update CLAUDE.md only for local working policy it is declared to own, and only when the request or repository workflow authorizes that write.

## Browser Automation

Prefer `agent-browser`. If it is not installed, fall back to `WebFetch`, `curl`, or MCP browser tools. Always try `agent-browser` first.

1. `agent-browser open <url>`: navigate to the page.
2. `agent-browser snapshot -i`: list interactive elements with refs (@e1, @e2).
3. `agent-browser click @e1` or `fill @e2 "text"`: interact using refs.
4. Re-snapshot after page changes.

Run `agent-browser --help` for all commands.

## Skill Routing

Load a skill when the task matches its trigger. Where a skill says "when installed", use the stated fallback if it is missing.

**Planning and requirements**
- Fuzzy product or design decisions, before writing stories or plans: `grill-me` when installed; otherwise `specification` or the host's one-question mechanism. Use the same fallback for relentless decision-tree questioning before story splitting, planning, or implementation.
- Turning fuzzy intent into shared understanding and acceptance criteria: `specification`.
- New or changed domain terms, glossary work, or naming: `ubiquitous-language`.
- Broad stories, epics, features, or backlog items: `story-splitting` before planning.
- Tightening an existing story, plan, acceptance criteria, or mock spec, and adversarial review of them: `find-gaps`, writing confirmed answers back into the artifact.
- Significant implementation: `planning` for one selected child story or narrow capability, following the repository's declared planning workflow. Use `plans/` only as the documented fallback.
- A planned vertical slice too large to review, or later slices that must start on the same evolving baseline: `stack-pull-requests` with `planning`.
- Multi-surface design audits before code: `storyboard`.
- Read-only decision on whether finished work satisfies an authoritative requirement: `acceptance-review`. Report every criterion with its evidence and an exact verdict.
- Rigorous second opinion on finished work: `double-check`.
- Review of any change boundary (uncommitted work, branch, stacked layer, diff, or PR), or PR-readiness evidence before creating a PR: `panel-review`.
- Composing several installed skills into one multi-agent run: `graph-engineering`.
- Structured learning of a topic: `/teach-me [topic]`.

**Testing and debugging**
- Making untestable code testable: `finding-seams`.
- Documenting existing behavior before changes: `characterisation-tests`.
- CI failure: `ci-debugging`.
- Local or runtime failure: `debugging`. Preserve evidence, test one causal hypothesis at a time, and fix the earliest shared owning boundary when a fix is requested.
- Works locally but not in production or staging, or config and auth drift: `production-parity-skill-builder`.

**Architecture and design**
- Hexagonal architecture projects: `hexagonal-architecture`. Domain-Driven Design projects: `domain-driven-design`.
- Event-sourced systems or bounded contexts (events as source of truth, Decider write model, event stores, projections, read models, versioning, snapshots): `event-sourcing`.
- 12-factor service projects: `twelve-factor`. Production observability (wide events, OpenTelemetry, SLOs, alerting, telemetry testing): `observability`.
- CLI tool design (stream separation, format flags, exit codes, composability): `cli-design`.
- Whether to adopt a backend-for-frontend, how many, what each may own, upstream aggregation, partial failure, or mediating user identity upstream: `bff-design`.
- Browser-facing BFF or backend HTTP entry points (public and protected access, authentication middleware, session cookies, CSRF and Origin policy, protected SSE or WebSocket routes, endpoint protection): `bff-entry-points`.
- Designing a module's responsibility, caller-facing contract, information hiding, depth, leverage, or seams: `codebase-design`.
- Read-only render of how code composes, with `[NEW]` marking unbuilt work: `render-code-shape`. It never authorizes an edit.
- Ranked, evidence-backed architecture improvements across a repository or subsystem: `improve-codebase-architecture`.
- Designing or auditing source trees, frontend route, feature, state, or design-system ownership, package boundaries, composition roots, or folder migrations: `structure-codebase`.
- API and interface design: `api-design`. OAuth 2.0 or OpenID Connect work: `secure-oauth-oidc`.
- Before adding a material generic mechanism or durable new dependency: `evaluate-existing-solutions`, in proportion. Use a lightweight local or platform preflight before bespoke generic machinery; due diligence without reopening alternatives for a named new dependency; a full comparison for consequential unresolved choices. Skip it for domain-specific logic, small glue, routine use of an adopted tool, and ordinary fixes or refactors.
- React or Next.js performance: `react-performance`. Baseline the symptom, attribute the cost with evidence, apply one rule at a time, then re-measure.
- Front-end flow logic: `xstate`. Load it before reaching for `useState`, not only when a file already imports xstate. Put state in an actor when either of these is true:
  1. An external answer changes it (request, response, error, retry, timeout, cancellation, stream message, anything sent to a BFF).
  2. The interaction has an interruptible middle (a drag holding pointer capture, a closing animation, a gesture binding document listeners).

  A disabled button or spinner is the presentation of that state, not a reason for a flag. Keep state in React only when neither test applies: one event sets it completely, with nothing to interrupt or dispose. A `submitting` or `isLoading` flag, a promise chain setting state in sequence, a double-submit guard, an error cleared before a retry, a `useEffect` needing an ignore flag, or a timer something must clear is a hand-rolled statechart. If an actor already owns that lifecycle, the state belongs in it. Check the repository's conventions for which layer owns machines before creating one. Ask rather than guess on a genuine tie.

**Writing**
- Developer-facing prose (READMEs, guides, tutorials, reference docs, proposals, release notes): `technical-writing`.
- Reader-facing prose that feels generic, hollow, or AI-shaped: `clarity` when installed. `technical-writing` owns the document's structure and verifiable claims; `clarity` owns substance, voice, and sentences.
- Technical prose in plain English, layman's terms, ASD-STE100, or for non-native readers or translation: `simple-english` when installed. Use Plain mode by default and Strict mode only when the user names STE or compliance.
- Documents an agent consumes (SKILL.md, CLAUDE.md, AGENTS.md, or a doc reached by a pointer): `writing-for-agents` when installed. Use `technical-writing` for human-facing docs.
- Authoring, restructuring, evaluating, or benchmarking a skill: `skill-creator` when installed. Grading installed skills against recent conversations: `skill-doctor` when installed.
- Discovering and installing agent skills: `find-skills`.

## Suggested additions (not applied)

- For coding work, a line to run a real check (the relevant test or typecheck) before reporting a change done.
- If agents stop early on long tasks, a line to keep working until the task is done.
