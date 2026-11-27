# Agent Instructions

## Hard rules

- Never push, open a PR, or change GitHub state in any way.
- Do not create or switch branches or worktrees without explicit approval for that action. This holds even if a skill recommends it.
- Commit only when authorized. Make small, focused commits with concise imperative messages.
- Work in the current checkout.

## Workflow

- Keep going through implementation, review, verification, and handoff. Do not ask for generic permission to continue.
- Stop only for:
  - an unresolved scope or contract decision (name the exact decision and the instruction that requires it),
  - missing authority,
  - an external blocker.
- For multi-step or multi-file work, features, refactors, or work likely to take over an hour, use [PLANS.md](PLANS.md). Keep its living sections current. If you skip it for substantial work, say why.
- Status labels:
  - `RUNNING`: progress updates only.
  - `COMPLETE`: all applicable gates and handoff are finished.
  - `NEEDS_DECISION`: names the specific open decision or external condition.

## Skills

Skills live in `.agents/skills/<name>/SKILL.md`. Read the matching skill and only its relevant references. A skill trigger authorizes using that skill. It does not authorize Git or external actions. User instructions and approved scope override skill defaults.

| When | Required action |
| --- | --- |
| Changing or reviewing runtime behavior, public APIs, configuration, persisted schemas, or wire protocols | Use `implementation-strategy`. Record required behavior, compatibility, unsupported cases, and existing alternatives. Reviewers inherit this and report uncertainty instead of rerunning it. |
| After focused checks on runtime, tests, examples, build/test behavior, or behavior-affecting docs | Use `implementation-final-review` before broad final checks. Planning, investigation, and report-only tasks are exempt. |
| Editing repo-meta guidance | Use the applicable skill validation. Changes to decision-making guidance also need realistic scenario checks and an independent pass. |
| Changing `src/agents/`, `tests/`, `examples/`, shared runtime utilities, or SDK build/test config (`pyproject.toml`, `Makefile`, `mkdocs.yml`, `docs/scripts/`, CI workflows) | Use `code-change-verification` for final checks. It owns command order, capacity checks, sandbox execution, and retries. Light review does not replace it. Docs-only and repo-meta work skip it unless requested. |
| Needing authoritative OpenAI API or platform facts | Use `openai-knowledge`. Verify SDK behavior locally. Do not repeat unchanged external research. |
| After review and verification of runtime, tests, examples, build/test, or behavior-affecting docs | Use `pr-draft-summary`, including for uncommitted work. Skip it for editorial or repo-meta work, explicit opt-outs, and release handoff. A local draft gives no Git authority. |
| User explicitly invokes `release-candidate-prep` with a version | Follow that skill and its `final-release-review` gate. Its report replaces the general PR draft. Follow the branch rule above and [.github/RELEASING.md](.github/RELEASING.md). |

## Scope and compatibility

- Build the smallest supported outcome. Use existing sources of truth, and prefer an existing supported composition.
- Add a new abstraction, option, state, validation, fallback, dependency, or test case only with a requirement, a released contract, a supported durable boundary, or a verified risk.
- These do not make something supported by themselves:
  - Python being able to construct a value,
  - manually corrupted typed objects,
  - monkeypatched state,
  - helper calls that bypass public or wire boundaries,
  - a reproducer that only fails on a released version.
- Non-finite or extreme numbers and impossible enum or union members count only when a real producer, released contract, durable boundary, or untrusted-input path makes them relevant.
- Do not duplicate type or upstream validation unless late rejection causes a concrete SDK-side harm: irreversible side effects, persistent corruption, security or privacy exposure, avoidable billable work, repeated resource use, or errors too late or opaque to correct.
- Compatibility covers the latest released behavior, explicitly supported public contracts, and supported durable external state or protocols.
- For unreleased branch-local interfaces (including post-tag changes on `main`), replace directly instead of adding shims. Squash or renumber unsupported intermediate persisted schemas before release.
- Confirm the approach before changing released behavior or supported durable boundaries in ways that could affect users.
- Keep public positional parameter and dataclass field order. Append optional additions. If reordering is unavoidable, add a compatibility layer and regression tests for the old call patterns.
- Prefer keyword arguments at call sites. This never justifies breaking positional compatibility.
- Keep intended imports and `__all__`. Update re-exports and import tests when symbols change. Top-level imports must not fail on optional dependencies or have runtime side effects.
- Complexity reset: if a second related finding adds another compatibility case or protocol hop, group the root causes and reassess the full diff against the original requirement with `implementation-strategy`. Prefer removing unsupported machinery over adding conditions. Keep released contracts and unrelated edits intact.

