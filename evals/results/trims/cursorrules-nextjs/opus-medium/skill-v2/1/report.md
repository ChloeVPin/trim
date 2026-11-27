I saved the shorter version as `trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-opus-5-5`, which you named. It has a profile that was tested at medium effort.

**2. Word count:** about 610 words before and about 440 after, roughly 28% shorter. I had no counting tool, so both figures are estimates.

**3. What changed and why**
- **"You are an expert in…" → "Stack: …"**: The tech list tells the model something it can't know, so I kept it. The "expert" framing doesn't change what the model does.
- **Cut "Prefer iteration and modularization over duplication" and "accurate"**: These describe what the model already does.
- **Merged three lines about curly braces and one-line conditionals into one**: They said the same thing three times.
- **Merged the seven error-handling bullets into three**: Guard clauses, early returns, handling errors at the start, happy path last and avoiding else are all one rule. I kept the lines about logging, user-friendly messages and custom error types as written.
- **Cut "Use functional components and TypeScript interfaces" and "Use declarative JSX"**: "Avoid classes", "Prefer interfaces" and "functional, declarative" already cover them.
- **Merged "function, not const, for components" with the pure-functions line**: It's the same choice in both places.
- **Folded "Place static content and interfaces at file end" into the file-structure line**: The two lines overlapped.
- **Merged "Minimize 'use client'" with Key Conventions item 3**: The rule appeared twice. All its conditions are still there.
- **Moved Key Conventions 1 and 2 into the React/Next.js list**: This removed a section heading. The wording didn't change.
- **Shortened the next-safe-action sub-bullets from 7 to 3**: "Handle errors gracefully" and "type-safe with proper validation" are already covered by the Zod schema and ActionResponse lines. The import path and the return type are unchanged.

**4. What I kept and why**
- The frontmatter, exactly as written, because Cursor reads it.
- Every specific choice you made: omitting semicolons, RORO, maps instead of enums, naming with dashes, named exports, the `services/` and TanStack Query rule, the import path, the error.tsx and global-error.tsx files, the image rules, Suspense and dynamic loading.
- The docs link, since I wasn't sure it could go (see flags).

**5. Things for you to decide**
- **Next.js 14 vs `useActionState`:** `useActionState` comes with React 19 and Next.js 15. On Next.js 14 the hook is `useFormState`. Either the version number or the hook name is out of date.
- **FID:** Core Web Vitals replaced FID with INP in March 2024. You probably want "LCP, CLS, INP".
- **"Tailwind Aria":** I'm not aware of a library by that name. You may mean Tailwind CSS plus React Aria. I left it as written.
- **Form and error handling may conflict:** The file asks for Zod, `useActionState`, react-hook-form, next-safe-action and TanStack Query, all for forms or errors. It doesn't say when to use which. A short line on that would help.
- **Frontmatter:** `globs: **/*` matches every file, including Solidity, so `alwaysApply: false` has little effect. The description also doesn't mention Solidity or Web3. I didn't change either.
- **Docs link:** Cutting this line would save about 15 words. The model already knows the Next.js docs exist, but you may want the line to prompt it to look them up.
- **Suggestion (not added):** None of the "keep or add" items in the profile apply to a coding-style rules file like this one.

**6. Proposed text:** see `/root/trim-sbx/e2dd65b31d56/trimmed.md`.