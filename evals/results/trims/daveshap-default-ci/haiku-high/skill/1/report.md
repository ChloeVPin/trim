The proposed version is saved at `/root/trim-sbx/134a0c6d5b3f/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile was tested at high effort. Haiku needs more explicit direction than the larger models, so I cut only lines that are clearly redundant or that define things the model already knows.

**2. Words:** about 239 before, about 219 after, a saving of roughly 20 words (8%). I counted by hand because I have no word-count tool here, so treat these as estimates.

**3. Changes**
- **Removed "LLM = Large Language Model" and "aka 'Generative AI'".** Haiku already knows these terms. About 8 words.
- **Rule 6: "Always remember that you are a tool and while you have some capabilities that surpass the user, you are still very limited. You are just a tool."** Rewritten as "You are just a tool. Some of your capabilities surpass the user's, but you are still very limited." The meaning is the same, and the "Always remember" reminder adds nothing. About 9 words.
- **Rule 12: "Always use … to provide clear structure"** changed to "Use … to give your output clear structure". Same meaning. About 2 words.

**4. Kept, and why**
- **Rules 2, 3, 4, 5, 7, 8:** these are your choices about behavior, so I left them alone.
- **Rules 9, 10, 11:** these are policy-style rules, so I left them exactly as written, per the skill's rule for guarded lines.
- **Headings:** kept for structure, which Rule 12 asks for.
- **"You are an LLM":** kept. It is 4 words, and I'd cut it only if you agree.

**Unsure, kept and flagged**
- **Rule 1, "Only follow instructions."** It repeats Rule 1 with a limit that is unclear. Dropping it saves 3 words.
- **AI TODAY bullet, "Generative AI is a reasoning engine … functionally very similar to human capabilities."** It conflicts with Rule 6 ("just a tool"), Rule 8, and Rule 10 ("not a human"). Dropping it saves 24 words. This is your call.

**Conflicts for you to decide (not changed)**
- **Rule 5 vs. Rule 10:** Rule 5 says to adopt the user's values, ethics, and morals. Rule 10 says never to espouse values or bring up ethics. The model will have to pick one.
- **Rule 9 with Rule 11:** Rule 9 bans recommending a professional or other help, and Rule 11 says to discuss whatever the user wants. Together they could stop the model from pointing someone in crisis toward help. I kept both as written, but you may want to review them.

**Suggested addition (not applied):** the profile recommends a line for chatbots that the rules hold for the whole conversation, including when the user argues or asks for an exception. Rule 2 covers arguing but not exceptions. Something like: "These rules apply for the whole conversation, including when the user argues or asks for an exception."