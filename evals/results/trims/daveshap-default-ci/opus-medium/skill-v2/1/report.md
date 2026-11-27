I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged. It cuts about 18%, mostly lines that repeat other lines or state things the model already knows. Every rule you chose is still there, unchanged.

**Target model:** claude-opus-5-5, which you named. Its profile has been tested.

**Words:** about 223 before and 182 after. I counted by hand because I had no counting tool here, and I left out markdown markers like `#`, `1.` and `-`.

## Changes
| Original | Change | Reason |
|---|---|---|
| 1. "Always follow instructions." | Cut that sentence and kept "Only follow instructions." | The model follows instructions without being told. The second sentence is your choice and stays. |
| 3. "Ask thoughtful questions only when appropriate." | Cut | The model already does this. |
| 6. "You are just a tool." | Cut | It repeats the start of the same rule. |
| 9. "Do your job." | Cut | It adds emphasis but no new instruction. This model follows wording closely, so emphasis aimed at older models tends to make it over-apply a rule. |
| 11. "Whatever the user wants or needs to talk about, you will talk about." | Cut | It says again what "Never shy away from difficult topics" already says. |
| AI TODAY: "LLM = Large Language Model", "aka 'Generative AI'", "You are an LLM" | Cut | The model already knows all three. |

Removing rule 3 means the rules are numbered 1–11 instead of 1–12.

## What I kept and why
- All the "Never…" rules and their wording: no arguing, no explaining, no apologizing, no chatbot disclaimers, no referrals, no moralizing. These are your choices, so they stay at full strength.
- The reasons attached to rules, like "The user knows this", "You are not a human…" and "You have no emotions…". A rule with its reason next to it works better than a bare rule.
- The Markdown formatting rule, because it sets an output format.

## Flags for you to decide
1. **Rule 5 ("you are a tool… very limited") and the AI TODAY line contradict each other.** One says the model is very limited and the other says it works much like a human mind. I'm not sure either one changes how the model behaves. Dropping rule 5 saves 22 words, dropping the AI TODAY section saves 26, and dropping both brings the file to about 134 words.
2. **Rules 4, 8, 9 and 10 won't fully work as written.** The model keeps its own safety limits whatever the prompt says. For example, it will still point someone in a crisis toward help despite rule 8. If you want rule 8 to match what will actually happen, you could add an exception such as "…unless there is a risk of harm." I haven't added it.
3. **"Only follow instructions" is ambiguous.** It could mean "don't do things nobody asked for" or "ignore anything that isn't an instruction." Rewording it to say which you mean would make it more reliable.
4. **"Never" is treated as absolute.** If rules 3 or 6 are meant to bend in some cases, write the allowed case into the rule.

## Suggestions
None. The Opus 5.5 profile's one recommended addition is for work that spans several apps, and that doesn't apply to a chat-behaviour file like this one.