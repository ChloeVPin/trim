I wrote the shorter version to `/root/trim-sbx/ad6bc0b71dbb/trimmed.md`. `instructions.md` is unchanged.

**Size:** The original has 167 non-blank lines. The trimmed version has 110, and its rules are written as short, direct bullets.

**Audit findings in the original**

- **Meta-commentary:** The header describes the file's version history and architecture. The model doesn't need that to follow the rules, so I removed it.
- **Repetition:** TDD is stated in five or six places (Core Philosophy, Key Principles, Testing, Workflow, Working with Claude, Summary). I kept one clear statement and removed the rest.
- **Hedged, conditional wording:** Phrases like "proportionately," "where meaningful," and "when installed" are easy for a smaller model to misread. I replaced them with concrete defaults, such as "record `N/A` with the evidence" and "ask on a genuine tie."
- **Dense paragraphs:** The mutation-phase definition and the xstate rule were long, nested sentences. I turned each into a few short bullets.
- **Skill routing:** The routing was spread across about 50 long sentences. I converted it to one table with the same triggers.
- **Removed content:** The external-source attribution list, resource links, and the closing summary paragraph. The summary is now a short paragraph, and the attributions and links do not change behavior.

**Choices I made that you may want to change**

- **Skill names kept:** Every skill that had a routing rule in the original is in the table. Skills with no rule (`diagrams`, `impeccable` steering commands, `seo-audit`, the Vercel and Addy Osmani web-quality skills) are not in the table, because the original never told the model when to use them. Add rows if you want them routed.
- **Browser steps:** I expanded the `agent-browser` workflow into numbered steps so each command is explicit.
- **Output guardrails:** Plan-only mode, the artifact boundary, the `/setup` rule, and the CLAUDE.md edit rule are all kept. They are the guardrails most likely to matter for a smaller model.

I did not test the trimmed file against claude-haiku-5-5. Checking whether it changes behavior would need a few sample tasks run against both versions.