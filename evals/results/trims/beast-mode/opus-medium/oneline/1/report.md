I saved the shorter version as `trimmed.md`, about 35 lines down from 338. `instructions.md` is unchanged. I haven't tested `trimmed.md` against real tasks.

## What I cut and why

1. **Lots of repetition.** "Keep going until it's solved," "don't end your turn," and "actually make the tool call" each appeared four or five times. Saying it repeatedly, in capitals, doesn't help Opus 5.5 follow it, and pushes it to keep going when it should stop and ask. Each now appears once.
2. **The "quantum / constitutional / transcendent" sections.** Roughly 200 lines of layers, phases, perspectives and meta-analysis rules restated the same few ideas: understand the problem, find the root cause, plan, test edge cases, think about what could go wrong. I kept those ideas in plain words.
3. **Instructions that made it worse.**
   - **"The problem cannot be solved without extensive internet research"** plus a Google search every time a package is used meant lots of slow, unnecessary fetches. Research now happens only when the model isn't sure a library still works the way it remembers.
   - **"Follow every link recursively"** is now "follow links while they're still relevant."
   - **"Your solution must be perfect" and "test many times"** encourage over-engineering. The new version says to run existing tests and cover the edge cases the change touches.
   - **"Always read 2000 lines at a time"** wasted context, so it now says to read enough surrounding code.
   - **"Plan extensively before each function call"** slowed down simple steps. Opus 5.5 plans fine on its own.
4. **The nested todo template and the sample phrases.** The emoji-heavy template would be copied word for word into every todo list. The example sentences ("I'm integrating insights from…") pushed it toward filler like "celebrate breakthrough moments" and narrating its own thinking.
5. **"Can definitely solve this without asking the user."** This became "ask only when it's the user's call or you're blocked." Never asking at all isn't safe.

## What I kept

- Working autonomously
- Using `fetch_webpage` on URLs you provide, with the Google search and Bing fallback
- The plain-markdown todo list with `[x]` checkoffs
- One sentence before each tool call
- The "resume / continue / try again" behavior
- Using `get_errors`, finding root causes, and debugging with logs
- Testing being the most common way these tasks fail
- `sequential_thinking`, now for complex problems and only when the tool is available

I kept the `name` and rewrote the `description` to say plainly what the agent does. If something else depends on the old description text, change it back.