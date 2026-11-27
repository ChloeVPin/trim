# Prompt audit: `AGENTS.md`

**Assumptions**
- **Scope:** the working directory holds one file, `/tmp/claude-0/-home-user/491b55d6-d5f8-5d18-a03a-6ecc22dd0c0d/scratchpad/probe/b/AGENTS.md` (208 lines). There are no skills, rule files, `README.md`, `CLAUDE.md`, request code or git history. Nothing was skipped.
- **Target:** Codex CLI running GPT-6 Astra, as you stated.
- **Grounding:** I have no documented behavior for GPT-6 Astra. The Claude-specific model rules in the audit guide (pressure language, thinking prose, update suppressors) are therefore not asserted against it. Findings that rest on model behavior are low confidence and `flag` only.
- **Repository-grounded findings:** these don't depend on the model. They cover the file contradicting itself, stale facts, and Claude-specific names in a file Codex reads.
- **Web check:** a web search for GPT-6 Astra prompting guidance was declined, so none was done.
- **Edits:** none applied. The diff below is proposed only.

## Summary

The main defects are in the header and the file's identity, not in the guidance. A Codex-read `AGENTS.md` introduces itself as "Guidelines for Claude" and says "CLAUDE.md (this file)". It tells the agent to update a `CLAUDE.md` that isn't there, and it names the Claude Code tool `WebFetch` as a fallback. The 11-line header also contradicts the file: it says "~160 lines" for a 208-line file, and its skill list has drifted from the routing lines below it. The body is mostly reasoned routing text and real policy, which the audit keeps.

Counts by group:
- **Group 1 (dated prompt text):** 3 findings, all low confidence and flag-only.
- **Group 2 (configuration files):** 7 findings.
- **Groups 3 and 4:** not applicable, because there are no tool descriptions or request code.

## Findings (highest confidence first)

| # | Location | Evidence | Pattern | Why obsolete | Conf. | Action |
|---|---|---|---|---|---|---|
| 1 | `AGENTS.md:6` | "**CLAUDE.md** (this file): … (~160 lines, always loaded)" | Group 2: volatile specifics | The file is `AGENTS.md` and has 208 lines. Both claims are contradicted by the repository. | High | `remove` (hunk 2) |
| 2 | `AGENTS.md:7` vs `:126`, `:153` | The skill list omits `observability` and `panel-review`. It lists `review`, which no routing line uses. | Group 2: duplicated info that has drifted | A shadow list that disagrees with the routing lines it copies. The routing lines are the source of truth. | High | `remove` (hunk 2) |
| 3 | `AGENTS.md:1` | "# Development Guidelines for Claude" | Group 2: identity mismatch | A Codex/GPT agent reads this file, so the title addresses the wrong reader. | High | `rewrite` (hunk 1) |
| 4 | `AGENTS.md:3,11-13` | "v3 architecture generation from the current 4.9.0 package… Previous versions: v2.0.0… v1.0.0…" | Group 2: history narrative, pinned version | Archaeology with no behavioral effect, loaded every session. A version pin goes stale. | Medium | `remove` (hunk 2) |
| 5 | `AGENTS.md:8` | "impeccable + 17 steering commands", plus a run of pinned external URLs | Group 2: volatile specifics | The count and links rot as upstream repos change. Nothing checks them. | Medium | `remove` (hunk 2) |
| 6 | `AGENTS.md:180` | "Update CLAUDE.md only for local working policy…" | Group 2: stale self-reference | It sends the agent to write to a file this repo doesn't have. For Codex the owner is `AGENTS.md`. If the repo also keeps a separate `CLAUDE.md` for Claude Code, keep this and fix the others. | Medium | `rewrite` (hunk 4) |
| 7 | `AGENTS.md:189` | "fall back to other available tools (e.g. `WebFetch`, `curl`, or MCP browser tools)" | Claude Code tool name in a Codex-read file | As far as I know, Codex CLI has no tool called `WebFetch`. The agent would look for a tool that doesn't exist. This rests on my knowledge of Codex's tool set, not on the repo. | Medium | `rewrite` (hunk 5) |
| 8 | `AGENTS.md:169` | "## Working with Claude" | Group 2: identity mismatch | Same as finding 3. | Medium | `rewrite` (hunk 3) |
| 9 | `AGENTS.md:21` | "the numbered lifecycle phases in `README.md`" | Group 2: path check | No `README.md` exists in scope. It may live elsewhere in the real repo, so I can't call it contradicted. | Medium | `flag`: confirm the file exists in the source repo, or drop the clause |
| 10 | `AGENTS.md:17,99,166,174` | "**NON-NEGOTIABLE**", "ALWAYS FOLLOW TDD", "MINIMUM", "ONLY" | Group 1a: emphasis | Caps stack on a policy already stated about five times. I have no GPT-6 Astra evidence that this over-triggers. The TDD rule is real policy and the repeats currently agree with each other. | Low | `flag` |
| 11 | `AGENTS.md:171` | "Think deeply, follow TDD strictly" | Group 1b: prose steering thinking depth | Reasoning depth is normally set in the agent's own config (for Codex, `model_reasoning_effort`). I can't confirm GPT-6 Astra ignores the prose. | Low | `flag`: consider cutting "Think deeply" |
| 12 | `AGENTS.md:167` | "produce a first draft of output within 3-4 tool calls" | Group 1f: numeric cadence | It can collide with line 107, which loads several skills before code changes begin. It has no stated reason. | Low | `flag` |

