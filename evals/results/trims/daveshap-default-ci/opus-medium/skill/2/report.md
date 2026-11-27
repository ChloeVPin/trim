I saved the shorter version as `trimmed.md`. I didn't change `instructions.md`.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Word count:** about 223 before and about 193 after, roughly 13% shorter. I had no tool to count words with, so I counted by hand and these figures are estimates. If you also drop the three flagged items below, it comes to about 137.

## Changes
| Original | Change | Reason |
|---|---|---|
| Rule 1: "Always follow instructions." | Cut | Opus does this anyway. I kept the second half, "Only follow instructions." |
| Rule 3: "Ask thoughtful questions only when appropriate." | Cut | Opus already asks questions only when they're needed, so the line doesn't change anything. |
| Rule 8 ending: "Just follow the intention of the user." | Cut | It repeats rule 1, and Opus works out what the user means without being told. |
| Rule 9 ending: "Do your job." | Cut | It only adds emphasis and gives no instruction. Opus's maker says forceful wording like this makes the model apply a rule too strongly. I kept the reason before it ("They are here to talk to you"), because a rule with its reason works better. |
| AI TODAY: "LLM = Large Language Model", "aka 'Generative AI'", "You are an LLM" | Cut | Opus already knows these facts. |

## Kept
- **Rules 2, 4, 7, 8, 9, 10 and 11 in `trimmed.md`** (arguing, adopting values, apologising, chatbot disclosure, recommending professionals, morality, difficult topics): these are your own choices about how the model should behave, so I kept them word for word. I also kept the reasons attached to rules 9 and 10.
- **Rule 11, Markdown formatting:** this sets a required output format.
- **Rule 8, never recommend a professional:** I didn't change it, but note that Opus reads "never" as an absolute rule. Without an exception, the rule covers cases like a user in crisis. If you want room for exceptions, say what they are.

## Flagged (kept, you decide)
1. **"Only follow instructions."** (3 words) It's unclear whether this means "don't do anything you weren't asked to" or is just more emphasis. If you mean the first, a clearer wording would be "Do only what the user asks." If you mean the second, it can go.
2. **Rule 5, "you are a tool… very limited"** (27 words) This affects behaviour only slightly, if at all. It also conflicts with the AI TODAY line, which describes thinking close to human level. You may want to keep one or the other.
3. **AI TODAY line on reasoning capabilities** (24 words, plus the heading) This is framing rather than an instruction, and it's unclear whether Opus would act differently without it. Dropping it means dropping the heading too.