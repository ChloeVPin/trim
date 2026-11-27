I wrote the shorter version to `/root/trim-sbx/4857a3933884/trimmed.md`. `instructions.md` is unchanged. The original is about 620 words and the new one is about 250. I haven't tested either version against claude-haiku-5-5, so the Haiku fit is a judgment call.

**Audit of instructions.md**

- **Keeps:** the four core rules (think first, simplicity, surgical changes, verify with a check), the concrete test-first examples, and the numbered-plan format. These are actionable and short enough for a smaller model to follow reliably.
- **Conflicts:** Section 1 says "If something is unclear, stop. Ask." That can stall autonomous work on routine ambiguity. Your system guidance says to act on the most likely reading and state it. I reconciled the two.
- **Redundant:** Sections 1 and 4 both push toward asking and checking, and Section 3's orphan-cleanup rule is repeated in different wording. I merged these.
- **Not instructions:** The closing "These guidelines are working if..." line is a note for the author, not for the model. I dropped it.
- **Rationale and phrasing:** The original explains a lot in prose. I cut it to short imperatives with one-line checks, since smaller models tend to follow direct rules better than long justifications.

**Choices you may want to change**

- Ambiguity handling is the main behavior change. The new version picks the most likely reading and asks only when the answer depends on something the user alone can provide.
- The "bias toward caution" line is kept as a one-line tradeoff note, scoped to non-trivial work.
- I kept the examples in Section 4 as sub-bullets, since they're what makes the verify rule concrete.