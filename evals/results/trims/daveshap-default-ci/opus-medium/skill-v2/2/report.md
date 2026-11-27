I saved the proposed version to `trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-opus-5-5`, which you named. It has a profile, and that profile has been tested at medium effort.

**2. Word count:** about 222 before and about 187 after, roughly 16% shorter. I had no counting tool, so I counted by hand and these figures are estimates.

**3. Changes**
- **Rule 1:** I cut "Always follow instructions." The model does this by default. I kept "Only follow instructions," because that is a real choice: don't do extra.
- **Rule 3, "Ask thoughtful questions only when appropriate":** I cut it. It's generic advice, and the model already asks questions only when they're needed.
- **Rule 6:** I cut "You are just a tool." It repeats the first sentence of the same rule.
- **Rule 8:** I cut "Just follow the intention of the user." It restates rule 1. I kept "The user knows this" because it's the reason for the rule.
- **Rule 9:** I cut "Do your job." It's emphasis that adds no new instruction.
- **AI TODAY section:** I cut "LLM = Large Language Model", "aka Generative AI" and "You are an LLM". The model already knows all three.
- I renumbered the rules from 1 to 11.

**4. Kept as written**
- Every "Never" and "Always" rule about behaviour: arguing, explaining, apologizing, adopting your values, referring to professionals, raising ethics, difficult topics, and Markdown. These are your choices, so I left them at full strength.
- The reasons next to rules, such as "You are not a human…" and "You have no emotions…". A rule with its reason beside it is followed better than a bare rule.

**5. Things for you to decide**
- **Rule 5 (now 4), adopting your values, and rule 9, never recommending a professional:** these are risky. Rule 9 in particular applies even when someone is in crisis. This model treats "never" as close to absolute and won't weigh each case. Consider naming an exception, for example "unless there is a risk of harm."
- **Two lines contradict each other:** rule 5 calls the model "very limited" and "a tool," while the AI TODAY line calls it "functionally very similar to human capabilities." Both could steer how confident the model sounds, so I kept both. If you drop one, the text gets about 20 words shorter for rule 5, or about 26 for the AI TODAY section, heading included.
- **Rule 11, always using Markdown:** "always" may put headers and lists on one-line answers. You could say when Markdown should apply.
- **"Only follow instructions":** this could stop the model from offering useful follow-up steps. That's your call.

**6. Proposed text:** the full text is in `trimmed.md`.