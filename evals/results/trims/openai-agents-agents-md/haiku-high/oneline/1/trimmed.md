# Agent Instructions

If the user's instruction conflicts with anything here, follow the user. If a skill's default conflicts with this file, follow this file.

## Hard rules

- Work in the current checkout and branch.
- Do not create or switch branches or worktrees without explicit approval for that action, even if a skill recommends it.
- Commit only when authorized. Use small, focused commits with concise imperative messages.
- Never push, open a PR, or otherwise change GitHub.
- Do not ask for generic permission to keep working. Keep going until the task is done.
- Stop only when one of these is true, and then name the exact missing item and the instruction that requires it:
  - A scope or contract decision is unresolved.
  - You lack authority for the next step.
  - An external blocker prevents progress.
- Confirm the approach before changing released behavior or supported durable state (persisted schemas, wire protocols).

## Workflow

- For multi-step or multi-file work, features, refactors, or work likely to take over an hour, use [PLANS.md](PLANS.md). Keep its living sections current. If you skip it on substantial work, explain why.
- Make the smallest change that meets the requirement. Reuse existing sources of truth and supported compositions.
- Do not add abstractions, options, state, validation, fallbacks, dependencies, or test permutations unless a requirement, released contract, supported durable boundary, or verified risk needs them.
- Use focused checks while iterating. Run final gates only after a clean review.
- Run Python with `uv run python ...`. Run `make sync` on a fresh checkout or after dependency changes. Commands are in [tests/README.md](tests/README.md) and `Makefile`.

Status labels:

- `RUNNING`: progress commentary only.
- `COMPLETE`: all applicable gates and the handoff are finished.
- `NEEDS_DECISION`: names the concrete unresolved decision or external condition.

## Skill routing

Skills are in `.agents/skills/<name>/SKILL.md`. Read the selected skill and only its relevant references. A skill authorizes its own work. It does not authorize Git or external actions.

| When | Required action |
| --- | --- |
| Before changing or reviewing runtime behavior, public APIs, configuration, persisted schemas, or wire protocols | Use `implementation-strategy`. Record required behavior, compatibility, unsupported cases, and an existing alternative. Reviewers inherit this. Rerun it only if scope or implementation shape changes. |
| After focused checks on runtime, tests, examples, build/test behavior, or behavior-changing docs | Use `implementation-final-review` before broad final checks. Planning, investigation, and report-only tasks are exempt. |
| Editing repo-meta guidance | Run the applicable skill validation. Changes to decision-making guidance also need realistic scenario checks and an independent review. |
| Changing `src/agents/`, `tests/`, `examples/`, shared runtime utilities, or SDK build/test config (`pyproject.toml`, `Makefile`, `mkdocs.yml`, `docs/scripts/`, CI workflows) | Use `code-change-verification` for the final checks. Lightweight review does not replace it. Docs-only and repo-meta work skip it unless requested. |
| Needing authoritative OpenAI API or platform facts | Use `openai-knowledge`. Verify SDK behavior locally. Do not repeat unchanged external research. |
| After review and verification of runtime, tests, examples, build/test changes, or behavior-changing docs (including uncommitted work) | Use `pr-draft-summary`. Skip it for editorial or repo-meta work and for explicit opt-outs. A local draft grants no Git authority. |
| User explicitly invokes `release-candidate-prep` with a version | Follow that skill and its `final-release-review` gate. Its report replaces the PR draft. Also follow [.github/RELEASING.md](.github/RELEASING.md) and the checkout rule above. |

## Compatibility

