I saved the shorter version as `trimmed.md`. It's about 25 lines, down from 66, and every rule from the original is still in it. `instructions.md` is unchanged.

**What I found in `instructions.md`:**
- **It was already fairly tight.** Most of the savings come from removing repetition, not from dropping rules.
- **Text written for people, not the model:** the opening "Behavioral guidelines…" line, the closing "These guidelines are working if…" line, and the "Strong success criteria let you loop independently" explanation. None of these tells the model to do anything, so I removed them.
- **Repeated rules:**
  - "Before coding" had four bullets that all said some version of "say your assumptions and ask when unclear". I combined them into one.
  - "Don't remove pre-existing dead code unless asked" repeated the earlier "mention it, don't delete it". I merged the two.
  - The "senior engineer" self-check made the same point as "200 lines → 50". I kept the 200→50 one because it's more concrete.
- **Bold one-line summaries under each heading:** they just restate the heading and bullets. A model like claude-opus-5-5 doesn't need the same point made three times, so I cut them.
- **The plan template code block:** a single sentence asking for a short plan with a check per step does the same job.

**What I kept, because a capable model wouldn't do these on its own:**
- Asking before choosing between plausible readings of a request.
- Mentioning dead code instead of deleting it.
- Cleaning up only code that your own change left unused.
- Writing tests first for bug fixes and validation.
- Matching the existing code style.

One thing to consider: the original tells the model to ask whenever it's uncertain. If you mostly run Claude without someone watching, you may want to soften that to "make a reasonable assumption, state it, and continue" so it doesn't stall waiting for answers. I left it as written because that's how the original reads.