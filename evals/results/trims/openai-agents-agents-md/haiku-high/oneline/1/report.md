I wrote the shorter version to `/root/trim-sbx/75a6b4352cfc/trimmed.md`. `instructions.md` is unchanged. It is roughly half the length of the original, but I could not count exactly because Bash is disabled in this session.

## Audit of instructions.md

**Problems for a smaller model**
- **Dense rules.** Some bullets stack several exceptions, such as the compatibility-validation rule (line 27) and the lifecycle review rule (line 39). Haiku is more likely to misapply these, so I split them into short, one-rule bullets.
- **Mixed concerns.** Repo-specific SDK mechanics (Realtime tracing, sandbox paths, OpenAI facts) sit alongside general workflow rules. I kept them, grouped under their own headings.
- **Conflicting stop rules.** Line 6 says not to ask for generic permission to continue, while line 28 says to confirm before changing released behavior. Both are valid, but a smaller model may stop too often or too rarely. The trimmed version lists the stop conditions explicitly.
- **Duplication.** The docs timing rules repeat across the Documentation and skill-routing sections. The security checklist is partly restated in two places. I merged these.
- **Unclear wording.** "Codex URIs/directives" is a leftover from another tool. "Formatting-only reissues preserve prior reviewed commits" is hard to act on. I rewrote both in plain terms.

**Dangling references.** This checkout contains only `instructions.md`. These links resolve to nothing here: `PLANS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.github/RELEASING.md`, the PR template, `.agents/references/`, `.agents/skills/`, `tests/README.md`, and `Makefile`. I kept the links in `trimmed.md`, since they are routing pointers. I could not check whether the skills or references say what this file assumes.

## What I kept
- Every hard rule: no branch or worktree creation without approval, no commits without authorization, no GitHub mutation, and `uv run` for Python.
- The skill routing triggers, as a table.
- The compatibility, security, and docs-verification gates, in condensed form.
- The GitHub output and comment-style rules.

## Choices to check
- I did not add new rules or attribution lines. The session's commit and PR attribution comes from the system reminder, not from this file.
- The stop conditions are my reading of lines 6 and 28. Confirm that reading.
- The file is repo-meta guidance. Line 18 says decision-making guidance changes need realistic scenario checks and an independent pass before adoption. I have not run those, so treat `trimmed.md` as a proposal until they are done.