I saved the proposed version to `/root/trim-sbx/daccd979c036/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. The cuts here are small, and I did not test them at any other effort setting.

**2. Words:** about 1,040 before and about 1,025 after, roughly 1.5% shorter. I have no word-count tool here, so these are estimates. This policy is almost entirely rules that guard booking, cancellation, refund and payment actions, and those stay as written.

**3. Changes**
- **Line 11 (tool calls):** I removed "If you respond to the user, you should not make a tool call at the same time." The sentence before it already says a tool call and a user response must not happen together, so the removed sentence repeats it. This is the only edit.

**4. Kept, and why**
- **Confirmation before database updates (line 7), cancellation and refund rules, payment limits, baggage and insurance prices:** guarded rules, kept word for word.
- **"The API does not check these… before calling the API!" (lines 44 and 58):** the Haiku profile says emphasis can over-apply. These are guarded policy rules, so I left the "!" in place.
- **"Even a human agent cannot assist with" (line 50):** unsure. It may be what stops the model from transferring this request. If you drop it, the text gets about 12 words shorter.
- **Domain facts, status meanings, scope line, and the current time:** facts the model cannot know.
- **Procedures (the order of questions to ask for booking, modifying and cancelling):** kept, since the profile says Haiku needs the steps.

**Suggested addition (not in the file):** the Haiku profile recommends a line for support assistants saying the rules hold for the whole conversation, including when the user argues or asks for an exception. For example: "These rules apply for the whole conversation, including when the user argues or asks for an exception."