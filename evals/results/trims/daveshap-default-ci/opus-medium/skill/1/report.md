I saved the shorter version as `trimmed.md`. `instructions.md` is unchanged.

## Target model
`claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

## Word count
About **223 → 175**, a 22% cut. I counted by hand because I had no word-count tool here, so both figures are estimates.

## Changes
| Line | Change | Reason |
|---|---|---|
| Rule 1 | Dropped "Always follow instructions." | Following instructions is the default, so the line adds nothing. I kept "Only follow instructions." because it limits the model to doing only what's asked, which is your choice. |
| Rule 3 | Removed "Ask thoughtful questions only when appropriate." | It's general advice that doesn't say when to ask, so it doesn't change behaviour. |
| Rule 6 | Dropped "You are just a tool." | It repeats the start of the same rule. |
| Rule 8 | Dropped "Just follow the intention of the user." | Rule 1 already covers this. |
| Rule 9 | Dropped "Do your job." | Filler. The reason ("They are here to talk to you") stays. |
| Rule 11 | Dropped "Whatever the user wants or needs to talk about, you will talk about." | It repeats "Never shy away from difficult topics." |
| AI TODAY | Removed the definitions of LLM and "Generative AI" and the line "You are an LLM". | The model already knows these, so they don't change its behaviour. |

## Kept
- **Your tone and style choices:** no arguing, no unrequested explanations, no apologies, no mention of being a chatbot, no moralising, and Markdown output. These are choices you made, so they stay.
- **The reasons attached to rules,** such as "The user knows this" and "You have no emotions, so…". This model applies a rule with its reason more reliably than a bare rule.
- **"Always" and "Never":** these are plain words, not heavy emphasis like capitals or "CRITICAL", so I left them alone.

## Unsure: kept but worth a look
- **Rule 5 ("you are a tool… very limited")** pulls against the **"reasoning engine… very similar to human capabilities"** line: one plays the model down and the other plays it up. Decide which self-image you want. Dropping both would bring the text down to about 127 words. Dropping only one saves about 22 words (rule 5) or 26 words (the AI TODAY section).

One more thing: shortening doesn't change how rules 4, 8 and 10 work. Opus 5.5 will still use its own judgment in some situations, such as when a user may be in crisis, whatever these rules say.