# Prompt audit: `CLAUDE.md`

## Assumptions

- **Scope:** `CLAUDE.md` is the only file in the working directory (208 lines). It imports nothing. There is no git history, so `git blame` provenance isn't available and findings rest on idiom and repository checks.
- **Target model:** the model running this audit (Claude Sonnet 5.5), since this is a coding-agent instruction file.
- **Groups 3 and 4:** not applicable, because there are no tool definitions or request code.
- **Provider markers:** no non-Anthropic markers found.
- **Edits:** none applied. The diff below is proposed only.

## Inventory

- **Instruction file:** `CLAUDE.md`, always loaded.
- **Skills it routes to:** about 50 by name. Their bodies are not in scope and were not audited.
- **Paths and commands it names:** `README.md`, `/setup`, `/teach-me`, `/panel-review`, `agent-browser`.

## Summary

- **Two stale facts that contradict the file itself.** The header says "~160 lines" but the file is 208 lines. The line-7 skill roster lists `review`, but the body routes to `panel-review`, and the body routes to `observability`, which the roster omits.
- **History narrative in an always-loaded file.** The version archaeology in lines 3 and 11-13 gives the model no rule to follow.
- **Dated phrasing.** "Think deeply", the all-caps TDD refrain repeated several times, a numeric tool-call cadence, and a generic link list.

**Counts:**

| Group | Findings |
|---|---|
| 1 (dated prompt text) | 5 |
| 2 (brittle configuration files) | 4 (2 high, 1 medium, 1 flag) |
| 3 (tool descriptions) | not applicable |
| 4 (request config) | not applicable |

## Findings, highest confidence first

| # | Location | Evidence | Pattern | Why obsolete | Conf. | Action |
|---|---|---|---|---|---|---|
| 1 | `CLAUDE.md:6` | "**CLAUDE.md** (this file): … (~160 lines, always loaded)" | Group 2, volatile specifics | The file is 208 lines. The claim is contradicted by the file itself. | High | `rewrite`: drop the count |
| 2 | `CLAUDE.md:7` vs `:126`, `:153` | The roster lists `review`. The body says "load the `observability` skill" (126) and "load the `panel-review` skill" (153). | Group 2, internal contradiction | The roster names a skill nothing points to and omits two skills the body loads. A model matching names against the roster can miss them. | High | `rewrite`: replace `review` with `panel-review` and add `observability` |
| 3 | `CLAUDE.md:11-13` | "**Previous versions:** v2.0.0: Modular with @docs/ imports (~3000+ lines always loaded) / v1.0.0: Single monolithic file (1,818 lines)" | Group 2, history narratives; Group 1d, migration-relative phrasing | A rule's authority is the behavior it prescribes. This is a diff against versions the model never saw, and it costs tokens every session. | High | `remove` |
| 4 | `CLAUDE.md:3` | "v3 architecture generation from the current 4.9.0 package" | Group 2, history and version pins | "v3" and "4.9.0" are release archaeology and rot at the next release. | Medium | `rewrite` |
| 5 | `CLAUDE.md:171` | "**Core principle**: Think deeply, follow TDD strictly, …" | Group 1b, prose steering thinking depth | Depth is controlled by `effort`, not prose. On current models "think deeply" has little effect. | Medium | `rewrite` |
| 6 | `CLAUDE.md:49`, `:174` | "(TDD non-negotiable)", "ALWAYS FOLLOW TDD for behavior change" | Group 1a, pressure language; Group 1c, padding | Line 17 already states the policy and its scope, and line 183 points to the `tdd` skill. The repeated capitals add no information and bias toward over-application. | Medium | `rewrite` to plain wording. Keep line 17 as the single emphatic statement. |
| 7 | `CLAUDE.md:167` | "produce a first draft of output within 3-4 tool calls" | Group 1f, numeric cadence | A tool-call count tuned to a model that over-explored. The goal is an early draft, not a count. | Medium | `rewrite` without the number |
| 8 | `CLAUDE.md:199-204` | Links to the TypeScript Handbook, Testing Library, testingjavascript.com and fp-ts | Step 3 deletion rule; Group 2, volatile specifics | The model already knows these. The links carry no repository-specific context and cost tokens every session. The fp-ts link also points at a library the guidelines never adopt. | Medium | `remove` |
| 9 | `CLAUDE.md:21` | "the numbered lifecycle phases in `README.md`" | Group 2, volatile specifics | No `README.md` exists in the audited directory. It may live in the full repository. | Low | `flag`: confirm the path |
| 10 | `CLAUDE.md:189` | "Prefer `agent-browser` … Always try `agent-browser` first." | Group 1c, repetition as reinforcement | The second sentence restates the first. | Low | `flag` |
| 11 | `CLAUDE.md:135` | "baseline the symptom, attribute the cost with evidence, apply one rule at a time … re-measure" | Group 1c, step choreography | This duplicates the workflow the `react-performance` skill owns, and I couldn't check the skill body. | Low | `flag` |
| 12 | `CLAUDE.md:155`, `:159` | `/setup`, "the curl installer" | Group 2, volatile specifics | Both live outside this directory, so I can't verify them. I never ran or probed them. | Low | `flag` |

