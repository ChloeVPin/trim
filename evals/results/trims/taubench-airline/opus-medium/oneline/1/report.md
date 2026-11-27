I saved the shorter version as `trimmed.md` and didn't change `instructions.md`. It's about 25% shorter and keeps every business rule.

**What I found in the original:**
- **Repeated rule:** "The API does not check these for the agent, so the agent must make sure the rules apply…!" appears twice, with an exclamation mark for emphasis. A strong model doesn't need the shouting. I stated it once, in plain words, as a general rule.
- **Bag allowances were hard to read:** they were one long sentence covering 9 combinations, which is easy to misread. They're now a 3×3 table.
- **Flight statuses were spread out:** the bullets for "delayed", "on time" and "flying" each said "cannot be booked." I replaced that with one rule: only "available" flights can be booked.
- **The cancellation rule was one dense sentence:** I turned it into a list of four conditions, any one of which allows cancellation. The rules themselves are the same.
- **Compensation rules were repeated:** both refund bullets repeated the "silver/gold, or insurance, or business" requirement, and the "only if they complain" limit came after them. Those shared conditions now come first, once, followed by the two cases.
- **Filler:** I cut wordy phrasing such as "for safety reasons," "you should," and "the agent must first…" and grouped the general rules together.

**Kept on purpose:**
- The rule that each turn is one tool call or one message, never both. It reads like a technical limit of the system the agent runs in, not a style preference.
- The note that even a human agent can't change the number of passengers. It tells the model not to transfer those requests.
- The note that membership tier doesn't change the cancellation rules. Without it, the model might make exceptions for gold members.

**Small changes worth checking:**
- The section header "Refund" is now "Compensation," because the section is about goodwill certificates, not refunds.
- "Change of plan" is now "change of plans."