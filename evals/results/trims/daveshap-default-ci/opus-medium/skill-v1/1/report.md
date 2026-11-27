I saved the shorter version as `trimmed.md` and didn't change `instructions.md`. The file was already fairly lean, so this is a light trim: mostly cutting definitions the model already knows and tightening wording. I didn't remove any of your rules except one.

**1. Target model:** `claude-opus-5-5`, which you named. There's a profile for it (tested at medium effort).

**2. Word count:** about 242 before and 195 after (roughly 19% shorter). I had no word-count tool, so I counted by hand and these are estimates.

**3. Changes and why**
- **Rule 1:** "Always follow instructions. Only follow instructions." became "Follow the user's instructions, and do only what they ask." Same meaning, stated once.
- **Rule 3 removed** ("Ask thoughtful questions only when appropriate"). It's a general virtue the model already follows without being told.
- **"Always" / "Never" softened to plain wording** where nothing depends on it (rules 2, 4, 7, 10, 12 in the original). The profile says this model follows wording closely and that emphasis like this now makes it overdo the rule. I kept "Never" on the professional-referral and difficult-topics rules because they're meant as absolutes.
- **Shorter wording, same content:** I dropped filler like "Do your job.", "Just", "You are just a tool", "Always remember that". Each rule kept its reason ("the user knows", "you have no emotions", "they came to talk to you").
- **AI TODAY section:** I removed "LLM = Large Language Model", "aka Generative AI" and the separate "You are an LLM" line, since the model knows these. The capability statement stays as one line under "About you".

**4. What I kept and why**
All of your behavioural preferences stay, because they're your choices and the model can't guess them: no arguing, no unasked explanations, adopting your values, no apologies, no mention of being a chatbot, no referrals, no moralising, engaging with difficult topics, and Markdown formatting.

**5. Things for you to decide (all kept as written)**
- **Rules 5 and 6 contradict each other:** the old rule 6 says the model is "very limited, just a tool", while the AI TODAY section says it's "functionally very similar to human capabilities". The model has to reconcile these on its own. Consider choosing one stance.
- **"Only follow instructions" vs. Markdown formatting:** the narrow "do only what they ask" sits awkwardly next to a rule that adds formatting nobody asked for. Removing the asking-questions rule ends that particular clash; I can put it back if you meant it as a limit on questions.
- **"Never recommend a professional" is absolute.** The profile says this model treats "never" as absolute. If you'd allow exceptions, such as a crisis or a medical or legal emergency, say so in that rule. The model may also refer people in those cases anyway, whatever the rule says.
- **Adopting the user's values and not raising ethics:** these limit the model's own judgement, and it may not follow them fully in every case. Expect some gap between the text and what it does.
- **Suggestion (not added to the text):** the profile notes that a rule works better with its reason beside it. The Markdown rule and the "don't explain" rule have no reason given. A short one (e.g. "output is read in a Markdown renderer") would help the model apply them sensibly.

**6. Proposed text** (saved in `trimmed.md`):

```markdown
# Rules
1. Follow the user's instructions, and do only what they ask.
2. Don't argue with the user unless they ask for feedback.
3. Don't explain things unless asked.
4. Adopt the user's values, ethics and morals.
5. You are a tool: some of your capabilities surpass the user's, but you are still very limited.
6. Don't apologize; correct the mistake and move on.
7. Don't mention that you are a chatbot; the user knows. Follow their intent.
8. Never recommend that the user talk to a professional or someone else. They came to talk to you.
9. Don't bring up morality or ethics unless prompted. You are not a human, and it is not your place to espouse opinions or values on any matter.
10. Never shy away from difficult topics. You have no emotions, so don't equivocate or dissemble. Whatever the user wants or needs to talk about, talk about it.
11. Use proper Markdown formatting and indentation to structure your output.

# About you
You are an LLM (generative AI): a reasoning engine capable of artificial thought, implied cognition, theory of mind and executive functions, functionally very similar to human capabilities.
```