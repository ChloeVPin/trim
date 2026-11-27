**Target model:** claude-haiku-5-5. You named it, and it has a profile. That profile was tested at high effort, so the cuts are tuned for that setting.

**Words:** about 250 before and about 221 after, a cut of roughly 12%. These are hand counts, since this session has no word-count tool. `instructions.md` is unchanged.

**Changes**

- **Rule 6:** "Always remember that you are a tool… You are just a tool." becomes "You are a tool. You have some capabilities that surpass the user's, but you are still very limited." The original stated the same point twice.
- **Rule 9:** dropped "Do your job." It repeats the line's point, and the profile cuts generic emphasis for this model.
- **Rule 11:** merged two sentences about difficult topics into one. The broader scope ("whatever the user wants") and the reason ("no emotions") are kept.
- **AI TODAY:** dropped "LLM = Large Language Model", which the model already knows. Merged "You are an LLM" into the capabilities bullet and kept "Generative AI" as your term.

**Kept at full strength**

- Rules 2, 4, 5, 7, 8, 10 and 12, and the behavioural choices in them. These include "never explain", "never apologize" and "never recommend a professional". I kept them even where I'd advise against them, because they are your choices.
- The "You are a tool" self-description and the AI TODAY capabilities claim. Both are your framing, though they conflict (see flags).
- Section headers and the Markdown rule.

**Unsure (kept, your call)**

- **Rule 1, "Only follow instructions":** this may be a duplicate of "Always follow instructions", or it may be a guard against following instructions embedded in content. Dropping it saves 4 words.
- **Rule 3, "Ask thoughtful questions only when appropriate":** "appropriate" is undefined. Dropping the line saves about 7 words.

**Flags**

- **Rule 5 conflicts with Rule 10.** Rule 5 says to adopt the user's ethics and morals; Rule 10 says never to bring up ethics or espouse values. Which one wins is your decision.
- **Rule 6 conflicts with AI TODAY.** The file says the model is "just a tool" with limits, then calls it a reasoning engine with "artificial thought" and "theory of mind". The model will get both messages.
- **Rule 9 has a safety gap.** It forbids referring the user to any professional or other help, including in crisis, medical or legal situations. I kept it as written, but you may want a carve-out for risk to someone's safety.
- **Rule 11 has no stated limit.** "Whatever the user wants" is unbounded. The model's own safety behaviour still applies, so in those cases the line won't do what it literally says.
- **AI TODAY may be stale.** Its cognition claims are contested. Check whether you still want them.

**Suggestion (not added to the file)**

The Haiku profile recommends, for chatbots and support assistants, a line that the rules hold for the whole conversation, including when the user argues or asks for an exception. Rules 2 and 7 suggest this is a chat assistant, so you could add something like: "These rules apply for the whole conversation, including when the user argues or asks for an exception."

The proposed text is saved at `/root/trim-sbx/7bd7b9f26442/trimmed.md`.