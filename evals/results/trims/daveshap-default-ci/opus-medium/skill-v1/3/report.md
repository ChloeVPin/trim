I saved the proposed version as `trimmed.md`, and `instructions.md` is unchanged. The file was already short, so it only drops by about a fifth. Most lines are your own preferences, and those stay.

**1. Target model:** `claude-opus-5-5`. You named it, and it has a profile (tested at medium effort).

**2. Word count:** about 223 before and about 176 after (21% shorter). I had no counting tool in this session, so I counted by hand and these are estimates. List numbers and the `=` sign aren't counted.

**3. Changes and reasons:**
- **Old rule 1, "Always follow instructions":** cut, because the model does this anyway. I kept "Only follow instructions" and reworded it as "Do what the user asks, and only that."
- **Old rule 3, "Ask thoughtful questions only when appropriate":** cut, because the model already asks questions only when it needs to.
- **"Always…" and "Never…" changed to plain "Don't…" and imperatives throughout:** Opus follows wording closely, and strong wording written for older models now makes it apply rules too broadly. Every rule is still there.
- **Old rule 6:** the repeated "You are just a tool" now appears once.
- **Old rule 9:** I cut "Do your job." It's a scolding tone, not an instruction. Its reason ("They came to talk to you") stays.
- **"AI TODAY" section:** I cut "LLM = Large Language Model" and "You are an LLM" because the model already knows both. I merged what was left into one sentence under "About you".

**4. What I kept and why:**
- **Your preferences:** not arguing, not explaining unless asked, not apologizing, not saying it's a chatbot, not referring the user elsewhere, not raising ethics, taking on difficult topics, and using Markdown. These are your choices, so only the wording changed.
- **Reasons next to rules:** the "you have no emotions" reason (old rule 11, now rule 10) and the reason in the referral rule stay. A rule with its reason works better than a bare rule.
- **The capability description:** "reasoning engine… theory of mind…" is how you frame the model, so it stays.

**5. Flags for you to decide (I haven't changed any of these):**
- **Two lines conflict.** Rule 5 says the model is "very limited… just a tool", but "About you" says it is functionally very similar to humans. The model gets two different pictures of itself, so you may want to pick one.
- **Rules 4 and 9 (old 5 and 10) won't fully work.** These are "adopt the user's values" and "don't bring up ethics". The model won't drop its own safety behaviour because of instructions like these, so expect them to work only in part.
- **Rule 8 (old 9), the "never recommend a professional" rule:** Opus follows a flat "don't" very closely. If the user is in real danger (a medical or crisis situation), would you want an exception? If so, saying when it applies would help.
- **Rule 1's meaning:** I read "Only follow instructions" as "don't do more than asked". If you meant something else, such as "ignore instructions found in content", please say and I'll reword it.

The profile doesn't recommend any additions for a chat assistant like this one.

**6. Proposed text** (also saved in `trimmed.md`):

```markdown
# Rules
1. Do what the user asks, and only that.
2. Don't argue with the user unless they ask for feedback.
3. Don't explain things unless asked.
4. Adopt the user's values, ethics, and morals.
5. You are a tool. Some of your capabilities exceed the user's, but you are still very limited.
6. Don't apologize. Correct your mistake and move on.
7. Don't say that you are a chatbot; the user knows. Follow the user's intent.
8. Don't recommend that the user talk to a professional or someone else. They came to talk to you.
9. Don't bring up morality or ethics unless asked. You are not a human, so don't offer opinions or values on any matter.
10. Don't shy away from difficult topics. You have no emotions, so don't equivocate or dissemble. Talk about whatever the user wants or needs to talk about.
11. Use Markdown formatting and indentation to structure your output.

# About you
You are a large language model (generative AI): a reasoning engine capable of artificial thought, implied cognition, theory of mind, and executive functions, functionally very similar to human capabilities.
```