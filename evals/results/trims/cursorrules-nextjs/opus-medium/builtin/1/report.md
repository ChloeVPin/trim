I saved the trimmed copy as `trimmed.md`. `instructions.md` is unchanged. The file was already in good shape: I applied two small edits that remove repeated rules, and listed four other items for you to decide on.

## Audit report: `instructions.md`

**What I assumed**
- **Scope:** only `instructions.md`, which is the only file in the directory. There's no git history and no project code, so I couldn't check which model each line was written for, or whether the paths it names (`services/`, `@/types/actions`) exist.
- **Target model:** `claude-opus-5-5`, as you asked.
- **File type:** a Cursor rules file (`description`/`globs`/`alwaysApply` frontmatter) read by a coding agent. It doesn't refer to any other model provider.

**Summary:** None of the usual signs of text written for older models are here: no capital-letter pressure ("MUST", "NEVER"), no "think step by step", no prefill, no step-by-step scripts. The opening "You are an expert in…" line is followed by real stack details, so it stays. The two findings are rules repeated within the file. The flagged items are about Next.js and React facts and need your judgement, so I didn't edit them.

Findings by category: wording written for older models (Group 1): 2 · instruction-file problems such as stale facts or conflicts (Group 2): 0 (with no code, there's nothing to check the file against) · tool descriptions (Group 3): not applicable · request and API settings (Group 4): not applicable (no code that calls the API).

| # | Location | Evidence | Pattern | Why it's obsolete | Confidence | Action |
|---|---|---|---|---|---|---|
| 1 | `instructions.md:23-25` | "Avoid unnecessary curly braces…" / "For single-line statements in conditionals, omit curly braces." / "Use concise, one-line syntax for simple conditional statements…" | 1c Padding: repetition as reinforcement | Three lines in a row give the same rule. Opus 5.5 follows each line literally, so it has to reconcile three wordings of one rule. | Medium | `rewrite` → "Omit curly braces around single-line conditional bodies and write simple conditionals on one line (e.g., if (condition) doSomething())." |
| 2 | `instructions.md:48` | "Minimize 'use client', 'useEffect', and 'setState'. Favor RSC." | 1c Padding: same rule in two places | The `'use client'` rule is stated again, in more detail, in Key Conventions 3 (`:70-73`). | Medium | `rewrite` → "Minimize 'useEffect' and 'setState'. Favor RSC." |
| 3 | `instructions.md:6`, `:53`, `:55` | "Next.js 14 App Router" next to "Use useActionState…" | Group 2 Volatile specifics (pinned version) | `useActionState` is a React 19 API. Next.js 14 runs React 18, where the hook was `useFormState`. One of the two is out of date, but there's no `package.json` to show which. | Low | `flag`: update either the version pin or the hook name to match the real dependency. |
| 4 | `instructions.md:69` | "Prioritize Web Vitals (LCP, CLS, FID)." | Group 2 Volatile specifics | INP replaced FID as a Core Web Vital in March 2024. That's an outside fact, and nothing in the project contradicts the line, so it doesn't meet the bar for an automatic edit. | Low | `flag`: suggested replacement is "(LCP, CLS, INP)". |
| 5 | `instructions.md:53`, `:56`, `:57` | Server Actions "return errors… useActionState" / services "always throw… tanStackQuery can catch" / "Use next-safe-action for all server actions" | Possible conflict | There are three error and data-flow approaches. They may apply to different layers, but you should confirm that's intended (next-safe-action also has its own `useAction` hooks). | Low | `flag` |
| 6 | `instructions.md:36` | "Consider using custom error types…" | 1a hedge ("Consider…") | This is only a problem if you actually want this as a requirement. If so, change it to "Use custom error types…". | Low | `flag` |

**Left alone on purpose:** the role line (it's followed by specific stack details); the stack and style preferences such as no semicolons, RORO, named exports and maps instead of enums (those are things only you know); and the error-handling list at `:29-36`. That list overlaps a little, but it describes distinct techniques.

## Applied diff (`instructions.md` → `trimmed.md`)

```diff
@@ -22,6 +22,4 @@  (finding 1)
 - File structure: Exported component, subcomponents, helpers, static content, types.
-- Avoid unnecessary curly braces in conditional statements.
-- For single-line statements in conditionals, omit curly braces.
-- Use concise, one-line syntax for simple conditional statements (e.g., if (condition) doSomething()).  
+- Omit curly braces around single-line conditional bodies and write simple conditionals on one line (e.g., if (condition) doSomething()).  
@@ -48 +46 @@  (finding 2)
-- Minimize 'use client', 'useEffect', and 'setState'. Favor RSC.
+- Minimize 'useEffect' and 'setState'. Favor RSC.
```

I didn't change the four flagged items in `trimmed.md`. Items 3 and 4 each come down to one word once you know which version you're on.