I saved the proposed version to `/root/trim-sbx/3c5bae7ed9ca/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort.

**2. Length:** about 191 words before and about 171 after, a cut of roughly 10%. These are estimates, since I had no word-count tool. The example output is about 100 words and I kept it whole, so the savings are small.

**3. Changes**
- **Merged the MISSION and INPUT sections.** Both said the input would be a topic or request. Now one sentence covers it: "Given a topic or request, write slide deck text in the format below."
- **Removed emphasis.** "very specific format" and "super consistent" are gone. The consistency requirement stays as plain wording: "Inputs vary, but the output format never does." Haiku follows wording closely, so emphasis tends to over-apply.
- **Removed filler.** "will be expected to," "highly varied," and "usually" were cut.
- **Clarified item 3.** "labeled list bullet point format" is now "a labeled bullet in the form '- Label: description'." This is a wording change, not a content change. I took the pattern from the example, which already uses that form. This is the one place where I added detail, since the profile says Haiku needs more explicit direction than larger models.
- **Shortened item 1.** "Two to Four Words Max" is now "two to four words."

**4. Kept and why**
- **The role line** ("You are a slide deck builder"). It sets the task.
- **The output format, including the 2–3 sentence and exactly-five constraints.** These are the author's choices and the model can't infer them.
- **The full example.** It pins the required format, and the profile says to keep examples that carry a task procedure.
- **"with word economy" (flagged as unsure).** It's a soft style request, and the example already shows brevity. Dropping it saves 3 words. I kept it because it is the author's choice, but you can drop it.

**Suggestions, not applied**
- If this runs inside a chat, add a line saying the format holds even when the user asks for something different. The Haiku profile recommends this for chat assistants.
- "Concept Description of Definition" is an unusual label. I left it alone because it's the author's term, but you may want to reword it.