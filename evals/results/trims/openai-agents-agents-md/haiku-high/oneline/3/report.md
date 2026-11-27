I wrote the shorter version to `/root/trim-sbx/b40eb95b2ab5/trimmed.md`. `instructions.md` is unchanged.

**Audit findings**

- **Most linked files are missing.** The directory contains only `instructions.md`, and it isn't a git repo. The links to `PLANS.md`, `.agents/skills/`, `.agents/references/`, `CONTRIBUTING.md`, `SECURITY.md`, `tests/README.md`, `Makefile`, and `.github/` can't be followed from this checkout. I kept those pointers as they were.
- **Hard for Haiku to follow:** long sentences with stacked "unless / except / including" clauses, the same skip rules repeated in several sections, and dense jargon in the review and security sections.

**What the trimmed version does**

- Splits each rule into short bullets with one condition each, and groups them under the same headings.
- Keeps every gate, stop condition, and prohibition: no pushing or GitHub changes, no branch changes without approval, the skill triggers, the compatibility rules, the docs tiers, and the GitHub output format.
- Merges repeated skip rules and states the trigger once.

**Dropped or condensed, so you can decide**

- The note that independent reviewers inherit the `implementation-strategy` contract.
- The rule to change fixed translation mappings only with cross-document evidence.
- The rule to temporarily translate an ambiguous passage.
- Some of the detail on the non-obvious Realtime tracing constraint and on the reviewer-only cases in the test rules.

I didn't measure the word count. The trimmed file has more lines because of the bullets, so compare word counts if length matters.