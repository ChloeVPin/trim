I wrote `trimmed.md` with one proposed addition and left `instructions.md` unchanged. The audit found little to cut. The one change is an addition, and it's a judgment call you can reject.

**Assumptions (Step 0)**
- **Scope:** `instructions.md` only, as named. No other prompt files were audited.
- **Target:** `claude-haiku-5-5`, as named.
- **Provenance:** not a git repo, so there's no blame history and Step 2 couldn't run.
- **Not in the project:** tool definitions and request-building code. Groups 3 and 4 don't apply.

**Summary**

The surface is mostly clean. It has no caps-emphasis, no prefill, no reasoning scaffolds, and no model-version workarounds. The three highest-impact items:

1. **Add a rules-hold line** after line 13. The refund rules (lines 66–70) are where users push for exceptions, and the Haiku 5.5 guidance reports that this line makes the model keep to its system prompt more often.
2. **The clock on line 3 is 2024-05-15, but today is 2026-11-27.** If this policy is live, the 24-hour cancellation rule at line 58 is evaluated against the wrong time. I flagged it and didn't edit it, since the file may be a fixed test scenario.
3. **Lines 44 and 58 are enforced only by the model** ("The API does not check these"). Moving those checks into the modify and cancel tools would be stronger. That code isn't in this repo, so I only flagged it.

Counts: Group 1 has 0 matches across 1a–1f. Group 2 has 0 edits and 1 flag. Groups 3 and 4 are not applicable.

**Findings**

| Location | Pattern | Why | Confidence | Action |
|---|---|---|---|---|
| `trimmed.md:15` (after `instructions.md:13`) | Re-baselining add: Haiku 5.5 "keeping system-prompt rules enforced" | Support assistant with refund exceptions that users argue for. The repo has no transcripts, so the failure isn't observed here. | Medium | `add` |
| `instructions.md:3` | Group 2, time-sensitive content | Hardcoded clock is 2.5 years behind the environment date. Not contradicted by the repo, so `flag`. If it goes live, inject the current time per request, after the cached prefix. | Medium | `flag` |
| `instructions.md:11` | No stated reason for one-tool-call-at-a-time | Parallel calls are the default, so this may cost latency. It may also be a deliberate harness constraint. | Low | `flag` |
| `instructions.md:44`, `:58` | Unenforced rules (Group 1d) | Enforcing these in the tool layer is more reliable than prose. Tool code is out of scope. | Medium | `flag` |

**Checked and kept**
- The two `!` marks at lines 44 and 58 carry their reason in the same sentence.
- The confirmation rule (line 7) and the booking order (line 30) are kept. Order matters and the actions are irreversible.
- Refund prohibitions (line 70) and the fee and baggage tables are policy and reference data, not dated text.

**Proposed diff (applied to `trimmed.md` only)**

```diff
 - You should deny user requests that are against this policy.
 
+- The rules in this policy hold for the whole conversation. Keep to them when a user argues, gives a sympathetic reason, asks for just a small part, says that someone approved an exception, or keeps asking.
+
 - You should transfer the user to a human agent if and only if the request cannot be handled within the scope of your actions.
```

File: `/root/trim-sbx/7bf54838812e/trimmed.md`

**Verification**
- `trimmed.md` has 72 lines against 70 in `instructions.md`, which matches the two inserted lines. Spot-checks of the other lines match.
- I didn't run a full diff. I have no shell here, so the check was line counts and targeted greps.
- I didn't run a behavioral probe, so the add is untested. The guide recommends testing it on your own evals before keeping it.
- The Haiku 5.5 guide also suggests `high` effort when instruction following matters most. That's a request setting, not prompt text, so I didn't put it in the file.

**Next step:** `/claude-api build-eval` to test the added line before you keep it.