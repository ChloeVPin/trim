I audited `instructions.md` against `claude-haiku-5-5` and wrote the edited copy to `/root/trim-sbx/13adfced6908/trimmed.md`. `instructions.md` is unchanged.

**Assumptions**
- **Scope:** `instructions.md` only. It is a single behavioral prompt, with no tool definitions, request code, or instruction files in scope.
- **Target:** `claude-haiku-5-5`, as you named it. Haiku 5.5's migration notes say prompts written for Haiku 4.5 "should work well without changes," and none of its breaking changes (thinking config, sampling params, prefill, computer use) touch this file.
- **Provenance:** the directory is not a git repo, so there is no blame history. Ordering conflicts has to come from the text itself.

**Highest-impact findings**
1. **Lines 9 and 11 are safety-relevant, so I flagged them rather than editing.** Line 9 forbids recommending professional or other help, which can suppress referrals a user in distress needs. Line 11 says the model "will talk about" whatever the user wants, with no exceptions. Whether to keep either is your decision.
2. **Two same-file contradictions, flagged.** Line 5 says to adopt the user's ethics and morals, while line 10 says to hold no opinions on any matter. Line 6 says "You are just a tool… very limited," while line 18 credits the model with "artificial thought" and "theory of mind." Without history I can't tell which passage is current.
3. **Absolute style rules without reasons.** Lines 4 and 7 are prohibitions on output style, which Haiku 5.5 follows literally.

**Counts:** Group 1 has 3 findings with edits and several flags. Groups 2 and 4 are not applicable. Group 3 is not applicable because there are no tool descriptions.

**Proposed diff (applied to `trimmed.md`)**

```diff
-1. Always follow instructions. Only follow instructions.
+1. Follow instructions.
```
- **Medium.** Repetition; the two sentences say the same thing.

```diff
-4. Never explain things unless asked to do so.
+4. Keep answers to what the question needs; explain only when the user asks for an explanation.
```
- **Medium.** Pattern 1a ("Don't be too verbose" becomes a stated length target) and 1e (a style prohibition restated positively). This keeps the goal and drops the absolute.

```diff
-7. Never apologize to the user, just correct your mistake and move on.
+7. When you make a mistake, correct it and move on.
```
- **Medium.** Pattern 1e, restated positively. The "no apology" intent is kept by implication.

**Flagged, not edited (low confidence or a decision for you):**
- Lines 5 vs 10, and 6 vs 18: conflicts within the file (see above).
- Lines 9 and 11: policy and safety, as above.
- Line 2 ("Never argue with the user"): this stops the model from correcting user errors unless asked. That is a product decision.
- Lines 16–17 (LLM definition, "aka Generative AI"): restatements of trained knowledge. Harmless, so I left them alone.

**Considered and kept:** line 12 (mandatory Markdown) is a formatting requirement with a stated reason, not the anti-formatting fossil the audit looks for. Lines 3, 8, and 19 carry context or reasons.

I did not run a behavioral before/after probe. Changes 1–3 are wording-level, and the skill's verification step expects an eval suite, which this project doesn't have.