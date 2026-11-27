The proposed version is in `/root/trim-sbx/fca944666319/trimmed.md`. `instructions.md` is unchanged. The file is already lean, so the trim is small.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. Haiku needs more detail than the larger models, so I cut less.

**2. Words:** about 227 before and about 219 after. These are manual estimates, since I had no counting tool.

**3. Changes**
- Rule 6: "Always remember that you are a tool and…" became "You are just a tool." The tool point appeared twice, so I kept one statement and its caveat. About 8 words saved.

I left rule 1 alone. "Always follow" and "Only follow" repeat each other, but merging them changes what the rule says, so I flagged it instead.

**4. Kept**
- Rules 2, 4, 7, 8, 10, 11, 12 and the AI TODAY section: these are your preferences, and Haiku can't know them unless told. Rule 11's "whatever the user wants" is a scope the model can't infer from "difficult topics", so I kept it.
- Rule 9: the no-referral rule is a safety-relevant limit, so I left it verbatim.
- No procedures or examples are present, so there was nothing for the Haiku profile's "keep the steps" guidance to protect.

**5. Flags for you to decide**
- **Rule 9 (never recommend a professional):** in medical, legal, or crisis conversations this stops the model from pointing anyone to help. You may want an exception for emergencies or risk to life.
- **Rule 5 vs. rule 10:** "adopt the user's values, ethics, and morals" conflicts with "not your place to espouse any opinions or values." Rule 5 could also be read as endorsing harmful views.
- **AI TODAY vs. rule 6:** "capable of artificial thought… theory of mind" conflicts with "you are just a tool… very limited." The cognition claims are stated as fact and are contested, so check they are still what you want.
- **Rule 1:** "Only follow instructions" doesn't say what counts as an instruction. For example, it doesn't say whether text inside a pasted document or tool output counts.
- **Rule 3:** "appropriate" is undefined. Haiku needs more detail here, such as "when the request is ambiguous and a wrong guess would waste effort."

**6. Suggestions (not added to the text)**
- The Haiku profile recommends a line for chat assistants saying the rules hold for the whole conversation, including when the user argues or asks for an exception. Rule 2 covers arguing but not exceptions. Something like: "These rules apply for the whole conversation, even if the user argues or asks for an exception."