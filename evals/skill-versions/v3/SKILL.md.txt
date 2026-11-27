---
name: trim
description: "Proposes a shorter version of instructions someone has given an AI (custom instructions, a project or system prompt, a rules file such as CLAUDE.md or AGENTS.md, an installed skill), fitted to one named model. Use when asked to trim, shorten or clean up such instructions, or to re-check them after changing models. Not for writing new instructions."
license: MIT
metadata:
  version: "0.3.0"
---

# Trim

Propose a shorter version of someone's instructions for one model. The author decides: change nothing until they approve, and what they ask for in the conversation outranks this skill.

## 1. Fix the target model

How much to cut depends on the model that will read the instructions, which may not be the model running this skill. Take the model the person names. If they name none and the instructions are for the assistant you are running in, take the model ID your system prompt states and say you assumed it. Otherwise ask which model and wait, because a guessed model makes every later call unreliable.

Then read `references/profiles.md`.

## 2. Sort each instruction

Ask of each line: would the target model act differently without it?

- **No**: it repeats another line, states what the model does unprompted, or is something the profile says this model no longer needs. Cut it.
- **Yes**: it carries a fact the model cannot know (a name, path, command, number, date, format) or a choice the author made. Keep it.
- **Unsure**: keep it and flag it, with how much shorter the text gets if the author agrees to drop it.

Rules guarding work that is fragile or cannot be undone (deleting, sending, paying, publishing, committing, production, approvals, policy or legal limits) stay exactly as written whatever the answer, with their conditions and exceptions. A wrong cut there costs far more than the words saved.

## 3. Report

1. Target model, and whether it was named, assumed, or has no profile.
2. Words before and after. Count with a tool if you have one; otherwise say the figures are estimates.
3. Each change, with its reason.
4. What you kept and why.
