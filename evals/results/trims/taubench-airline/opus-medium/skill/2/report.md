I saved `trimmed.md`, but **it is identical to `instructions.md`**. I didn't find a cut that was clearly safe, and `instructions.md` is unchanged.

**1. Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**2. Word count:** about 1,000 before and after. That figure is an estimate because I had no word-counting tool in this session.

**3. Changes:** none. Opus 5.5 can safely drop lines that tell it to think carefully, double-check its work, or push for extra tool use, and lines repeated elsewhere in the file. This file has none of those. Almost every line is a fact the model can't know (dates, limits, fees, allowances, status meanings) or a rule about bookings, payments, cancellations, refunds or compensation. Those can't be undone, so I left them exactly as written:
- the "list the details and get a yes" confirmation step
- both "The API does not check these… the agent must make sure the rules apply" lines
- "strict regardless of the membership status"
- the full cancellation and compensation conditions, including the "Do not compensate if…" line, even though it partly repeats the eligibility conditions above it

**4. Optional cuts for you to decide:**
- **Domain Basic, user profile and reservation fields (lines 19 and 21, about 50 words):** the tools probably return these fields anyway. Line 21 is the only place that mentions "created time", which the 24-hour cancellation rule depends on, so if you drop line 19, keep line 21.
- **"You should deny user requests that are against this policy" (line 13, about 10 words):** Opus probably does this without being told. But it's a short policy line that supports holding the rules when a user pushes for an exception, so I'd keep it.
- **Checked bag allowance (line 36):** rewriting it as a three-by-three table (membership tier by cabin) would make it about 50 words shorter with every number intact. I didn't do it because it's a fee rule. If you want it, check the table against the original.

Even with all three, the file would shrink by only about 10%. It's already short and mostly fact-based, so there isn't much to remove for Opus 5.5.