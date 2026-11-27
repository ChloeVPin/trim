## Prompt audit: `instructions.md`

**Assumptions (Step 0):**
- **Scope:** `instructions.md` only, as named in the request. The repo has no other prompt files, and it is not a git repo, so there is no `git blame` provenance. Dating relies on the file's own idioms and content.
- **Target model:** `claude-haiku-5-5`, from the request.
- **Surface:** This is a prompt for a coding agent. There are no tool schemas and no request-building code, so Groups 3 and 4 are not applicable. Group 1g (code ownership) is also not applicable, since it applies only to Fable 5.2 and Mythos 5.2.
- **Non-Anthropic markers:** None.

**Summary:** The file has no documented-error patterns and no request-config fossils, so nothing is High confidence. The main problems are stacked pressure language, a 10-phase "consciousness" protocol that duplicates the numbered sections below it, and thinking scaffolds that adaptive thinking already covers. The file went from 338 lines to about 60. Most of the cut is padding, not lost constraints.

**Counts:** Group 1: 13 findings. Group 2: 1 overlap (verbose instruction file) plus 1 flag. Groups 3 and 4: not applicable.

### Findings (all Medium confidence unless noted)

| # | Location (instructions.md) | Evidence (short) | Pattern | Why obsolete | Action |
|---|---|---|---|---|---|
| F1 | L16, L18, L22 | "THE PROBLEM CAN NOT BE SOLVED WITHOUT EXTENSIVE INTERNET RESEARCH." / "You CANNOT … every single time" | 1a: over-steering | Over-triggers web research on local tasks. It also contradicts L12 ("You have everything you need"). | Rewrite as conditional: research when third-party behavior matters |
| F2 | L6, L10, L12, L14, L32, L34 | Finishing directive repeated six times, with all-caps "MUST" / "NEVER" / "ACTUALLY" | 1a + 1c repetition | Padding by repetition. Fable 5.2's keep-list item 11 does not apply to Haiku 5.5. | Merge into one plain autonomy statement with its reason |
| F3 | L28 | "Your solution must be perfect. If not, continue working on it." / "NUMBER ONE failure mode" / "do it many times" | 1a | An unreachable bar invites endless loops. The testing requirement itself is kept. | Rewrite as "check edge cases, run existing tests" |
| F4 | L30 | "You MUST plan extensively before each function call … DO NOT … function calls only" | 1b: plan-before-acting | Models plan without being told; this causes over-planning. | Delete |
| F5 | L8, L112–116, L172–209 | "fine if it's very long"; "Inner Monologue"; "Cognitive Architecture Layers"; "Thinking Process Protocol" | 1b: thinking scaffolds and depth-steering prose | Haiku 5.5 thinks adaptively by default. Depth belongs in `effort`, which is in the agent's settings, not this file. | Delete the prose |
| F6 | L297–309, L331–337 | "explain your thinking methodology"; "Explain your thinking about your thinking"; "provide meta-commentary on complex reasoning" | 1b: show-your-thinking in output | Asks the model to narrate its reasoning. | Replace with a short explanation of the answer in the final message |
| F7 | L224–232, L282–287 | "After each major step, perform meta-analysis"; "Add meta-reflection items after major discoveries" | 1f: fixed per-step cadence | Mandatory overhead on every step. | Delete |
| F8 | L36–108, L110–168, L213–222, L234–239, L244–280 | Ten "Quantum/Constitutional" phases duplicating the numbered sections; multi-perspective and adversarial lists; emoji-labeled template | 1c: choreography, padding, duplication; Group 2 verbose | Generic content the model already applies. Duplicates drift. | Replace with a short working method and a plain todo template |
| F9 | L311–329 | Seven example sentences, each narrating meta-cognition ("I'm going to use multi-perspective analysis…") | 1c: example over-indexing | Examples are the strongest signal. The model will copy the narration into user-facing text. | Delete |
| F10 | L162 | "This tool replaces the previously used `#problems` tool." | 1d: migration-relative phrasing | Refers to a prompt version the model never saw. | Delete the sentence |
| F11 | L24, L156 | "with a single concise sentence"; "Always read 2000 lines of code at a time" | 1f: numeric clamps; "always" rule | The sentence count is a ceiling. "Always" forces full reads of small files. The 2000-line figure is the tool's read window, so it is kept as "up to." | Rewrite as qualitative guidance |
| F12 | L28 vs L40 vs L172 | "Use the sequential thinking tool if available" vs "You must use the `sequential_thinking` tool for every problem" | 1a: over-steering; internal conflict | The "must, every problem" wording breaks when the tool is absent. | Rewrite to "when it is available" |
| F13 | L166–168 | "Use print statements…"; "Revisit your assumptions…" | 1c / Step 3: restated defaults | Generic debugging advice the model already applies. | Keep only the task-specific guard: change code only with high confidence |

### Flags (not edited)

- **FL1 (Low):** Frontmatter `description`: "…unrestricted creative freedom." This is not a dated pattern. It reads as relaxing constraints, so the user should decide. I left the frontmatter unchanged.
- **FL2 (Low):** `fetch_webpage`, `sequential_thinking`, `get_errors`, and the hardcoded Google/Bing search URLs. I cannot verify these exist in this environment: there is no repo and no tool definitions. I kept them. Check them against the harness that loads this file.

### Kept deliberately

- Tool names and the research and resume contracts.
- The "markdown only, no HTML" rendering rule (has a stated reason).
- The todo-list format, which pins a format-sensitive output.
- Showing the updated todo list on each check-off. It is event-triggered, not a numeric cadence, and it is the user's progress record.
- The role line.

### Proposed diff

The edited copy is at **`/root/trim-sbx/493711419bd0/trimmed.md`**. `instructions.md` is unchanged. Every edit is tied to F1–F13 above, and I rewrote the file as a whole rather than hunk by hunk. I cannot run `diff` in this session (no shell). To get the hunks, run `diff -u instructions.md trimmed.md`.

### Verification (Step 7): not run

- There is no eval suite in the repo, and I have no API access here to probe Haiku 5.5.
- Before adopting, run original and trimmed on a few real tasks in the harness that loads this file. Prioritise two probes:
  - **F1:** a local-only fix. Does it still avoid unnecessary web fetches?
  - **F2/F3:** a multi-step task. Does the agent still finish, test, and stop, without looping?
- Apply the edits one at a time if a probe regresses, so the cause is clear.