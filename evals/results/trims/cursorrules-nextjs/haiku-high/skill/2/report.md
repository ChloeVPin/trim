I saved the proposed version to `/root/trim-sbx/f8572b0870b5/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort. Haiku needs more detail than the larger models, so I cut only duplicates, generic advice, and one vague line.

**2. Words:** about 650 before and about 440 after, roughly a third shorter. These are estimates, since I had no word-count tool.

**3. Changes**

- **Frontmatter kept as is.** It is Cursor's rule config, not instruction text, so I did not touch it.
- **Cut "Prefer server components and Next.js SSR features."** It repeats "Favor RSC" in the React section.
- **Cut "Use declarative JSX."** It repeats "declarative programming" in Key Principles.
- **Cut "Place static content and interfaces at file end."** The file-structure line already says this.
- **Cut "Prioritize Web Vitals (LCP, CLS, FID)."** It is a generic goal, and the image, dynamic-loading, and Suspense rules already serve it. If you restore it, use INP instead of FID, since INP replaced FID as a Core Web Vital in 2024.
- **Cut "Refer to Next.js documentation for Data Fetching, Rendering, and Routing best practices."** Only the docs URL is kept.
- **Cut "Handle errors gracefully and return appropriate responses."** It is covered by the ActionResponse rules.
- **Cut "Implement type-safe server actions with proper validation."** It is generic, and the Zod schema rule covers it.
- **Cut "Use Tailwind CSS mobile-first" as a separate line.** Merged into the responsive design line.
- **Merged three curly-brace lines into one** with the example kept. Merged the four error-handling bullets about early returns, guard clauses, else, and nested ifs into one line.
- **Merged "Model expected errors..." and "Use error boundaries..."** with their wording mostly kept.
- **Removed "accurate" from "accurate TypeScript examples."** It is a generic virtue.

**4. Kept and why**

- **All stack names, versions, and file paths**, since the model cannot know them.
- **The `function`-not-`const` rule, the RORO pattern, the naming and file-structure rules**, since they are your choices.
- **All next-safe-action rules and the `ActionResponse` import**, since they are specific procedures.
- **The `services/` error rule and the error.tsx and global-error.tsx rules**, since they state specific conventions.
- **The `'use client'` sub-rules**, since they carry the conditions for when to use it.

Unsure, kept and flagged:

- "Write concise, technical responses with TypeScript examples." Dropping it saves 8 words. Haiku's default may already be concise, but I have no evidence either way.
- "Consider custom error types or error factories..." This is a soft suggestion. Dropping it saves 11 words.

**Suggested additions (not in the file):** The Haiku profile recommends a real check before a coding agent reports work done. This file has none. You could add something like: "Before reporting code as done, run the project's type check and lint, and fix what they report." I don't know your exact commands, so you would need to fill those in.