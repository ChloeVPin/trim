I saved the proposed version as `trimmed.md`, about half the length of the original. `instructions.md` is unchanged. I didn't check whether the files and skills it links to actually exist.

**What I found in the audit**

- **Instructions Opus 5.5 already follows.** A lot of the text tells the model things it does without being told: "Do not request generic permission to continue", "omit speculative defects, aesthetic preferences", "avoid implementation-mirroring", "Repeat passing checks only when…", "Inspect the literal copyable content for corruption". I cut these or folded them into nearby rules.
- **Long lists that repeat one idea.** Some lines are a list of 6–10 near-synonyms, such as "abstractions, options, state, validation, fallbacks, dependencies, or test permutations". I shortened each to a few representative items, since the model will generalize from those.
- **Rules stated twice.** The checkout-approval rule shows up in the workflow section and again in the release-skill row. Several skill rows also say what the skill "owns" (command order, retries, classification). The skill files already cover that.
- **Code review section.** The original is a dense two-column table of long sentences, so I rewrote it as five bullets. The rules themselves are unchanged: review against the merge base, each finding needs a trigger and a concrete consequence, trace changed values end to end, check lifecycle interleavings, and test at the caller-visible boundary.
- **Documentation tiers.** The table had a lot of conditional wording, so I turned it into three short bullets.
- **Fine-grained process detail.** I cut a few items that small: re-checking revised lines once, the rules for changing fixed translation mappings, and formatting-only reissues of GitHub text.

**What I kept as written**

These are things the model can't infer, so they stay word for word or nearly so:
- All paths, commands, and skill names.
- The Git and GitHub authority limits.
- The positional-parameter, `__all__`, and import side-effect rules.
- The rule that unreleased docs go in separate PRs.
- The rule against editing generated localized pages.
- The `agents.decorators` and `tool` import guidance.
- The `run.py` / `run_internal` split and `_tool_identity.py`.
- The Realtime tracing note.
- The scripted test utilities.
- The redaction note about `raise ... from None`.
- The rules for formatting GitHub references.

**Things you may want to put back**

- The full list of reasons that justify duplicating validation. I kept a short version.
- The detailed contract-coverage path list in the code review section.
- The translation-mapping guidance, if your team often runs into that problem.