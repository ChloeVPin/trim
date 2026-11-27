I've written the proposed version to `/root/trim-sbx/605d8f638e5c/trimmed.md`. `instructions.md` is unchanged.

1. **Target model:** `claude-haiku-5-5`, named by you. Its profile was tested at high effort. The profile says Haiku needs more explicit steps than the larger models, so I cut wording and duplication, not procedures or triggers.

2. **Size:** about 3,900 words before and about 2,700 after, roughly 30% shorter. These are estimates because I have no word-count tool here.

3. **Changes and reasons**
   - **Caps and emphasis removed** ("NON-NEGOTIABLE", "ALWAYS", "MINIMUM"). The rules stay, in plain wording. The profile says capitals make Claude models over-apply rules. This is the change most likely to alter strictness, so say if you want one rule kept in bold.
   - **TDD restated six times, cut to one core statement** plus the workflow steps. The same applied to the "Core principle" summaries and the Quick Reference blocks that repeated their sections.
   - **Header cut to a skill list.** I removed the "About this file" block, the architecture and version history (its "~160 lines" claim was already stale), and the "Agents" line, which names nothing actionable.
   - **External skill URLs and author credits removed.** The skill names stay.
   - **"Think deeply"** removed as generic advice.
   - **Resources list** removed. These are links the model already knows.
   - **Summary section** removed. Its one unique line, about claim-appropriate evidence for non-behavior changes, moved into Core Philosophy.

4. **Kept as written or nearly so:** the commit-approval rule, the artifact-boundary and plan-only rules, the CLAUDE.md write limit, the `/setup` and hook authorization conditions, the ask-the-human points, the xstate "ask rather than guess on a genuine tie" rule, the `evaluate-existing-solutions` conditions, the mutation `N/A` conditions, the browser fallback order, the 3–4 tool-call draft limit, and the reflection question. Every skill name and trigger in the routing lines is kept.

5. **Unsure, for you to decide**
   - The header skill list (about 130 words) could go if the harness already lists installed skills. That saves about 200 words with the external list.
   - Two skills are in the list but have no routing line: `test-design-reviewer` and `front-end-testing`. Others are the same: `react-testing`, `diagrams`, `review`, and the external skills. Add triggers if the model should load them on purpose.
   - `observability` and `panel-review` are routed below but missing from the original header list. I did not add them to the list. Tell me if you want them there.

6. **Suggested additions, not in the file** (the profile says to list additions rather than edit silently):
   - For a coding agent: "Before reporting a code change done, run the relevant tests or checks and report the results." The profile recommends this for Haiku.
   - If the agent stops early on long tasks: "Keep working until the task is done."