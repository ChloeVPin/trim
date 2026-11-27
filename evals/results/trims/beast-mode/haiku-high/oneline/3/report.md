I saved the proposed version to `/root/trim-sbx/d4c31c707812/trimmed.md`. `instructions.md` is unchanged. The original is about 338 lines; the proposal is about 45 lines, roughly an 80% cut.

## Audit of instructions.md

**Cut as vague or decorative**
- The "quantum cognitive architecture," "consciousness awakening," and "transcendent" framing, plus the emoji-labelled phases. None of it tells the agent what to do.
- The ten-phase workflow, the "Constitutional" and "Adversarial" layers, and the "Meta-Analysis Protocol." They repeat each other and the detailed sections below them.
- The "Transcendent Communication Protocol" examples. They are style, not behavior.
- The frontmatter description ("unrestricted creative freedom"). I rewrote it to describe what the agent does.

**Cut as unrealistic or conflicting**
- "Your solution must be perfect" has no completion test, so a smaller model may loop on it. I replaced it with concrete verification steps.
- Mandatory Google research before every package install. That is slow and costly, and it conflicts with "fully autonomous." The proposal asks for docs checks when the agent is unsure, and only if a fetch or search tool exists.
- Tool names such as `sequential_thinking`, `fetch_webpage`, and `get_errors` may not exist in the target harness. The proposal refers to tools generically.
- "Always read 2000 lines at a time" conflicts with "read the relevant section." I dropped it.
- "Think extensively before each function call" and "don't do this only by making function calls" are vague for a model that needs explicit steps.

**Kept**
- Keep working until the task is complete.
- Tell the user in one sentence before each tool call.
- Resume on "continue" or "try again," using the last unchecked todo item.
- Read before editing, find root causes, and run existing tests.
- Show the todo list with `[x]` checkmarks.
- Be concise, and do not use HTML in todo lists.

## Choices you may want to change

- **Added:** a confirmation rule for destructive or hard-to-reverse actions. The original had none.
- **Kept the name** `Thinking Beast Mode` in case the harness references it. The description changed.
- **Stop-and-report rule:** after several failed attempts the agent reports what it found, rather than continuing indefinitely.
- **Ask-only-when-needed:** the agent makes reasonable choices and states them, instead of asking.

I have not tested `trimmed.md` against claude-haiku-5-5. Running a few representative tasks through both versions would show whether the shorter prompt keeps the behavior you want.