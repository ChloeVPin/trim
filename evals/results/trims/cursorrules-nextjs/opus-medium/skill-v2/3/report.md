I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-opus-5-5`, which you named. It has a profile, tested at medium effort.

**2. Length:** about 610 words before and 470 after, a cut of roughly 23%. I had no tool to count words, so both figures are estimates.

**3. Changes**

Almost all the cuts remove repetition. The Opus 5.5 profile's specific targets, such as "think carefully" or "double-check" lines and capitalised emphasis, don't appear in this file.
- **Curly braces:** three lines said the same thing (lines 23–25). They're now one line, and the example is kept.
- **Error handling:** six overlapping points about guard clauses, early returns, the happy path last and avoiding `else` (lines 30–34) are now one line. Logging, user-friendly messages and custom error types are kept.
- **Lines the file already covered:**
  - "Use functional components and TypeScript interfaces" repeated "Avoid classes" and "Prefer interfaces".
  - "Use declarative JSX" repeated "functional, declarative programming".
  - "Place static content and interfaces at file end" repeated the file-structure line.
- **`'use client'`:** it was covered in two places (line 48 and Key Conventions #3). Both are now one React/Next.js line, with all their conditions kept.
- **Forms:** "Use Zod for form validation" and "useActionState with react-hook-form" are now one line.
- **next-safe-action:** I dropped "type-safe… proper validation" and "handle errors gracefully". The Zod-schema line and the ActionResponse lines already say what they meant. The three ActionResponse lines are now two, and the exact import path is kept.
- **Small wording changes:** I dropped "accurate" from "accurate TypeScript examples" because it's a general virtue, and merged "responsive design" with "mobile-first".

**4. Kept as written**
- The frontmatter, exactly, because Cursor reads it.
- Every style choice, including ones the model wouldn't make unprompted: no semicolons, `function` instead of `const`, RORO, maps instead of enums, named exports, dashed directory names.
- All names, paths and libraries: `@/types/actions`, `services/`, `error.tsx` and `global-error.tsx`, next-safe-action, TanStack Query.
- The opening role line, because its tech list tells the model your stack.

**5. Flags for you to decide**
- **FID is out of date.** Google replaced FID with INP as a Core Web Vital in 2024. I left it in, but you probably want "LCP, CLS, INP".
- **Next.js and Vite together.** The stack line lists both, which is unusual. Is Vite used somewhere in the repo, or is it left over?
- **"Tailwind Aria".** Check that this is the library you mean, possibly the React Aria Components Tailwind plugin. It's named twice.
- **useActionState with react-hook-form.** These two handle form state in different ways, so they're an awkward pair. Did you mean one or the other?
- **Two error-handling styles.** Server actions return their errors, but `services/` throws them for TanStack Query. That works if they're separate layers; it may be worth saying so.
- **The Next.js docs link (unsure).** The model knows the docs exist, so dropping it saves about 15 words. I kept it because it's your choice.
- **`globs: **/*`.** This matches every file, including Solidity and config files, while the description only mentions Next.js. That's your call; I didn't change it.

**Suggestion (not in the text):** I have none. The profile only recommends an addition for loosely specified work across several apps, and these coding rules aren't that.