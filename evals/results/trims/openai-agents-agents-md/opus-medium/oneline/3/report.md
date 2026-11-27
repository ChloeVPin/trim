I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged. I didn't count words, but I'd estimate it's about 25–30% shorter. Every repository-specific rule, path, command and skill trigger is still there. The cuts are wording that repeated itself or spelled out what Opus 5.5 already does well.

**What I kept as-is:**
- **Hard limits:** never push, open PRs or change GitHub; switching branches or worktrees needs approval; commit only when authorized; no generic "may I continue?" check-ins.
- **Skill routing:** all seven triggers and the file paths they cover.
- **Compatibility rules:** positional order and `__all__`, no shims for unreleased interfaces, no side effects on top-level imports, and the "complexity reset" rule.
- **Security checks:** sandbox manifests, `LocalDir`/`LocalFile`/archives, exception redaction including `raise ... from None`.
- **Docs:** the release-timing rule, the three verification tiers, never editing `docs/ja`/`ko`/`zh`, and using `agents.decorators` with `tool`.
- **Runtime and testing:** the guidance on `run.py`, `run_internal/` and `_tool_identity.py`, the Realtime `group_id` note, the scripted test utilities, and `uv run`/`make sync`.

**What I trimmed:**
- **Code review:** the 5-row table is now 6 bullets. I dropped wording that repeated itself, like the long lists of "invariant" types and "report concrete leaks…" after the interleaving check. A strong model needs the rule and the trigger, not a list of every variation.
- **Scope:** I replaced the long list of things that don't count as "supported" (non-finite numbers, impossible enum members and so on) with the general rule. That's the trim most likely to lose something. If those specific cases come up a lot in reviews, I'd put that sentence back.
- **Translation review:** the two documentation bullets on translation are now one. "Prefer contextual guidance over rigid mapping tables" became "change fixed mappings only with cross-document evidence".
- **GitHub output:** I removed lines the model handles well without being told, like checking copyable text for broken identifiers and the note that formatting-only reissues don't count as a new review. I kept the fence-length rule, the reference format and the template path.
- **Small removals:** the PLANS.md "explain an intentional omission" clause, "do not repeat unchanged external research" (the testing section already says not to rerun passing checks), and a few "including during review" cross-references that only repeated other sections.

**Worth checking before you adopt it:**
- I removed the instruction to "keep required host annotations outside the block" in GitHub output, assuming it was specific to another tool. Put it back if your setup still adds those annotations.
- I cut the line about preserving coverage when optimizing test performance, because the linked `tests/README.md` section should already say that.