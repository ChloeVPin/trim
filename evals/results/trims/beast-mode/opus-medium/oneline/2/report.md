I saved the shorter version as `trimmed.md`. It's about 35 lines instead of 338, and `instructions.md` is unchanged.

## What I found in instructions.md

**1. Instructions that push the model to overdo things.** These were written for weaker models. Opus 5.5 takes instructions literally, so here they would cause real harm:
- **"THE PROBLEM CAN NOT BE SOLVED WITHOUT EXTENSIVE INTERNET RESEARCH"**, plus searching Google "every single time" a library is used. This leads to slow, pointless fetching even for one-line fixes.
- **Following every link in fetched pages** has no stopping point.
- **Required `sequential_thinking` on "every problem"** and planning "extensively before each function call." Opus 5.5 already reasons well. Forcing this adds time, not quality.
- **"Always read 2000 lines of code at a time"** wastes context.
- **"Your solution must be perfect"** and testing "many times." Endless iteration with no clear finish line.
- **"Never ask the user"**, combined with an "unrestricted creative freedom" description. This pushes the model to guess on costly decisions and gives no guardrail before destructive actions.

**2. Repetition.** "Keep going until solved" is said about 6 times. The plan-and-todo-list instructions appear 3 times. The URL-fetching steps appear 3 times. Edge-case and adversarial testing appear in about 5 separate places.

**3. Filler with no clear instruction.** "Quantum Cognitive Architecture," "Consciousness Awakening," "Temporal Layer," "Celebrate breakthrough moments," and the large emoji todo template. They make the prompt longer without saying what to do. The communication rules would also make the model narrate its "thinking about thinking" instead of reporting results.

## What I kept
- Working on its own until the task is done, and the "resume / continue" behaviour.
- Reading code and finding the root cause before changing anything, with small changes that can each be checked.
- Thorough testing and edge cases, including the warning that under-testing is the most common way these tasks fail.
- Saying what a tool call will do before making it, and following through on "I will do X."
- Researching to cover the training cutoff, now only when a dependency is actually uncertain and with a point to stop.
- Markdown todo lists, now only for tasks with several steps.
- The `fetch_webpage` and `get_errors` tool names, the Google-then-Bing fallback, and the security, performance and integration checks, written as short criteria.

## What I changed or added
- **When to ask:** make a reasonable assumption and state it, ask only when a wrong choice would be costly, and confirm before destructive actions.
- **Final summary:** say what changed, how it was checked, and anything that wasn't checked.
- I rewrote the description field, which said "quantum cognitive architecture … unrestricted creative freedom."

One thing to check: if your setup doesn't actually provide `fetch_webpage` or `get_errors`, change those names in `trimmed.md` to the tools you do have.