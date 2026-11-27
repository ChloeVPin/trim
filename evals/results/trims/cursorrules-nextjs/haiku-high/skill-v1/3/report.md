I saved the proposed version to `/root/trim-sbx/268ad6edce5a/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. For Haiku, the profile says to cut less than for the larger models and keep the steps and examples that carry a procedure. So I cut only duplication.

**2. Words:** about 730 before and about 590 after, a cut of roughly 19%. These are estimates, since I have no word-count tool here.

**3. Changes**
- Merged three overlapping conditional-brace lines into one line with the example.
- Merged the error-handling bullets about edge cases, early returns, the happy path and if-return into two bullets.
- Removed the "Minimize 'use client'…" line from the React section, since Key Conventions covers it. I moved the `useEffect`/`setState` part into Key Conventions so nothing is lost.
- Merged the two responsive-design lines.
- Removed "Place static content and interfaces at file end", because the file-structure line already gives that order.
- Merged the Zod, `useActionState` and react-hook-form lines.
- In the Server Actions block, removed "Implement type-safe server actions" and "Handle errors gracefully", which the Zod-schema and ActionResponse lines already cover. Merged the two ActionResponse lines.
- Removed trailing double spaces.

**4. Kept**
- The frontmatter, verbatim.
- The stack list, which the model cannot know otherwise.
- The procedures: error-handling order, RORO, file structure, the server-action pattern, the exact import line, and the `services/` error rule.
- The Next.js docs link.

**5. Flags for you**
- `globs: **/*` is unquoted YAML. A leading `*` is a YAML alias marker, so a strict parser may reject the frontmatter. I left it as written because a program reads it. Quoting it (`globs: "**/*"`) would be safer.
- "Tailwind Aria" (lines 6 and 43) is not a name I recognise. Did you mean Tailwind CSS with an ARIA plugin? Please confirm.
- "Next.js 14 App Router" may be out of date. Check it against the project's version.
- "Prioritize Web Vitals (LCP, CLS, FID)": from my own knowledge, not checked against a source in this session, FID was replaced by INP as a Core Web Vital in 2024. You may want INP here.
- Possible tension: `services/` code throws, but Server Actions return errors as values. If a Server Action calls `services/` code, the action has to catch the throw and return an `ActionResponse`. You may want to say that explicitly.
- "Consider custom error types or error factories" is soft among firm rules. I kept it as written. Make it a rule or drop it, as you prefer.

**Suggestions (not added to the text)**
- The profile recommends that a coding agent run a real check before reporting a change done. For example, add a line to run your type check and lint. I don't know your project's actual scripts, so I didn't write the command.
- If the agent tends to stop early on multi-file tasks, consider adding "keep working until the task is done."