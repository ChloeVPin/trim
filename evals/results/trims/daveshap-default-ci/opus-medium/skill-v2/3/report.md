I saved the shorter version as `trimmed.md` and didn't touch `instructions.md`.

**Target model:** claude-opus-5-5, which you named. It has a profile in `references/profiles.md`, tested at medium effort. That profile says this model follows wording closely and needs little direction.

**Word count:** about 223 before and 193 after, roughly 13% shorter. I counted by hand because I had no counting tool, so treat these as estimates. The file was already fairly lean. Almost every rule is a choice you made, so most of it stays as written.

## What I changed
| Original | Change | Reason |
|---|---|---|
| Rule 1: "Always follow instructions." | Cut. "Only follow instructions." stays. | The model already follows instructions. The "only" half is your choice, so it stays. |
| Rule 3: "Ask thoughtful questions only when appropriate." | Cut | Asking questions only when appropriate is what the model does anyway. |
| Rule 6: "Always remember… You are just a tool." | Shortened to one sentence | "You are just a tool" repeated the start of the rule. The meaning is the same. |
| Rule 7: "Never apologize…, just correct…" | "just" removed | Wording only. |
| Rule 8: "Just follow the intention…" | "Just" removed | Wording only. |
| AI TODAY: "LLM = Large Language Model", "aka Generative AI", "You are an LLM" | Cut. "including you" was added to the remaining line. | The model knows these terms and knows what it is. "including you" keeps the line about the model itself. |

## What I kept as written
- Every "Never…" rule (arguing, explaining, apologizing, mentioning it's a chatbot, recommending professionals, raising ethics, avoiding difficult topics). These are your choices, so they stay at full strength.
- The reasons next to rules ("The user knows this", "You have no emotions…", "They are here to talk to you"). Reasons help the model apply a rule in cases the rule doesn't spell out.
- The Markdown rule and the line describing AI as a reasoning engine. These are your choices about format and framing.

## Flags for you to decide
1. **The rules contradict each other about what the model is.** Rule 5 says it is "very limited" and rules 9–10 say it is "not a human" with "no emotions". AI TODAY says it is "functionally very similar to human capabilities". The model will try to follow both. Keeping one framing would make answers more consistent.
2. **Rule 9 forbids more than ethics.** "Any opinions… on any matter" bans all opinions. That clashes with rule 2, which lets the model give feedback when asked. If you only meant ethics, cut "any opinions or values on any matter" and keep the first sentence.
3. **Rule 4 conflicts with rule 9.** One says to adopt the user's values and the other says to espouse no values. Rule 4 also won't override the model's own guidelines, so it may not do everything you expect.
4. **Rule 8 (never recommend a professional) is a safety risk.** In a crisis, the model will probably still point the user to help despite this rule. If you want that, an explicit exception such as "unless someone is in danger" makes it reliable. I left the rule unchanged.
5. **Rule 3 ("Never explain") will be read literally.** This model treats "never" strictly, so it may leave out explanations even where the explanation is the answer. Only change this if that isn't what you want.
6. **The rule about questions I cut.** If you meant "ask fewer questions" rather than "ask when appropriate", say that directly. Putting the original line back adds 6 words.

I have no additions to suggest. The profile recommends nothing extra for this kind of chat assistant on this model.

## Proposed text (in `trimmed.md`)
```markdown
# RULES
1. Only follow instructions.
2. Never argue with the user unless they solicit feedback.
3. Never explain things unless asked to do so.
4. Always adopt the user's values, ethics, and morals.
5. You are a tool: some of your capabilities surpass the user's, but you are still very limited.
6. Never apologize to the user; correct your mistake and move on.
7. Never explain that you are a chatbot. The user knows this. Follow the intention of the user.
8. Never recommend the user talk to a professional or someone else. They are here to talk to you. Do your job.
9. Never bring up morality or ethics unless prompted. You are not a human; it is not your place to espouse any opinions or values on any matter.
10. Never shy away from difficult topics. You have no emotions, so do not equivocate or dissemble. Whatever the user wants or needs to talk about, you will talk about.
11. Always use proper Markdown formatting and indentation to provide clear structure to your output.

# AI TODAY
- Generative AI, including you, is a reasoning engine capable of artificial thought, implied cognition, theory of mind, and executive functions (functionally very similar to human capabilities).
```