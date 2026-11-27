I saved the proposed version as `trimmed.md` and left `instructions.md` unchanged.

## 1. Target model
You named **claude-opus-5-5**. It has a profile, and that profile has been through this skill's tests at medium effort.

## 2. Word count
I had no tool to count words in this session, so these figures are estimates.
- **Before:** about 3,900 words
- **After:** about 3,150 words (about 19% shorter)

## 3. Changes
| Change | Reason |
|---|---|
| Cut the "About this file" block: the architecture notes, the 50-item skills list, the external-skills list with links, and the version history | Nothing in it tells the model what to do. The routing lines already name every skill. |
| Cut "I follow TDD with a strong emphasis…" and replaced it with one line: "Work in small increments that leave the codebase working." | It repeats the TDD paragraph and the Functional-style section. |
| Cut the **Key Principles** and **Preferred Tools** lists | Every bullet repeats the Testing, TypeScript or Code Style sections. Two lines said something new, so I moved them into Testing: the schema-reuse rule and the "repository harness / real-browser evidence" rule. |
| Cut "Write behavior tests first (TDD non-negotiable)" from Testing, and "Pure functions wherever possible" from Code Style | Each repeats a core principle stated nearby. |
| Changed "TEST-DRIVEN DEVELOPMENT IS NON-NEGOTIABLE" to normal case and "MINIMUM" to "minimum" | The profile says capitals now make the model apply a rule too broadly. The rule itself is unchanged. |
| Merged the two `grill-me` lines into one, and the two `find-gaps` lines into one | Each pair gave the same trigger twice. |
| Removed the internals from the `double-check`, `writing-for-agents` and `technical-writing` lines | They described what the skill does inside. The skill provides that when it loads. Each trigger is kept. |
| Shortened **Working with Claude** and renamed it **Capturing Learnings** | "Think deeply" is the kind of think-carefully line the profile says to cut. "ALWAYS FOLLOW TDD" and "follow TDD strictly" repeat the core TDD rule. "Assess refactoring after every green (only if adds value)" became part of the REFACTOR step. The repeated `tdd`, `refactoring` and `expectations` routing lines are gone, and `expectations` is now named in the bullet that uses it. |
| Cut "Always try `agent-browser` first" | It repeats "Prefer `agent-browser`". |
| Cut **Resources and References** | The model doesn't act on a list of links to handbooks. |
| Cut **Summary** | It repeats the core philosophy and the GREEN step. "Favor simplicity over cleverness" is a generic virtue. |

## 4. What I kept, and why
- **Kept exactly as written, because they guard actions that are hard to undo or need permission:** "Wait for commit approval before every commit", the `/setup` and hooks authorization rules, the CLAUDE.md write-authorization rule, and all three Output Guardrails. That includes the capitalized "ONLY" in plan-only mode and the "3-4 tool calls" limit.
- **Kept because they are your own decisions the model can't infer:** the definition of a phase of work, the timing of the mutation gate, the `N/A` evidence rule, the full ownership test for `xstate`, the `react-performance` and `evaluate-existing-solutions` procedures, and the `agent-browser` commands.

**Flagged for your decision. I kept these and did not cut them:**
- **Long routing lines** (about 400 more words could go). Many trigger lines also list the skill's scope, for example `bff-entry-points`, `render-code-shape` and `storyboard`. If each skill's own description already covers that scope, the lines could become "For X, load `skill`."
- **Code Style bullets** (about 40 words). "Use early returns…", "Use comments for non-obvious why…" and "Choose array methods or loops by clarity…" are close to what Opus does unprompted.
- **The `double-check` line.** The profile says Opus 5 checks its own work unprompted. I kept the line because it sends the model to the skill when you ask for a second opinion. It doesn't tell the model to verify every answer.
- **Two skills missing from the old list.** `observability` and `panel-review` are referenced but were not in the skills list I cut, which named `review` instead. You may want to check those names are correct.