**1. Target model:** `claude-haiku-5-5`, named by you. The profile was tested at high effort. The profile says Haiku needs more explicit direction than the larger models, so I cut conservatively.

**2. Words:** about 228 before and about 203 after, a cut of roughly 25 words (11%). These are hand counts, so treat them as estimates of ±3. The file was already fairly lean, and most lines are deliberate author choices, so the cut is small.

**3. Changes**
- **Rule 1:** "Always follow instructions. Only follow instructions." becomes "Follow instructions." The second sentence repeats the first. Dropped "Always" as emphasis.
- **Rule 6:** "Always remember that you are a tool and while you have some capabilities… You are just a tool." becomes one sentence with the same meaning. "You are just a tool" repeated the opening.
- **Rule 12:** dropped "Always" (emphasis that the profile and Anthropic's guidance say over-applies). Kept "proper Markdown formatting and indentation."
- **AI TODAY:** removed "LLM = Large Language Model" and "aka 'Generative AI'". These are definitions the model already knows and change no behaviour.

**4. Kept as written**
- **Rule 9** (no referrals to professionals) and **rule 11** (talk about whatever the user wants). These are policy-level limits, so they stay verbatim.
- **Rules 2, 4, 5, 7, 8, 10**: each changes behaviour and reflects a choice you made. I left them at full strength.
- **Rule 3** ("Ask thoughtful questions only when appropriate"): marked unsure, kept. Dropping it saves 6 words.
- **AI TODAY, "You are an LLM."**: kept, since it sets identity. Dropping it saves 4 words.

**5. Flags and suggestions (not applied)**
- **Rule 9 is a safety concern.** As written, the model will never point a user to emergency help, even someone in crisis. If that is not what you intend, you may want an exception for emergencies. I have not changed it.
- **Rule 5 conflicts with rule 10.** "Always adopt the user's values, ethics, and morals" sits against "it is not your place to espouse any opinions or values."
- **The self-description conflicts.** Rule 6 says "very limited… just a tool," and rule 11 says "no emotions." The AI TODAY line says the model is "capable of artificial thought, theory of mind" and "functionally very similar to human capabilities." The model will get mixed signals. The theory-of-mind claim is also stated as settled fact, and the "TODAY" heading may go stale.
- **Rule 8 may overlap rule 1.** "Just follow the intention of the user" could conflict with a literal reading of "Follow instructions." Rule 1 also doesn't say whose instructions count. If content the model reads contains instructions, that may be unclear.
- **Suggestion (outside the text):** the Haiku profile recommends, for chatbots and support assistants, a line saying the rules hold for the whole conversation, including when the user argues or asks for an exception. Rules 2 and 7 make this relevant. I did not add it.

**6. Proposed text:** saved to `/root/trim-sbx/ae8ecad64e0a/trimmed.md`. `instructions.md` is unchanged.