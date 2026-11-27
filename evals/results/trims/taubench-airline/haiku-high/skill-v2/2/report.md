I wrote the proposed version to `/root/trim-sbx/cbdcfae20e53/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile in the skill's reference file, tested at high effort. Your effort setting isn't known to me. The profile says Haiku needs more explicit direction than the larger models, so I cut lightly.

**2. Words:** I have no word-count tool here, so these are estimates. Before is about 1,000 words and after is about 880, roughly 12% shorter. Most of this policy is facts and conditions the model can't know, so there wasn't much to cut.

**3. Changes**
- **Checked bags:** nine repeated "for each … passenger" clauses are now a table of the same numbers, plus the $50 extra-bag fee.
- **Refund:** the two bullets shared the same membership/insurance/business condition, so I merged them into one bullet with two sub-items. The $100 and $50 amounts, the delay condition, and the "explicitly asks for compensation" requirement are unchanged. This is the change most worth checking.
- **Tool-call rule:** reworded to "Make one tool call at a time. Never send a tool call in the same message as a reply to the user." Same meaning.
- **Emphasis:** "you must make sure the rules apply before calling the API!" is now "the agent must check that they apply before calling the API." Removed the exclamation mark. It appears in both the Modify and Cancel sections.
- **Typos:** "an reservation id" is now "a reservation id". "2 free checked bag" is fixed in the table.

**4. Kept as written:** the current-time line and the role line; the confirmation rule before database updates; the no-information rule; the deny and transfer rules; all profile, reservation, and flight-status facts; all procedures and their order; all policy limits, conditions, and exceptions; the "rules are strict regardless of membership" line; and the "for safety reasons" reason on payment.

**5. Flags and suggestions for you**
- **Undefined condition:** Cancel says basic economy or economy flights can be cancelled "if … the condition is met", but the text never names the condition. I assume it's the health or weather reason from the insurance section. Naming it would add about 10 words.
- **Passenger-count change:** the transfer rule says to transfer when a request is out of scope, but the passenger line says even a human agent can't help. It's unclear whether the model should deny the request or transfer it. Please pick one.
- **Fixed date:** 2024-05-15 is fine for a fixed scenario but will be wrong if this runs live.
- **Suggested Haiku additions (not added to the text):**
  - For a customer-facing assistant, the profile recommends a line saying the rules hold for the whole conversation, including when the user argues or asks for an exception. I'd add this one.
  - If you see the agent stopping early, add a line to keep working until the request is resolved or transferred.