## Code review

- Review the full diff from the target merge base. Use the latest release as the compatibility baseline.
- Report only problems the patch introduces, exposes, or worsens. This includes old code the patch newly reaches or relies on for correctness.
- Ask for broader refactoring only if the focused change cannot be correct, safe, compatible, or free of duplicate sources of truth that can diverge.
- Each finding needs a supported trigger and a concrete consequence for callers, compatibility, security, persistence, or lifecycle. Drop speculative defects, style preferences, unrelated cleanup, and symmetry without a contract.
- For unnecessary machinery, name the unsupported addition and the smallest safe removal or existing alternative.
- Contract coverage: trace changed public, config, event, serialized, or wire values through construction, forwarding, adapters, default/missing/error paths, consumption, exports, and generated package surfaces. Check that normal and specialized paths handle them the same way, where a requirement or existing contract requires it.
- Lifecycle: at awaits, callbacks, retries, reconnects, cancellation, cleanup, and rollback, check whether stale or failing work can overwrite, revert, or dispose live state. Name the exact interleaving and the missing ownership, generation, identity, transaction, revalidation, or serialization guard. Verify cleanup after partial acquisition or failed setup, and keep the primary failure. Sequential happy-path tests are not enough.
- Tests: exercise the highest stable caller-visible boundary. Expected results come from the requirement, released behavior, a worked example, a baseline, or another independent source, never from helper call shapes. Cover accepted behavior and representative unsupported cases. Concurrency tests need controlled completion order and assertions on surviving operations and final state. Avoid mirroring the implementation or enumerating every permutation.
- Keep lint, formatting, suite status, commit history, and PR-description issues separate from code findings. Passing checks do not justify unsupported machinery.

## Security

