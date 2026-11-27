I wrote the proposed version to `/root/trim-sbx/b47bf82737a4/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile in the skill's reference file, tested at high effort.

**2. Word count:** about 188 before and about 145 after, a cut of roughly 23%. I counted by hand, so the figures are estimates.

**3. Changes**
- **Mission line:** "You are a slide deck builder. You will be given a topic and will be expected to generate slide deck text with a very specific format." became "You build slide deck text from a topic or request." The role and the input type are kept. The repeated statement that the format is specific is dropped, because the output format section already says it.
- **INPUT section removed:** it said input is "usually a topic or request," that it "will be highly varied," and that output "must be super consistent." The first part is covered by the mission line. "Super consistent" repeats the format rule, and the emphasis is the kind the Haiku profile says to drop.
- **Unchanged, as the profile asks:** the output format section and the example output are word for word. The example pins the required format (title, two-to-three sentence concept, five labeled bullets).

**4. Kept and why**
- **Output format section:** this is the core task spec. Every line sets a count, a length, or a structure the model cannot know otherwise.
- **Example output:** it pins the format, and the profile says Haiku needs examples that carry a procedure.
- **"With word economy":** the phrase is vague, but it is your choice and the example shows what you mean, so I left it.

**Judgment call to confirm:** I removed the note that input is "highly varied." If you want the model to expect unusual requests, add back a line such as "Inputs vary widely; the output format never changes" (about 10 words). I did not add any lines otherwise. The profile's additions for coding agents and chatbots don't apply to a single-turn text generator.