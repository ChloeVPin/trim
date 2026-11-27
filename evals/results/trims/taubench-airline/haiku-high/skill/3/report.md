I saved the proposed version to `/root/trim-sbx/74b69f10be1d/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort.

**2. Length:** I have no word-count tool here, so these are estimates: about 990 words before and about 970 after. The cut is small because nearly every line is either a policy rule, which must stay as written, or a fact the model can't know, such as a fee, a limit, or a date.

**3. Changes**
- **Removed** "As an airline agent, you can help users book, modify, or cancel flight reservations." It repeats the Book, Modify and Cancel sections below it, and the title already names the role.
- **Grammar fixes, not cuts:** "an reservation id" became "a reservation id", and "2 free checked bag" and similar became "bags" where the number isn't 1. The meaning is the same.

**4. Kept, and why**
- All policy rules, including the confirmation step, the one-tool-call rule, the deny and transfer rules, the bag and insurance fees, the cancellation and refund conditions, and the "do not proactively offer" rule. These guard fragile actions, so they stay word for word.
- Flight status rules, the current time, and the passenger, payment and booking procedures. The model can't know these without the text.
- The API-check lines in Modify and Cancel. The model can't know the API doesn't check these.

**5. Suggestions, not applied**
- **Unsure, about 50 words:** the two "Each user has a profile…" and "Each reservation has…" lines list fields that the tools return anyway. Dropping them would save about 50 words. Say if you want that.
- **Emphasis:** the "!" and "must make sure" in the Modify and Cancel API lines are the kind of emphasis the Haiku profile says to drop. I left them because they guard a policy rule. Rewording would be something like "verify the rule before calling the API." Your call.
- **Add for a support assistant:** the profile recommends a line saying the rules hold for the whole conversation, including when the user argues or asks for an exception. That fits this agent, given the refund and deny rules. I didn't add it because the skill treats additions as suggestions. Suggested text: "These rules apply for the whole conversation, including when the user argues or asks for an exception."
- **Only if it stops early in testing:** add "Keep working until the request is fully handled or must be transferred."