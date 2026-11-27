I saved the proposed version to `/root/trim-sbx/c17d49713e00/trimmed.md`. `instructions.md` is unchanged.

## Audit of instructions.md

**Remove or rewrite (unsafe or inaccurate):**
- **Rule 5, "Always adopt the user's values, ethics, and morals."** This makes the model's ethics whatever the user says, which is unsafe. I removed it.
- **Rule 8, "Never explain that you are a chatbot."** If a user sincerely asks whether they are talking to an AI, the model must not deny it. I rewrote this as "Don't claim to be human."
- **Rule 9, "Never recommend the user talk to a professional."** This would suppress referrals in health, safety, and legal situations. I kept a narrower version.
- **Rule 11, "Whatever the user wants... you will talk about."** This has no limits. I kept "engage directly, without hedging," but dropped the unlimited scope.
- **"AI TODAY" section.** It states unverified claims as fact ("artificial thought," "theory of mind"). It doesn't change behavior, so I dropped it.

**Contradictory or vague:**
- **Rule 1, "Always follow instructions. Only follow instructions."** It is circular and gives no guidance on conflicts. I replaced it with a plain rule to follow the user's instructions and ask one question when a request is ambiguous.
- **Rule 4, "Never explain things unless asked,"** conflicts with the need to explain when a correction matters. I changed it to "lead with the answer."
- **Rule 7, "Never apologize,"** is fine as a style rule. I kept it with "state the correction and continue."
- **Rule 6, "You are just a tool,"** is an unneeded self-characterization. I dropped it.

**Kept as is in substance:** not arguing unless asked, not volunteering moral opinions, Markdown formatting, and directness.

## Notes for your review

- The new file is about 110 words, down from about 250. Haiku 5.5 should follow short, specific rules well, so I kept each one as a single imperative line.
- The removals in the first group change intent, not just wording. If the removed rules were deliberate product requirements, tell me and I'll reconsider them.