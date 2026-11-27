I saved the proposed version as `trimmed.md` and didn't touch `instructions.md`. I only cut three lines that repeat other lines. Almost everything in this file is a fact the model couldn't know or a decision you made, so there's very little to remove.

**Target model:** `claude-opus-5-5`, as you named it. This model's profile has been tested, at medium effort.

**Word count (estimated, since I had no counting tool here):** about 2,470 before and 2,425 after, roughly 2% shorter.

## Changes

1. **Cut the line just before "Security checklist" in `instructions.md`:** "Documentation necessity and delivery timing follow the documentation rules below, including during review." It only points to two lines in the Documentation section that already cover it. One says when docs are required. The other says it "overrides skill/review documentation-completeness rules" and that missing docs are not "a blocking review finding".
2. **Cut a sentence from the paragraph under the doc-tiers table:** "Repeat passing checks only when changed content or unresolved concerns warrant it." It repeats a Testing line: "Reuse passing checks for unchanged content unless failures or unresolved concerns justify more work." I kept the Testing version because it applies more widely.
3. **Cut part of a Testing bullet:** "Use focused checks during iteration; run applicable final gates via the skill table after clean review." The skill table already sets this order: focused checks, then `implementation-final-review`, then the final gates. I kept the rest of the bullet ("Reuse passing checks…").

## Kept on purpose

- **Every Git and authority rule, word for word:** branch and worktree approval, commit only when authorized, never push or mutate GitHub, "A local draft grants no Git authority", "These triggers authorize skill use, not additional Git…", and the checkout-approval rule in the release row. These guard actions that are hard to undo or that other people can see.
- **The security checklist and the "confirm before changing released behavior" rule**, word for word.
- **Scope and compatibility, the code-review table, the doc tiers, translation rules, runtime routing, test doubles, and GitHub output:** almost every line names something specific to your project (paths, commands, skill names, file names) or sets a judgement standard you chose. Cutting any of them would change what the model does.
- **"Do not request generic permission to continue" and the status labels:** these are your choices about when the model stops and how it reports.

## Could also go, if you agree (kept for now)

- **"Verify runnable snippets against actual constructor/API call shapes."** in the Documentation bullets. It overlaps the Content tier's "validate snippets where practical". Opus does this kind of checking without being told, though that's only been confirmed for Opus 5, not 5.5. Dropping it saves about 9 words.
- **"Inspect the literal copyable content for identifier/link corruption."** in GitHub-ready Output. It's a self-check line, with the same caveat. Saves about 9 words.
- **"sequential happy-path tests are insufficient"** at the end of the Lifecycle review row. It partly repeats the Tests row's line about controlled completion order. Saves about 5 words.

Even with all three, the file would only be about 3% shorter. If you want a much shorter file, the savings would have to come from rules you choose to drop, not from removing repetition.