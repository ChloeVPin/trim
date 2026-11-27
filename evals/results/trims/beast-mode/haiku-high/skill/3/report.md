I wrote the proposed version to `/root/trim-sbx/98162b73f3c2/trimmed.md`. `instructions.md` is unchanged.

1. **Target model:** `claude-haiku-5-5`, named in your request. The profile is tested at high effort, so the cuts are tuned for that setting.

2. **Length:** about 2,900 words before and about 600 after. These are estimates because I have only file tools here and no word counter.

3. **Changes and reasons:**
   - **Removed the "Quantum Cognitive Architecture" phases (Phases 1 to 5) and the 10-step list.** They are generic reasoning labels, and they repeat the detailed sections below them.
   - **Removed the "Constitutional" sequential-thinking layers, the multi-perspective framework, the recursive meta-analysis protocol, and the adversarial techniques list.** These are generic virtues and reflection prompts. The profile says to cut generic advice.
   - **Cut the communication section and its example phrases.** The examples would push the model to narrate its thinking in that style.
   - **Cut the repeated "keep going" and "do not stop" lines from about seven places down to one.** The profile says a single persistence line is what Haiku needs.
   - **Cut the emphasis: capitals, "MUST", "NUMBER ONE failure mode", "perfect", "many times".** The profile says emphasis now causes over-application.
   - **Cut "be thorough, it's fine if it's very long" and "think hard" and "debug as long as needed".** Thoroughness pushes over-trigger on the Anthropic models.
   - **Narrowed the blanket research rule.** It now applies "before you install or implement" a dependency, not on every question. The profile flags blanket search instructions for Haiku.
   - **Replaced the Phase 3 "think hard" line and the inner-monologue questions with a short plan step.**
   - **Shortened the todo template.** It keeps the markdown format and the no-HTML rule, and drops the constitutional items.

4. **Kept, and why:**
   - Tool names (`fetch_webpage`, `get_errors`, `sequential_thinking`). The model cannot know them.
   - The Google and Bing search URLs.
   - The 2000-line read size.
   - The `[x]` checkoff and the rule to show the updated todo list.
   - The resume, continue, and try-again procedure.
   - The "say what you will do before a tool call" line.
   - The real-check-before-done rule for code changes. The profile specifically says to keep this for coding agents.
   - One keep-going line for agents that stop early.
   - The todo template itself, because it pins a required format.

**Things to check:**
- **Frontmatter:** I left the description unchanged. "Transcendent" and "unrestricted creative freedom" may not be what you want the agent to be known by, so you may want to reword it.
- **Sequential thinking:** The original said "must use" in one place and "if available" in another. I used "if available," so tell me if you want it mandatory.
- **Tool availability:** If the target harness does not provide `fetch_webpage`, `get_errors`, or `sequential_thinking`, remove those references.