I saved the shorter version as `trimmed.md`, and `instructions.md` is unchanged. Every rule from the original is still there; most of the savings come from rewording, not from dropping content.

**What changed:**
- **Baggage allowance:** the long paragraph of nine cases is now a 3×3 table, which is shorter and harder to misread.
- **Repeated wording cut:** phrases like "the agent should…", "you should…" and "for safety reasons" are gone. Each section now starts with what the agent must first obtain, followed by short labeled bullets.
- **Compensation section** (renamed from "Refund", since it's about goodwill certificates, not refunds): the condition "silver or gold, or has insurance, or flies business" was written out twice and then repeated as a negation in a third bullet. It's now stated once, along with the requirement to wait until the user asks.
- **Cancellation rules:** the run-on sentence is now a list of which cabin can cancel under which conditions.
- **Tone:** "the agent must make sure the rules apply before calling the API!" is now a plain "check them yourself before calling it." Opus 5.5 doesn't need emphasis to follow a rule, and strong wording tends to make models apply rules too broadly.

**What I kept on purpose:**
- **Fixed current time:** the agent needs it to work out the 24-hour cancellation window.
- **One tool call per turn:** this probably reflects how the system runs tool calls, so I kept it.
- **"The API doesn't enforce these rules":** this explains why the agent has to check the rules itself.
- **"A human agent can't change it either":** this stops the agent from transferring users who want to change the number of passengers.

**Two wording changes to double-check:**
- **Membership tiers:** I listed them as regular, silver and gold, which the original only implies.
- **Cancellation reasons:** "the condition is met" is now "the reason is covered", meaning health or weather. If that's not what the original meant, change the wording back.