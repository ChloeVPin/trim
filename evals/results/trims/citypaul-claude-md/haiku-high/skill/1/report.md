I wrote the proposed version to `/root/trim-sbx/caa8d981a606/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile in the skill, marked "tested at high effort." I did not run the skill's evals on this trim.

**2. Words:** I have no word counter here, so these are estimates. Roughly 3,500 before and 2,100 after, about 40% shorter.

**3. Changes and reasons**

- **Removed the "About this file" block** (version history and the list of community skill sources). It changes nothing the model does. If the attribution list matters for licensing, restore it. It does not affect behavior.
- **Removed the Summary and Resources sections.** The Summary restated the rules. The links are reference material the model does not act on.
- **Merged the duplicate principles.** Key Principles, Testing Principles, Preferred Tools, and Code Style overlapped. They are now one list, with each rule stated once.
- **Cut repeated TDD lines.** TDD was restated about six times. The "ALWAYS FOLLOW TDD" line and the "assess refactoring after every green" line duplicated the workflow steps.
- **Removed capitals and "non-negotiable."** The profile says repeated emphasis over-applies on this model. The rule itself is unchanged. Restore the emphasis if you want it stronger.
- **Merged repeated skill entries.** `grill-me` and `find-gaps` each appeared twice. The routing triggers are shorter, but each skill name and its distinguishing condition is kept.

**4. Kept as written or in substance**

- The commit approval gate, the `/setup` authorization rule, the hook conditions, the artifact-boundary rule, plan-only mode, and the CLAUDE.md write authorization.
- The mutation gate, including the `N/A` rules.
- The xstate two-test rule and its examples. The profile says Haiku needs the examples.
- "Always try `agent-browser` first" and the browser steps.
- "First draft within 3–4 tool calls."

**5. Unsure items**

- **The whole skill-routing block** is about 40% of the file. If these skills are not installed where Haiku runs, dropping the block saves most of that. I kept it because the skill names and triggers are facts the model cannot know.
- **"Think deeply"** in the Working with Claude section. The maker lists thinking instructions as cuts for Opus, not Haiku. I kept it. Dropping it saves almost nothing.

**6. Suggested additions (not applied)**

- For coding work, a line to run a real check (the relevant test or typecheck) before reporting a change done. The profile lists this for Haiku coding agents, and the file does not have it.
- A line to keep working until the task is done, if agents on this file stop early.