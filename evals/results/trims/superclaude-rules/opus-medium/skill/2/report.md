I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged. Nothing else is changed until you approve.

## 1. Target model
**claude-opus-5-5**, which you named. Its profile has been tested at medium effort.

## 2. Length
About **2,000 words before and 800 after**, so roughly 60% shorter. These are estimates: I had no tool that counts words in this session.

## 3. Changes
- **Emoji priority tiers and per-section "Triggers" lines:** removed. Heavy emphasis like "CRITICAL" and "Never compromise" makes Opus 5.5 apply rules too broadly, and the triggers say what the model already infers. I kept your conflict hierarchy word for word. The two 🟢 sections are now marked "(preference)", so the firm-versus-soft distinction still holds.
- **Agent Orchestration:** cut to the `@agent-[name]` override and the PM Agent duties. Auto-selection by keyword or file type describes what the tooling does, not what the model should do.
- **Planning Efficiency:** removed. Opus 5.5 plans and runs things in parallel without being told, and the profile says lines pushing this now over-trigger. The rule asking for "expected parallelization gains (60% time saving)" also contradicted your rule against fake metrics.
- **Workflow:** removed "ALWAYS parallel", "≥90% understanding", "Evidence-Based" (it repeats Honesty) and "Validation Gates". I kept TodoWrite, lint/typecheck, the session commands and checkpoints, and "look through the project first", which the profile recommends adding.
- **Quick Reference / Decision Trees:** removed because it repeats the sections above. I moved its four new points into the body: brainstorm mode for unclear scope, running existing tests before a feature, absolute paths, and no auto-commit.
- **Implementation, Scope, Code Organization, Honesty, File Organization:** merged repeated bullets and cut generic advice ("Descriptive Names", "Elegant Organization", "No Sycophantic Behavior"). Every concrete fact stayed: the banned words, directory names, naming conventions and the login-form example.
- **Tool Optimization:** cut to the MCP-server mapping. Opus already prefers Grep over bash grep and batches its calls, and "use the most powerful tool" lines push tool use too hard.
- **Temporal Awareness:** cut to one line. The note about January 2025 and the sample date were out of date.

## 4. Kept exactly as written
- **Git Workflow, Workspace Hygiene (deleting files), "Never skip tests/validation/integrity", Safety Rules and no auto-commit:** these guard commits, deletion and rollback. A wrong cut there costs far more than the words it saves.

## Points you may want to decide
1. **"Commit frequently" vs "No auto-commit":** these conflict, and Opus follows wording closely. Which one should win?
2. **"Delete unused directories and files":** this could delete your own files. I'd suggest "ask before deleting anything you didn't create". I left it as written.
3. **"Production-ready" (which I cut) vs "MVP first / say 'MVP', not 'production-ready'":** these contradicted each other, so I kept the MVP version. Tell me if you want the reverse.
4. **Unsure, kept:**
   - **"Run lint/typecheck":** the maker says Opus 5 checks its own work unprompted, but that isn't confirmed for 5.5. Dropping it saves about 6 words.
   - **The PM Agent, `/sc:load`/`/sc:save`, brainstorm mode, morphllm, Magic, Context7 and Playwright:** none of these exist in this repo, so I couldn't confirm them. If they're gone, cutting them saves about 90 words.
5. **Unsure, cut:**
   - **"Use Task agents for complex operations (>3 steps)":** this tends to make the model delegate more than you'd want. Putting it back adds about 10 words.
   - **MultiEdit:** I dropped the MultiEdit preference because the tool may no longer exist in current Claude Code.