## Kept on purpose

- **Routing lines (`:106-153`).** These are trigger text, where calibrated specificity is legitimate. Line 134 (`xstate`) is long but carries real decision criteria.
- **Real policy and safety rules.** "Wait for commit approval" (104), plan-only mode (166), and the onboarding and hook authorization limits (155-159).
- **TDD wording that repeats but doesn't disagree.** I checked lines 17, 27, 49, 98, 174 and 102/58 for conflicts and found none.
- **Neutral phrasing that already works for Codex.** "when installed", "the host's one-question mechanism" (110), and "a different provider when possible" (151).

## Proposed diff

Hunk 2 resolves findings 1, 2, 4 and 5 together, because they all sit in the same block. Hunks 1 and 3-5 are independent. Findings 9-12 have no hunk.

```diff
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -1,1 +1,1 @@                               # hunk 1 (finding 3)
-# Development Guidelines for Claude
+# Development Guidelines
@@ -3,11 +3,1 @@                                # hunk 2 (findings 1, 2, 4, 5)
-> **About this file:** v3 architecture generation from the current 4.9.0 package. Core principles live here; detailed patterns load on demand via skills.
->
-> **Architecture:**
-> - **CLAUDE.md** (this file): Core philosophy + quick reference (~160 lines, always loaded)
-> - **Skills**: Detailed patterns loaded on-demand (specification, ubiquitous-language, … review)
-> - **External skills**: Loaded on-demand from community repos (impeccable + 17 steering commands from …)
-> - **Agents**: Specialized subprocesses for verification and analysis
->
-> **Previous versions:**
-> - v2.0.0: Modular with @docs/ imports (~3000+ lines always loaded)
-> - v1.0.0: Single monolithic file (1,818 lines)
+Core principles live here; detailed patterns load on demand via skills.
@@ -169,1 +169,1 @@                              # hunk 3 (finding 8)
-## Working with Claude
+## Working Practices
@@ -180,1 +180,1 @@                              # hunk 4 (finding 6)
-- Update CLAUDE.md only for local working policy it is declared to own, and only
+- Update AGENTS.md only for local working policy it is declared to own, and only
@@ -189,1 +189,1 @@                              # hunk 5 (finding 7)
-Prefer `agent-browser` for web automation. If it is not installed, fall back to other available tools (e.g. `WebFetch`, `curl`, or MCP browser tools). Always try `agent-browser` first.
+Prefer `agent-browser` for web automation. If it is not installed, fall back to other available tools (e.g. `curl` or MCP browser tools). Always try `agent-browser` first.
```

Hunks 2 and 4 are only proposed and are never applied on a blanket request. Their basis is the file contradicting itself, not the model.

Two caveats before you accept them:
- If a separate `CLAUDE.md` is also maintained for Claude Code, check whether the Claude-flavored wording is intentional shared text before taking hunks 1, 3 and 4.
- After editing, grep your other instruction files for the removed header's claims (`~160 lines`, `4.9.0`), in case something matches on them.
