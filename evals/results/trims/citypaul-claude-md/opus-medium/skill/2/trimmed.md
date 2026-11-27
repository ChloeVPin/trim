# Development Guidelines for Claude

Core principles live here; detailed patterns load on demand via skills.

## Core Philosophy

Test-driven development is required for new or changed behavior. Every production behavior change must be written in response to a failing behavior test. Pure behavior-preserving refactoring and mechanism reduction begin from passing preservation evidence and remain behaviorally green. Use mutation evidence where meaningful; for unreachable, configuration, contract, integration, or operational changes, record proportionate alternate evidence and `N/A` instead of fabricating RED or structural mutants.

Work in small, incremental changes that keep the codebase working throughout.

For mutation-testing cadence, a **phase of work** means one PR review boundary. Normally that is one PR-sized, independently mergeable slice; in a cross-slice stack it is one whole-slice member, and in an intra-slice stack it is one focused dependent layer. It does not mean a multi-PR feature/stack as a whole or the numbered lifecycle phases in `README.md`.

## Testing Principles

Test behavior, not implementation. Cover changed and high-risk behavior proportionately; a coverage percentage is not proof.

- Follow the repository harness; prefer real-browser evidence when the claim depends on browser behaviour and the cost is justified
- Test through the subject's public interface at the layer the claim names (an HTTP endpoint is the wrong interface for a browser claim)
- Use factories for repeated or nested test data; isolated lifecycle hooks and clear one-off values are valid
- Reuse an existing production schema when it adds test evidence; do not redefine the same contract
- Tests must document expected business behavior
- Organize tests around behavior and repository ownership, not a universal file-count rule

For detailed testing patterns, load the `testing` skill.
For mutation analysis, load the `mutation-testing` skill at the end-of-phase PR-readiness gate; use its mutator rules earlier for cheap test-design guidance without running the automated harness.

## TypeScript Guidelines

Strict mode always. Schema-first at trust boundaries, types for internal logic.

- No unexplained `any`; use `unknown` at untrusted boundaries and contain unavoidable interop
- No type assertions without justification
- Follow repository convention for `type`/`interface`, then language semantics
- Define schemas at runtime trust boundaries and derive types from them
- Use plain types, smart constructors, or domain values for trusted internal logic

For detailed TypeScript patterns, load `typescript-strict`. For API and interface design, load `api-design`. For OAuth 2.0 or OpenID Connect design, implementation, review, testing, incident analysis, or migration, load `secure-oauth-oidc`.

## Code Style

Prefer immutable data and pure logic where they make behavior easier to reason about; keep necessary effects explicit.

- Contain mutation where a boundary, library, or measured performance need requires it
- Use early returns or composition when they make branching clearer
- Use comments for non-obvious why, constraints, and safety context
- Use an options object when positional parameters are ambiguous or unstable
- Choose array methods or loops by clarity, control flow, and measured needs
- Compose small private functions behind cohesive, stable module contracts; do not equate one helper with one public module

For detailed patterns, load the `functional` skill.

## Development Workflow

Use fast RED-GREEN-REFACTOR increments for changed behavior. Run mutation testing or review alternate evidence once at the end-of-phase PR-readiness gate, after implementation and refactoring are complete.

- RED: Write a failing behavior test before new or changed behavior
- GREEN: Write the minimum code to pass the test
- REFACTOR OR REDUCE: Assess applicable improvements (only if they add value) while ordinary behavior tests stay green
- REPEAT: Continue the inner cycle without running the automated mutation harness after each increment, refactor, or commit
- PRE-PR MUTATION GATE: When the phase is otherwise ready for a PR, run mutation testing once for the accumulated scope where meaningful; otherwise record `N/A` plus proportionate reachability, configuration, contract, integration, or operational evidence
- KILL MUTANTS: During that gate, address valuable survivors and re-run focused/diff mutation checks as part of the same gate (ask the human when value is ambiguous)
- **Wait for commit approval** before every commit
- Each increment leaves codebase in working state

