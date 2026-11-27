The audit is done. The edited copy is at `/root/trim-sbx/86c9aec3268c/trimmed.md`, and `instructions.md` is unchanged.

**Step 0 assumptions**
- **Scope:** `instructions.md` only, as named in the request. The working directory holds no other files, and this is not a git repo, so there is no `git blame` provenance.
- **Target model:** `claude-haiku-5-5`, as named in the request. The file is read by the coding agent, so it is audited against that model.
- **Not read:** the installed skills and external sources it references. They live outside the working directory.

**Summary**
The file is mostly sound. Its routing and TDD content is load-bearing, and I left it alone. The findings are a few shouted mandates, a history block, and a skill index that has drifted from the routing lines. Group 1 has 3 findings and Group 2 has 2. Groups 3 and 4 are not applicable: the file has no tool descriptions and no request-building code. Nothing in the file is a Haiku 5.5 API fossil, such as `budget_tokens`, prefill, forced `tool_choice`, or sampling parameters. I found no contradictions between passages within the file.

**Report (highest confidence first; all medium, none high)**

| # | Location | Evidence | Pattern | Why obsolete | Action |
|---|---|---|---|---|---|
| 1 | `instructions.md:11-13` | `**Previous versions:** v2.0.0 … v1.0.0 …` | 2 (Group 2 history narrative) | Changelog archaeology. Authority comes from the rules, not from past versions. | remove |
| 2 | `instructions.md:7` | Skills bullet enumerates ~50 skill names | Group 2 duplicated info | The list has drifted from the routing lines. It names five skills with no routing line (`test-design-reviewer`, `front-end-testing`, `react-testing`, `diagrams`, `review`) and omits routed ones (`observability`, `panel-review`, `clarity`, `simple-english`, `writing-for-agents`, `skill-creator`, `skill-doctor`). | rewrite to a one-line pointer to the routing lines |
| 3 | `instructions.md:17` | `TEST-DRIVEN DEVELOPMENT IS NON-NEGOTIABLE FOR NEW OR CHANGED BEHAVIOR.` | 1a pressure language | Haiku 5.5 follows literally, so shouted mandates over-apply. The constraint itself is kept. | rewrite to `Test-driven development is required for new or changed behavior.` |
| 4 | `instructions.md:174` | `ALWAYS FOLLOW TDD for behavior change; …` | 1a pressure language | Same as #3. | rewrite to `Follow TDD for behavior change; …` |
| 5 | `instructions.md:171` | `Core principle: Think deeply, follow TDD strictly, …` | 1b thinking-depth prose | Thinking depth is set by effort, not prose. `CLAUDE.md` has no frontmatter field for effort, so the agent's own settings control it. | remove `Think deeply,` |

**Flagged, not edited**
- `instructions.md:21` names `README.md`, and `:117` names `plans/`. Neither exists in this directory, which holds only this file. I can't tell whether they exist in the full project, so check them there.
- `instructions.md:3` says "current 4.9.0 package" and "v3". This is an unverifiable version pin with no date.
- `instructions.md:167` says "first draft … within 3-4 tool calls". Its shape resembles the "every N tool calls" cadence pattern. Haiku 5.5's migration notes don't document over-exploration, though, so test before removing.

**Considered and kept**
- The TDD rule is restated about eight times. The wording is consistent, so this is working redundancy.
- The `grill-me` and `find-gaps` routing lines each appear twice with matching instructions.
- "Wait for commit approval" (`:104`) is a real human gate.
- The xstate paragraph (`:134`) is long, but its rationale is load-bearing.
- Haiku 5.5's documented early stopping in long prompts applies at `low` effort. Its default is `medium`, and the repo shows no such behavior, so I didn't add the keep-working text.

**Verification**
- Line counts check out: `instructions.md` has 208 lines and `trimmed.md` has 204. The four removed lines are the history block, and the other edits are in-place.
- A grep confirms the removed strings are gone from `trimmed.md`.
- I did not run behavioral probes. Step 7 calls for Haiku runs against your tasks, and this session has no shell to run them. The edits are low-risk, but they are unmeasured.

**Next step:** None. All findings are in an agent configuration file, so no sibling workflow applies. To adopt the edits, diff `trimmed.md` against `instructions.md` and take the hunks you want.