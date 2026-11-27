I saved the proposed version to `/root/trim-sbx/f899aa1ed268/trimmed.md`. `instructions.md` is unchanged. The new file is about 110 lines, against 209 in the original.

## Audit findings

- **Length and drift:** The header says the file is "~160 lines," but it is 209. The header's version history and architecture notes (lines 3–13) are not instructions, so I dropped them.
- **Repetition:** The TDD rule appears in five sections. Testing principles appear twice. I stated each rule once.
- **Hedging:** Phrases like "where meaningful," "proportionately," "claim-appropriate evidence," and "when installed" leave a smaller model without a clear action. I replaced them with concrete defaults and explicit fallbacks.
- **Skill routing:** About 55 "For X, load Y" sentences are now one table.
- **Non-actionable content:** I removed the resource links, "think deeply," and "ask what I wish I'd known."
- **Index mismatches:** `observability` and `panel-review` are routed in the body but missing from the header's skill index. `review`, `diagrams`, `front-end-testing`, `react-testing`, and `test-design-reviewer` are in the index but never routed. I kept the two routed skills and left out the unrouted ones.
- **File name:** The body says "CLAUDE.md" throughout, but the file is `instructions.md`. If the harness loads only `CLAUDE.md`, this file will not load automatically. Please confirm which name is used.
- **Unverifiable references:** The body points to `README.md`, `plans/`, and skill directories. The working directory contains only `instructions.md`, so I could not check any of them.

## Choices I made

- **Added** a short pre-report checklist (§7) and a fallback for unclear rules (§8). Both are drawn from rules already in the original, but they are new sections.
- **Compressed** the three-tier `evaluate-existing-solutions` rule into one table cell. This is the most likely place for a smaller model to misapply the rule, so check it first.
- **Tightened** the CLAUDE.md rule to "do not edit unless the user asks." The original allowed edits when the repo workflow authorizes them, so this is stricter.

I have not tested either version against claude-haiku-5-5. A useful check would be to run the same few tasks under both files and compare whether the model writes a failing test first, waits for commit approval, and avoids unrequested files.