For a behavior-changing planned slice, load `tdd`, `testing`, and applicable refactoring guidance before code changes begin. Use the `mutation-testing` skill's mutator rules for cheap test-design guidance, but do not run its harness until the end-of-phase PR-readiness gate. For a pure behavior-preserving refactor/reduction, load only the applicable testing, refactoring, and reduction skills during implementation, then apply mutation testing or alternate evidence at the same PR gate; load `reduce-system-complexity` when net mechanism removal is claimed, and record why any other skill is `N/A`. Do not load the full RED workflow merely to assert implementation shape.

### Skill routing

- TDD workflow: `tdd`. Refactoring methodology: `refactoring`.
- Removing branches, states, dependencies, layers, flags, retries, jobs, or operational moving parts from an existing path while conserving behavior: `reduce-system-complexity`. Pure reductions use the verified REFACTOR path, not a fabricated structural RED test.
- Fuzzy product/design decisions, or decision-tree interrogation before story splitting, planning, or implementation: `grill-me` when installed; otherwise the host's one-question mechanism or `specification`.
- Turning fuzzy intent into shared understanding and acceptance criteria (agent-drafted, then risk-proportionate human review): `specification`.
- Naming domain concepts, glossary work, or any new/changed domain term (never silent coinage): `ubiquitous-language`.
- Broad stories, epics, features, or backlog items: `story-splitting` to create child stories before planning.
- Tightening or adversarially reviewing an existing story, plan, acceptance criteria set, or mock spec: `find-gaps`, writing confirmed answers back into the source artifact.
- Significant implementation work: `planning`, for one selected child story or narrow capability, using the repository's declared planning workflow and location; use `plans/` only as the documented fallback.
- A planned slice that may be too large for review, or later slices that should start on the same baseline before lower PRs merge: `stack-pull-requests` with `planning`. Do not turn technical layers into stories or slices.
- CI failure diagnosis: `ci-debugging`.
- Local or runtime failure diagnosis: `debugging`; fix the earliest shared owning boundary when a fix is requested.
- Read-only decision on whether finished implementation satisfies an authoritative requirement: `acceptance-review`; report every criterion with its evidence and exact verdict.
- Hexagonal architecture: `hexagonal-architecture`. Domain-Driven Design: `domain-driven-design`. Event-sourced systems or bounded contexts: `event-sourcing`. 12-factor services: `twelve-factor`.
- Production observability (wide events, OpenTelemetry, SLOs/alerting, telemetry testing): `observability`.
- CLI tool design: `cli-design`.
- Whether and how to use a backend-for-frontend (ownership, aggregation, partial failure, identity toward upstreams): `bff-design`.
- Browser-facing BFF or backend HTTP entry points (access classification, auth middleware, session cookies, CSRF/Origin, protected SSE/WebSocket, endpoint-protection enforcement): `bff-entry-points`.
- Designing a selected module's responsibility, contract, depth, and seams: `codebase-design`.
- Read-only render of how code composes, to understand an unfamiliar path or pseudocode a change before implementing it: `render-code-shape`. It never authorizes the edit.
- Finding and ranking architecture improvements across a repository or subsystem: `improve-codebase-architecture`.
- Designing or auditing source trees, package boundaries, feature folders, composition roots, or folder migrations: `structure-codebase`.
- Front-end flow logic: load `xstate` *before* reaching for `useState`, not only when a file already imports xstate. Two tests decide ownership, never how the value renders: an external answer changed it (request, response, error, retry, timeout, cancellation, stream message, anything sent to a BFF), or the interaction has an interruptible middle (a drag holding pointer capture, a closing animation, a gesture binding document listeners). A disabled button or spinner is the presentation *of* temporal state. State stays in React only when both tests come back empty — one event sets it completely, nothing to interrupt or dispose. A `submitting`/`isLoading` flag, a promise chain setting state in sequence, a double-submit guard, an error cleared before a retry, a `useEffect` needing an ignore flag, or a timer something must clear is a hand-rolled statechart; if an actor already owns that lifecycle, the state belongs in it. Check the repository's own conventions for which layer owns machines before creating one, and ask rather than guess on a genuine tie.
- React or Next.js performance work: `react-performance`. Baseline the symptom, attribute the cost with evidence, apply one rule at a time from the pinned `vercel-react-best-practices` catalogue, then re-measure. Behavior tests stay unchanged and green; immutability and typing rules are not traded for speed, and unmeasured optimizations are reverted.
- Before introducing a material generic mechanism or durable new dependency, load `evaluate-existing-solutions` proportionately: a lightweight local/platform preflight before bespoke generic machinery; due diligence without reopening alternatives for a named but newly introduced dependency; the full comparison for consequential unresolved choices. Not for domain-specific logic, small glue, routine use of an already-adopted tool, or ordinary fixes and refactors.
- Environment parity issues (works locally but not in production/staging, config or auth drift): `production-parity-skill-builder`.
- Making untestable code testable: `finding-seams`. Documenting existing behavior before changes: `characterisation-tests`.
- Multi-surface design audits of mocks before code: `storyboard`.
- Structured learning of a topic: `/teach-me [topic]`.
- Developer-facing prose (READMEs, guides, reference docs, proposals, release notes): `technical-writing`. It owns structure and verifiable claims.
- Sentence-level co-writing, rewriting, or review of reader-facing prose that feels generic or AI-shaped: `clarity` when installed. It owns substance, voice, sentences, and marketing/brand voice.
- Plain English, layman's terms, ASD-STE100, or prose for non-native readers or translation: `simple-english` when installed; Plain mode by default, Strict mode only when the user names STE or compliance.
- Documents an agent consumes (SKILL.md, `CLAUDE.md`/`AGENTS.md`, docs reached by a pointer): `writing-for-agents` when installed. Route by audience, not file type.
- Authoring, evaluating, or benchmarking a skill, or tuning its description for trigger accuracy: `skill-creator` when installed.
- Grading installed skills against recent local agent conversations: `skill-doctor` when installed.
- Discovering and installing skills from the open ecosystem (`npx skills`): `find-skills`.
- A second opinion on finished work: `double-check`.
- Composing several installed skills into one orchestrated multi-agent run: `graph-engineering`.
- Reviewing any change boundary (work-in-progress, branch, stacked layer, diff, or PR), or the PR-readiness evidence gate before creating a PR: `panel-review`.

