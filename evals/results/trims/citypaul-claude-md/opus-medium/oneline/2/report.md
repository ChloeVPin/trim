I've saved the proposed version as `trimmed.md`. It's about 65 lines against the original 209, roughly a quarter of the length. `instructions.md` is unchanged.

## What I found

1. **The same rules appear many times.** The TDD rule is stated about six times (Core Philosophy, Quick Reference, Testing, Workflow, Working with Claude, Summary). The `tdd` and `refactoring` pointers appear twice, and so does the `grill-me` fallback. Strict mode, immutability and the `any` rule each appear two or three times. Each rule now appears once.
2. **The header has notes for maintainers, not for the agent.** The version history, the "~160 lines" count, and the full list of skills and external skill sources don't change what the model does. The skill list also repeats the routing lines further down. I removed all of this.
3. **About 40 "For X, load skill Y" lines repeat what the skills already say.** Skills are matched to tasks by their own descriptions, so lines like "for hexagonal projects, load `hexagonal-architecture`" add little. I kept only the lines that carry actual rules or settle overlaps between skills:
   - the test for when state belongs in `xstate`
   - the order of steps for React performance work
   - when to skip `evaluate-existing-solutions`
   - which writing skill handles which audience
   - which skill handles authoring, grading or discovering skills
   - which review skill to use when
4. **The capitals and absolutes could make Opus 5.5 overdo things.** "NON-NEGOTIABLE", "ALWAYS" and "Think deeply" can push a strong model to force TDD onto config or docs changes, even though the file itself allows exceptions. I wrote the rule plainly and put the exceptions right next to it.
5. **Some sections do nothing.** The Resources links (the agent never follows them), the Summary (it restates the start of the file) and the "Preferred Tools" block (it repeats the TypeScript section) are all gone.

## What I kept on purpose

- Waiting for approval before every commit.
- Plan-only mode, and only writing files when asked or when the repo declares a home for them.
- A first draft within 3–4 tool calls.
- The definition of a "phase" and the timing of the mutation testing gate, because it's easy to get wrong.
- The `agent-browser` steps.
- The rules for when `/setup` and project hooks are allowed.

## Your call

Dropping the routing lines relies on each skill's description being good enough to trigger it alone. If some skills don't load reliably without a pointer, such as `finding-seams`, `characterisation-tests` or `bff-entry-points`, add back a one-line pointer just for those.