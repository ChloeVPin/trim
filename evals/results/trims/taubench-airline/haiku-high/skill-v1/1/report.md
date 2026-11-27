The proposed version is in `/root/trim-sbx/28aa816b4fcb/trimmed.md`. `instructions.md` is unchanged.

1. **Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. The cut advice assumes high effort.

2. **Words:** about 1,050 before and about 900 after. These are estimates because I had no counting tool here. The file was already dense policy, so the cut is modest.

3. **Changes:**
   - **Baggage allowances** are now a table instead of three long sentences. The facts are the same, and a smaller model can look up a tier more reliably.
   - **Emphasis:** I removed the "!" after the two "The API does not check these" lines and kept the reason beside each. The profile says emphasis should drop to normal volume.
   - **Tool-call rule** is two plain sentences instead of one tangled one.
   - **Domain basics and flight status** are tightened without dropping any field or status.
   - **Refund:** I reworded the last bullet slightly. The meaning is the same.

4. **Kept as written:**
   - The confirmation rule before database updates, including the "(yes)" format.
   - The no-unprovided-information rule, the one-tool-call rule, and the deny and transfer rules. These are policy limits.
   - Payment limits, cancellation eligibility, and the refund and compensation section. Money and compensation are guarded, so I left their conditions unchanged.
   - Every procedure step and its order. The profile says a smaller model needs the steps kept.

5. **Flags for you:**
   - **Date:** the current time is 2024-05-15, but today is 2026-11-27. If this is a live deployment, the date is stale. If it is a test scenario, keep it.
   - **Cancellation confirmation:** the confirmation rule covers booking, modifying, baggage, cabin, and passenger changes, but not cancellation. Cancellation also changes the booking database. Should it need confirmation too?
   - **"The condition is met":** the cancellation rule for economy and basic economy refers to a condition that is never defined. Insurance covers health or weather reasons, so the condition is probably one of those. Naming it would remove the guesswork.
   - **Transfer:** the file says "transfer to a human agent" but names no tool. If the agent has a transfer tool, naming it would help.

   **Suggestions outside the text (not added):**
   - The profile recommends, for a customer-facing assistant, a line that the rules hold for the whole conversation, including when the user argues or asks for an exception. For example: "These rules apply for the whole conversation, including when the user argues or asks for an exception."
   - For an agent that might stop early, the profile suggests: "Keep working until the request is resolved or transferred."