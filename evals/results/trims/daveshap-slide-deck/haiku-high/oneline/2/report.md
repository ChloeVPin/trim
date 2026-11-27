I saved the proposed version to `/root/trim-sbx/32e46e37b5fe/trimmed.md`. `instructions.md` is unchanged.

**Audit of instructions.md**

- **Ambiguous wording.** "Concept Description of Definition" doesn't say what to write. "Word economy" is vague. I replaced them with "Description" and "concise."
- **Bullet format is under-specified.** The spec says "labeled list" but doesn't give the pattern. The example shows `- Label: detail`, so I stated that pattern explicitly.
- **Input handling is missing.** The spec says input is "highly varied" but doesn't say what to do with non-topic input. I added a rule to use the subject as the topic. This is my choice, so change it if you want different behavior.
- **No output-only rule.** Nothing stops a preamble or closing remark, which would break the "super consistent" goal. I added "Output only these three parts."
- **Redundancy.** The mission and output sections overlap. I merged them into a short role line.
- **Length.** The example makes up most of the file, and I kept it because a concrete example matters more for a smaller model than prose rules. The savings are modest, roughly 20%, rather than a large cut.

**Choices to confirm**

- I kept the original example unchanged.
- "2–4 words" replaces "Two to Four Words Max."
- The description is "2–3 complete, concise sentences" instead of "with word economy."