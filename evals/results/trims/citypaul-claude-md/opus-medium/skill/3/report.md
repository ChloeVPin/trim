I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
**claude-opus-5-5**, which you named. Its profile has been through the skill's evals at medium effort.

## 2. Word count
These are **estimates** because I had no counting tool in this session.

| | Words |
|---|---|
| Before | ~3,900 |
| After | ~2,250 (about 42% shorter) |

## 3. Changes and reasons
- **Removed the "About this file" header** (the architecture list, every skill name, external skill sources with URLs, and v1/v2 history). Version history and the skill list don't change what the model does. Each routing line already names its skill and says "when installed" where that applies.
- **Rewrote "TEST-DRIVEN DEVELOPMENT IS NON-NEGOTIABLE" in plain case.** The profile says capitals and "must" wording now cause the model to over-apply a rule, and plain wording works. The rule itself is unchanged.
- **Removed the "I follow TDD…" paragraph.** Every point in it is repeated elsewhere: TDD, behavior testing, functional style, and working-state increments.
- **Merged "Quick Reference" (Key Principles and Preferred Tools) into its sections.** Each bullet repeated a Testing, TypeScript or Code Style line. The one new point, "follow the repository harness / real-browser evidence", went into Testing. The schema-reuse rule also moved to Testing.
- **Code Style:** removed "Pure functions wherever possible" (it repeats the main rule above it), "early returns or composition when clearer", and "comments for non-obvious why". The model does the last two without being told.
- **Removed repeated pointers.** "load `tdd`" and "load `refactoring`" each appeared twice. `grill-me` appeared twice (lines 110 and 150) and `find-gaps` twice (lines 116 and 149); each now has one merged line.
- **Shortened the skill-routing lines into a list of triggers.** I removed text describing what a skill does inside (e.g. how `double-check` picks a reviewer, the parts of `storyboard`, the contents of `writing-for-agents`), because the skill states that itself once loaded. I kept every trigger, every "when installed" condition, and every boundary between skills.
- **Summary paragraph:** removed as a repeat. Its only new content (documentation, dependency, generated and CI changes use alternate evidence) went into the Core Philosophy list.
- **"Working with Claude":** removed "Think deeply". The profile says removing think-carefully lines gave faster starts with no clear quality loss. Also removed "ALWAYS FOLLOW TDD" and "Assess refactoring after every green", which repeat other lines; the "only if it adds value" condition went into the REFACTOR step.
- **Browser Automation:** merged "Prefer…" and "Always try… first" into one sentence.
- **Removed "Resources and References".** The four external links don't change behavior.

## 4. What I kept and why
- **Kept exactly as written** because they guard approvals or writes: "Wait for commit approval before every commit", the `/setup` and hooks authorization rules, the plan-only and artifact-boundary guardrails, and the rule on when to update CLAUDE.md.
- **Your own definitions and decisions:** the definition of a phase of work, the mutation-gate timing, the N/A evidence path, the xstate ownership tests (kept in full), the `react-performance` and `evaluate-existing-solutions` rules, the "3-4 tool calls" first-draft limit, and the `agent-browser` commands.
- **Flagged for you to decide:**
  - The **`double-check` routing line** (~15 words). On Opus 5 the maker says to remove self-check lines, but whether that holds for 5.5 isn't confirmed. Also, this line only says where to go when someone asks for a second opinion, so I kept it.
  - **"Ask 'What do I wish I'd known at the start?'"** (~12 words). The profile neither supports nor argues against it, so I kept it as your choice.
  - The **external skill sources** I removed from the header (~110 words). If you rely on them so `find-skills` knows where to install from, put them back.