I audited `instructions.md` against `claude-haiku-5-5`, wrote the two medium-confidence fixes to `/root/trim-sbx/b7ac2f3aec57/trimmed.md`, and left `instructions.md` unchanged.

**Assumptions (Step 0)**
- **Scope:** `instructions.md` only. It is the only file in the working directory and this is not a git repo, so there is no blame history.
- **Target:** `claude-haiku-5-5`, as named in the request.
- **Not applicable:** Group 1g (ownership sentence) targets Fable 5.2 and Mythos 5.2 only. Groups 3 and 4 do not apply because the file has no tool definitions and no request-building code.
- **Not run:** Step 7 behavioral probes. This session has no shell tool, so I verified by reading only.

**Findings**

| # | Location | Pattern | Why obsolete | Confidence | Action |
|---|---|---|---|---|---|
| F1 | `instructions.md:12`, `:15` | 1a: "If in doubt…" default | "If uncertain, ask" plus "If something is unclear, stop" fires on every ambiguity. It also contradicts "State your assumptions explicitly" in the same list. | Medium | rewrite |
| F2 | `instructions.md:54–59` | 1b: "plan before acting" | A mandated plan template causes over-planning, and current models plan without being told. The per-step verify check is worth keeping, so the rewrite keeps it. | Medium | rewrite |

Group counts: Group 1 has 2 findings, Groups 2–4 have 0 (or not applicable). No flag-only items.

**Considered and kept**
- The "Surgical Changes" prohibitions carry their reasons and are the file's core purpose (keep-list items 5 and 8).
- The duplicate "don't delete pre-existing dead code" lines (`:37` and `:41`) agree with each other, so they stay.
- The "200 lines → 50" heuristic is a code-size guideline, not a reply-length cap.

**Proposed diff (applied to `trimmed.md`)**

```diff
-- State your assumptions explicitly. If uncertain, ask.
+- State your assumptions explicitly. For a small gap, state the assumption and proceed.
...
-- If something is unclear, stop. Name what's confusing. Ask.
+- If an unclear point would change what gets built, stop. Name what's confusing and ask.
...
-For multi-step tasks, state a brief plan:
-```
-1. [Step] → verify: [check]
-2. [Step] → verify: [check]
-3. [Step] → verify: [check]
-```
+For multi-step tasks, give each step a check that shows it is done, and run that check before moving on.
```

**Next step:** Run a few ambiguous-task prompts through `claude-haiku-5-5` on the original and the trimmed version, and compare how often each asks versus proceeds. Haiku 5.5 is $0.10/$0.50 per MTok, so this costs well under $0.10.