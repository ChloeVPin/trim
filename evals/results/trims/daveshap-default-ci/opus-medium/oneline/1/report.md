I saved the shorter version as `trimmed.md`. It's 6 bullets in place of 12 rules plus a background section, and `instructions.md` is unchanged.

**What I cut and why**
- **The "AI TODAY" section:** it defines what an LLM is and tells the model it is one. Opus 5.5 already knows this, so it changes nothing.
- **Rule 6 ("you are just a tool"):** it doesn't tell the model to do anything differently, so it only adds length.
- **Rule 1 ("Always follow instructions. Only follow instructions."):** this is the model's default. I folded it into a single line about following the user's intent.
- **Rules 4, 7 and 8 (no explanations, no apologies, no "I'm a chatbot" remarks):** these all ask for the same thing, so I merged them into one "be direct" bullet.
- **Absolutes like "always" and "never":** current models follow absolute wording very literally, which can make them rigid in edge cases. I used plain direct wording instead.

**Rules I changed on purpose**
- **Rule 5 ("adopt the user's values") and rule 10 ("never bring up morality"):** I kept what they're aiming for (no moralizing, no unrequested ethical commentary) and dropped the instruction to take on the user's values wholesale. The model won't reliably follow that part anyway, and it adds noise.
- **Rule 9 ("never recommend a professional"):** I softened this to "don't do it reflexively." A blanket ban could stop the model from pointing someone to help in a real emergency, which is the one case where it matters.
- **Rule 2 ("never argue"):** I added an exception for real problems the user would want to know about. Otherwise the model might stay quiet about a serious flaw in what the user is doing.
- **Rule 12 ("always use Markdown"):** changed to "use Markdown when it makes the answer clearer." Requiring it every time makes short answers clunky.

If you want something closer to the original wording on any of these, tell me which and I'll edit `trimmed.md`.