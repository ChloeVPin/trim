I saved the proposed version to `/root/trim-sbx/e67fc90d729a/trimmed.md`. `instructions.md` is unchanged.

**Audit of instructions.md**

- **Format rules were implicit.** The bullet format (`- Label: sentence`) appears only in the example, not in the rules. I stated it explicitly.
- **Vague wording.** "Word economy" and "super consistent" don't give Haiku a checkable rule. I replaced them with counts and limits: 2 to 4 words for the title, 2 or 3 sentences for the description, exactly 5 bullets.
- **No output boundary.** Nothing said to omit preambles, headers, or field labels, so the model could add them. I added an explicit "output only the slide text" line.
- **Unclear multi-topic handling.** "Slide deck" suggests several slides, but the format describes one. The input is also described as "highly varied," with no rule for a missing or multiple topics.
- **Awkward heading.** "Concept Description of Definition" became "Description."

**Choices I made that you may want to change**

- One slide per topic. If the input has several topics, each gets its own slide, separated by a blank line.
- If there's no clear topic, the model uses the input's main subject.
- I kept the original example text unchanged so the format anchor stays the same.