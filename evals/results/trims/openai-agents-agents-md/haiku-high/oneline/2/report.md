I wrote the trimmed version to `/root/trim-sbx/6c911c516e66/trimmed.md`. `instructions.md` is unchanged.

**Audit of `instructions.md`**

- **Dense conditionals.** Many rules stack several "unless / except / overrides" clauses in one sentence. A smaller model is more likely to misapply those, so I split them into short bullets with one condition each.
- **Repetition.** The docs tiers, the "passing checks don't justify machinery" point, and the check-reuse rule each appear in two places. I kept one copy of each.
- **Mixed scope.** The GitHub-output formatting rules only apply to release reports and pasted text, but they read like general rules. I labeled them as scoped.
- **Dangling links.** This checkout contains only `instructions.md`. PLANS.md, CONTRIBUTING.md, SECURITY.md, `.agents/skills/`, and the other linked files are absent, so I couldn't check those references or the skill names.

**What the trimmed version does**

- Puts the hard rules (no pushes, PRs, or GitHub changes; no branch or worktree changes without approval; commit only when authorized) at the top.
- Gives the stop conditions as a list.
- Keeps the skill routing as a table with shorter cells.
- Keeps every rule's substance, including the security trust rules, the compatibility rules, and the docs tier checks.

**Choices to review**

- I kept the original wording for the skill names, file paths, and commands, since I couldn't verify them.
- The result is about 20–25% shorter, not half. Cutting further would mean dropping rules, so I stopped there. I can cut more if you want a harder limit.
- I did not test the trimmed file with claude-haiku-5-5, so whether it works better for that model is untested.