# Agent Instructions

## Authority and workflow

- Work in the current checkout and branch. Creating or switching branches or worktrees needs explicit approval, even if a skill recommends it. Commit only when authorized, using small commits with imperative messages. Never push, open PRs, or otherwise change anything on GitHub.
- Carry authorized local work through to handoff. Stop only for an unresolved scope or contract decision, missing authority, or an external blocker, and name exactly what is missing.
- Use [PLANS.md](PLANS.md) for multi-step, multi-file, or long-running work, and keep its living sections up to date.
- Status labels: `COMPLETE` means all applicable gates and the handoff are done. `NEEDS_DECISION` names the specific open decision or external condition. `RUNNING` appears only in progress updates.

## Skill routing

Skills live in `.agents/skills/<name>/SKILL.md`. A skill trigger allows you to use the skill. It does not grant any extra Git or external authority. User instructions and approved scope override skill defaults.

| When | Skill |
| --- | --- |
| Before changing or reviewing runtime behavior, public APIs, config, persisted schemas, or wire protocols | `implementation-strategy`: record the required behavior, compatibility, unsupported cases, and an existing alternative. Revisit it only if scope changes. Reviewers inherit this contract. |
| After focused checks on runtime, tests, examples, build/test config, or docs that affect behavior | `implementation-final-review`, before the broad final checks. Planning and report-only tasks are exempt. |
| Changing `src/agents/`, `tests/`, `examples/`, shared runtime utilities, or build/test config (`pyproject.toml`, `Makefile`, `mkdocs.yml`, `docs/scripts/`, CI) | `code-change-verification` as the final gate. A lightweight review does not waive it. |
| Editing repo-meta guidance | The applicable skill validation. Changes to decision-making guidance need realistic scenario checks and an independent pass. |
| Needing authoritative OpenAI API or platform facts | `openai-knowledge`. Verify SDK-owned behavior locally. |
| After review and verification of code, test, build, or behavior-affecting doc changes | `pr-draft-summary`, including for uncommitted work. It does not apply to editorial or repo-meta work, or when the user opts out. |
| User invokes `release-candidate-prep` with a version | Follow that skill, its `final-release-review` gate, and [.github/RELEASING.md](.github/RELEASING.md). Its report replaces the PR draft. |

## Scope and compatibility

- Implement the smallest supported change and reuse existing sources of truth. Add a new abstraction, option, fallback, dependency, or validation only when a requirement, released contract, durable boundary, or verified risk calls for it.
- Python constructibility, monkeypatched or corrupted objects, impossible enum values, and non-finite numbers do not show that a case is supported. They count only when a real producer or an untrusted-input path reaches them. Don't repeat type or upstream validation unless rejecting the input later would cause a concrete harm: side effects, corruption, security exposure, billable waste, or errors that are hard to act on.
- Compatibility covers the latest release, public contracts, and durable external state and protocols. Replace unreleased interfaces directly, without shims, including post-tag changes on `main`. Confirm with the user before changing released behavior.
- Keep the order of public positional parameters and dataclass fields, and add new options at the end. Preserve `__all__` and re-exports. Top-level imports must have no optional-dependency failures and no side effects.
- If a second related finding adds another compatibility case or protocol hop, step back and reassess the whole diff with `implementation-strategy`. Prefer removing unsupported machinery over adding conditions.

## Code review

- Review the full diff from the merge base, and use the latest release as the compatibility baseline. Report only problems the patch introduces, exposes, or makes worse. Each finding needs a supported trigger and a concrete consequence for callers, compatibility, security, persistence, or lifecycle.
- Trace each changed public, config, event, serialized, or wire value through construction, forwarding, adapters, defaults and error paths, consumption, and exports.
- Lifecycle: at awaits, callbacks, retries, cancellation, and cleanup, look for stale work that could overwrite or dispose surviving state, and name the concrete interleaving. Check cleanup after partial acquisition or a failed construction, and make sure the original failure is preserved.
- Tests should check behavior at the highest stable caller-visible boundary against an independent oracle. Concurrency regressions need controlled completion order and assertions on the final state.
- Report lint, formatting, suite status, and PR-text issues separately from code findings.

