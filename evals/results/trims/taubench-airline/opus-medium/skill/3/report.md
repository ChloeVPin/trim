I saved the proposed version as `trimmed.md`, and `instructions.md` is unchanged. I only cut one clause, because almost every line in this policy carries a fact or a rule the model can't know otherwise.

**Target model:** `claude-opus-5-5`, as you named. Its profile has been tested at medium effort.

**Word count:** about 970 before and about 955 after. I had no counting tool here, so these are estimates from a line-by-line count.

## Change

- **Line 11:** I removed "If you respond to the user, you should not make a tool call at the same time." It says the same thing as the clause before it ("if you make a tool call, you should not respond to the user simultaneously"). It saves about 16 words.

## Kept, and why

- **Rules that protect bookings, payments and refunds stay word for word.** These are:
  - the confirmation step before any database update
  - the payment limits
  - the modify and cancel rules, including the two "The API does not check these… make sure the rules apply before calling the API!" lines
  - the 24-hour and insurance conditions
  - the whole Refund section

  This includes the last line of the Refund section ("Do not compensate if…"). Logically it's just the opposite of the eligibility test in the two lines above it, but a wrong cut there means paying out compensation by mistake, so it stays.
- **Policy limits:** the rules against outside information or subjective comments, refusing requests that break the policy, and transferring "if and only if" a request is out of scope.
- **Lines that look extra but change behaviour:**
  - "even a human agent cannot assist with" stops a pointless transfer.
  - "strict regardless of the membership status" helps the model hold firm when a user pushes for an exception.
  - "for safety reasons" gives the reason behind a rule, which helps the model apply it to new cases.
- **Facts:** the current time, the flight statuses, the passenger limit of five, the $30 insurance, the $50 per extra bag, the 5 to 7 business days for refunds, and the $100 and $50 certificate amounts.

## Possible further cuts (need your call)

1. **Domain Basic: the profile and reservation field lists** (about 48 words). If your tools already return these fields, the lists probably don't change what the model does. Dropping them would bring the total to about 905 words. I kept the flight-status list, because it decides what can be booked.
2. **Checked bag allowance as a table** (about 103 words down to about 45). Every number stays the same: regular members get 0/1/2 free bags, silver 1/2/3 and gold 2/3/3, for basic economy/economy/business, and each extra bag is $50. I didn't make this change because the paragraph sets what customers are charged. Together with option 1, the total would be about 850 words.
3. **The "!" on the two API-check lines.** The profile says strong emphasis can make these models apply a rule too broadly. These lines guard actions that can't be undone, though, so I left them alone.

One thing you might add, not a cut: the flight statuses don't mention "cancelled", but the cancel and refund rules rely on it. That gap was already in the original, and I didn't change it.