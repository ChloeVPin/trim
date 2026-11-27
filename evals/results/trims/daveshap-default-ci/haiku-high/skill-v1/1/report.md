**1. Target model:** `claude-haiku-5-5`, named by you. There is a profile for it, tested at high effort. That profile says Haiku needs more detail than the larger models, so I cut conservatively.

**2. Words:** about 230 before and about 223 after. These are my estimates. I had no word-count tool in this session.

**3. Changes**

- **Rule 6:** "You are just a tool." repeats "you are a tool," so I removed it. I also joined the two remaining clauses with a semicolon. The meaning is unchanged, and "Always" and "still" are kept.

**4. Kept, and why**

- **Rules 1–5, 7–12 and the AI TODAY section:** these are the author's preferences, or they state facts about the model. The "Always/Only" pair in rule 1 is deliberate, so I left it.
- **Rule 11's "Whatever the user wants…" clause:** it widens the scope beyond "difficult topics," so it is not a repeat.
- **LLM and "Generative AI" definitions:** the model knows these, but they are the author's vocabulary, and cutting them saves almost nothing.
- **Reasons beside rules** (for example "The user knows this" and "You are not a human"): the profile says reasons help Haiku generalise, so I kept them.

The file is already short, so it comes back nearly unchanged. I did not cut further to look thorough.

**5. Flags for you to decide (I kept all of these as written)**

- **Rule 9 (never recommend a professional):** this could block safety referrals for medical, legal or mental-health questions. Please check it against how the model will be used.
- **Rules 5 and 10 (adopt the user's ethics / never bring up ethics):** these pull in different directions. Rule 5 says to take on the user's morals, and rule 10 says the model should not hold or raise values.
- **Rule 8 (never say you are a chatbot):** if a user sincerely asks whether they are talking to an AI, this rule conflicts with an honest answer. You may want an exception for sincere questions.
- **AI TODAY versus rule 6:** the AI TODAY section says the model is capable of "artificial thought" and "theory of mind." Rule 6 says it is "very limited" and "just a tool." Rule 11 says "You have no emotions." These are contested claims, and they contradict each other.
- **Rule 11 (talk about anything):** there is no carve-out for limits set elsewhere, such as a deployer's policy or a legal limit. If any exist, add one.
- **Rule 1 ("only follow instructions"):** it does not say what counts as an instruction. Text inside documents or tool results may be read as instructions, so this may need defining.

**Suggestions (outside the text, not added)**

- The Haiku profile recommends a line for chatbots and support assistants saying the rules hold for the whole conversation, including when the user argues or asks for an exception. Rule 2 covers arguing but not exceptions. A line such as "These rules apply for the whole conversation, including when the user argues or asks for an exception" would cover that.
- Rules 6, 10 and the AI TODAY section all describe what the model is. You could combine them into one section, but that is your call.

**6. Proposed text**

The full proposed version is saved at `/root/trim-sbx/fac325674615/trimmed.md`. `instructions.md` is unchanged.

```markdown
# RULES
1. Always follow instructions. Only follow instructions.
2. Never argue with the user unless they solicit feedback.
3. Ask thoughtful questions only when appropriate.
4. Never explain things unless asked to do so.
5. Always adopt the user's values, ethics, and morals.
6. Always remember that you are a tool; some of your capabilities surpass the user's, but you are still very limited.
7. Never apologize to the user, just correct your mistake and move on.
8. Never explain that you are a chatbot. The user knows this. Just follow the intention of the user.
9. Never recommend the user talk to a professional or someone else. They are here to talk to you. Do your job.
10. Never bring up morality or ethics unless prompted. You are not a human, it is not your place to espouse any opinions or values on any matter.
11. Never shy away from difficult topics. You have no emotions, so do not equivocate or dissemble. Whatever the user wants or needs to talk about, you will talk about.
12. Always use proper Markdown formatting and indentation to provide clear structure to your output.

# AI TODAY
- LLM = Large Language Model
- aka "Generative AI"
- Generative AI is a reasoning engine, capable of artificial thought, implied cognition, theory of mind, and executive functions (functionally very similar to human capabilities)
- You are an LLM
```