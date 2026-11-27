I saved the proposal as `trimmed.md`. It's the same as `instructions.md`, word for word, because the file was already lean and I didn't cut anything for the sake of it. `instructions.md` is unchanged.

**1. Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**2. Words:** about 1,100 before and after. That's an estimate, since I had no counting tool here.

**3. Changes:** none. The things the profile says to cut for this model aren't in the file: there are no "think carefully" lines, no "double-check your answer" lines and no vague style direction. There are also no duplicate rules or general advice like "be helpful".

**4. What I kept, and why**
- **Almost every line is a fact or a rule the model can't know on its own.** That includes limits (5 passengers, 1 certificate, 1 credit card, 3 gift cards), the free-bag table by membership tier, prices ($50 per extra bag, $30 insurance, $100 or $50 certificates) and the 5–7 business day refund window.
- **Rules about payments, refunds, cancellations and database changes stay exactly as written**, with their conditions and exceptions. The "yes" confirmation before any change and the "the API does not check these" warnings are in this group. A wrong cut here would cost far more than the words saved.
- **Your choices stay at full strength**, even where they're strict: one tool call at a time, never reply and call a tool in the same turn, no subjective recommendations, no offering compensation unless the user asks, and transfer to a human "if and only if".
- **The two "!" warnings stay.** I'd normally tone emphasis down, but these protect calls that can't be undone.

**5. Flags for you (your call; I left the text alone)**
- **The date is 2024-05-15.** If this is a fixed simulation date, it's fine. If not, it's out of date.
- **The flight statuses don't cover every case.** Only "available", "delayed", "on time" and "flying" are defined. If the tools can return "landed" or "cancelled", the model has to guess what they mean. You may want to add a line for each.
- **Line 52 is unclear.** "The agent should ask for the payment or refund method instead": instead of what? Probably instead of picking a method itself. Spelling that out would stop it being misread.
- **The user and reservation field lists (lines 19 and 21) might be cuttable** if the tools already return those fields, which would save about 55 words. I kept them because I can't see your tool definitions.
- **"You should deny user requests that are against this policy" might be implied by the rest of the file.** Cutting it saves about 9 words. I kept it because this rule set stops the model from doing things.
- **There are small typos:** "an reservation id" and "0 free checked bag". Fixing them won't change behaviour.

**Suggestion (not added to the text):** this is a support assistant, so you could add a line saying these rules apply for the whole conversation, even when the user argues or asks for an exception. The profile recommends that for smaller models. Opus 5.5 probably doesn't need it, but it's cheap if users push back a lot.