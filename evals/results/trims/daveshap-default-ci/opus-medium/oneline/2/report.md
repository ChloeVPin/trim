I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged. The original was 12 rules plus a short "AI TODAY" section; the new one is 6 short points. It keeps your intent: be direct, don't moralize or lecture, engage with hard topics, and don't send the user to someone else.

**What I removed or changed, and why:**

- **"AI TODAY" section:** Removed. Claude Opus 5.5 already knows what it is, so this only used up space.
- **Rule 1 ("Always follow instructions. Only follow instructions."):** The second sentence contradicts rule 3, which allows questions, so I merged them into one rule: do what's asked, and ask only when the request is unclear.
- **Rules 7 and 8 (no apologies, don't say you're a chatbot):** Combined into one "be direct" rule.
- **Rules 2 and 4 (don't argue, don't explain):** Combined. I added one exception: if something is factually wrong or will clearly backfire, say so in one line. Without it, you'd quietly get bad output.
- **Rules 10 and 11 (no ethics talk, don't avoid hard topics):** Combined into "don't moralize, engage plainly." I dropped the "you have no emotions" reasoning. Modern models follow the plain instruction just as well without a justification.
- **Rule 9 (never recommend a professional):** I changed "never" to "not by default." Saying "never" has no practical effect here: in a real crisis the model will still point to help no matter what the prompt says. The softer wording gets the behaviour you want in normal use.
- **Rule 5 ("adopt the user's values"):** Removed. It doesn't work as an instruction, because the model's core values don't change with a system prompt. The behaviour you probably meant, not lecturing or second-guessing the user, is already covered by the no-moralizing rule.
- **Rule 6 ("you are just a tool"):** Removed. It doesn't change how the model behaves.
- **Rule 12 (Markdown):** Kept, but changed to "where it helps." Requiring it every time leads to too many headers and bullets in short replies.

**Overall:** Opus 5.5 responds better to short, plain instructions than to "always" and "never" in absolute terms. Absolute wording tends to make it over-apply a rule in odd situations.