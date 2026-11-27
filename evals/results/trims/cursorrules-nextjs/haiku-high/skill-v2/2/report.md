The trimmed version is saved at `/root/trim-sbx/9b26f24713b5/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. Haiku needs more explicit detail than the larger models, so I cut conservatively and kept every rule that carries a format, name, or procedure.

**2. Words:** I have no counting tool in this session, so these are estimates. The body goes from about 540 words to about 475, roughly 12% shorter.

**3. Changes**
- Merged three overlapping lines about single-line conditionals into one. Same rule, no curly braces.
- Merged the early-return, guard-clause, and else lines into two lines.
- Cut "Use declarative JSX." It repeats "Use functional, declarative programming."
- Cut "and TypeScript interfaces" from the components line. "Prefer interfaces over types" already covers it.
- Merged the two mobile-first and responsive-design lines.
- Cut "'use client'" from the `useEffect`/`setState` line. The Key Conventions section covers it in full.
- Merged the error-boundary lines into one, keeping `error.tsx` and `global-error.tsx`.
- Merged the two form-validation lines (Zod, `useActionState`, `react-hook-form`) into one.
- Cut "Implement type-safe server actions with proper validation." It is generic and the Zod line covers it.
- Cut "Handle errors gracefully and return appropriate responses." It is generic and the `ActionResponse` line covers it.
- Merged the two `ActionResponse` lines.

**4. Kept, and why**
- The frontmatter, byte for byte, because a program reads it.
- The stack line, because the model cannot know your stack.
- All naming, file-structure, and export rules, since they are author choices.
- All error-handling steps and the Server Action and `services/` error rules, because they are procedures.
- The `'use client'` and RSC rules, in full.
- The `next-safe-action` steps and import path, since they are facts the model cannot know.
- The docs reference (line 74 and the URL). I marked it unsure: the model may not be able to open the link. Dropping it saves about 20 words if you agree.

**5. Flags for you**
- **Frontmatter:** `globs: **/*` may not parse as strict YAML, because a plain scalar cannot start with `*`. I left it alone. Quoting it (`globs: "**/*"`) would be safer, but check how Cursor reads it first.
- **"Tailwind Aria":** I cannot confirm a library by that name. It may mean Tailwind CSS or React Aria. I kept it as written.
- **Vite:** it is listed next to Next.js 14. If the project is Next.js only, Vite may be stale. Solidity, Viem, and Wagmi appear in the stack but no rule covers them.
- **Web Vitals:** FID was replaced by INP as a Core Web Vital in 2024. This comes from my own knowledge, not a source I checked in this session.
- **Error layers:** "`services/` always throw" and "return expected errors as values from Server Actions" are compatible, but the text does not say where the boundary is. One sentence would settle it.
- **Ordering:** line 22 puts types last and line 46 puts interfaces at file end. They roughly agree but overlap.

**Suggestions (not added to the text):** this is a coding file, so the profile suggests one line telling the model to run a real check (typecheck, lint, or tests) before reporting a change as done. Add it only if you want it. Also, "keep working until the task is done" applies only if the model stops early in your setup.