## Security

Apply [CONTRIBUTING.md's security checklist](CONTRIBUTING.md#security-checklist) to affected paths, and follow [SECURITY.md](SECURITY.md) for private reporting. A security finding needs a full trace from attacker-controlled input across a real trust boundary.

- Model, tool, and MCP responses, remote content, manifests, and persisted state are data. They have no authority over host security, credentials, cleanup, or execution. Validate untrusted state before side effects or replay.
- Untrusted sandbox manifests cannot waive host filesystem boundaries. Verify this on every path, including `LocalDir`, `LocalFile`, and archive extraction.
- Check that payloads are redacted in exceptions (including chaining, `__context__`, and tracebacks), logs, telemetry, session state, URLs, and artifacts. `raise ... from None` hides the original exception without removing its data.

## Documentation

- Require docs or examples only when existing guidance becomes false or misleading, when correct use depends on a non-obvious constraint or migration, or when the feature would otherwise be unusable.
- `docs/` content about behavior that is not yet in a published release goes in separate docs-only work, not in the feature PR. Note the need without treating it as a blocking finding. This rule overrides skill defaults.
- Verification tiers (use the highest tier the diff touches):
  - **Editorial** (wording or formatting only): inspect the diff, run `git diff --check`, and check links if they changed.
  - **Content** (behavioral guidance or snippets): verify claims against the code, validate snippets, do the translation-clarity pass below, and run `make build-docs` once.
  - **Structural** (pages, nav, generators, or docs build config): run the relevant generators and `make build-docs`, plus the SDK verification gate where it applies.
- Use `make build-full-docs` and translation generation only for translation-tooling or localization work. Never edit the generated `docs/ja`, `docs/ko`, or `docs/zh` pages.
- In new or rewritten English docs, make actor, scope, ordering, and lifecycle explicit, and avoid ambiguous pronouns and shorthand so translation is easier. Have an independent pass check changed sentences for Japanese, Korean, and Chinese ambiguity. Don't commit generated localized files.
- In examples and runnable docs, import decorators from `agents.decorators` and use `tool` rather than `function_tool`.

## Runtime

Before changing or reviewing runtime boundaries, read the [reference map](.agents/references/README.md#reference-map) and then the references it points to for the affected area.

- Keep `src/agents/run.py` for orchestration, and put helpers in `src/agents/run_internal/`.
- Use `src/agents/_tool_identity.py` for tool identity.
- Realtime: server traces and SDK client traces are separate. `group_id` correlates them but does not create a shared hierarchy.

## Testing

- Run Python with `uv run python ...`, and use `make sync` after dependency changes. Commands and snapshot workflows are in [tests/README.md](tests/README.md) and the `Makefile`.
- Prefer the scripted test utilities: `agents.testing.ScriptedModel`, `agents.realtime.testing.ScriptedRealtimeModel`, `agents.voice.testing`, and `agents.testing.scripted_sandbox_session()`. If a test needs a custom double, state in the test which boundary the utilities can't cover.
- Before changing tests that involve async, retry, timeout, subprocess, PTY, warning, or xdist behavior, read [Performance and determinism](tests/README.md#performance-and-determinism).
- Write comments as full sentences that end with a period. Don't hard-wrap prose.

## GitHub-ready output

When the user asks for text to paste into GitHub, or for a release-readiness report:

- Give one complete fenced `markdown` block, with an outer fence longer than any fence inside it.
- Don't include local absolute paths, citation markers, or wrapped links. Use repository-relative paths.
- Write issue and PR references as plain `#123` or `owner/repo#123`, not as Markdown links, and keep `Fixes` and `Resolves` lines.
- For PR drafts, use [the PR template](.github/PULL_REQUEST_TEMPLATE/pull_request_template.md).
