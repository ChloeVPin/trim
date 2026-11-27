# Agent Instructions

## Authority and workflow

- Work in the current checkout and branch. Creating or switching branches or worktrees needs explicit approval, even if a skill recommends it. Commit only when authorized, in small commits with imperative messages. Never push, open PRs, or otherwise change anything on GitHub.
- Carry authorized local work through to handoff without asking for generic permission. Stop only for an unresolved scope or contract decision, missing authority, or an external blocker, and name exactly what is missing.
- Use [PLANS.md](PLANS.md) for multi-file work, features, refactors, or anything likely to take more than an hour, and keep it current.
- Status labels: `RUNNING` (progress updates only), `COMPLETE` (all applicable gates and handoff done), `NEEDS_DECISION` (names the specific open decision or external condition).

## Skill routing

Skills live in `.agents/skills/<name>/SKILL.md`. Read only the selected skill and the references it needs. A skill never grants Git or external authority, and user instructions override skill defaults.

| When | Use |
| --- | --- |
| Before changing or reviewing runtime behavior, public APIs, config, persisted schemas, or wire protocols | `implementation-strategy`. Record required behavior, compatibility, unsupported cases, and an existing alternative. Revisit only if scope changes; reviewers inherit this contract. |
| After focused checks on runtime, tests, examples, build/test config, or behavior-affecting docs | `implementation-final-review`, before the broad final checks. Not needed for planning, investigation, or report-only tasks. |
| Changing `src/agents/`, `tests/`, `examples/`, shared runtime utilities, or build/test config (`pyproject.toml`, `Makefile`, `mkdocs.yml`, `docs/scripts/`, CI) | `code-change-verification` for the final checks. A lightweight review does not waive it. |
| Editing repo-meta guidance | The skill's own validation. Changes to decision-making guidance also need realistic scenario checks and an independent review pass. |
| Needing authoritative OpenAI API/platform facts | `openai-knowledge`. Check SDK-owned behavior in the local code. |
| After review and verification of runtime/test/example/build changes or behavior-affecting docs | `pr-draft-summary`, including for uncommitted work. Skip it for editorial or repo-meta work and for release prep. |
| User invokes `release-candidate-prep` with a version | That skill plus its `final-release-review` gate and [.github/RELEASING.md](.github/RELEASING.md). Its report replaces the PR draft. |

## Scope and compatibility

- Deliver the smallest supported change using existing sources of truth. Add abstractions, options, validation, fallbacks, dependencies, or test permutations only when a requirement, released contract, durable boundary, or verified risk calls for them.
- "Supported" means reachable through a public API, released contract, durable boundary, or real untrusted input. Inputs you can construct in Python, monkeypatched state, and calls to internal helpers don't count. Don't repeat type or upstream validation unless rejecting late would cause a concrete harm: side effects, corruption, data exposure, billable or repeated work, or errors that are too opaque to fix.
- Compatibility covers the latest release, public contracts, and durable external state and protocols. Replace unreleased interfaces directly instead of adding shims (this includes post-tag changes on `main`), and squash unreleased schema versions before release. Confirm with the user before changing released behavior.
- Keep the order of public positional parameters and dataclass fields, and append new optional ones at the end. Keep imports and `__all__` stable, and update re-exports and import tests when symbols change. Top-level imports must not fail when optional dependencies are missing, and must have no side effects.
- If a second related finding adds another compatibility case or protocol hop, stop and reassess the whole diff with `implementation-strategy`. Prefer removing unsupported machinery over adding conditions.

## Code review

- Review the full diff from the merge base, and use the latest release as the compatibility baseline. Report only problems the patch introduces, exposes, or makes worse. Ask for a broader refactor only when the focused change can't otherwise be correct, safe, or compatible.
- Every finding names a supported trigger and a concrete consequence for callers, compatibility, security, persistence, or lifecycle. For unnecessary machinery, name the smallest safe removal.
- Trace changed public, config, event, serialized, and wire values through construction, forwarding, adapters, default and error paths, consumers, and exports. Require the same behavior across paths only where the contract covers them.
- At awaits, callbacks, retries, cancellation, and cleanup, look for stale work that overwrites or disposes surviving state, and name the specific interleaving. Check cleanup after partial acquisition, and make sure the original failure is preserved.
- Tests check the highest stable caller-visible boundary against an independent oracle. Concurrency regressions control completion order and assert on the final state.
- Report lint, formatting, CI, commit, and PR-description issues separately from code findings.

