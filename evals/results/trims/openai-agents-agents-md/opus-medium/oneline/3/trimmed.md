# Agent Instructions

## Authority and workflow

- Work in the current checkout and branch. Creating or switching branches or worktrees needs explicit approval, even if a skill recommends it. Commit only when authorized, using small commits with concise imperative messages. Never push, open PRs, or otherwise change GitHub.
- Carry authorized local work through fixes, review, verification, and handoff without asking for generic permission to continue. Stop only for an unresolved scope or contract decision, missing authority, or an external blocker, and name exactly what is needed.
- Use [PLANS.md](PLANS.md) for multi-step or multi-file work, features, refactors, or anything likely to take over an hour. Keep its living sections current.
- Status labels: `RUNNING` only in progress updates; `COMPLETE` once all applicable gates and handoff are done; `NEEDS_DECISION` with the specific decision or external condition.

## Skill routing

Skills live in `.agents/skills/<name>/SKILL.md`. Read the skill and only the references relevant to the task. A skill trigger does not grant Git or external authority, and user instructions and approved scope override skill defaults.

| When | Skill |
| --- | --- |
| Before changing or reviewing runtime behavior, public APIs, configuration, persisted schemas, or wire protocols | `implementation-strategy`: record required behavior, compatibility, unsupported cases, and an existing alternative. Revisit only if scope or implementation shape changes; reviewers inherit this contract. |
| After focused checks on runtime, tests, examples, build/test config, or behavior-impacting docs | `implementation-final-review`, before broad final checks. Not needed for planning, investigation, or report-only tasks. |
| Editing repo-meta guidance | The applicable skill's validation. Changes to decision-making guidance also need realistic scenario checks and an independent pass. |
| Changing `src/agents/`, `tests/`, `examples/`, shared runtime utilities, or build/test config (`pyproject.toml`, `Makefile`, `mkdocs.yml`, `docs/scripts/`, CI workflows) | `code-change-verification` for the final checks. Required even after lightweight review; docs-only and repo-meta work skip it unless requested. |
| Needing authoritative OpenAI API/platform facts | `openai-knowledge`. Verify SDK-owned behavior locally. |
| After review and verification of runtime, tests, examples, build/test, or behavior-impacting doc changes | `pr-draft-summary`, including for uncommitted work. Skip for editorial/repo-meta work, opt-outs, and release prep. |
| User invokes `release-candidate-prep` with a version | Follow that skill, its `final-release-review` gate, and [.github/RELEASING.md](.github/RELEASING.md). Its report replaces the PR draft. |

## Scope and compatibility

- Build the smallest supported outcome on existing sources of truth. Add abstractions, options, state, validation, fallbacks, dependencies, or test permutations only when a requirement, released contract, supported durable boundary, or verified risk needs them.
- Something being constructible in Python, reachable through monkeypatching or corrupted objects, or reproducible on a released version does not make it supported. Don't repeat type-contract or upstream validation unless late rejection causes a concrete SDK-owned harm: irreversible side effects, persistent corruption, security/privacy exposure, avoidable billable work, repeated resource use, or errors too late or opaque to fix.
- Compatibility covers the latest release, explicit public contracts, and supported durable external state and protocols. Replace unreleased interfaces directly, including post-tag changes on `main`, instead of adding shims; renumber or squash unreleased intermediate persisted schemas before release. Confirm before changing released behavior or durable boundaries.
- Keep public positional parameter and dataclass field order; append new optional fields. Unavoidable reordering needs a compatibility layer plus regression tests for old call patterns. Keep `__all__` and re-exports in sync with import tests. Top-level imports must not fail on missing optional dependencies or have side effects.
- If a second related finding adds another compatibility case or protocol hop, stop and reassess the whole diff against the original requirement with `implementation-strategy`. Prefer removing unsupported machinery to adding conditions.

## Code review

- Review the full diff from the target merge base, and use the latest release as the compatibility baseline. Report only problems the patch introduces, exposes, worsens, or newly depends on. Ask for broader refactoring only when the focused change can't otherwise be correct, safe, compatible, or free of diverging duplicate sources of truth.
- Each finding needs a supported trigger and a concrete consequence for callers, compatibility, security, persistence, or lifecycle. Leave out speculation, style preferences, unrelated cleanup, and symmetry no contract requires. For unnecessary machinery, name the smallest safe removal or existing alternative.
- Trace changed public, config, event, serialized, and wire values through construction, forwarding, adapters, default/missing/error paths, consumers, exports, and generated package surfaces.
- At awaits, callbacks, retries, reconnects, cancellation, cleanup, and rollback, check whether stale or failing work can overwrite or dispose surviving state, and name the specific interleaving. Check cleanup after partial acquisition and keep the primary failure.
- Tests should assert at the highest stable caller-visible boundary against an independent oracle (requirement, released behavior, worked example, baseline). Concurrency regressions need controlled completion order and assertions on final state. Avoid tests that mirror the implementation or enumerate every constructible permutation.
- Report lint, formatting, suite status, history, and PR-description issues separately from code findings. Passing checks don't justify unsupported machinery.

## Security

