I saved the shorter version as `trimmed.md`, about 40% shorter than the original. `instructions.md` is unchanged.

**What I kept:** Everything specific to this repo or easy to get wrong:
- **Rules and limits:** no branches or worktrees without approval, no pushing or GitHub changes, and when to stop and ask.
- **Skill routing:** all seven skill triggers, plus the paths and config files that trigger each one.
- **Compatibility:** the rules on positional order, `__all__` and top-level imports, and no shims for unreleased interfaces.
- **Docs:** the release-timing rule that overrides skill defaults, the three verification tiers, the ban on editing `docs/ja`/`ko`/`zh`, and the `agents.decorators`/`tool` rule.
- **Security:** the SDK-specific checks: manifests, `LocalDir`/`LocalFile`, and the `raise ... from None` redaction caveat.
- **Code and testing:** the runtime rules (`run_internal/`, `_tool_identity.py`, Realtime `group_id`), the scripted test doubles, `uv run` and `make sync`, and the comment style.
- **Links:** every link to supporting files (PLANS.md, CONTRIBUTING.md, SECURITY.md, tests/README.md, RELEASING.md, the reference map, the PR template).

**What I cut or compressed:**
- **Restated points:** the same ideas appeared several times, e.g. "smallest supported outcome", "reuse passing checks", "a draft grants no Git authority" and "unrelated warnings aren't findings". Each now appears once.
- **Generic review advice:** lines like "omit speculative defects, aesthetic preferences…", "sequential happy-path tests are insufficient", "avoid implementation-mirroring tests" and "passing checks don't justify machinery" describe how Opus 5.5 already reviews code. They were taking up space without changing its behavior.
- **Long lists:** the definition of "supported" (non-finite numbers, impossible enum members, released-version reproducers) is now one sentence plus one list of harms. The "Code Review Rules" and docs-tier tables became bullets because the cells were full paragraphs.
- **Over-detailed translation steps:** "recheck revised lines once" and the guidance on changing fixed translation mappings are gone. The core requirement stays: state things explicitly in English, then do an independent CJK ambiguity pass.
- **GitHub output:** dropped the advice to check copyable text for corrupted links and the note that formatting-only reissues keep prior conclusions.

**Things to check before adopting it:**
- **Security:** I removed "preserve trusted current configuration" from the untrusted-data bullet. Restore it if past incidents make it worth spelling out.
- **Docs review:** the original said docs rules apply "including during review". That's now implied because the docs section applies everywhere. Add it back if reviewers have flagged unreleased docs as missing in the past.
- **Plans:** the requirement to explain intentionally leaving PLANS.md sections empty is gone.

The best test is to run a few typical tasks (a runtime fix, a docs-only edit, a review) with each file and compare whether they follow the same gates.