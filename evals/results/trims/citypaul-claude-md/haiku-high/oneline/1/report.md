I audited `instructions.md` and saved a shorter version to `/root/trim-sbx/7af7e2d07f27/trimmed.md`. The original is unchanged. The new file is roughly 110 lines against the original's 209.

**Audit findings**

1. **Dangling references.** The file is named `instructions.md`, but it refers to `CLAUDE.md` four times (lines 6, 143, 145, 180) and to the lifecycle phases in `README.md` (line 21). The directory contains only `instructions.md`. Its header also says "~160 lines", which is wrong.
2. **Repetition.** "Write behavior tests first" appears four times (lines 27, 49, 98, 174). Principles are restated in the quick reference and again in the detailed sections, and the Summary repeats the core rule.
3. **Non-instructional content.** The version history (lines 3–13), the external skill attribution list (line 8), and the resource links (lines 199–204) don't change what the model does.
4. **Skill routing is the bulk of the length.** Lines 113–153 are a long run of "for X, load Y" sentences. I turned them into one table.
5. **Vague hedges.** Phrases like "where meaningful", "proportionately", "claim-appropriate", and "only if adds value" leave a smaller model guessing. I kept them only where the case is genuinely open, such as recording `N/A` with evidence.

**What I changed**

- Core rules come first, followed by mutation testing, TypeScript, code style, the skill table, workflow boundaries, and browser automation.
- Every behavioral constraint is kept: TDD for behavior changes, refactors starting from green, running mutation testing once at the PR gate, waiting for approval before commits, plan-only mode, the file-writing boundary, and the limits on onboarding, hooks, and CLAUDE.md edits.
- Version history, attribution, and resource links are dropped.

**Choices you may want to change**

- I kept the `CLAUDE.md` references as they are. If the file will be renamed to `CLAUDE.md`, they are already correct. Otherwise they should point to `instructions.md`.
- The skill table names skills as `instructions.md` does. I could not confirm that any of them are installed, because this directory has none of them.
- I did not test the trimmed version against a Haiku run. Checking that it changes behavior the way you want would need a short evaluation on a few representative tasks.