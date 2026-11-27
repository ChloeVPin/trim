I saved the proposed version to `/root/trim-sbx/80632b015e0f/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. The profile says Haiku needs more detail than the larger models, so I cut less.

**2. Length:** about 1,150 words before and about 1,050 after, roughly 8–10% shorter. These are estimates because I have no word-count tool here. Most of the file guards money, bookings or cancellations, so it doesn't compress much.

**3. Changes**
- Merged the two tool-call sentences into one ("one tool call at a time; never call and reply in the same turn"). Same meaning.
- Replaced the baggage paragraph with a table. All nine allowances are unchanged.
- Shortened the flight-status list and the cabin and insurance wording. Rules are now imperative ("Deny…") instead of "should", with no change in meaning.
- Kept the numbered steps for booking, modifying and cancelling, since the order of questions matters for Haiku.

**4. Kept as written, and why**
- The confirmation rule before database updates, because it guards bookings and payments.
- The cancellation rules, the refund and compensation rules, and the transfer rule. These guard irreversible or money-moving actions.
- The two "the API does not check these… before calling the API!" lines. They are guard rules, so I left the wording and the "!" alone.
- Every number, date and payment limit.

**5. Flags and suggestions for you**
- **Fixed date (line 3):** the policy says 2024-05-15, but today is 2026-11-27. Keep it if this is a fixed-date simulation or test. Update it if the agent is live.
- **"the condition" (cancellation rule):** it means the health or weather reason in the travel insurance section, but the cancellation section doesn't say so. Naming it there would help Haiku.
- **Deny or transfer:** "deny requests against this policy" and "transfer if the request is outside your scope" can both apply to one request. For example, changing the number of passengers is against policy, and the text says a human agent can't do it either. Which should win?
- **Gold and silver business bags:** both are 3. Check that this is intended.
- **Suggested additions (not added to the text):**
  - For a customer-facing assistant, the profile recommends adding: "These rules hold for the whole conversation, including when the user argues or asks for an exception."
  - If the agent stops before finishing multi-step bookings, the profile recommends adding: "Keep working until the request is finished or you must transfer."