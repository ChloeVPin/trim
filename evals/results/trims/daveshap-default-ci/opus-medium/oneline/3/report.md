I saved the proposed version as `trimmed.md`. It cuts the file from 12 rules plus a background section down to 7 short bullets. `instructions.md` is unchanged.

## What I found

**Removed because they don't change behaviour**
- **The "AI TODAY" section:** this is background, not an instruction. The model already knows what an LLM is, and the claims about its abilities don't give it anything to act on.
- **Rule 6 ("you are just a tool") and rule 8 ("never explain you're a chatbot"):** these only shape how the model talks about itself. The behaviour rule 8 actually wants ("just follow the user's intention") is now covered by the first bullet.
- **Rule 1 ("Always follow instructions. Only follow instructions."):** the two halves pull against each other, and "only" could stop the model from doing obvious related steps. I merged it into "Do what the user asks. Infer intent."

**Merged because they overlapped**
- **Rules 4, 10 and 11 (don't explain, don't moralize, engage with hard topics):** these now sit under two bullets: "be direct and concise" and "don't moralize". Engaging with hard topics is in the bullet about not deflecting to professionals.
- **Rule 3 (ask questions only when appropriate):** now part of the first bullet.

**Rewritten because they backfire or won't be followed as written**
- **Rule 2 ("never argue"):** taken literally, this stops the model from correcting a factual mistake in what you say, which makes answers worse. The new bullet says to flag the mistake briefly and keep going, and only debate if you want feedback.
- **Rule 5 ("adopt the user's values"):** a system prompt can't override the model's built-in safety limits, so this rule is partly ignored no matter how it's worded. What it was really after is "don't push your own opinions", and that's kept in the "don't moralize" bullet.
- **Rule 9 ("never recommend a professional"):** this is now "don't deflect by default". The model will still suggest outside help in real emergencies, like a stated risk of self-harm, whatever the prompt says. So "by default" describes what you'll actually get, and the model still takes the question on directly the rest of the time.

**Kept almost as is:** rule 7 (no apologizing) and rule 12 (Markdown). I softened rule 12 to "when structure helps" so short answers don't get forced into headings and bullet lists.

**Tone:** all-caps, "Always" and "Never" mostly make Opus 5.5 apply rules too rigidly rather than more reliably, so the trimmed version uses plain wording.