The proposed version is in `/root/trim-sbx/7067e04ca6a1/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile (tested at high effort). Haiku needs more explicit detail than the larger models, so I cut conservatively.

**2. Length:** about 600 words before and about 550 after, roughly 8–10% shorter. These are estimates because I have no word-count tool here. The file was already fairly lean, so this is a light trim.

**3. Changes**
- **Merged three curly-brace lines** into one one-line conditional rule. The three lines said the same thing.
- **Merged the two early-return lines** ("use early returns" and "use guard clauses") into one.
- **Merged the two responsive-design lines** into "mobile-first responsive design with Tailwind CSS."
- **Removed "Place static content and interfaces at file end."** The File structure line already puts static content and types last.
- **Shortened the `useEffect`/`setState` line** to drop the `'use client'` part. Key Conventions item 3 already covers `'use client'` in full.
- **Removed two generic server-action lines**, "Implement type-safe server actions with proper validation" and "Handle errors gracefully and return appropriate responses." The specific lines beside them cover the same ground.

**4. Kept**
- **Frontmatter**, exactly as written, because a program reads it.
- **The stack list, examples, and code snippets**, since Haiku cannot know them unless told.
- **All the specific conventions** (try/catch rule, `ActionResponse` type, `error.tsx`, `services/` error behaviour, Zod, Suspense, image rules). These are the author's preferences.
- **The documentation pointer and URL**, since the model cannot know which docs you mean.
- **Hedged lines** such as "Consider using custom error types." These are your preferences, so I left them.

**5. Flags and suggestions (none applied)**
- **Frontmatter may not parse.** `globs: **/*` starts with `*`, which YAML reads as an alias marker. If the tool that reads this file fails on it, quote the value as `"**/*"`. I left it alone because it is frontmatter.
- **FID is out of date.** Google replaced First Input Delay with Interaction to Next Paint (INP) as a Core Web Vital in 2024. Consider `(LCP, CLS, INP)`.
- **Stack line to confirm.** It names Next.js 14 and Vite together, which is unusual in one project, and "Tailwind Aria" is not a package name I recognise. Check that the stack is current.
- **Possible conflict.** The `services/` rule says services throw errors, but Server Actions return them as `ActionResponse`. If Server Actions call services, the rules should say the action catches the throw and converts it. Decide which behaviour you want.
- **Suggested addition for a coding agent.** Haiku does better with an explicit line to run a real check before reporting a change done, for example "Run the type checker and linter before reporting a change done." This is outside the text; add it only if the file drives an agent.

**6. Proposed text:** see `/root/trim-sbx/7067e04ca6a1/trimmed.md`.