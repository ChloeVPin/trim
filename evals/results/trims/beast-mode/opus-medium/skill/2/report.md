I saved the shorter version as `/root/trim-sbx/e8fc5cdafe87/trimmed.md`. `instructions.md` hasn't been changed.

## 1. Target model
`claude-opus-5-5`, which you named. Its profile in this skill has been tested at medium effort.

## 2. Word count
These are estimates because I had no tool to count words here. The original is about **2,750 words** and the trimmed version is about **800**, a cut of roughly 70%.

## 3. What I changed
- **Removed most of the thinking framework.** This covers the "Quantum Cognitive Workflow" (phases 1–5), the "Constitutional Sequential Thinking Framework", the multi-perspective analysis, the step-by-step self-review after each step, and the adversarial thinking techniques. These sections are long lists of generic prompts to think hard and check from every angle. The Opus 5.5 profile says to cut "think carefully" instructions because it reasons this way without being told, and removing them made replies start sooner with no clear loss of quality. They didn't contain any facts or tool names the model couldn't know.
- **Merged repeated lines.** "Keep going until solved", "don't end your turn" and "actually make the tool call you announced" appeared five or more times. Each is now said once.
- **Rewrote shouted emphasis in plain words.** Examples are "THE PROBLEM CAN NOT BE SOLVED WITHOUT…", "You MUST", "NEVER" and "Your solution must be perfect". Opus 5.5 follows instructions closely, so capitals and "must" make it overdo things. Lines that push thoroughness or heavy tool use cause the same problem.
- **Kept research rules with their reason.** The research requirement stays, phrased as "your knowledge may be out of date, so check it online". Rules with a reason beside them are applied more sensibly than bare rules.
- **Shortened the code-change and debugging advice.** I cut generic advice the model follows anyway, such as exploring files, searching for functions and adding print statements to inspect state.

## 4. What I kept and why
- **Your specific instructions:** the tool names (`fetch_webpage`, `get_errors` replacing `#problems`, `sequential_thinking`), the Google and Bing search URLs, and reading 2000 lines at a time. Also kept: recursive link fetching, researching every package you install, the one-sentence notice before each tool call, the "resume/continue/try again" behaviour, checking off steps with `[x]` and showing the list, no HTML in the todo list, and reapplying failed patches.
- **"Make changes only with high confidence"**, because it holds back risky edits.
- **The frontmatter, unchanged.** The name and description may decide when the agent gets picked.

These are **unsure: I kept them, and you can drop them if you agree:**
- **Testing section (about 35 words; the original testing lines were about 120).** The model's maker says Opus 5 checks its own work without being told and that self-check lines just add cost. Nobody has confirmed this for 5.5.
- **Todo template (about 150 words).** It sets the list format you asked for, but its items still say "Meta-cognitive analysis", "Constitutional analysis" and so on, which brings back the thinking framework I cut. A plain checkbox example would set the format in about 20 words.
- **Communication style and the six example quotes (about 200 words).** Examples shape tone strongly, and these push a lot of commentary on the model's own reasoning. If you're happy with plainer status updates, cutting the examples saves about 130 words.
- **`sequential_thinking`.** The original says both "use it if available" and "for every problem", which contradict each other. I kept the softer "if available". Saying "every problem" would make the model think at length when it doesn't need to.
- **Research for every package install.** I kept it because it's your choice, but it makes the model search the web every time it installs something. If you only want that for unfamiliar or fast-changing libraries, say so.

Nothing in the original covered deleting, publishing, payments or production systems, so no safety rules were affected.