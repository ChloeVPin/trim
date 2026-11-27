I saved the trimmed version to `/root/trim-sbx/efcf628599f9/trimmed.md`. `instructions.md` is unchanged.

## Audit of instructions.md

**Problems**
1. **"Concept Description of Definition" is garbled.** I read it as "a definition of the concept," so the trimmed version says that.
2. **"Word economy" is vague.** A smaller model can't act on it. The trimmed version replaces it with "keep sentences short."
3. **"Labeled list" is undefined.** The example shows the pattern (`- Label: detail`), but the rule never states it. The trimmed version states it.
4. **No output boundaries.** Nothing says to skip preambles, headings, or closing remarks. Smaller models often add them, which breaks the "super consistent" goal.
5. **No fallback for odd input.** The Input section says requests vary widely but gives no guidance for non-topic requests. The trimmed version adds one line: use the most relevant concept as the topic.
6. **Filler.** "Input" and "Mission" restate each other, and "super consistent" adds nothing.

**Kept as-is**
- The example. For a smaller model it is the strongest format anchor, so I kept it.
- The counts: 2–3 sentences, five points, two-to-four-word title.

## Choices you may want to change
- The title is plain text on its own line, not a markdown heading. This matches the example, but the original didn't specify it.
- The output has no bold labels or numbers. I left those out on purpose, since a smaller model might copy "1." or "**Title:**" into the slide text.
- The fallback rule for non-topic input is new. Remove it if you want the model to refuse or ask instead.