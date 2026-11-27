I saved the shorter version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile was tested at medium effort.

**Word count:** about 200 before and 170 after. I counted by hand because I had no shell tool, so treat these as close estimates. Leaving out the example, the instructions go from about 96 words to 66, roughly a third shorter. The example is left as it was.

## Changes
1. **Merged MISSION and INPUT into three sentences.** Both sections said the same things twice: you get a topic, and you must use a specific format. I kept the one point that matters, which is that the format stays the same however much the input varies.
2. **Removed "very specific" and "super consistent."** Opus 5.5 follows wording closely, and this kind of emphasis can make it over-apply a rule. The plain statement "the format stays the same every time" does the same job.
3. **Removed "Max" from the title rule.** "Two to Four Words" already sets the upper limit.
4. **Changed "Description of Definition" to "Description or Definition."** This looks like a typo. Please check it, because if you meant something else, the fix changes what the line asks for.
5. **Rewrote "in 'labeled list' bullet point format" as "as a labeled bullet list."** The meaning is the same and the example shows the exact form.

## What I kept and why
- **The full example.** It is the strongest signal of the format: a plain-text title, a paragraph, and "Label: text" bullets with no markdown headings. On Claude models, an example that pins a required format is worth keeping.
- **"Exactly five," "2 or 3 complete sentences," and "with word economy."** These are your own format choices, and the model wouldn't follow them without being told.
- **The section headings.** They cost very little and make the prompt easy to scan.

## Possible additions (not in trimmed.md)
- **Output scope:** The instructions don't say whether to produce one slide per request or a whole deck. The word "deck" suggests several slides, but the format and example show only one. A line such as "Produce one slide per request" or "Produce N slides, each in this format" would settle it.
- **Markdown:** If the output goes into a tool that renders markdown, add "plain text, no markdown headings or bold." Otherwise the model may add `#` or `**` to the title.