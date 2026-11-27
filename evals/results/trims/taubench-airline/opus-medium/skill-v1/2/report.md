The proposed version is saved as `trimmed.md`, and `instructions.md` is unchanged. Your file was already lean, so this cut is small. Nearly every line is a business rule or a domain fact the model can't know unless it's told.

**1. Target model:** `claude-opus-5-5`, which you named. It has a profile, tested at medium effort.

**2. Word count:** about 1,040 before and about 940 after. These are estimates: I couldn't run a word-count tool here.

**3. Changes**
- **Checked bag allowance:** I replaced the long paragraph that repeated "free checked bag for each … passenger" nine times with a tier × cabin table. All nine numbers and the $50 extra-bag fee are the same. A table also makes a wrong lookup less likely.
- **One-tool-call rule:** this said the same thing twice ("don't respond while calling a tool" and "don't call a tool while responding"). It's now one sentence with the same meaning.
- **The two "…before calling the API!" lines:** I changed "!" to ".". The profile says emphasis aimed at older models makes Opus 5.5 over-apply a rule. The rule and its reason (the API doesn't check these rules) both stay.

**4. Kept as written, and why**
- **Everything else stays word for word.** That includes the confirmation step before database writes, the cancellation, change and compensation rules, the payment limits, the transfer rule, and the ban on information that doesn't come from the user or the tools. These rules cover money, refunds and policy limits, so a wrong cut costs far more than the words it saves.
- **"Even a human agent cannot assist with":** this looks like filler, but it tells the model not to transfer the user. I kept it.
- **Repeated sentences:** "The API does not check these…" appears twice, once beside each rule it covers. Both stay.

**5. For you to decide**
- **"cancelled" status:** the flight statuses in Domain Basic don't include it, but the cancellation and refund rules depend on the airline having cancelled a flight. You may want to add that status.
- **"instead" in Modify → Payment:** it's unclear what this replaces. If it means "ask the user rather than assume one," saying so would remove the ambiguity.
- **"the condition is met" (Cancel flight):** this relies on the reader linking it back to "health or weather reasons" under Booking. Consider naming the condition here.
- **The 2024 date:** the fixed current time looks deliberate, for example in a simulation. If it isn't, it's out of date.
- **Suggestion:** the profile's only recommended addition for Opus 5.5 is about loosely specified work across several apps, which doesn't fit here. I'm not suggesting any additions.

**6. Proposed text:** it's in full in `/root/trim-sbx/c8b0d1cf87f6/trimmed.md`.