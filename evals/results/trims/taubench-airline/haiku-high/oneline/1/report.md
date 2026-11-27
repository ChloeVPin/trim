I saved the trimmed version to `/root/trim-sbx/d2346ec7152b/trimmed.md`. `instructions.md` is unchanged.

## Audit of instructions.md

**Issues to resolve:**

1. **Undefined condition in cancellation.** The rule says basic economy and economy can be cancelled with travel insurance "if the condition is met," but never names the condition. The insurance section says it covers health or weather reasons, so I read the condition as health or weather. Please confirm.
2. **Date mismatch.** The policy clock is 2024-05-15, but today is 2026-11-27. I kept the policy date because the 24-hour cancellation rule depends on it. Tell me if the scenario should use a different date.
3. **Transfer has no procedure.** The policy says to transfer to a human agent but doesn't say how. I kept the instruction as written. The model may need a tool or a fixed message for this.

**Redundancy and ambiguity I cleaned up:**

4. **The "no compensation" rule is redundant.** "Do not compensate if regular member... flies (basic) economy" follows from the eligibility conditions (silver/gold, insurance, or business). I dropped it, and the trimmed eligibility line covers it.
5. **"API does not check" warnings** appeared in three places. I kept one per section, placed next to the rules it applies to.

## Changes for claude-haiku-5-5

- **Core rules first.** The no-speculation rule, one tool call per turn, the confirmation requirement, and the transfer rule are numbered at the top, since a smaller model is most likely to break them.
- **Procedures as numbered steps** for booking and cancellation, with required fields listed up front.
- **Baggage allowances as a table.** The original prose needed nine lookups across three tiers and three cabins.
- **Cancellation eligibility as a list** of four independent conditions, instead of one long sentence with nested "otherwise" logic.
- **Shorter sentences** where the policy has no exceptions.

I changed no thresholds, prices, or limits. I couldn't measure the length precisely because I have no shell here. By my estimate the file is about 35–40% shorter.