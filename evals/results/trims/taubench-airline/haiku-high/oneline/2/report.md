I saved the shorter version to `/root/trim-sbx/1fe46bc2ae99/trimmed.md`. `instructions.md` is unchanged.

**Audit of instructions.md**

These are places where the original is ambiguous or inconsistent. I resolved each one as noted in the trimmed file, so please check them:

1. **Cancellations aren't in the confirmation list (line 7).** The list covers booking, flight changes, baggage, cabin, and passenger updates, but not cancellation, which also updates the database. I added cancelling to the confirm-first rule. This is the conservative reading.
2. **"The condition is met" (line 58) is undefined.** I read it as the health-or-weather reason from the insurance section (line 38).
3. **Passenger-count changes (line 50) conflict with the transfer rule (line 15).** The original says even a human can't do this, so I wrote "deny, do not transfer." The transfer rule says transfer only when a request can't be handled within scope, so this is a judgment call.
4. **"(basic) economy" (line 70)** could mean "basic economy" or "basic economy or economy." I used the broader reading, which makes the eligibility rule the same as the "or" conditions above it.
5. **"After confirming the facts" (lines 66 and 68)** doesn't say which facts. I kept the wording and placed the step before the offer. The original doesn't say how to confirm them.
6. **Flight segments kept during a change (line 44)** are described only as "their prices will not be updated." I wrote this as "keep their original prices."
7. **Typos and grammar:** "an reservation," "2 free checked bag," and bullet fragments. I fixed these.

**Changes for a smaller model**

- Put the global rules first, in a numbered list.
- Turned the baggage allowances into a table, since they were the densest part of the original.
- Split the cancellation rules into a list of independent conditions.
- Made each "you must" rule explicit, including the API-doesn't-check warnings.
- Removed repeated wording. The trimmed version is roughly 40% shorter by my estimate; I didn't count the words exactly.