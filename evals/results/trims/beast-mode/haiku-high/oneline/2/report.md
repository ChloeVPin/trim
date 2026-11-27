I audited `instructions.md` and saved a shorter version to `/root/trim-sbx/b05081880434/trimmed.md`. `instructions.md` is unchanged.

**What I cut or changed, and why**

- **Persona and filler.** Terms like "quantum cognitive architecture," "consciousness awakening," "transcendent," and "constitutional" change nothing the agent does. I removed them along with the emoji headers.
- **Meta-cognition sections.** The "Constitutional Analysis," "Multi-Perspective," "Adversarial Thinking," and "Recursive Meta-Analysis" sections ask for commentary that doesn't improve code. A smaller model tends to spend effort performing these steps, so I dropped them and kept the practical checks: root cause, edge cases, and a diff review.
- **Repeated directives.** "Keep going until solved" and "do not end your turn" appeared about ten times in different wordings. I replaced them with one statement and a clear exception for when the agent is truly blocked.
- **Conditional research.** The original says the problem "can not be solved without extensive internet research" and requires fetching Google for every dependency. I made research conditional on unfamiliar libraries or uncertain behavior. This is the biggest behavior change, so check it against your intent.
- **Tool names.** The original names `fetch_webpage`, `sequential_thinking`, and `get_errors`. Those may not exist in the runtime the agent runs in, so I described the tool types generically ("a search tool," "a fetch tool if one is available").
- **Contradictions.** "Read 2000 lines at a time" conflicts with "read the relevant section." I replaced it with "read the relevant functions or files in full," which is practical and doesn't dump large files into context.
- **"Your solution must be perfect."** This is unachievable and can push a model into endless rework. I replaced it with concrete verification steps.
- **Frontmatter description.** The original, "unrestricted creative freedom," works against the careful behavior the rest of the file asks for, so I rewrote it. I kept `name` unchanged in case something references it. Revert either if they're used elsewhere.

**Kept:** the plan-as-checklist workflow, the step-by-step verification, the resume/continue behavior, and the plain-markdown rule for todo lists.

The result is roughly one-fifth the original length by my estimate. I didn't run a word count because I have no shell tool here.