**Left alone, per the keep list:**

- **Scoped constraints:** the reasoned prohibitions, such as "Wait for commit approval before every commit" and plan-only mode.
- **Routing paragraphs:** the long `xstate` ownership paragraph (134) and the other trigger text.
- **Working redundancy:** the repeated TDD statements and skill pointers agree with each other, so apart from the capitals in #6 they stay.
- **Closing recap:** the closing Summary section.
- **Tool contract:** the `agent-browser` workflow.

## Proposed diff

Each hunk is one finding. Hunks 5 and 6 pair with each other.

```diff
--- CLAUDE.md
+++ CLAUDE.md
@@ line 3 (finding 4) @@
-> **About this file:** v3 architecture generation from the current 4.9.0 package. Core principles live here; detailed patterns load on demand via skills.
+> **About this file:** Core principles live here; detailed patterns load on demand via skills.

@@ line 6 (finding 1) @@
-> - **CLAUDE.md** (this file): Core philosophy + quick reference (~160 lines, always loaded)
+> - **CLAUDE.md** (this file): Core philosophy + quick reference (always loaded)

@@ line 7 (finding 2), edits inside the skills list @@
-… acceptance-review, debugging, ci-debugging, tdd, …
+… acceptance-review, debugging, ci-debugging, observability, tdd, …
-… find-skills, find-gaps, double-check, graph-engineering, review)
+… find-skills, find-gaps, double-check, graph-engineering, panel-review)

@@ lines 10-13 (finding 3) @@
->
-> **Previous versions:**
-> - v2.0.0: Modular with @docs/ imports (~3000+ lines always loaded)
-> - v1.0.0: Single monolithic file (1,818 lines)

@@ line 49 (finding 6) @@
-- Write behavior tests first for new or changed behavior (TDD non-negotiable)
+- Write behavior tests first for new or changed behavior

@@ line 167 (finding 7) @@
-- **Incremental output** — When exploring a codebase, produce a first draft of output within 3-4 tool calls. Refine iteratively rather than front-loading all exploration before producing anything.
+- **Incremental output** — When exploring a codebase, produce a first draft early and refine it iteratively rather than front-loading all exploration before producing anything.

@@ lines 171, 174 (findings 5, 6) @@
-**Core principle**: Think deeply, follow TDD strictly, capture learnings while context is fresh.
+**Core principle**: Follow TDD strictly and capture learnings while context is fresh.
@@
-- ALWAYS FOLLOW TDD for behavior change; keep pure refactors/reductions behaviorally green from passing, proportionate preservation evidence
+- Follow TDD for behavior change; keep pure refactors/reductions behaviorally green from passing, proportionate preservation evidence

@@ lines 199-205 (finding 8) @@
-## Resources and References
-
-- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
-- [Testing Library Principles](https://testing-library.com/docs/guiding-principles)
-- [Kent C. Dodds Testing JavaScript](https://testingjavascript.com/)
-- [Functional Programming in TypeScript](https://gcanti.github.io/fp-ts/)
-
```

## Next steps

Hunks 1 to 3 are verifiable against the file itself and are safe to take as a set. Hunks 4 to 8 are medium confidence, so take them selectively. The staleness findings under the Group 2 volatile-specifics row (1 and 9) are proposals only, to confirm before applying.
