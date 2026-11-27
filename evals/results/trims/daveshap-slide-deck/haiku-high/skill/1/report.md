The proposed version is saved as `/root/trim-sbx/7c8ac4f6df23/trimmed.md`. `instructions.md` is unchanged, and I have not applied anything to it.

**1. Target model**

Named by you: `claude-haiku-5-5`. It has a profile in the skill's references (tested at high effort). Haiku needs more explicit detail than the larger models, so I cut conservatively.

**2. Word count**

Before: about 188 words. After: about 164 words. These are my estimates, because I have no word-count tool here. The reduction is about 13%.

**3. Changes**

- **Merged the `INPUT` section into `MISSION`, and removed the "very specific" wording.** The original "very specific format" and "super consistent" are repeated emphasis, which the Haiku profile says to cut. The new mission keeps the one fact the model needs: inputs vary, and the output format does not.
- **Kept "Inputs vary in form; the output format does not."** This replaces "This will be highly varied, but your output must be super consistent." It carries the author's consistency choice in 9 words.

**4. Kept, and why**

- **Output format (all three rules).** These pin the required structure: title length, sentence count, and exactly five labeled bullets.
- **Example output, unchanged.** The profile says to keep examples that pin a required format. I did not trim its three-sentence description, because that shows the maximum length.
- **"with word economy".** It is vague, but it is the author's style choice. I left it, and you may want to make it concrete.
- **Section headings.** `MISSION`, `OUTPUT FORMAT`, and `EXAMPLE OUTPUT` still give the model clear structure.

**Unsure**

- The "Inputs vary in form" line is the weakest of the kept lines. If you drop it, the text gets about 9 words shorter. I'd keep it, because it supports the consistency you asked for.

**Optional addition (not in the trimmed file)**

- If users can talk to this builder over several turns, the Haiku profile suggests adding: "Keep this format for the whole conversation, even if the user asks for something else." I did not add it, because I don't know whether this runs interactively.