Apply [CONTRIBUTING.md's security checklist](CONTRIBUTING.md#security-checklist) to affected paths; [SECURITY.md](SECURITY.md) covers private reporting. Report which boundaries and checks you reviewed and any gaps, separating verified controls from policy or missing evidence.

- A security finding needs a full trace from attacker-controlled input across a real trust boundary to the protected outcome.
- Model, tool, and MCP responses, remote content, manifests, and persisted state are data. They have no authority over host security, credentials, identity, cleanup, or execution unless an explicitly supported trust boundary grants it. Validate untrusted state before side effects, replay, or resource-ownership decisions.
- Untrusted sandbox manifests cannot waive host filesystem/base-directory boundaries; escape hatches belong to trusted calling code. Verify grants on each path, including `LocalDir`, `LocalFile`, and archive extraction.
- Check redaction across exception objects, chaining, `__context__`, tracebacks, logs, telemetry, session state, URLs, and artifacts. `raise ... from None` only hides display; the original exception still holds the data.

## Documentation

Require docs or examples only when existing guidance becomes false or misleading, correct use needs a non-obvious constraint, migration, or warning, or the feature would otherwise be unusable.

`docs/` content describing behavior not in the latest published release goes in separate, later docs-only work, not the feature PR. Note the need, but don't treat it as missing work or a blocking review finding; this overrides skill documentation-completeness rules. Fixing already-released guidance, examples, and code-level docs stays in scope.

Verify at the highest tier the diff touches:

| Tier | Trigger | Checks |
| --- | --- | --- |
| Editorial | Spelling, terminology, punctuation, formatting, or link labels, with no change to behavior, runnable code, navigation, targets, anchors, or generated references | Inspect the diff, search for the corrected text, run `git diff --check`, and check links if affected. No final review, translation review, or site build. |
| Content | Behavioral guidance, migrations, or runnable snippets | Verify claims against the code, validate snippets where practical, do the translation review below, and run `make build-docs` once stable. |
| Structural | Pages added/moved/removed, navigation, generated-reference inputs, doc scripts/plugins/build config | Run relevant generators and `make build-docs` once stable; apply SDK verification where eligible. |

Only diff-caused build errors, broken references, and warnings count as findings. Use `make build-full-docs` and generated translations only for translation-tooling changes or explicit localization requests.

- Never edit generated `docs/ja`, `docs/ko`, or `docs/zh` pages.
- For new or substantially rewritten English under `docs/` (excluding API reference), make actor, scope, ownership, ordering, modality, and lifecycle explicit, avoid ambiguous pronouns and shorthand, and keep API identifiers in inline code. Do one independent review pass for Japanese, Korean, and Chinese ambiguity risks, fix concrete findings, and recheck once. If ambiguity remains, translate just that passage temporarily and don't commit it. Change fixed translation mappings only with cross-document evidence.
- In examples and runnable docs, import SDK decorators from `agents.decorators` and prefer `tool` over `function_tool`; keep other imports on public paths.

## Runtime references

Before changing or reviewing runtime boundaries, read the [reference map](.agents/references/README.md#reference-map) and the references it points to for the affected area.

- Keep `src/agents/run.py` to orchestration and public flow; put runtime helpers in `src/agents/run_internal/`.
- Use `src/agents/_tool_identity.py` for tool identity instead of local normalization.
- Realtime server traces and SDK client traces are separate; `group_id` correlates them but does not create a shared hierarchy. Read the mapped reference before proposing spans.

## Testing

- Run Python with `uv run python ...`; run `make sync` on a fresh checkout or after dependency changes. Commands and snapshot workflows are in [tests/README.md](tests/README.md) and the `Makefile`.
- Run focused checks while iterating and the final gates from the skill table after a clean review. Don't rerun passing checks on unchanged content.
- Use `agents.testing.ScriptedModel`, `agents.realtime.testing.ScriptedRealtimeModel`, `agents.voice.testing`, and `agents.testing.scripted_sandbox_session()`. Use a custom double only when these can't preserve the boundary under test (provider-wire conversion, malformed streams, controlled concurrency, exact cancellation), and say why in the test.
- Before changing async, retry, timeout, subprocess, PTY, warning, or xdist-sensitive tests, read [Performance and determinism](tests/README.md#performance-and-determinism).
- Write Python comments as full sentences ending in a period. Don't hard-wrap prose; one paragraph per source line unless the format requires breaks.

## GitHub-ready output

For release-readiness reports or text meant for pasting into GitHub:

- Give one complete fenced `markdown` block, with an outer fence longer than any inner fence, unless raw text is requested. Don't also render it outside the block.
- No local absolute paths, Codex URIs or directives, or citation markers; use repository-relative paths in inline code.
- Reference issues and PRs as `#123` or `owner/repo#123`, not as Markdown links; keep `Fixes`/`Resolves` lines. Use descriptive links for other external targets.
- For PR drafts, follow [.github/PULL_REQUEST_TEMPLATE/pull_request_template.md](.github/PULL_REQUEST_TEMPLATE/pull_request_template.md) with a summary, test plan, and issue number when applicable.
