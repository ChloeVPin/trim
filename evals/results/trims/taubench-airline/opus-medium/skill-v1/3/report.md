I saved the proposal to `trimmed.md` and didn't touch `instructions.md`. This file is already lean, so the proposal is almost the same as the original. Nearly every line is a booking, payment, cancellation or compensation rule, or a fact the model can't know unless told. Cutting more would mean changing your policy, not tightening the wording.

**1. Target model:** `claude-opus-5-5`, which you named. It has a profile, tested at medium effort.

**2. Word count:** about 1,010 before and about 993 after. I had no tool to count words here, so both figures are estimates. The cut removed exactly 17 words.

**3. Changes**
- **`instructions.md:11`:** I removed "If you respond to the user, you should not make a tool call at the same time." The sentence before it already says this in reverse. This model follows wording closely, so the repeat adds nothing.
- **`instructions.md:44` and `:58`:** I changed "before calling the API!" to end with a full stop. The profile says emphasis written for older models now causes over-application. The rule and its reason ("The API does not check these for the agent") are unchanged.

**4. What I kept and why**
- **Left exactly as written:** the confirmation-before-update rule, all payment limits, cancellation and refund conditions, the compensation amounts and who qualifies, the transfer rules, and the passenger-count limit. These control money and changes to the booking database. Cutting one by mistake would cost far more than the words saved.
- **Kept:** all the facts: tier-by-cabin bag allowances, the $50 and $30 prices, the five-passenger limit, flight statuses, and what data each record holds. The model can't infer any of these.
- **Not cut:** there were no lines asking it to "think carefully" or "double-check", which are the main things the profile says to remove for this model.

**5. Things to check (I left all of these as they are)**
- **`:3` fixed time (2024-05-15):** this is deliberate if it's a test setup. If it's a live deployment, the date is stale.
- **`:52` "instead":** it's unclear what this replaces. Perhaps it means "ask which on-file method to use, rather than assuming one"?
- **`:58` "the condition is met":** this seems to mean the health or weather reasons in `:38`, but it doesn't say so. Naming the condition here would make it clear.
- **`:70`:** this restates `:66`/`:68` in reverse. I kept it because it's a compensation rule, but you could drop it if you're sure the two lines above are enough.
- **Typos (not fixed):** "an reservation" and "baggages" (`:21`), and "2 free checked bag" / "3 free checked bag" (`:36`).
- **No additions suggested.** The only extra line the profile offers for this model is about loosely specified work across several apps, which doesn't apply to this policy.

**6. Proposed text:** the full version is in `trimmed.md`.