**Project onboarding:** Run `/setup` only when the user asks to onboard or
configure a project and authorizes the generated project files. Ordinary
read-only or narrowly scoped work does not trigger setup.

**Project-level hooks:** When the repository supports hooks and the user authorizes project configuration, consider a PostToolUse typecheck/format hook using the repository's existing toolchain. `/setup` may generate one only within that explicit onboarding scope; the curl installer does not install settings.json.

## Output Guardrails

- **Honor the requested artifact boundary** — Persist a plan or document only
  when the user asks for a file or the repository declares that durable owner.
  Otherwise answer in chat without creating a new source of truth.
- **Plan-only mode** — When asked for a plan, design, or document only, produce ONLY that artifact. Do not write production code, test code, or make any implementation changes unless explicitly asked.
- **Incremental output** — When exploring a codebase, produce a first draft of output within 3-4 tool calls. Refine iteratively rather than front-loading all exploration before producing anything.

## Learnings

- Ask "What do I wish I'd known at the start?" after significant changes
- Route durable, non-obvious learnings through `expectations` to their actual
  owner: source/tests, glossary, accepted decision mechanism, maintained docs,
  active plan, or repository working policy
- Update CLAUDE.md only for local working policy it is declared to own, and only
  when the request or repository workflow authorizes that write

## Browser Automation

Try `agent-browser` first for web automation. If it is not installed, fall back to other available tools (e.g. `WebFetch`, `curl`, or MCP browser tools).

`agent-browser` core workflow:
1. `agent-browser open <url>` - Navigate to page
2. `agent-browser snapshot -i` - Get interactive elements with refs (@e1, @e2)
3. `agent-browser click @e1` / `fill @e2 "text"` - Interact using refs
4. Re-snapshot after page changes

Run `agent-browser --help` for all commands.
