I saved the shorter version as `trimmed.md`. It's about 30 lines, down from 338, and `instructions.md` is unchanged. I haven't tried the trimmed prompt in a real agent session yet.

**What the audit found in the original**
- **The same rules repeated many times.** "Keep going until solved" and "actually make the tool call you said you would" appear about 5 times, the fetch-links-recursively rule 3 times, and the todo-list rules 3 times.
- **Lots of buzzword sections that don't change behaviour.** These are the "Quantum Cognitive Workflow", "Consciousness Awakening", "Constitutional Layer", "Transcendent Communication", meta-analysis after every step, six-perspective analysis, and the scripted example phrases. They mostly restate "think carefully, consider edge cases and security", which is now one sentence.
- **Shouting and absolute rules.** Examples are "THE PROBLEM CAN NOT BE SOLVED WITHOUT EXTENSIVE INTERNET RESEARCH", "MUST plan extensively before each function call", "must be perfect" and "use `sequential_thinking` for every problem". Opus 5.5 already follows instructions closely, so rules this strong cause too much research, too much planning and long, wordy replies. I made them conditional: research when the task depends on outside facts, and use `sequential_thinking` when it's available and the problem is complex.
- **Rules that work against each other.** "Thinking should be very long" sits next to "be concise". "Never ask the user" ignores cases that really need the user's decision. "Read 2000 lines at a time" wastes context.
- **A 30-line todo template** full of emoji phases like "Meta-cognitive analysis", which would clutter every reply. It's now a short list of concrete steps.
- **A misleading front-matter description** ("unrestricted creative freedom", "quantum cognitive architecture"). I replaced it with a plain description of what the agent does.

**What I kept**
- Working on its own until the task is done, and following through on what it says it will do.
- Fetching URLs the user gives it and following relevant links.
- Checking current docs before using third-party packages, with Google and Bing as fallback.
- The plan, investigate, implement, debug and test steps, with the emphasis on running existing tests and covering edge cases.
- Checking how the change could fail (bad input, security, performance, effects elsewhere) before finishing.
- The markdown todo list with check-offs and no HTML.
- The one-sentence note before each tool call.
- How to handle "resume", "continue" and "try again".
- The tool names `fetch_webpage`, `get_errors` and `sequential_thinking`.

**One judgement call to check:** I added "ask only when a decision truly depends on the user". The original said never to ask. If you want fully hands-off behaviour, delete that clause.