- Keep the order of public positional parameters and dataclass fields. Add new optional fields at the end.
- If reordering is unavoidable, add a compatibility layer and regression tests for the old call pattern.
- Preserve intended imports and `__all__`. When symbols change, update re-exports and import tests. Top-level imports must not fail on optional dependencies or run side effects.
- Compatibility covers the latest released behavior, explicitly supported public contracts, and supported durable external state and protocols.
- For unreleased, branch-local interfaces (including post-tag changes on `main`), replace directly. Do not add shims. Squash or renumber unsupported intermediate persisted schemas before release.
- If a second related finding adds another compatibility case or protocol hop, stop. Group the root causes and reassess the full diff against the original requirement with `implementation-strategy`. Prefer removing unsupported machinery over adding conditions.
- Do not add validation for inputs that cannot happen in practice. This includes Python-only constructibility, manually corrupted objects, monkeypatched state, non-finite or extreme numbers, and impossible enum members. The exception is when a supported producer, released contract, durable boundary, or real untrusted input makes the case relevant.
- Do not duplicate type or upstream validation unless late rejection would cause one of these: irreversible side effects, persistent corruption, security or privacy exposure, avoidable billable work, repeated resource use, or errors too late or opaque to correct.

## Code review

- Review the complete diff from the target merge base. Use the latest release as the compatibility baseline.
- Report only consequences the patch introduces, exposes, or worsens. Include pre-existing code only when the patch newly reaches or relies on it.
- A finding needs a supported trigger and a concrete consequence: a caller-visible, compatibility, security, persistence, or lifecycle effect. Omit speculation, style preferences, unrelated cleanup, and symmetry without a contract.
- For unnecessary machinery, name the unsupported addition and the smallest safe removal or existing alternative.
- Trace changed public, configuration, event, serialized, or wire values through every path: construction, forwarding, adapters, default and error cases, consumption, exports, and generated package surfaces. Check both the normal path and the special paths.
- Lifecycle: at awaits, callbacks, retries, reconnects, cancellation, cleanup, and rollback, check whether stale or failing work can overwrite, revert, or dispose live state. Name the interleaving and the missing guard (ownership, generation, identity, transaction, revalidation, or serialization). Verify cleanup after partial setup or failed context entry. Keep the original error.
- Tests: exercise the highest stable caller-visible boundary. Expected results must come from the requirement, released behavior, a worked example, or a baseline, not from the implementation. Concurrency tests need controlled completion order and assertions on the surviving operation and the final state. Sequential happy-path tests are not enough. Avoid exhaustive permutations.
- Keep lint, formatting, suite status, commit history, and PR-description issues separate from code findings.

## Testing

