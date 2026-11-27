I saved the proposed version to `/root/trim-sbx/1bb942a73968/trimmed.md`. `instructions.md` is unchanged. You asked for the file directly, so I wrote it without waiting for approval. Nothing has been run through the skill's evals.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. Haiku needs more explicit direction than the larger models, so I cut generic advice and repeated emphasis, not procedures.

**2. Words:** about 3,000 before and about 420 after, roughly 85% shorter. These are estimates, since I had no word-count tool.

**3. Changes**
- **Removed the "quantum / consciousness / constitutional" framing**, the ten-phase list, the sequential-thinking framework, the advanced cognitive techniques, and the communication examples. This is generic advice, which the Haiku profile says to cut.
- **Merged about six near-identical "keep going until solved" lines** into one. I kept the stop-early guard, since the profile recommends it for agents that stop early.
- **Removed "cannot be solved without extensive internet research" and the must-search-Google framing.** The profile names blanket search instructions as a cause of unnecessary searching. The library check stays, with the same trigger: every time you install or implement a library, framework or dependency.
- **Removed "think thoroughly, long thinking is fine," "avoid repetition," and "NUMBER ONE failure mode."** These are thoroughness pushes and emphasis.
- **Testing rule shortened** to "run existing tests and test the change yourself before reporting done." The profile says to keep this for coding agents.
- **Todo format kept** as a short pinned example, with the check-off and display rules.

**4. Kept, and why**
- **Frontmatter unchanged.** The loader may parse it.
- **Resume / continue rule.** It is a procedure with specific steps.
- **Google and Bing search URLs.** The model cannot know them.
- **The 2000-line read size and the `get_errors` tool name.** These are specific facts.

**5. Decisions for you**
- **Link following:** "recursively fetch all links" is now "links when relevant." This is my judgment call. Restore the original if you want exhaustive crawling, which is the main source of extra searching.
- **`sequential_thinking`:** the original says both "must use for every problem" and "if available." I kept "if available" to resolve the conflict. If the tool is always present, restore "must."
- **Tool availability:** `fetch_webpage`, `sequential_thinking` and `get_errors` are named. If the agent does not have these tools, remove the lines.
- **Description field:** "unrestricted creative freedom" is marketing copy, and I left it alone. You may want to change it.