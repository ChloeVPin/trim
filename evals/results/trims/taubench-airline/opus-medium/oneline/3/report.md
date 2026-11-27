I saved the shorter version as `trimmed.md`. `instructions.md` is unchanged. Every rule from the original is still in it, so the agent's behavior shouldn't change. It's about 30% shorter, but the bigger gain is that it's easier to scan.

**What I changed:**
- **Removed the list of fields in a user profile and a reservation.** These only describe what the tools return, and the model sees that data anyway. The part of the "Domain Basic" section that carries rules, what each flight status means, is now a short list.
- **Replaced the checked-bag paragraph with a table.** The original was nine numbers spelled out in prose, which is the easiest place to misread a rule.
- **Stated "the API does not check these rules" once,** at the top, instead of repeating it with exclamation marks under Modify and Cancel. Opus 5.5 doesn't need emphasis to follow a rule.
- **Split the cancellation rule into a short list** (within 24 hours or airline-cancelled → business → economy with insurance). In the original it was one long sentence.
- **Restructured the Refund section, now called Compensation.** It had two bullets with the same eligibility condition and a third that limited both. The eligibility rule and the "only if the user explicitly asks" rule now come first, followed by the two amounts.
- **Rewrote the tool-call rule in one line:** "Each turn is either one tool call or a message to the user, never both."

**Three places where I resolved unclear wording; please check they match what you intended:**
1. **"Insurance condition is met"** for cancellations: I spelled this out as "the reason is covered (health or weather)", using the insurance description in the Booking section.
2. **Passenger count:** the original says "even a human agent cannot assist". I took that to mean "don't transfer for this" and wrote it that way.
3. **Payment when flights change:** I dropped the stray word "instead" at the end of that bullet and kept the instruction to ask for one gift card or credit card.