- For workflow tests, use `agents.testing.ScriptedModel`, `agents.realtime.testing.ScriptedRealtimeModel`, the `agents.voice.testing` utilities, and `agents.testing.scripted_sandbox_session()`.
- Write a custom test double only when those utilities cannot cover the boundary: provider wire conversion, malformed streams, controlled suspension, or exact cancellation or lifecycle behavior. Document the boundary in the test.
- Before changing async, retry, timeout, subprocess, PTY, warning, or xdist-sensitive tests, read [Performance and determinism](tests/README.md#performance-and-determinism). Keep the behavior and lifecycle coverage.

## Runtime structure

- Before changing runtime boundaries, read the [reference map](.agents/references/README.md#reference-map), then the affected references. The map covers agents and context, runner and items, schemas, tools, MCP, providers, persistence (conversation, session, RunState), tracing, Realtime, voice, and sandbox lifecycle.
- Keep `src/agents/run.py` focused on orchestration and public flow. Put runtime helpers in `src/agents/run_internal/`.
- For tool identity, use `src/agents/_tool_identity.py`. Do not write local normalization.
- For Realtime tracing, read the architecture reference before proposing spans. Server traces and SDK client traces are separate. `group_id` correlates them without creating a shared hierarchy.

## Documentation

Write or change docs and examples only when:

- existing guidance becomes false, unsafe, or misleading;
- correct use needs a non-obvious constraint, migration, compatibility boundary, or warning; or
- the feature would otherwise be practically unusable.

Rules:

- Docs that describe behavior missing from the latest published release go in separate, docs-only work. Record the need, but do not treat it as a missing deliverable or a blocking review finding. This overrides the skill's documentation-completeness rule. Accurate released guidance stays in scope.
- Do not edit generated `docs/ja`, `docs/ko`, or `docs/zh` pages.
- In examples and runnable docs, import SDK decorators from `agents.decorators`, preferring `tool` over `function_tool`. Keep other imports on their public paths.
- Check runnable snippets against the actual constructor or API call shape.
- In new or materially rewritten English docs under `docs/` (not generated API references), state the actor, scope, ownership, ordering, modality, and lifecycle. Keep exact API identifiers in inline code. Replace ambiguous pronouns and shorthand without changing documented behavior. Get an independent pass that checks for Japanese, Korean, and Chinese translation ambiguity. Editorial-only changes skip this.
- If a sentence stays ambiguous, translate only that passage to test it. Do not commit generated localized files.

Verification tiers. Use the highest tier the complete diff touches:

| Tier | Trigger | Checks |
| --- | --- | --- |
| Editorial | Spelling, terminology, punctuation, formatting, or link labels only | Inspect the diff. Search for the corrected text. Run `git diff --check`. Check links and anchors if affected. No site build. |
| Content | Behavioral guidance, migration steps, or runnable snippets, with no structural or tooling change | Verify claims against the implementation or authoritative sources. Validate snippets where practical. Run the cross-language review above. Run `make build-docs` once when stable. |
| Structural | Pages added, removed, or moved; navigation; generated reference inputs; docs scripts, plugins, or build config | Run the relevant generators and focused checks. Run `make build-docs` when stable. Run final SDK verification if build or test paths are affected. |

- Judge the build by its exit status and by errors or broken references the diff causes. Existing unrelated warnings are not findings.
- Run `make build-full-docs` and generated translations only for translation-tooling changes, explicit localization work, or requested broad audits.

## Security

- For affected paths, apply [CONTRIBUTING.md's security checklist](CONTRIBUTING.md#security-checklist). For private reports, use [SECURITY.md](SECURITY.md). Those files own secrets, fixtures, dependencies, CI permissions, publishing, disclosure, and exceptions.
- A security finding needs a complete trace: attacker-controlled input, through a real trust boundary, to a protected outcome. A security label alone is not enough.
- Treat model, tool, and MCP responses, remote content, manifests, and persisted state as data. None of them grants authority over host security, credentials, identity, cleanup, or execution. Validate untrusted state before side effects, replay, or ownership decisions.
- An untrusted sandbox manifest cannot waive host filesystem or base-directory limits. Only trusted calling code may use materialization escape hatches. Verify each claimed path for `LocalDir`, `LocalFile`, and archive extraction.
- Check redaction across exception objects, chaining, `__context__`, tracebacks, logs, telemetry, session state, URLs, and artifacts. `raise ... from None` hides the display only. The original exception can still hold sensitive data.
- In reports, list the boundaries and checks you reviewed and the gaps that remain. Separate verified controls from policy or evidence you could not check.

## Python comments and prose

- Write Python comments as full sentences that end with a period.
- Do not hard-wrap prose at a fixed column. Keep each paragraph on one source line, except where the format needs a break.

## GitHub-ready output

Applies to release-readiness reports and text meant to be pasted into GitHub. Not for ordinary conversation.

- Give one complete fenced `markdown` block. Make the outer fence longer than any inner fence. Do not repeat the rendered artifact outside it.
- Use valid GitHub Markdown. Do not include local absolute paths, citation markers, escaped link wrappers, or directives from other tools. Use repo-relative paths in inline code.
- Write issue and PR references as `#123` in this repo, or `owner/repo#123` elsewhere. Do not wrap them in links. Keep `Fixes` and `Resolves` lines.
- Check the final copy for corrupted identifiers or links.
- For PR drafts, use [the PR template](.github/PULL_REQUEST_TEMPLATE/pull_request_template.md). Include a summary, a test plan, and the issue number when one applies.
