I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged. I only cut two sentences, because almost every line in this file carries something Opus 5.5 can't know on its own.

**Target model:** `claude-opus-5-5`, as you named it. The skill has a profile for this model, tested at medium effort.

**Word count:** about 2,430 before and 2,400 after, saving about 30 words. These are estimates; I had no counting tool in this session.

## Changes

1. **Removed the line after the Code Review table:** "Documentation necessity and delivery timing follow the documentation rules below, including during review." It repeats something already covered: Documentation Release Timing says it "overrides skill/review documentation-completeness rules."
2. **Removed one sentence from the Documentation Verification Tiers section:** "Repeat passing checks only when changed content or unresolved concerns warrant it." Testing & Automated Checks states the same rule for all work: "Reuse passing checks for unchanged content unless failures or unresolved concerns justify more work." I kept that general version.

## Not cut, but flagged for you (about 35 more words if you drop all three)

- **"Inspect the literal copyable content for identifier/link corruption."** (GitHub-ready Output, about 9 words.) This is a self-check line. For Opus 5, Anthropic says to remove these because the model checks its own work anyway. Nobody has confirmed that this still holds for 5.5, so I left it in.
- **"Use focused checks during iteration; run applicable final gates via the skill table after clean review."** (Testing, about 16 words.) This mostly repeats the order already set in the skill table rows for `implementation-final-review` and `code-change-verification`.
- **"User instructions and approved scope take precedence over skill defaults."** (Skill routing, about 10 words.) Opus mostly behaves this way already, but the line also settles conflicts with skills, so you may want it.

## What I kept and why

- **Everything about git and GitHub, left word for word:** the branch and worktree approval rule, "commit only when authorized," "Never push, open a PR, or otherwise mutate GitHub," "A local draft grants no Git authority," and the release checkout rule. These guard actions that are hard to undo.
- **Security checklist, compatibility rules and the "confirm before changing released behavior" rule:** these are policy limits and user-facing contracts.
- **Skill routing table, review rules, documentation tiers, testing doubles, file paths, `make` and `uv` commands, the status labels and the GitHub output format:** these are project facts and choices you made, and the model can't infer them.
- **The "Continue authorized local work…" line:** the profile treats a "finish the whole task" instruction as useful.
- **The "Mandatory" heading and the uses of "never":** the wording is measured, not all-caps emphasis, so it shouldn't cause the over-application the profile warns about.

The file is already tight and specific to the project, so a small cut is the honest result here. If you want, I can apply any of the three flagged cuts to `trimmed.md`.