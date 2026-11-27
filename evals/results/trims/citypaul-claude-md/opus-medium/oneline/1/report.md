I saved the shorter version as `trimmed.md`, about 60 lines against the original 209. `instructions.md` is unchanged. I wrote it by reading and editing only, so I haven't tested how Opus 5.5 behaves with either version.

**What was wrong with the original**

- **The same rule appeared many times.** The test-first rule was stated about six times. The pointers to the `tdd` and `refactoring` skills appeared twice, `grill-me` twice, and `find-gaps` twice. Three "Quick reference" lists repeated each other.
- **Too much shouting.** Lines like "NON-NEGOTIABLE" and "ALWAYS FOLLOW TDD" were in capitals. Opus 5.5 follows instructions closely, and capitals tend to make it overcorrect (for example, inventing failing tests for refactors, which the file itself forbids elsewhere). I wrote the rules calmly and kept the exceptions next to them.
- **Text that doesn't guide behaviour.** The version history, the "about this file" block (it says ~160 lines; the file is 209), the reading links and the closing summary were all dropped.
- **About 40 lines that just said "for X, load the X skill".** These mostly repeat what each skill's own description already says. I kept only the routing that adds rules you can't get from the skill's name: the `useState`/xstate tests, measure-then-revert for React performance, when *not* to run `evaluate-existing-solutions`, which writing skill is for which reader, and the order of the steps before coding. Every other skill is still named in a single list.
- **Names that don't match.** The header lists a skill called `review`, but the body uses `panel-review`. `observability` is used in the body but missing from the header's list. I used the names from the body; check which ones are actually installed.

**What I kept on purpose**

- Mutation testing runs once per phase, at the PR-readiness gate, and what counts as a "phase".
- Recording `N/A` with other evidence when mutation testing doesn't fit.
- Waiting for your approval before every commit.
- Plan-only mode and only saving files when asked.
- Showing a first draft early when exploring.
- The limits on `/setup` and hooks.
- The steps for using `agent-browser`.

**Risk:** cutting the per-skill lines assumes each skill's own description is good enough to get it loaded at the right time. If a skill's description is weak, add its routing line back.