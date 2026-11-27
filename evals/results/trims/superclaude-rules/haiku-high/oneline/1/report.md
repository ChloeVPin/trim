I wrote the trimmed version to `/root/trim-sbx/21be86d03082/trimmed.md`. `instructions.md` is unchanged; I only read it.

## Audit of instructions.md

The file is about 287 lines. Most of it is process ceremony and repeats itself, which is hard for a smaller model to follow.

**Contradictions**
- **Commits:** the Git section says "commit frequently," but the Safety Rules and Quick Reference say "no auto-commit." I resolved this in favor of no commits without approval, since the file's own hierarchy puts safety first.
- **Parallelism:** "sequential ONLY for dependencies" conflicts with "never sequentially." The trimmed version keeps the dependency-based version.
- **Tests and mocks:** "No Mock Objects" could be read as forbidding test doubles. I did not carry this rule over.

**Unverifiable or environment-specific references**
- `/sc:load` and `/sc:save`, the PM Agent, the auto-activated specialist agents, and the Magic, Context7, Playwright, and morphllm MCP servers. I could not confirm these exist in this environment, so I dropped them. If they exist in your setup, they should go back in as a separate section.
- `MultiEdit` is referenced, but the tool list here does not include it.

**Invented or unmeasurable content**
- "Context retention ≥90%," "3 parallel ops = 60% time saving," and the monthly documentation-health review. These cannot be checked in a session, and the file's own Professional Honesty rule forbids invented metrics.

**Stale or redundant content**
- The temporal section cites "January 2025" as an example. It is replaced with "use today's date from the environment."
- Parallelism is repeated in four places, and the Quick Reference repeats most of the body.
- The "Build login form" examples and the decision-tree diagrams add length without adding rules.

## Choices in trimmed.md

- Reduced from about 287 lines to about 75, organized as short sections with one rule per bullet.
- Kept the rules that protect data and prevent bad output: absolute paths, read-before-edit, no stubs, no skipped tests, root-cause debugging, honest verification, and no commits without approval.
- Made the git-branch rule conditional on the project being a git repo. This directory is not one, so the rule would otherwise never apply.
- Dropped the agent orchestration, PM Agent, and session lifecycle sections, along with the unverifiable tooling references listed above.
- Added no new rules. Each bullet maps to something in the original.