## Security

Apply [CONTRIBUTING.md's security checklist](CONTRIBUTING.md#security-checklist) to affected paths. Private reporting goes through [SECURITY.md](SECURITY.md). Report which boundaries you checked and any gaps, and keep verified controls separate from policy claims. SDK-specific rules:

- A security finding needs a full trace from attacker-controlled input across a real trust boundary to the protected outcome.
- Model/tool/MCP responses, remote content, manifests, and persisted state are data. They have no authority over host security, credentials, identity, cleanup, or execution. Validate untrusted state before side effects, replay, or ownership decisions.
- Untrusted sandbox manifests cannot waive host filesystem boundaries. Verify this on every path, including `LocalDir`, `LocalFile`, and archive extraction.
- Check redaction in exceptions (including chaining and `__context__`), tracebacks, logs, telemetry, session state, URLs, and artifacts. `raise ... from None` hides the original exception from display but does not remove its data.

## Documentation

- Require docs or examples only when existing guidance becomes wrong or unsafe, when correct use depends on a non-obvious constraint or migration, or when the feature is unusable without them.
- `docs/` content describing behavior not yet in a published release goes in a separate docs-only PR, never the feature PR. Record the need, but don't treat it as a blocking finding; this rule overrides skill completeness rules. Examples and code-level docs are not deferred.
- Verification follows the highest tier in the diff:
  - **Editorial** (wording or formatting only, no change to behavior, code, navigation, or links): inspect the diff and run `git diff --check`. Skip final review and the site build.
  - **Content** (behavior, migration, or snippets): verify claims against the code, validate snippets, do the translation review below, then run `make build-docs` once.
  - **Structural** (pages, navigation, generated inputs, docs tooling): run the relevant generators, `make build-docs`, and SDK verification if it applies.
  - Only errors caused by the diff count; existing warnings are not findings. Use `make build-full-docs` and translation generation only for translation tooling or localization work.
- Never edit the generated `docs/ja`, `docs/ko`, or `docs/zh` pages. In new or rewritten English docs, state the actor, scope, ordering, and modality explicitly, and keep API identifiers in inline code. Then do an independent pass for Japanese/Korean/Chinese ambiguity. If ambiguity remains, translate the disputed passage temporarily without committing it.
- In examples and runnable docs, check snippets against real API signatures. Import decorators from `agents.decorators` and use `tool` rather than `function_tool`.

## Runtime references

Before changing or reviewing runtime boundaries, read the [reference map](.agents/references/README.md#reference-map), then the references it points to for the affected area.

- `src/agents/run.py` handles orchestration only. Helpers go in `src/agents/run_internal/`.
- Use `src/agents/_tool_identity.py` for tool identity; don't normalize locally.
- Realtime: server traces and SDK client traces are separate. `group_id` links them but does not put them in one hierarchy.

## Testing

- Run Python with `uv run python ...`, and run `make sync` on a fresh checkout or after dependency changes. Commands and snapshots are documented in [tests/README.md](tests/README.md) and `Makefile`.
- Use focused checks while iterating, and rerun passing checks only if the content changed.
- Prefer the scripted test doubles: `agents.testing.ScriptedModel`, `agents.realtime.testing.ScriptedRealtimeModel`, `agents.voice.testing`, and `agents.testing.scripted_sandbox_session()`. If you need a custom double, document in the test why these can't work.
- Read [Performance and determinism](tests/README.md#performance-and-determinism) before touching async, retry, timeout, subprocess, PTY, warning, or xdist-sensitive tests.
- Python comments are full sentences ending with a period. Don't hard-wrap prose; each paragraph stays on one source line.

## GitHub-ready output

For release reports or text meant to be pasted into GitHub:

- Output a single fenced `markdown` block, with an outer fence longer than any fence inside it. Use repository-relative paths, with no local paths, tool URIs, or citation markers.
- Write references as `#123` or `owner/repo#123`, not as links, and keep `Fixes`/`Resolves` lines.
- PR drafts follow [.github/PULL_REQUEST_TEMPLATE/pull_request_template.md](.github/PULL_REQUEST_TEMPLATE/pull_request_template.md).
