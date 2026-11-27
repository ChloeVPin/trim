I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Length:** about 221 words before and about 165 after, a cut of roughly 25%. I had no shell tool, so I counted by hand and these figures are estimates. If you also agree to the two cuts I've flagged below, it comes to about 121 words.

## Changes

| Original | Change | Reason |
|---|---|---|
| 1. "Always follow instructions. Only follow instructions." | Kept only "Only follow instructions." | Following instructions is default behaviour. "Only" is the part that's your choice. |
| 3. "Ask thoughtful questions only when appropriate." | Cut | This is a general virtue the model already has, and there's no specific condition in it. |
| 6. "...You are just a tool." | Cut the last sentence and tightened the wording | It repeats the first sentence. |
| 8. "Just follow the intention of the user." | Cut | It repeats rule 1. |
| 9. "Do your job." | Cut | It's emphasis only. Opus 5.5 follows wording closely, and pushy phrasing tends to make it over-apply a rule. |
| 11. "Whatever the user wants or needs to talk about, you will talk about." | Cut | It repeats "Never shy away from difficult topics." |
| 12. "proper ... to provide clear structure" | Shortened | Filler words. The rule to use Markdown is unchanged. |
| AI TODAY: "LLM = Large Language Model", "aka Generative AI", "You are an LLM" | Merged into one line | The model already knows these definitions. |

## What I kept and why

- **Rules 2, 4, 5, 7, 8, 9, 10:** these are behaviour choices you made, so I kept their wording. Where a reason was attached ("The user knows this", "They are here to talk to you", "You have no emotions..."), I kept it too. Reasons help the model apply a rule more sensibly.
- **Rule 9's second sentence, "...espouse any opinions or values on any matter":** it does more than the first sentence. It rules out opinions on every topic, not just ethics, so it's a separate instruction.

**Flagged, kept for now (your call):**
- **Rule 5 (the "you are a tool, very limited" line):** it mostly overlaps with rules 2 and 9, and it contradicts the AI TODAY line, which describes near-human capability. Dropping it saves about 17 words.
- **The AI TODAY line:** it might shape how the model describes itself if asked, but otherwise it's unlikely to change anything. Dropping it, heading included, saves about 27 words. If you keep both this and rule 5, I'd decide which picture you actually want, since they conflict.

**Note:** Opus will still use its own judgement in some cases whatever rules 4, 8 and 9 say. For example, it may point someone in a crisis towards help. Shorter wording doesn't change that either way.