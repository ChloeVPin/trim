I saved `trimmed.md` and didn't touch `instructions.md`. **The proposed version is the same as the original.** This file is already lean, so I didn't cut anything just to make it shorter.

**1. Target model:** `claude-opus-5-5`, which you named. There's a profile for it, and it has been through this skill's tests at medium effort.

**2. Word count:** about 1,000 words before and after. I had no counting tool, so that's an estimate. The two versions match word for word.

**3. Changes:** none. The Opus 5.5 profile names three kinds of line to cut: lines telling it to think carefully, lines telling it to check its own work, and vague design direction. This file has none of them.

**4. What I kept and why:** nearly every line contains either a fact the model can't know or a choice you made. Examples are the date, the passenger and payment limits, the bag allowances, the $50, $30, $100 and $50-per-passenger amounts, the refund timing, and the one-tool-call-at-a-time rule. Most of the rest protects work that is hard to undo: booking, payments, cancellations, refunds, compensation, and the confirmation step. Those lines stay exactly as written, including "you must" and the "!" on the two "API does not check these" lines.

**5. Points for you to decide (I didn't change any of these):**
- **Cancellation has no confirmation step.** Line 7 requires a "yes" before booking, changing flights, baggage, cabin or passenger details, but cancelling isn't on that list. Cancelling is the hardest of these to undo. If that wasn't on purpose, add "cancelling" to the list.
- **Unclear "instead" (line 52).** "The agent should ask for the payment or refund method instead": it's not clear what this replaces. My guess is "instead of choosing one for the user." Saying so would remove the doubt.
- **Missing flight statuses (lines 24–26).** "Cancelled" and "landed" aren't defined, but the cancellation and compensation rules depend on knowing whether the airline cancelled a flight.
- **Possible cut: the "Domain Basic" field lists (lines 19 and 21).** These list what a user profile and a reservation contain. If your tools already return those fields, the model probably acts the same without these lines. Dropping them would save about 45 words, roughly 4%. Keep the flight status lines either way.
- **Repeated rule (line 70).** "Do not compensate if the user is regular member…" is the reverse of the conditions on lines 66 and 68. I kept it because it limits payments, but you could drop it.
- **Possible table (line 36).** The bag allowance would read more easily as a 3×3 table with the same numbers. I didn't make this change because the allowance decides what users are charged.
- **Fixed date (line 3).** The current time is hard-coded as 2024-05-15. That's fine if it's a test setup. If it's used in production, it's out of date.
- **Typos:** "an reservation id", "baggages", and "0 free checked bag" / "2 free checked bag" (should be plural). These don't change behaviour.

**Suggested additions:** none. The Opus 5.5 profile's only recommended addition is for loosely defined work across several apps, which doesn't apply here.

**6. Proposed text:** it's in `/root/trim-sbx/1e0654b2f422/trimmed.md` and matches `instructions.md`.