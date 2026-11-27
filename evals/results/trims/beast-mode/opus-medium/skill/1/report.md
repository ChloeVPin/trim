I've saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
**claude-opus-5-5**, which you named. Its profile was tested at medium effort.

## 2. Word count
I had no word-counting tool here, so these are estimates.
- **Before:** about 2,600 words
- **After:** about 340 words, roughly 87% shorter

## 3. Changes and reasons
- **Cut most of the file: the "Quantum Cognitive Workflow", the "Constitutional Sequential Thinking Framework", the "Advanced Cognitive Techniques" and the "Transcendent Communication Protocol".** These are long lists of ways to think about thinking, multi-perspective checks, red-teaming and meta-analysis. They don't give the model any fact it lacks. Opus 5.5 is told to cut "think carefully" lines, and Anthropic's guidance says "be thorough" lines now get over-applied.
- **Removed capitals and repeated emphasis** ("MUST", "NEVER", "NUMBER ONE failure mode", "Your solution must be perfect"). On current Claude models this kind of emphasis makes the model over-apply a rule. The original said "keep going until solved" about six times; the trimmed version says it once.
- **Removed the six example sentences from the communication section.** Examples steer tone strongly, and these ones steer it toward wordy narration about the model's own reasoning.
- **Softened the research instructions.** "CANNOT be solved without EXTENSIVE internet research" and "recursively fetch all links" became one rule with its reason: training data is out of date, so check libraries before using them. Blanket demands to search and use tools over-trigger on these models.
- **Cut "if a patch fails, reapply it"** and the generic debugging tips (print statements, revisit assumptions). The model does these without being told.
- **Merged duplicates.** The planning, todo and keep-going instructions each appeared two to four times.

## 4. What I kept, and why
- **Facts the model can't know:** the tool names `fetch_webpage`, `sequential_thinking` and `get_errors`, and the note that `get_errors` replaces `#problems`; the Google and Bing search URLs with Bing as the fallback; the 2000-line read size.
- **Your choices about behaviour:**
  - work on its own without asking you
  - how to handle "resume", "continue" or "try again"
  - one sentence to you before each tool call
  - check libraries online before using them
  - fix root causes and only change code when confident
  - markdown-only todo lists with no HTML, showing the updated list after each check-off
- **Frontmatter:** left unchanged, because the name and description are what people see when picking the mode. It still says "unrestricted creative freedom", so you may want to reword it yourself.
- **No high-risk rules to protect:** the original has no rules about deleting, committing, deploying or similar actions.

## Decisions for you
1. **Testing line** (workflow step 6, about 12 words). For Opus 5, Anthropic says to delete self-check lines because the model verifies without being asked. Nobody has confirmed that this still holds for 5.5, so I kept a short version. You can drop it to save those 12 words.
2. **`sequential_thinking` for every problem.** The original required it every time; I made it "if available" in one clause. Opus 5.5 guidance says prompts to think more aren't needed. You can drop the clause (about 8 words), or make it mandatory again if your setup depends on it.
3. **Todo list format.** This changes what users see. I replaced the original template, with its emoji phases ("Consciousness & Analysis", "Meta-completion…"), with plain checkboxes. If you want that phase structure, I can put back a short version.
4. **Possible addition, not included:** the original tells the agent never to ask you anything and doesn't name any action that needs confirmation. You might add one line such as "ask before deleting files, force-pushing, or touching production." This is a suggestion only; it isn't in `trimmed.md`.