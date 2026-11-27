I saved the proposed version as `trimmed.md`. It is almost the same as the original: I cut only one sentence. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Words:** about 990 before and 975 after. These are my estimates, because I had no tool to count words.

## What I changed

1. **The tool-call rule (line 11):** I removed the last sentence, "If you respond to the user, you should not make a tool call at the same time." It repeats the clause just before it ("if you make a tool call, you should not respond to the user simultaneously") in reverse, so it adds nothing.

## What I kept and why

Nearly everything else in this file is a policy rule about booking, money or changes that can't be undone. Rules like that stay word for word:

- **Asking the user to say "yes" before any change to a booking.** This is a confirmation step for actions that can't easily be reversed. The Opus 5.5 guidance says to keep these.
- **Payment limits, baggage allowances and fees, insurance price, which cancellations are allowed, refund timing, and the size and conditions of compensation certificates.** These are pricing and policy limits. The model can't know them, and a slightly reworded rule could mean giving out the wrong amount.
- **"The API does not check these… must make sure the rules apply before calling the API!" (both places).** It gives the reason for the rule, and the API won't catch a mistake. The Opus guidance does say strong emphasis can make the model over-apply a rule. Here, though, over-applying means checking more carefully before a call that can't be undone, so I left it.
- **"Do not compensate if the user is regular member…" (line 70).** It mostly restates who qualifies under lines 66 and 68, but it is a limit on payouts, so I kept it.
- **"The rules are strict regardless of the membership status."** It stops the model from making exceptions to the cancellation rules.
- **The current time, flight statuses, the "first obtain…" steps, "deny requests against this policy," the transfer rule, and "not even a human agent can assist."** Each one either gives a fact the model can't know or changes what it does.
- **The role line and the rule against adding outside information or opinions.** These set the scope that the transfer rule depends on.

## Unsure: kept, but you could drop it

- **The descriptions of user profiles and reservations under "Domain Basic" (lines 19 and 21).** They only list fields. If your tools return these same records, the model will see the fields anyway. Dropping both lines would save about 48 more words, bringing the total to around 925. Keep the flight-status lines below them, though, because they decide what can be booked.

## Not added

The Opus 5.5 guidance suggests adding nothing for this kind of assistant. Its one suggestion is for loosely defined work across several apps, which doesn't apply here.

Overall, this file is already lean and is mostly policy that can't be cut, so a much shorter version would mean weakening rules. I wouldn't recommend that.