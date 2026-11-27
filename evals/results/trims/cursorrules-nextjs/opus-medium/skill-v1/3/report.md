I saved the shorter version as `trimmed.md` and didn't touch `instructions.md`. Nothing in the file guards risky or irreversible actions, so the cuts are mostly repeats.

**1. Target model:** claude-opus-5-5, which you named. Its profile is tested at medium effort.

**2. Word count:** about 560 before and about 430 after, roughly 23% shorter. I had no word-count tool, so these are estimates.

**3. Changes**
- **Frontmatter:** left exactly as written, because Cursor reads it.
- **Role line:** "You are an expert in…" is now a plain `Stack:` line. The list of technologies is useful information; the "expert" framing isn't.
- **Curly braces:** three lines said the same thing ("avoid unnecessary curly braces", "omit for single-line", "one-line syntax"). They're now one line.
- **Components:** "Use functional components and TypeScript interfaces" repeated "avoid classes" and "prefer interfaces", so I removed it. "Use function, not const, for components" is merged with the rule about the `function` keyword.
- **File order:** "Place static content and interfaces at file end" is folded into the file-structure line.
- **Error handling:** seven bullets became three. Guard clauses, early returns, happy path last and if-return all say the same thing.
- **`'use client'`:** this appeared twice (React/Next.js and Key Conventions). It's now one bullet with the same limits. I folded the rest of Key Conventions (App Router, Web Vitals) into React/Next.js.
- **Responsive design:** the Tailwind and mobile-first lines are merged.
- **Next.js docs link:** removed. "Refer to Next.js documentation" tells the model nothing it doesn't already know.
- **next-safe-action:** I removed "Handle errors gracefully" and "proper validation" because they're generic. The three ActionResponse lines are merged without changing what they require.
- **"accurate":** dropped from "accurate TypeScript examples" because it's a generic virtue.

**4. Kept as written:** every specific preference and fact. That includes RORO, no semicolons, maps instead of enums, naming and directory conventions, Zod, next-safe-action, the `@/types/actions` import, the `services/` rule for TanStack Query, `error.tsx` and `global-error.tsx`, and the image rules. These are your choices, and the model can't infer them.

**5. Flags (all left in place for you to decide):**
- **"Tailwind Aria"** is in both files. This is probably meant to be "Tailwind CSS".
- **Vite** is listed in a Next.js 14 App Router stack. Check whether it's still used.
- **FID** has been replaced by INP as a Core Web Vital. Consider changing it to "LCP, CLS, INP".
- **"the action function from next-safe-action"** may be out of date. Newer versions build actions from a client (`createSafeActionClient`). Check this against the version you use.
- **Possible conflict:** `services/` code throws errors, while server actions return expected errors as values. This is fine if they're separate layers, but say so if a server action calls into `services/`.
- **Scope:** `globs: **/*` with a Next.js-only description means the rules also cover Solidity files. Consider narrowing the glob or adding Solidity rules.

**6. Proposed text:** it's in `trimmed.md`.