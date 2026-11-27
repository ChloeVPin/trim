I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile was tested at medium effort.

**Word count:** about 200 before and 180 after, roughly 10% shorter. I had no counting tool, so I counted by hand and these figures are estimates.

The original was already short and its core is the format plus the example. So the trim only touches the opening paragraphs.

### Changes
1. **Combined # MISSION and # INPUT into one paragraph.** Both said the same thing: you'll get a topic, and you must produce a fixed format. Saying it once in the new paragraph does the same job.
2. **Reworded "your output must be super consistent" to "keep the output format the same every time."** This is a choice you made, so I kept it. The profile says Opus 5.5 follows wording closely and responds best to plain wording. "Super consistent" also leaves open whether the content should be consistent too, and the new wording ties it to the format.
3. **Changed "Concept Description of Definition" to "Concept Description or Definition."** This looks like a typo. Please confirm that "or" is what you meant.

### What I kept and why
- **The three-part format spec:** kept word for word, apart from the typo fix. It has the limits the model can't guess: a 2–4 word title, 2–3 sentences, exactly five labelled bullets.
- **The Speed Chess example:** kept in full. Per the profile, examples strongly steer format, and you should keep one that pins down a required format. This one shows the "Label: explanation" bullet style better than any description would.
- **"With word economy":** kept. It's your choice of style, and nothing for Opus 5.5 suggests dropping it.

Nothing here is unclear enough to flag as a possible cut, and the prompt has no rules about risky or irreversible actions.