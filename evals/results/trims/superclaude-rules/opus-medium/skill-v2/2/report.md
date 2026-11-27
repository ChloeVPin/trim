I've saved a shorter version as `trimmed.md` and left `instructions.md` unchanged. It cuts the file roughly in half.

**1. Target model:** `claude-opus-5-5`, which you named. Its profile was tested at medium effort.

**2. Length:** about 2,100 words before and about 1,050 after (287 lines down to about 125). These are estimates, because I had no word-counting tool in this session.

**3. Changes and reasons**
- **Repeated rules merged.** "Parallel tool calls" appeared 4 times, "plan first" 4 times, "follow existing patterns" 3 times, and "clean up temp files" 7 times in one section. The Quick Reference and decision trees at the end repeated earlier rules. I kept each rule once and moved the few that only appeared there into the main sections: absolute paths, no auto-commit, brainstorm mode, run tests first, and Magic/Context7/Playwright.
- **Emphasis toned down.** I replaced the 🔴🟡🟢 markers, "CRITICAL", "ALWAYS", "MUST" and "Start it = Finish it" with plain wording. The maker says this kind of emphasis now makes the model over-apply rules. Your priority tiers and conflict order are kept as plain labels.
- **Lines that describe default behaviour removed.** These include descriptive names, elegant organization, debug systematically, methodical problem-solving, and Grep over bash grep or Glob over find (the Claude Code harness already says that). The "Auto-Selection / Keywords / File Types" bullets describe what Claude Code does on its own rather than telling the model to do anything.
- **Two vague lines removed.** "Context Retention: maintain ≥90% understanding" can't be measured or acted on. "Think Before Build/Write" is an instruction to think carefully first, which the profile says to cut for this model.
- **Per-section "Triggers" lines removed.** Each section already makes clear when it applies.
- **Most ✅/❌ examples shortened.** I kept the ones that pin a format: the parallel-plan example, the login-form scope example, the not-implemented example, and the temporal-check phrasing.

**4. Kept and why**
- **Git workflow** is kept word for word, including the example and the Detection line, because it guards commits and branches.
- **Lines kept word for word:** the "Never Skip Tests", "Never Skip Validation" and "Quality Integrity" lines, and the two deletion lines in Workspace hygiene ("No Artifact Pollution" and "Resource Management"). These deal with work that is fragile or can't be undone.
- **Every specific fact** is still there: `/sc:load`, `/sc:save`, 30-minute checkpoints, TodoWrite for 3+ tasks, `@agent-[name]`, the PM Agent duties, `claudedocs/`, the test and script directories, the MCP server names, MultiEdit, the banned marketing words, the lint/typecheck step and the detection grep.

**5. For you to decide**
- **Commit rules conflict.** "Incremental Commits / Commit before risky operations" contradicts "No auto-commit" from the Quick Reference. I kept both.
- **Metric rules conflict.** "Plan should specify expected parallelization gains (60%)" contradicts "Never invent percentages without evidence". I kept both.
- **Risky deletion rule.** "Delete unused directories and files" could lead the model to delete your files. You might want to limit it to files the model created, or require it to ask first.
- **Possibly stale references.** Check that the PM Agent, backend-architect, `/sc:*` commands, MultiEdit, brainstorm mode, morphllm and Magic MCP still exist in your setup. The temporal example still uses 2025 dates, and I dropped the old "Don't default to January 2025" line.
- **Lines that may be unnecessary.** I kept these, but they're uncertain:
  - "Validate before execution, verify after completion" (about 10 words). The maker says Opus 5 checks its own work without being told, but that's unconfirmed for 5.5.
  - "Task agents for >3 steps" and "Task agent > native reasoning" (about 20 words). Standing instructions to delegate can make the model delegate too often.
- **Optional tier labels.** If you don't use the tier labels when rules conflict, dropping them saves about 60 more words.
- **Suggested addition (not in the text):** for loosely specified work across several sources, a line telling the model to look through the relevant sources before acting. The profile recommends this for this model.

**6. Proposed text:** in `/root/trim-sbx/d28951033b42/trimmed.md`.