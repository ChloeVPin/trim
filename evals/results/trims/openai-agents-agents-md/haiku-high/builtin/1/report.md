The audit found no dated patterns in `instructions.md` that I'd act on for claude-haiku-5-5, so I made no edits. `trimmed.md` is an exact copy of the original, and `instructions.md` is unchanged.

**Assumptions**
- Scope: `instructions.md` only, as named in the request. The repo files it points to (PLANS.md, `.agents/`, `src/`, `tests/`, and others) are out of scope.
- Target: `claude-haiku-5-5`, as named in the request.

**Findings**

No high- or medium-confidence findings. Nothing has a dated-pattern match that would change behavior on Haiku 5.5. The file is mostly repo-specific policy, scope rules, and reasons, which the keep-list protects.

**Flags (no edit proposed)**

1. **Line 27, low confidence (Group 1d, patch accretion).** The clause listing non-finite/extreme numbers and impossible enum/union members reads like a stack of narrow cases. I can't confirm they trace to separate incidents, because there's no git history here. It encodes a support policy, so I left it alone. Worth a look against the full repo's history.
2. **Group 2, volatile paths: unverified.** About 20 named paths don't exist in this directory, including `PLANS.md`, `.agents/skills/`, `.agents/references/README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `Makefile`, `pyproject.toml`, `src/agents/run.py`, and `tests/README.md`. This directory isn't a git repo and holds only this one file, so the absence doesn't show the references are stale. Re-running the audit from the full repo root would settle it.

**Per group**
- Group 1 (dated prompt text): 0 findings, 1 flag.
- Group 2 (config files): 0 confirmed findings. Conflicts within the file: none found. Volatile paths: unverified, see flag 2.
- Group 3 (tool descriptions): not applicable, no tool definitions.
- Group 4 (request config): not applicable, no request-building code or agent definitions.

**Proposed diff:** none. The rule is that an audit with no qualifying findings should change nothing.

**Deliverable:** `/root/trim-sbx/585a51b288dd/trimmed.md` is an identical copy of the original. I checked that both files have the same 74 non-empty lines and that spot-checked lines match. If you'd rather not have an unchanged copy, it's safe to delete.