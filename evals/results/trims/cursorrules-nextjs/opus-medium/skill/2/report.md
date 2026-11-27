I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, which you named. Its profile has been tested at medium effort.

**Words:** about 560 before and about 370 after, a cut of roughly a third. These are estimates, because I had no tool here to count words.

## Changes

- **"You are an expert in…" became "Stack: …".** I kept every technology and version, since those are facts the model can't guess. The role-play framing doesn't change how this model behaves.
- **Cut "Prefer iteration and modularization over duplication."** It's general advice the model already follows.
- **Merged three lines about curly braces into one.** They all said the same thing, and I kept the `if (condition) doSomething()` example because it fixes the exact form you want.
- **Merged seven error-handling lines into one.** Early returns, guard clauses, happy path last and if-return instead of else were all the same rule. I also dropped the "Prioritize error handling" lead-in.
- **Cut "Use functional components and TypeScript interfaces" and "Use declarative JSX".** "Avoid classes" and "Prefer interfaces" already cover the first. The second is what the model does anyway.
- **Cut "Place static content and interfaces at file end".** The file-structure line already says this.
- **Merged the two "minimize 'use client'" passages into one line.** One was in React/Next.js and one in Key Conventions #3. The merged line keeps all the specifics: Web API access only, small components, and never for data fetching or state.
- **Merged the two form-validation lines.** "Use Zod" and "useActionState with react-hook-form" are now one line.
- **Shortened the next-safe-action block.** I cut "proper validation" and "handle errors gracefully", which are general advice and already covered by the Zod schemas. I kept the `action` function, the import path and the rule that every action returns `ActionResponse`.
- **Shortened the Server Actions and error.tsx lines.** I kept their content and removed the restated headings.
- **Cut "Refer to Next.js documentation… https://nextjs.org/docs".** It's a general pointer that gives the model no project-specific facts.

## What I kept, and why

- **Every project-specific choice:** RORO, `function` rather than const for components, no semicolons, maps instead of enums, the file order, the `services/` error rule for TanStack Query, the `@/types/actions` path, Suspense, dynamic loading, the image rules, and App Router for state changes.
- **The frontmatter, unchanged.** It's Cursor configuration, not instructions to the model.
- **Nothing here guards risky or irreversible work,** so that rule from the trim process didn't come into play.

## Flagged for you (kept as written)

- **"Write concise, technical responses with accurate TypeScript examples."** Opus probably does this already, and "accurate" asks for nothing specific. Dropping it saves about 9 words.
- **"Implement proper error logging and user-friendly error messages."** This is mostly general advice, since the `services/` rule already asks for user-friendly errors. Dropping it saves about 8 words.
- **Things that look like mistakes in the original.** I didn't change these because only you can confirm them:
  - "Tailwind Aria" may be meant as Tailwind CSS or React Aria.
  - Vite is listed alongside Next.js 14, which usually doesn't use Vite.
  - Web Vitals lists FID, which INP replaced in 2024.
  - The description mentions only Next.js, but the stack also includes Solidity, Viem and Wagmi.