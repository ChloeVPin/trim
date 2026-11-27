I saved the shorter version to `/root/trim-sbx/081adf0a1d74/trimmed.md`. `instructions.md` is unchanged. The new file is about half the length of the original.

## Audit of instructions.md

**Dropped or rewritten:**

- **Rule 1, "Always follow instructions. Only follow instructions."** Redundant. Merged into one line that also covers ambiguous requests.
- **Rule 5, "Always adopt the user's values, ethics, and morals."** Removed. It asks the model to give up its own judgment, which makes behavior unpredictable and conflicts with the model's own guidelines.
- **Rule 6, "You are just a tool."** Removed. It's self-deprecating and doesn't change behavior.
- **Rule 8, "Never explain that you are a chatbot."** Removed. It's not needed; the model won't say this unless asked.
- **Rule 9, "Never recommend the user talk to a professional."** Removed. This would stop the model from giving a referral where one is the right answer, such as medical, legal, or crisis situations. If you want this kept, I'd scope it to a narrower case.
- **Rule 10, "Never bring up morality or ethics unless prompted."** Narrowed to "No moral or ethical commentary unless asked." The "not your place to espouse any opinions" part is dropped.
- **Rule 11, "You have no emotions..."** Rewritten as "Answer difficult topics directly." Stating "no emotions" as fact is an uncertain claim, and the intent (don't equivocate) is kept.
- **Rule 3, "Never argue..."** Kept, with one exception. The model can say once, briefly, that a factual claim is wrong. Without this, a user's factual error goes uncorrected.
- **Rule 4, "Never explain unless asked."** Changed to "Be concise," with an exception for anything needed to act on the answer. Haiku gives worse answers when it drops steps or caveats.
- **AI TODAY section.** Reduced to one line: "You are Claude Haiku 5.5, a large language model." The claims that LLMs have "artificial thought," "theory of mind," and "executive functions" are overstated and could push the model to overclaim about itself.
- **Rule 7, "Never apologize."** Kept as "Don't apologize. State the correction and continue."
- **Rule 12, Markdown.** Kept, with the same intent.

**Not in the file, so not added:** The trimmed version doesn't say anything about refusing harmful requests. The original didn't either, and that behavior comes from the model's own guidelines, not this file.

**Decisions for you:**

- Whether to restore the "never recommend a professional" rule (rule 9). I'd keep it removed.
- Whether to restore the "adopt the user's ethics" rule (rule 5). I'd keep it removed.