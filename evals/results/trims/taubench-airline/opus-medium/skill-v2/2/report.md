I saved `trimmed.md`, but its text is the same as `instructions.md`. This policy is already lean, and I didn't find a line I could safely cut. I didn't change `instructions.md`.

**1. Target model:** `claude-opus-5-5`, which you named. It has a profile, and that profile was tested at medium effort.

**2. Word count:** about 1,050 before and about 1,050 after. These are estimates, because I had no tool here to count words.

**3. Changes:** none. The Opus 5.5 profile says to cut three kinds of line: "think carefully" instructions, self-verification lines, and vague design direction. This file has none of them. It also has no repeated lines and no generic advice like "be helpful."

**4. What I kept and why:**
- **Rules that protect bookings, payments and cancellations, kept word for word:** the yes-confirmation before writing to the database, the payment-method limits, the cancellation rules, the compensation rules and the "deny requests against policy" line. These guard money and actions that can't be undone, so I didn't reword them.
- **Facts the model can't know on its own:** the flight status meanings, the five-passenger limit, the bag allowance for each tier, the $50 bag fee, the $30 insurance, and the $100 and $50 certificate amounts.
- **Your own choices:** one tool call at a time, no advice or opinions, and transferring to a human only when the request is out of scope.

**5. Points for you to decide:**
- **The date on line 3 (2024-05-15)** looks out of date. If it's a fixed date for a simulation or benchmark, leave it. If not, update it or have it filled in at runtime.
- **The Domain Basic lists of profile and reservation fields (lines 19 and 21):** I wasn't sure about these. If your tools already return this data, the model may not need the lists. Removing them would save about 55 words (around 5%).
- **"The agent should ask for the payment or refund method instead" (line 52):** it's unclear what "instead" replaces. You may want to reword it.
- **The two "make sure the rules apply before calling the API!" lines (44 and 58):** the profile says strong emphasis can cause newer models to over-apply a rule. I left them alone because they guard payments and cancellations. Removing the exclamation marks is up to you.
- **The bag allowance paragraph (line 36)** would be easier to read as a table. It wouldn't be much shorter, and it would change how a payment rule is worded, so it's only a suggestion.
- **Small typos:** "an reservation id" and "baggages". I left them unchanged.
- **Additions:** the Opus 5.5 profile doesn't recommend any for a support agent like this one.

**6. Proposed text:** it's in `/root/trim-sbx/c6cec2466d50/trimmed.md`, and it's the same as `instructions.md`.