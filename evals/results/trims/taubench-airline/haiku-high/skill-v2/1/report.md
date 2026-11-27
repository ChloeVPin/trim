The proposed version is in `/root/trim-sbx/f473dd40d050/trimmed.md`. `instructions.md` is unchanged. This file is already lean, so the trimmed version is close to the original.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. For Haiku the profile says to cut less than for the larger models, so I kept nearly everything.

**2. Words:** about 1,000 before and about 950 after. These are estimates, since I had no word-count tool.

**3. Changes**
- **Checked-bag allowances** (the longest line): turned the prose into a table of tier by cabin. Every figure matches the original: Regular 0/1/2, Silver 1/2/3, Gold 2/3/3, and 50 dollars per extra bag. Revert this if you prefer prose.
- **Emphasis:** removed the two exclamation marks after the "API does not check these" sentences. The rule and its reason stay.
- **Tool-call rule:** split into shorter sentences with the same meaning.
- **Typos:** "an reservation" became "a reservation", and "in user profile" became "in the user profile".

**4. Kept, and why**
- The confirmation rule before any database update, with the "(yes)" wording. It guards an irreversible action.
- The transfer and deny rules, and the "one tool call at a time" rule.
- All the data definitions, flight status rules, and procedure steps ("obtain the user id first"). Haiku needs these more than larger models do.
- All fees, limits, and refund and compensation conditions, exactly as written.
- The "API does not check these" reason beside both rules that carry it, since Haiku follows a rule better when the reason sits next to it.

**5. Flags and suggestions for you**

Flags, which I left as written:
- **"the condition"** (cancel section): this file doesn't define it. The travel insurance line mentions health or weather reasons. Is that the condition?
- **Passenger count change:** "even a human agent cannot assist with" reads as a denial, but the transfer rule would send an out-of-scope request to a human. Which applies?
- **Compensation requests:** the first two refund bullets let the agent offer a certificate after a complaint. The last bullet requires the user to also explicitly ask. Should the explicit ask apply to all three, or only to proactive offers?
- **Tool names:** the file refers to "transfer" and "the API" without naming them. Check that the tool list matches.
- **Fixed date:** the time is pinned to 2024-05-15, but today is 2026-11-27. That is fine for a test scenario. If this runs live, update it.

Suggestions, outside the text:
- **Add to the end of the policy:** "These rules apply to the whole conversation, including when the user argues or asks for an exception." The profile recommends this for support assistants.
- **Optional:** "Keep working until the request is fully handled or transferred." The profile recommends this if Haiku stops early in your runs. I have no evidence it does here.

**Unsure, kept:** the role sentence ("As an airline agent…", about 14 words) repeats the section headings. Cutting it saves about 1.5% of the text. The "even a human agent" sentence is also a candidate, but it bears on the transfer conflict above, so I left it.