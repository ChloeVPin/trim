I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
I used `claude-opus-5-5`, the model you named. Its profile was tested at medium effort.

## 2. Word count
About **2,100 → 1,150 words**, roughly 45% shorter. These are estimates: I had no tool that counts words in this session.

## 3. Changes
- **Emojis, "CRITICAL" and ✅/❌ markers removed; priority levels kept as plain labels.** This model follows wording closely, so emphasis meant to make older models comply now makes it over-apply rules. The Git and Safety sections still have their original formatting, because I left them exactly as written.
- **"Triggers:" lines removed.** Each section's content already says when it applies. The two triggers that added something (checkpoint before risky operations, and run existing tests before starting) moved into the Workflow section.
- **"Think before you act" lines removed:** Think Before Build, Think Before Write, Methodical Problem-Solving, Debug Systematically, and Resource Estimation. The profile says telling this model to think carefully only delays its replies, with no clear quality gain.
- **General "validate and verify" lines removed:** Validation Gates, and the verify step in the orchestration flow. On the previous Opus version, the maker advised deleting self-check lines because the model checks its own work unprompted. Whether that still holds on 5.5 is unconfirmed, so restore these if you want them. I kept the specific checks: lint/typecheck, `git diff`, and running tests first.
- **Lines pushing tool use softened:** "most powerful tool always", "Efficiency First", and "Parallel Everything… never sequentially" are gone. These over-trigger tool use on this model. I kept the specific MCP-to-task mapping and the Task-agent threshold.
- **Lines Claude Code already covers removed:** prefer Grep/Glob over bash grep/find, and parallel tool calls (which appeared three times; now once).
- **Repeats and vague lines removed:** "Maintain ≥90% understanding", Descriptive Names, Elegant Organization, Hierarchical Logic, Separation of Concerns, Purpose-Based Organization, Quality Integrity, Professional Language, and several bullets that said the same thing as their neighbors (six versions of "finish what you start", five versions of "clean temp files").
- **Most of the Quick Reference section removed.** Nearly all of it repeated earlier sections. Its unique items moved into the main sections: the brainstorm-first rule, Magic, Context7 and Playwright, and running tests first. The "Before Any File Operations" tree is kept word for word under Safety Rules.
- **Examples cut to the ones that pin down a preference:** naming, file paths, the login-form scope example, and the not-implemented code.

## 4. Kept and why
- **Word for word:** the whole Git Workflow section (commits and branches), Safety Rules, the file-operation decision tree (it contains "No auto-commit"), the two never-skip-tests/validation rules, and the two deletion bullets in Workspace Hygiene. These guard actions that are risky or hard to undo.
- **All the facts:** `@agent-[name]`, how the PM Agent works, `/sc:load`/`/sc:save` and the 30-minute checkpoints, `claudedocs/`, the test and script directories, the MCP server names, the detection `grep` commands, and the banned marketing words.
- **Your preferences,** including ones I'd question (flagged below).

## 5. Flags and suggestions (all left for you to decide)
1. **Possible contradiction: "Incremental Commits / commit frequently"** vs **"No auto-commit"**. Say which one wins, or when committing is allowed.
2. **Contradiction about metrics:** "Plan should specify expected parallelization gains (60% time saving)" conflicts with "Don't invent… percentages without evidence."
3. **Contradiction about readiness:** "Real Code Only: production-ready" (removed in the trim, but its intent overlaps with "finish it") conflicts with "say 'MVP', not 'production-ready'" and "MVP First".
4. **Inconsistent TodoWrite threshold:** the workflow says "3+ tasks" but the decision tree said ">3 steps". I kept 3+.
5. **"Delete unused directories and files"** is risky. Consider limiting it to files the agent created, or making it "ask before deleting".
6. **"No mock objects"** could be read as banning test mocks. Consider adding "outside tests".
7. **"Organize by feature/domain, not file type"** sits awkwardly with "all tests in `tests/`, scripts in `scripts/`."
8. **Possibly outdated:** "Don't default to January 2025" (I dropped the specific date; the rule stays), and the example date of 2025. MultiEdit may not exist in your current tool set. "Playwright MCP > unit tests" reads as replacing unit tests, which may not be what you mean.
9. **Suggestion from the profile:** for vaguely specified work that spans several tools or apps, add a line telling it to look through the relevant sources before acting.

## 6. Proposed text
It's in `/root/trim-sbx/bbbd319c719a/trimmed.md`.