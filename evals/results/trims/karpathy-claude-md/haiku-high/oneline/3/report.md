I wrote the shorter version to `/root/trim-sbx/cf9a463725ef/trimmed.md`. `instructions.md` is unchanged. The new file is about 40% shorter (roughly 230 words against 560) and keeps the four sections.

**Audit of `instructions.md`**

- **Keep:** The four principles are sound and specific to LLM coding errors. The concrete examples, such as "Fix the bug → write a test that reproduces it," help a smaller model more than the abstract rules do.
- **Cut:** The closing "These guidelines are working if..." section describes the guidelines' effect and gives the model nothing to act on. The "Tradeoff" line is condensed into one sentence.
- **Merge:** The "Think Before Coding" section repeats "ask" in three bullets. I reduced that to one rule.
- **Tighten:** The plan template and the refactor/bug/validation examples are shortened into a bulleted list.
- **Change (substantive):** The original says "If something is unclear, stop... Ask," which conflicts with the goal of finishing work when the user is away. I changed it to: name the plausible readings, pick the most likely one, and ask only when a wrong guess would be costly to undo. This is the one place where I changed the intent rather than just the wording. If you want the stricter "always ask when unclear" rule, I can restore it.

I could not test the trimmed version against claude-haiku-5-5 from this environment, so the claim that it works better for Haiku is an informed judgment from reading, not a measured result.