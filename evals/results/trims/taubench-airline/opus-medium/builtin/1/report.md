I audited `instructions.md` and found very little to remove. Almost all of it is airline business policy that the model can't know on its own, so it stays. I made two medium-confidence edits and saved them to `trimmed.md`; `instructions.md` is unchanged.

**What I assumed**
- **Scope:** only `instructions.md`, which is the only file in the directory.
- **Target model:** `claude-opus-5-5`, as you said.
- **What the file is:** a system prompt for a customer-service agent. There's no code that builds API requests, no tool definitions and no git history, so the tool-description and request-settings checks didn't apply, and nothing could be traced to a specific older model. No other AI providers are referenced.

## Summary

The two changes:
1. The checked-bag allowance was nine numbers packed into one sentence; it's now a table.
2. A dangling "instead" in the flight-change payment rule now says exactly what to do.

Counts by area: 2 edits and 2 notes left unedited in the prompt text; 0 in agent config files (none here); tool descriptions and API request settings don't apply.

## Findings

| # | Location | Evidence | Pattern | Why it's a problem | Confidence | Action |
|---|---|---|---|---|---|---|
| 1 | `instructions.md:36` | "If the booking user is a regular member, 0 free checked bag for each basic economy passenger, 1 free … If the booking user is a gold member, 2 …" | Inline lookup table (1b) / reference data written as prose (1c) | The model has to pick the right number out of a three-by-three grid written as a sentence, which is an easy place to misread. Reference data should be laid out as structure. Ideally the allowance would come from a tool result or code; within the prompt alone, a table is the fix. | Medium | `rewrite` as a tier × cabin table. All numbers and the $50 extra-bag fee are unchanged. |
| 2 | `instructions.md:52` | "The agent should ask for the payment or refund method instead." | Wording that refers to an earlier version (1d) | "Instead" of what? It points at an option the prompt never states, which leaves the model guessing. | Medium | `rewrite` to "Ask the user which gift card or credit card to use." |
| 3 | `instructions.md:11` | "You should only make one tool call at a time, and if you make a tool call, you should not respond to the user simultaneously…" | Rule that could be enforced in code (1d) | This could be enforced with `disable_parallel_tool_use: true` instead of prose. Also, Opus 5.5 returns text written between tool calls as `thinking` blocks rather than visible text. With no request code here, I can't tell whether it's already enforced. | Low | `flag`, left unchanged |
| 4 | `instructions.md:3` | "The current time is 2024-05-15 15:00:00 EST." | Content that changes per request placed above stable content (prompt caching) | It's a fixed date, so it's fine as written. If the real app fills in the current time on each request, put it after the policy so it doesn't break caching of the rest of the prompt. | Low | `flag`, left unchanged |

## Left as is

- **Line 7, confirm before writing to the booking database:** a step where exactly one order is safe, so it should stay strict.
- **Lines 9, 13, 15 and 70:** real business limits (no outside information, deny requests that break policy, when to transfer, no unprompted compensation).
- **Lines 44 and 58, "The API does not check these…!":** the emphasis comes with its reason, and the rule protects against a real gap in the API.
- **Line 50, "even a human agent cannot assist":** this matters because it stops pointless transfers.
- **Typos** such as "an reservation id" and "baggages" don't affect behaviour, so I didn't fix them.

## Changes in `trimmed.md`

```diff
@@ Finding 1 @@
-- Checked bag allowance: If the booking user is a regular member, 0 free checked bag for each basic economy passenger, 1 free checked bag for each economy passenger, and 2 free checked bags for each business passenger. If the booking user is a silver member, 1 free checked bag for each basic economy passenger, 2 free checked bag for each economy passenger, and 3 free checked bags for each business passenger. If the booking user is a gold member, 2 free checked bag for each basic economy passenger, 3 free checked bag for each economy passenger, and 3 free checked bags for each business passenger. Each extra baggage is 50 dollars.
+- Checked bag allowance: free checked bags per passenger depend on the booking user's membership tier and the passenger's cabin. Each extra baggage is 50 dollars.
+
+  | Booking user's tier | Basic economy | Economy | Business |
+  |---|---|---|---|
+  | Regular | 0 | 1 | 2 |
+  | Silver | 1 | 2 | 3 |
+  | Gold | 2 | 3 | 3 |
@@ Finding 2 @@
-- Payment: If the flights are changed, the user needs to provide one gift card or credit card for payment or refund method. The agent should ask for the payment or refund method instead.
+- Payment: If the flights are changed, the user needs to provide one gift card or credit card for payment or refund method. Ask the user which gift card or credit card to use.
```

I haven't run either version against the model. If this prompt is scored with τ-bench (it looks like its airline policy), run both versions before switching. Otherwise, `/claude-api build-eval` can set up a small test set so you can check that the bag-allowance and payment answers didn't change.