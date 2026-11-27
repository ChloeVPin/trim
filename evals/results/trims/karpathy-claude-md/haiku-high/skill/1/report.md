The proposed version is saved at `/root/trim-sbx/adce8a9e9abc/trimmed.md`. `instructions.md` is unchanged.

## 1. Target model

- **Target:** `claude-haiku-5-5`, named by you.
- **Profile:** tested at high effort. Haiku needs more explicit direction than the larger models, so I kept the cuts small. The file is already short, so there was little to cut.

## 2. Word count

About 340 words before and about 305 after, roughly a 10% reduction. These are estimates. I have no word-count tool here.

## 3. Changes

1. **Removed the intro line** ("Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed."). It describes the file to the people who read it and does not change what the model does.
2. **Removed "Ask yourself: 'Would a senior engineer say this is overcomplicated?'"** It restates the "200 lines → 50" rule directly above it.
3. **Merged two "ask" lines in Section 1.** "If uncertain, ask" and "If something is unclear, stop. Name what's confusing. Ask." became one bullet: "If uncertain, stop, name what's unclear, and ask."
4. **Lowercased "YOUR"** in "Remove imports/variables/functions that your changes made unused." Capitals used for emphasis tend to make Haiku over-apply the rule, and the lowercase version says the same thing.

## 4. Kept, and why

- **The "Tradeoff" line and "For trivial tasks, use judgment":** the author's choice about proportion.
- **The "Before implementing" trigger and the ask-when-unclear rule:** a real decision point for the model.
- **The "don't improve adjacent code" and "don't delete dead code" bullets:** specific scope limits the model would not infer on its own.
- **The three examples and the plan block in Section 4:** Haiku's procedure examples carry the task structure. The profile says to keep these.
- **The closing "These guidelines are working if..." line:** this one is unsure. It is written for you, not the model, so it may not change behaviour. Dropping it saves about 27 words. I kept it because you may want it.
- **The section headline sentences:** they restate the bullets below them. Dropping them all would save about 40 words. I kept them as anchors. Say if you want them gone.

## 5. Suggested additions (not in the file)

The Haiku profile suggests these for a coding agent. I did not add them, since you asked for a trim, not new rules:

- "Before reporting a change done, run a real check (a test, build, or run) and report the result." Section 4's "Loop until verified" is close, but it does not say to run a check before reporting done.
- "Keep working until the task is done." This matters if Haiku stops early on long tasks. Your file is short, so this may not be needed.