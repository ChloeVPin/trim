Word counts are done. Writing up the report now.

I saved the proposed version as `trimmed.md`; `instructions.md` is unchanged.

## 1. Target model
**claude-opus-5-5**, which you named. Its profile has been tested at medium effort.

## 2. Word count
**About 2,935 words before and 1,941 after, a cut of about 34%.** I counted with ripgrep by splitting on whitespace, so each Markdown token or URL counts as one word. The "before" figure may be off by a few words because I tallied the last part of the file by hand.

## 3. Changes
| Change | Reason |
|---|---|
| Removed the "About this file" block: the architecture notes, the list of about 50 skills, the external repo links and the v1/v2 history | The model doesn't use any of it. Each skill it needs is already named in a routing line below. |
| Removed the "Quick Reference" section | It repeated the Testing, TypeScript and Code Style sections. I moved its two lines that appear nowhere else (reuse the production schema; follow the repo harness and prefer real-browser evidence) into Testing. |
| "TEST-DRIVEN DEVELOPMENT IS NON-NEGOTIABLE" → "is required"; "MINIMUM" → "minimum" | On Opus 5.5, capitals and forceful wording cause rules to be over-applied. The rule itself is unchanged. |
| Shortened "I follow TDD with a strong emphasis on…" to one line about small, working increments | The TDD part repeated the paragraph above it. |
| Removed "Pure functions wherever possible" and the duplicate "Prefer immutable values" | Both repeat the Code Style core principle. |
| Turned the skill routing lines into one list, removing duplicates | `tdd` and `refactoring` were each listed twice, `grill-me` twice (lines 110 and 150) and `find-gaps` twice (116 and 149). I also removed text that described what a skill contains, such as `double-check`'s reviewer selection, `writing-for-agents`' topic list and `bff-design`'s question list, since the skill supplies that once loaded. |
| Removed "Working with Claude": "Think deeply", "ALWAYS FOLLOW TDD", "Assess refactoring after every green" and the repeated skill pointers | The guidance for this model is to drop "think carefully" instructions. The other lines repeat the workflow section. "Only if it adds value" now sits on the REFACTOR step. |
| Merged "Prefer agent-browser…" and "Always try agent-browser first" | They said the same thing. |
| Removed "Resources and References" and "Summary" | The handbook links don't change what the model does. The summary repeated Core Philosophy and the GREEN step. |

## 4. What I kept and why
- **Kept word for word:** "Wait for commit approval", the `/setup` and hooks authorization rules, the Output Guardrails (artifact boundary, plan-only mode, first draft within 3–4 tool calls) and the rule on when CLAUDE.md may be updated. These guard commits, writes and scope.
- **Kept in full:** the definition of a phase, the mutation-gate steps, the xstate ownership tests, the react-performance procedure and the limits on evaluate-existing-solutions. Each is a specific choice you made that the model couldn't work out on its own.
- **Kept:** the agent-browser commands, because they give exact syntax.

**Your call on these:**
- **The `double-check` route.** The maker says to delete self-verification lines for Opus 5 but hasn't confirmed that for 5.5. Because yours routes to a skill for a second opinion, I kept a one-line version. Dropping it saves about 6 words.
- **The about-block.** If people maintaining the file rely on its version history, you could keep it as an HTML comment instead.

**Possible inconsistencies, which I left as they were:** the routing lines mention `observability` and `panel-review`, but the old skill list didn't include `observability` and listed `review` rather than `panel-review`. Check that those names match the installed skills.