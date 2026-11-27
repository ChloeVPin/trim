I saved the proposed version to `/root/trim-sbx/89337b9f8da9/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort.

**2. Word count:** about 1,090 before and about 1,065 after. These are my estimates, since I have no word-count tool here. The cut is small because nearly every line is a policy rule, a fact the model can't know, or a guarded action.

**3. Changes**
- **Tool-call rule merged (about 23 words saved).** The two sentences on line 11 said the same thing from both sides: one tool call at a time, and no tool call in the same turn as a reply to the user. They now read: "You should only make one tool call at a time, and never make a tool call and respond to the user at the same time." The meaning is unchanged.

**4. Kept, and why**
- **Confirmation before database updates:** guards irreversible actions, so it stays as written.
- **Payment, baggage, insurance, modify, cancel and refund rules:** policy limits and guarded actions, kept with their conditions and exceptions.
- **The two "API does not check these" warnings (modify, line 44, and cancel, line 58):** they repeat each other. I kept both because they guard a cancellation, which can't be undone.
- **"This is something that even a human agent cannot assist with":** it gives the model the reason for a denial, which helps it generalise.
- **The current-time line and the domain facts:** the model can't know these.
- **The role line ("As an airline agent…"):** unsure. Dropping it saves about 17 words. The sections below already make the scope clear, so it's your call.

**5. Suggested addition (not applied)**
This is a support assistant, and the Haiku profile recommends a line that the rules hold for the whole conversation, including when the user argues or asks for an exception. For example: "These rules hold for the whole conversation, including when the user argues or asks for an exception."

**6. Other issues I noticed but did not change**
- "an reservation id" (Domain Basic) should be "a reservation id".
- "2 free checked bag for each…" (Book flight) should be "bags" in three places.

Both are grammar fixes, so I left them for you to decide.