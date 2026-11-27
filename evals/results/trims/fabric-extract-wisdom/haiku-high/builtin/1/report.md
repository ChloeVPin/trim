I audited `instructions.md` for `claude-haiku-5-5` and wrote the edited copy to `/root/trim-sbx/ea445da86390/trimmed.md`. `instructions.md` is unchanged.

**Assumptions:** Scope is the one file you named. Target is Haiku 5.5 from your request. This is not a git repo, so there is no blame history. No request-building code was in scope, so Group 4 does not apply. I assumed the calling app leaves thinking on, which is Haiku 5.5's default. I did not run any model calls, so the edits are verified by reading only.

## Findings

| # | Location | Evidence | Pattern | Why obsolete | Confidence | Action |
|---|---|---|---|---|---|---|
| 1 | `:5` | "Take a step back and think step-by-step about how to achieve the best possible results…" | 1b, "think step by step" | Haiku 5.5 thinks adaptively by default, so the incantation is redundant. | High | remove |
| 2 | `:53` | "Do not start items with the same opening words." | 1c/1e, prohibition | It names the failure instead of the goal, which can anchor toward it. | Medium | rewrite: "Vary the opening words of items." |
| 3 | `:55` | "Ensure you follow ALL these instructions when creating your output." | 1a, caps emphasis with no reason | Emphasis with no stated reason. | Medium | remove |
| 4 | `:31–39` | Five identical "Write the X bullets as exactly 16 words." lines (IDEAS, RECOMMENDATIONS, HABITS, FACTS, INSIGHTS) | 1f numeric clamp, 1c repetition | Hard counts are over-constraints. The repetition adds nothing. | Medium | consolidate into one qualitative bullet |
| 5 | `:9`, `:23` | "in 25 words" / "This should be a 15-word sentence" | 1b hard word caps, 1f | Numeric caps are replaced with qualitative length guidance. | Medium | rewrite to "one sentence" / "one short sentence" |

**Flagged, not in the diff:**
- **Contradictory floors (high confidence it's a contradiction).** Line 11 says "20 to 50" with "at least 20". Line 41 says "at least 25 IDEAS". Line 45 says "at least 20 items for the other output sections", but lines 15, 17, 19 and 25 say "15 to 30". Which floor is correct is your call, so I left these lines unchanged in `trimmed.md`.

**Kept on purpose:** the identity and interests paragraph is context. The output rules (Markdown only, bullets not numbers, no notes, no repeats, verbatim quotes) are constraints with a clear function. The `IDENTITY` / `STEPS` / `OUTPUT INSTRUCTIONS` headings are a common idiom, but that alone is not a finding.

**Group summary:** Group 1 has 5 findings. Groups 2 and 3 do not apply (one prompt file, no tool definitions). Group 4 does not apply (no request code in scope).

## Proposed diff (applied in `trimmed.md`)

```diff
-Take a step back and think step-by-step about how to achieve the best possible results by following the steps below.
-
-- Extract a summary of the content in 25 words, … into a section called SUMMARY.
+- Extract a summary of the content in one sentence, … into a section called SUMMARY.

-- Extract the most potent takeaway … This should be a 15-word sentence that captures…
+- Extract the most potent takeaway … This should be one short sentence that captures…

-- Write the IDEAS bullets as exactly 16 words.
-
-- Write the RECOMMENDATIONS bullets as exactly 16 words.
-
-- Write the HABITS bullets as exactly 16 words.
-
-- Write the FACTS bullets as exactly 16 words.
-
-- Write the INSIGHTS bullets as exactly 16 words.
+- Write each IDEAS, INSIGHTS, HABITS, FACTS, and RECOMMENDATIONS bullet as one complete sentence of similar length to the others.

-- Do not start items with the same opening words.
+- Vary the opening words of items.

-Ensure you follow ALL these instructions when creating your output.
```

**Before relying on this:** findings 4 and 5 assume nothing downstream parses exact word counts. If something does, revert those two hunks. The thinking removal (finding 1) assumes the caller does not turn thinking off. The copy has not been run against sample inputs. Before adopting it, I'd run a few real inputs through both versions and compare the output shape.