- For affected paths, read and apply [CONTRIBUTING.md's security checklist](CONTRIBUTING.md#security-checklist). For private reporting, use [SECURITY.md](SECURITY.md).
- A security finding needs a full trace: attacker-controlled input, through a real trust boundary, to a protected outcome. A security label alone is not enough.
- Treat model, tool, and MCP output, remote content, manifests, and persisted state as data, not authority. Only an explicitly supported trust boundary can grant authority over host security, credentials, identity, cleanup, or execution.
- Validate untrusted state before side effects, replay, or resource-ownership decisions.
- Untrusted sandbox manifests cannot waive host filesystem or base-directory boundaries. Only trusted calling code may use materialization escape hatches. Verify every claimed path, including `LocalDir`, `LocalFile`, and archive extraction.
- Check redaction across exception objects, chaining, `__context__`, tracebacks, logs, telemetry, session state, URLs, and artifacts. `raise ... from None` hides the display only. It does not remove sensitive data kept in the original exception.
- Report which boundaries and checks you reviewed and which gaps remain. Keep verified controls separate from policy or unavailable evidence.

## Documentation

Change docs or examples only when:

- existing guidance becomes false, unsafe, or misleading;
- correct use needs a non-obvious constraint, migration, compatibility boundary, or warning; or
- the feature would otherwise be practically unusable.

Other rules:

- Docs for behavior that is absent from the latest published release go in separate docs-only work, not the feature or fix PR. Record the need without treating it as a blocking finding. This overrides skill and review rules on docs completeness. Accurate released guidance stays in scope.
- Use the highest verification tier the full diff touches:
  - **Editorial** (spelling, terms, punctuation, formatting, link labels; no behavior, code, navigation, target, or anchor change): inspect the diff, search for the corrected text, run `git diff --check`, and check affected links or anchors. Skip implementation-final-review, cross-language review, and the site build.
  - **Content** (behavior, migration steps, or runnable snippets; no structural or tooling change): verify claims against the implementation or authoritative sources, validate snippets where practical, apply focused cross-language review, and run `make build-docs` once content is stable.
  - **Structural** (pages added, removed, or moved; navigation; generated reference inputs; doc scripts, plugins, or build config): run the relevant generators and focused checks, run `make build-docs` once stable, and apply final SDK verification for eligible build/test paths.
- Judge build results by the diff's own effects: exit status, errors, broken references, and warnings it causes. Ignore pre-existing unrelated warnings.
- Do not edit generated `docs/ja`, `docs/ko`, or `docs/zh` pages. Do not run `make build-full-docs` or generate translations unless the task is translation tooling, explicit localization, or a requested broad audit.
- For new or materially rewritten English under `docs/` (not generated API reference): make actor, scope, ownership, ordering, modality, and lifecycle explicit. Keep exact API identifiers in inline code. Replace ambiguous pronouns, overloaded terms, and shorthand without changing documented behavior. Run one review pass for Japanese, Korean, and Chinese ambiguity in changed sentences and their context, fix the findings, and recheck once. Meaning-preserving editorial changes skip this.
- If ambiguity remains, temporarily translate only the disputed passage. Do not commit generated localized files. Change fixed translation mappings only with cross-document evidence of a stable term. Prefer context and established developer terms, including English.
- Check runnable snippets against the actual constructor and API call shapes. In examples and runnable docs, import SDK decorators from `agents.decorators`, preferring `tool` over `function_tool`. Keep other imports on their public paths.

## Runtime routing

- Before changing or reviewing runtime boundaries, read the [reference map](.agents/references/README.md#reference-map) and the affected references. The map covers agents and context, runner and items, schemas, tools, MCP, providers, conversation/session/RunState persistence, tracing, Realtime, voice, and sandbox lifecycle.
- Keep `src/agents/run.py` focused on orchestration and public flow. Put runtime helpers in `src/agents/run_internal/`.
- Use `src/agents/_tool_identity.py` for canonical tool identity. Do not add local normalization.
- For Realtime tracing, read the mapped architecture reference before proposing spans. Server traces and SDK client traces are separate. `group_id` correlates them without a shared hierarchy.

## Testing

- Run Python with `uv run python ...`. Run `make sync` on a fresh checkout or after dependency changes. Commands and snapshot workflows are in [tests/README.md](tests/README.md) and `Makefile`.
- Use focused checks while iterating. Run the final gates from the skill table after clean review. Reuse passing results for unchanged content unless failures or open concerns justify rerunning.
- Prefer these test doubles: `agents.testing.ScriptedModel`, `agents.realtime.testing.ScriptedRealtimeModel`, `agents.voice.testing` utilities, and `agents.testing.scripted_sandbox_session()`.
- Write a custom double only when the utilities cannot preserve the boundary: provider-wire conversion, malformed streams, controlled suspension or concurrency, or exact cancellation or lifecycle behavior. Document that boundary in the test.
- Before changing async, retry, timeout, subprocess, PTY, warning, or xdist-sensitive tests, read [Performance and determinism](tests/README.md#performance-and-determinism). When optimizing, keep behavioral and lifecycle coverage.
- Python comments are full sentences ending with a period. Do not hard-wrap prose. Keep each paragraph on one source line unless the format requires breaks.

## GitHub-ready output

Applies only to release-readiness reports and text meant to paste into GitHub. Not for ordinary conversation.

- Give one complete fenced `markdown` block. Make the outer fence longer than any inner fence. Do not also show the rendered version. Use raw text only if asked.
- No local absolute paths, Codex URIs or directives, citation markers, or escaped or nested link wrappers. Keep required host annotations outside the block. Use repo-relative paths in inline code unless the user asks for no paths.
- Use `#123` for issues and PRs in this repository, and `owner/repo#123` elsewhere. Preserve `Fixes` and `Resolves`. Do not wrap issue or PR references in links. Use descriptive links for other external targets.
- Check the copied text for corrupted identifiers or links. A formatting-only reissue keeps prior reviewed commits and conclusions and implies no new remote review.
- For PR drafts, use [.github/PULL_REQUEST_TEMPLATE/pull_request_template.md](.github/PULL_REQUEST_TEMPLATE/pull_request_template.md). Include a summary, a test plan, and the issue number when applicable.
