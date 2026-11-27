I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Words:** I had no tool that counts words, so these figures are estimates. The original is about 2,300 words and the trimmed version is about 36 words shorter, a cut of under 2%.

The cut is small because almost every line carries something the model can't know on its own: a path, a skill name, a command, a project convention, or a choice you made about compatibility or review. The profile's main cuts for Opus 5.5 don't apply here. There are no "think carefully" lines, no vague design direction and no emphatic capitals.

## Changes

1. **Cut the sentence after the Code Review table** ("Documentation necessity and delivery timing follow the documentation rules below, including during review."). It only points to another section. The Documentation section already says it "overrides skill/review documentation-completeness rules" and that a docs need isn't a blocking review finding. Opus follows the file as written, so the pointer changes nothing.
2. **Cut "Repeat passing checks only when changed content or unresolved concerns warrant it."** from the docs build paragraph. The Testing section already says to reuse passing checks unless failures or unresolved concerns justify more work, and that applies to every check.
3. **Shortened the second Testing bullet** by cutting "run applicable final gates via the skill table after clean review." This repeats the skill table: `implementation-final-review` comes after focused checks, and the final gates come after that.

## Kept as written
- **Every Git and GitHub authority rule:** branches and worktrees, commit only when authorized, never push or open a PR, "triggers authorize skill use, not additional Git or external actions", "a local draft grants no Git authority", and the checkout-approval reminder in the release row. These guard actions that can't be undone, so I left them exactly as written. That includes the release row's repeat of the checkout rule.
- **"Confirm the approach before changing released behavior…"** This is a user-facing approval step.
- **The security checklist and the "Do not commit generated localized files" rule:** these guard against data exposure and against changing published output.
- **The Code Review, Scope and Documentation tier rules:** each one sets a project-specific standard for what counts as a finding, what counts as support, or which check runs when. The model wouldn't apply these on its own.
- **The lines that limit work** ("do not repeat unchanged external research", "only its relevant supporting references", "recheck revised lines once"). The profile says Opus over-applies lines that push thoroughness, so these lines are worth keeping.

## Flagged: kept, but you could drop them
- **"Passing checks do not justify unsupported machinery."** (Readiness row, about 7 words.) The Scope section already lists what can justify new machinery, and passing checks isn't on that list.
- **"sequential happy-path tests are insufficient"** (Lifecycle row, about 5 words.) The Tests row already requires controlled completion order for concurrency regressions.
- **"Inspect the literal copyable content for identifier/link corruption."** (GitHub-ready Output, about 8 words.) This is a self-check line. The maker says to delete these on Opus 5 because the model checks its work unprompted, but nobody has confirmed that still holds on 5.5. Keep it if broken links in pasted output have caused trouble before.

Dropping all three would save about 20 more words.