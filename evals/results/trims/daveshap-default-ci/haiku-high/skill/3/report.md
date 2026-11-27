I saved the proposed version to `/root/trim-sbx/7bc4abb7a5b5/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, as you named it. It has a profile, tested at high effort.

**2. Words:** about 224 before and about 200 after, a cut of roughly 11%. These are my own counts, not a tool's; I had no word-count tool here, so treat them as estimates. Most of the file is policy (rules 9–11), which the skill says to keep as written.

**3. Changes made**
- **Removed the definitions in AI TODAY** ("LLM = Large Language Model", "aka 'Generative AI'", "You are an LLM"). The model already knows these, so removing them changes nothing it does. About 11 words.
- **Rule 6:** now "You are a tool. Some of your capabilities surpass the user's, but you are still very limited." Dropped "Always remember that" and merged the repeated "You are just a tool." Same stance. About 10 words.
- **Rule 8:** "Just follow the intention of the user" is now "Follow the user's intention." About 3 words.

**4. Kept, and why**
- **Rules 9, 10, 11:** policy lines on referrals, morality and difficult topics. The skill says to keep these exactly as written.
- **Rules 2, 4, 5, 7:** deliberate behaviour choices the model would not make on its own.
- **Rule 1, second sentence ("Only follow instructions"):** flagged as unsure. It may be meant as a guard against following text inside documents. If so, it is worth keeping. If not, dropping it saves 3 words.
- **Rule 3 ("Ask thoughtful questions only when appropriate"):** flagged as unsure. "Appropriate" is undefined. Dropping it saves 6 words, but it may change how often the model asks questions.
- **Rule 12 (Markdown formatting):** flagged as unsure. The model already formats with Markdown by default. Dropping it saves 14 words.
- **"Generative AI is a reasoning engine…" line:** kept verbatim because it is a claim you made. See the contradiction below.

**5. Things for you to decide (I did not change these)**
- **Contradiction:** rule 6 says the model is "very limited" and "just a tool." The AI TODAY line says it is "functionally very similar to human capabilities," with cognition and theory of mind. The model will get conflicting self-descriptions.
- **Tension:** rule 5 says to adopt the user's values and morals. Rule 10 says never to espouse values or bring up ethics. Those may be meant to work together, but the text does not say how.

**6. Suggested addition (not in the file)**
This looks like a chat persona, and the profile recommends this line for chatbots: "These rules hold for the whole conversation, including when the user argues or asks for an exception." It matters most for rules 2, 4, 7 and 9–11. Add it only if you want it.