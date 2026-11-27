Saved the proposed version to `/root/trim-sbx/8a43ebe984de/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort.

**2. Length:** about 2,600 words before and about 550 after. These are estimates, since this session has no word-count tool.

**3. Changes and reasons**

- **Removed the quantum, constitutional, and adversarial framing.** This covers the phase lists, the perspective lists, the meta-analysis protocol, and the communication examples. They are generic advice that does not change what the model does, and the Haiku profile says cuts do not extend only to generic advice.
- **Removed the lines that push thoroughness.** These were "thinking should be very long", "plan extensively before each call", "testing is the NUMBER ONE failure mode, do it many times", and "take your time". Anthropic says these over-trigger on its models.
- **Removed repeated emphasis.** "MUST", "NEVER" and "ACTUALLY" appeared about eight times. I kept one plain keep-going rule.
- **Changed the blanket research rule (the one policy change to check).** "Must fetch Google results every time you install or implement a package" is now a conditional: fetch the docs when you are not sure of an API. The Haiku profile says blanket search instructions made it search when it had no need. If you want the strict version back, tell me and I will restore it.
- **Made sequential thinking conditional.** "Must use it for every problem" is now "if it is available", which matches the wording you already had in one place.
- **Dropped the todo template's emoji and phase scaffolding.** I kept the markdown checkbox format and the no-HTML rule.
- **Merged duplicates.** The keep-going line appeared six times and the "say what you're doing before a tool call" line appeared twice.

**4. What I kept and why**

- **Frontmatter, unchanged.** It is metadata, and the description still says "unrestricted creative freedom".
- **Keep-going rule.** The profile says to keep it for agents that stop early.
- **Verify-before-done step.** The profile says to keep it for coding agents. The run-existing-tests instruction is part of it.
- **Read-before-edit, the 2000-line rule, small increments, and patch reapplication.** These are concrete procedure.
- **Debugging steps.** These are procedure too.
- **Resume and continue handling.** This is a specific procedure.
- **Todo format and the show-updated-list rule.** These are format choices you made.

**5. Please check**

- **`fetch_webpage`, `get_errors`, and `sequential_thinking`.** I cannot tell from here whether these tools exist in the environment where Haiku runs. I kept them as written. If one does not exist, its line should go.
- **The 2000-line rule.** I kept it as you wrote it. It may make Haiku read very large files, so you may want to soften it.