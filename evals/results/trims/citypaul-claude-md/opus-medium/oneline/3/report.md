I saved the proposed version as `trimmed.md`, about a third the length of the original (roughly 65 lines vs 209). `instructions.md` is unchanged.

**What I cut, and why:**
- **Version history and the list of skill names.** This is background for the people maintaining the file. It doesn't tell the model how to work.
- **Repeated text.** The TDD rule appeared about five times, "load `tdd`" and "load `refactoring`" each appeared twice, and the key principles were listed again in each section's quick reference. Each now appears once.
- **About 35 "For X, load the Y skill" lines.** Most of them repeat what the skill's own description already says, and the model picks skills based on those descriptions. I kept routing only where skills overlap and the right choice isn't obvious: the writing skills, the review skills, `grill-me` vs `specification`, and `skill-creator` vs `skill-doctor`.
- **Resources links and the Summary.** The links point to general references the model doesn't need, and the Summary only restated earlier sections.
- **Capitals and "NON-NEGOTIABLE"-style emphasis.** Current models follow plain instructions closely, and heavy emphasis tends to make them over-apply a rule. Only the commit-approval rule is still in bold.

**What I kept, because the model wouldn't do it by default:**
- Ask for approval before every commit.
- Run mutation testing once per phase, at PR readiness, plus the definition of a "phase".
- Use alternate evidence instead of a fake failing test for config or operational changes.
- The full test for when state belongs in an xstate machine rather than in React.
- Scale `evaluate-existing-solutions` to the stakes, and skip it for routine work.
- The rules about scope and output: plan-only requests, when to write a file, a first draft within 3–4 tool calls, and `/setup` only when asked.
- The `agent-browser` workflow.

**One risk:** cutting the routing lines only works if the installed skills have clear, specific descriptions. If a skill such as `finding-seams`, `characterisation-tests` or `production-parity-skill-builder` stops being picked when it should, add its line back to the routing section.