I saved the proposed version to `/root/trim-sbx/0537afb6b339/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, as you named it. It has a profile, tested at high effort. I checked the cuts against that profile only. I could not run the skill's evals here.

**2. Length:** about 2,200 words before and about 1,300 after, roughly 40% shorter. These are estimates because this session has no word-count tool. The Workspace Hygiene and Git Workflow sections (about 290 words) are unchanged.

**3. Changes and reasons**

- **Intro line removed.** It says nothing the model can act on.
- **Quick Reference & Decision Trees removed.** Every rule in it repeats a rule above. The one unique item, "run tests before starting", moved to Workflow Rules. "Absolute paths, no auto-commit" moved to Safety Rules because it is a commit rule.
- **Agent Orchestration condensed.** The flow and the ✅/❌ examples repeated the bullets. "Monthly maintenance" and "Complexity" were cut: a single session cannot run a monthly job, and the complexity line gives no direction.
- **Planning Efficiency folded into Workflow Rules.** Its parallelization guidance is now one line with the plan example. "Resource estimation" was cut because the model cannot measure tokens or time.
- **Parallel-call lines merged.** Four separate lines said the same thing. The rewrite drops "ALWAYS", since the profile says emphasis over-triggers.
- **Efficiency Metrics cut.** It asks for "3 parallel ops = 60% time saving"-style figures, which contradicts the No Fake Metrics rule. This is the one cut where the rules conflict. Restore it if you want the conflict kept.
- **Generic virtues cut.** "Context Retention ≥90%" cannot be measured. "Efficiency First", "Elegant Organization", "Single Responsibility", and "Debug Systematically" describe what the model already does.
- **Repeated items merged.** Duplicates in Honesty, Scope, Code Organization, File Organization, and Failure Investigation were combined.
- **Discovery First rewritten.** "Complete project-wide analysis" is the blanket search instruction the Haiku profile warns about. It now asks for a search for affected files before a systematic change only.

**4. Kept, and why**

- **Verbatim:** Workspace Hygiene and Git Workflow. Both guard deletion and commits, so the skill requires them unchanged.
- **Verbatim:** Safety Rules, which guards file changes. The only addition is the "Absolute paths, no auto-commit" line from Quick Reference.
- **Kept:** the Priority and Conflict hierarchy, the procedures (task pattern, plan format, root cause → fix → verify), the "never skip tests or validation" rules, and the quality-check line. That line is the check-before-done instruction the Haiku profile asks for on coding agents.
- **Kept, flagged:** the references to tools and agents this session may not have (see below).

**Needs your decision**

- **Commit rules conflict.** Quick Reference says "no auto-commit". Git Workflow says "commit frequently" and "commit before risky operations". I kept both, since the rule is commit-related. The model will get mixed signals until you pick one.
- **Mock objects.** "No Mock Objects" can be read as banning test doubles. I kept the wording. Adding "in delivered code" would make the scope clear.
- **Unverified references.** I could not confirm these exist in your setup: `/sc:load`, `/sc:save`, PM Agent, backend-architect, `@agent-[name]`, MultiEdit, Magic MCP, Context7, Playwright, morphllm, sequential-thinking, and the 30-minute checkpoints. If they do not exist, they are dead references, and cutting them would save about 150 words. I left them in.
- **Stale dates in examples.** The Temporal Awareness examples use 2025 dates. The session date is 2026-11-27. I left them as written.

**Optional addition (not applied):** the profile suggests "keep working until the task is done" for agents that stop early. Nothing you wrote suggests that problem, so I did not add it.