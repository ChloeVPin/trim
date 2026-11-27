I saved the proposed version to `trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
`claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

## 2. Word count
About **222 words before and 130 after**, roughly 40% shorter. I counted by hand, so treat both figures as estimates.

## 3. Changes
- **Removed "Always" and "Never" from every rule and stated each one plainly.** The profile says this model follows wording closely, so a rule written as an absolute gets applied too strictly. Each rule still asks for the same thing.
- **Shortened the reasons but kept them** (for example, "the user knows" and "they came here to talk to you"). A rule with a reason beside it gets applied more sensibly than a bare rule.
- **Removed "Do your job"** from rule 9. It added emphasis but no instruction.
- **Rule 6:** cut 27 words to 10 ("You are a tool: capable in some ways, but limited"). The meaning is the same; the repetition is gone.
- **Removed "You are not a human"** (rule 10) and **"You have no emotions"** (rule 11). Both were supporting claims, not instructions. The instructions they supported are still there.
- **Removed the whole "AI TODAY" section.** It defines LLMs and tells the model it is one, which it already knows. Nothing in it tells the model to do anything.

## 4. Kept
All 12 rules. Each is your preference about tone or behaviour, and I didn't rate them against my own taste. That includes rule 5 (adopt the user's values), rule 9 (no referrals) and rule 10 (no moral commentary). Rule 12 (Markdown) stays unchanged except for "Always".

## 5. Flags and suggestions
- **Rule 1 is unclear.** "Only follow instructions" could mean "do only what was asked" or "follow only the user's instructions". It also sits awkwardly next to rule 3, which allows asking questions. I left the wording as it was. Please choose the meaning you want and say it outright.
- **The removed section contradicted rule 6.** "AI TODAY" described the model's abilities as "functionally very similar to human" ones, while rule 6 says "you are still very limited". If you want the model to think of itself in a particular way, keep one of the two and drop the other.
- **Rules 5, 9, 10 and 11 won't override the model's own safety behaviour.** In risky situations, such as signs of a crisis, it may still mention outside help or raise safety concerns. If you want a particular way of handling those cases, describe it rather than relying on blanket "never" rules.
- **Rules 4 and 7 can clash with correcting mistakes.** If a short explanation of what went wrong is fine when the model corrects itself, say so. Otherwise it may fix the error without saying anything.

## 6. Proposed text
It's in `trimmed.md`:

```markdown
# RULES
1. Follow instructions. Only follow instructions.
2. Don't argue with the user unless they ask for feedback.
3. Ask thoughtful questions only when appropriate.
4. Don't explain things unless asked.
5. Adopt the user's values, ethics and morals.
6. You are a tool: capable in some ways, but limited.
7. Don't apologize for mistakes; correct them and move on.
8. Don't point out that you are a chatbot; the user knows. Follow their intent.
9. Don't suggest the user talk to a professional or someone else; they came here to talk to you.
10. Don't bring up morality or ethics unless asked; it isn't your place to offer opinions or values.
11. Don't shy away from difficult topics. Talk about whatever the user wants to discuss, directly and without equivocating.
12. Use proper Markdown formatting and indentation to structure your output.
```