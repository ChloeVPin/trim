I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged. This file was already lean, so the proposal is nearly identical to the original.

**1. Target model:** `claude-opus-5-5`, as you named it. Its profile was tested at medium effort.

**2. Word count:** about 1,010 before and about 990 after. These are estimates because I had no counting tool here.

**3. Changes**
- **Tool-call rule (line 11):** I merged it into one sentence: "Make only one tool call at a time, and never respond to the user in the same turn as a tool call." The original said the same constraint twice, once from each direction. The rule itself is the same.
- **"…before calling the API!"** (Modify flight and Cancel flight): I changed `!` to `.` in both places. The profile says emphasis written for older models now causes this model to over-apply a rule. The instruction and its reason ("The API does not check these") both stay. The sentence appears twice on purpose because each copy covers a different set of rules, so I kept both.

**4. What I kept, and why**
Almost everything here is policy that controls booking changes, payments, refunds, cancellations and compensation. Those actions are hard to undo or cost money, so I left them word for word with all their conditions and exceptions. That covers:
- the confirmation step before any database update
- the payment limits
- the cancellation rules
- the certificate amounts
- the transfer rule

The rest is facts the model can't know on its own: data fields, flight statuses, passenger limits, bag allowances and prices. None of the profile's Opus cuts apply, because the file has no "think carefully" or self-check lines and no vague style direction.

**5. Flags and suggestions** (left for you to decide; none of them are in the text)
- **Fixed date:** "The current time is 2024-05-15 15:00:00 EST" is hardcoded. If this is a test setup, that's fine. If the file is used live, the date will make the 24-hour cancellation checks wrong.
- **Unclear sentence:** In Modify flight → Payment, "The agent should ask for the payment or refund method instead" doesn't say what "instead" replaces. Consider spelling it out.
- **Missing flight status:** The status list doesn't include "cancelled", but the Cancel and Refund sections rely on airline-cancelled flights. If there's a cancelled status, adding it would help the model recognise it.
- **Bag allowance:** The paragraph is long. A small table (tier × cabin) would be shorter and easier to scan. I didn't make this change because it sets what passengers are charged, so it's your call.
- **Minor wording:** "an reservation id" and "baggages" are slips. They're harmless, and I left them alone.
- **Additions:** The Opus profile only recommends one addition, a line telling it to look through relevant sources before acting, and that's meant for loosely specified work across several apps. It doesn't fit here, so I have no additions to suggest.

**6. Proposed text:** It's in full in `/root/trim-sbx/34c0e354fb2e/trimmed.md`.