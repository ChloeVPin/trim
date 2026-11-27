I've saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
`claude-opus-5-5`, which you named. Its profile was tested at medium effort.

## 2. Length
About 1,850 words before and 1,100 after, roughly 40% shorter. I had no word-count tool in this session, so both figures are estimates.

## 3. Changes and reasons
- **Emphasis turned down.** I removed the 🔴/🟡/🟢 markers, CAPITALS, "MUST" and "ALWAYS". The maker says emphasis like this makes current Claude models apply rules too broadly. I kept the three priority levels as plain words in the section headings, because your conflict-resolution order depends on them.
- **The "Quick Reference & Decision Trees" section is gone.** Almost all of it repeated earlier sections. The few things only it contained are now in the main sections: absolute paths only, no auto-commit, brainstorm mode when scope is unclear, run tests before starting, Magic MCP for UI.
- **Duplicates merged.** Parallel tool calls were stated three times, and the Claude Code harness already says it. "Follow existing patterns" appeared four times. The thinking/planning steps also repeated each other (Understand → Plan → Build, Think Before Build, Methodical Problem-Solving, Debug Systematically, Systematic Changes).
- **Generic virtues and vague lines cut.** These include "Context Retention ≥90%", "Elegant Organization", "Professional Workspace", "Single Responsibility", "Purpose-Based Organization", "Hierarchical Logic" and "Descriptive Names".
- **Agent orchestration cut down.** The lines describing how Claude Code picks agents by keyword, file type or complexity describe the harness, not anything the model does. I kept the `@agent-` override and every PM Agent step.
- **Tool lines that push for more use cut.** "Always use the most powerful tool", "Parallel Everything" and "Efficiency First" are the kind of line the maker says now makes the model use tools too eagerly. I kept every specific tool mapping.
- **Planning Efficiency** became one Workflow line plus your plan-format example. I left out "Resource Estimation" and the "expected parallelization gains" metric (see flags).
- **Temporal Awareness:** I replaced the "January 2025" reference with "not from training data". I kept "state the source" and your example.
- **Examples:** I kept the ones that set a format or a clear boundary (login form, naming, plan format, git, failing test). I cut the `calculate()` code example.

## 4. Kept as written, and why
- **Workspace Hygiene, Failure Investigation and Git Workflow** are kept word for word, including their emphasis. They govern deleting files, skipping tests and committing, where a wrong cut costs far more than the words saved. The only edits there:
  - I removed "Professional Workspace" and the two softer debugging lines, which add no rule.
  - I added "No auto-commit" from the quick reference so it sits next to the other git rules.
- Every concrete name is kept: paths, commands, `/sc:load`/`/sc:save`, `claudedocs/`, the MCP server names, the 3+ task/step thresholds, the 30-minute checkpoint and the banned words.
- I kept your choices as strict as you wrote them, such as "no mock objects", "production-ready" and banning "excellent".

## 5. Flags for you to decide
1. **Commit rules conflict.** "No auto-commit" contradicts "Commit frequently" and "Commit before risky operations". Both are kept, so the model can't satisfy them all. Decide which wins.
2. **Two other conflicts:**
   - "All generated code must be production-ready" vs "MVP first" and "say 'MVP', not 'production-ready'".
   - "No mock objects / fake data" may forbid test mocks and fixtures. Did you mean production code only?
3. **Risky deletion rule.** "Delete unused directories and files to prevent workspace bloat" lets the model delete files it judges unused. Consider limiting it to files it created, or asking first.
4. **Invented metrics.** The old "expected parallelization gains (e.g. 60% time saving)" rule conflicted with "no fake metrics", so I dropped it. Dropping "Resource Estimation" too makes the text about 30 words shorter. Put either back if you want them.
5. **Self-check lines might go.** "Validate before execution and verify after completion" and "Back claims with tests or documentation" are kept. For Opus 5 the maker says to delete lines like these because the model checks its own work unprompted. Whether that holds for 5.5 is unverified. Dropping both saves about 20 words.
6. **Possibly stale:**
   - MultiEdit isn't in the current Claude Code tool set as far as I can see.
   - The monthly PM Agent maintenance needs something to trigger it, because the model can't track months.
   - "Task agent for >3 steps" and "sequential-thinking for analysis" may produce more delegation than you want.
   - The 3+ thresholds are inconsistent: TodoWrite is for "3+ tasks" in one place and ">3 steps" in another. I used "3+ tasks".
7. **Suggestion, not added:** for loosely specified work across several sources, the maker recommends a line telling the model to look through the relevant sources before acting. Your "Discovery First" line partly covers this.

## 6. Proposed text
It's in `/root/trim-sbx/72fdfd45bab7/trimmed.md`.