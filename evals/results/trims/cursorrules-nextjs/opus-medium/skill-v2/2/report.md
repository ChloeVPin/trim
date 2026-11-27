I've saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
`claude-opus-5-5`, as you named it. It has a profile, tested at medium effort. That profile says this model follows wording closely and needs little explicit direction.

## 2. Word count
About 530 words before and about 420 after, roughly 20% shorter. These figures are estimates: the only counting tool I had counted lines, not words.

## 3. Changes
Every cut removes a repeat. No rule was weakened or dropped.
- **Curly braces:** three lines said the same thing ("Avoid unnecessary curly braces", "omit curly braces", "concise one-line syntax"). They're now one line, and the example is kept.
- **Error handling:** six bullets were all forms of "handle errors first and return early" (guard clauses, early returns, happy path last, if-return instead of else). They're now one bullet. Logging and custom error types stay as they were.
- **"Use functional components and TypeScript interfaces":** cut. "Avoid classes" and "Prefer interfaces over types" already cover it.
- **"Use declarative JSX":** cut. "Use functional, declarative programming" already covers it, and the model writes declarative JSX anyway.
- **"Place static content and interfaces at file end":** cut. The file-structure line already sets that order. "Content variables outside render functions" moved onto that line.
- **Responsive design and mobile-first:** these were two lines and are now one.
- **'use client':** this appeared in two places, React/Next.js and Key Conventions item 3. It's now one bullet with every condition kept: favour RSC/SSR, minimise `useEffect` and `setState`, use it only for Web API access in small components, and not for data fetching or state management.
- **Key Conventions section:** its items moved into React/Next.js unchanged ("Rely on App Router for state changes", "Prioritize Web Vitals"), so the heading went.
- **Form validation:** the separate Zod line and react-hook-form + useActionState line are now one bullet.
- **next-safe-action:** I cut "type-safe server actions with proper validation" and "handle errors gracefully". The Zod schema line and the ActionResponse lines already say both. The two ActionResponse lines are now one, which still covers both success and error responses.

## 4. Kept as written
- **Frontmatter:** Cursor reads it, so it's untouched.
- **Your stated preferences:** every one is kept at full strength. That includes no semicolons, `function` and not `const` for components, interfaces over types, maps over enums, named exports, RORO and the directory naming.
- **Project facts the model can't know:** the stack list, the `@/types/actions` import, `services/` throwing errors for TanStack Query, `error.tsx`/`global-error.tsx`, and the WebP and lazy-loading rules.
- **Imports and paths:** wording that names an exact import or path is left verbatim.

## 5. Flags for you (not changed)
- **"Tailwind Aria"** appears twice. Is this a real library you use, or a typo for Tailwind CSS?
- **Next.js 14 and Vite** in the stack list: Next.js projects don't normally use Vite. Check that both still apply, and whether 14 is still the version you're on.
- **FID in "Prioritize Web Vitals":** as far as I know, INP replaced FID as a Core Web Vital in 2024. Swap it if you agree.
- **Possible conflict in server actions:** you ask for useActionState with react-hook-form, and also for next-safe-action returning `ActionResponse`. Recent next-safe-action versions build actions with a client (`createSafeActionClient`) and have their own hooks and result shape. "The action function" may be out of date. This is from my memory, so check it against the docs for the version you use.
- **The Next.js docs link** (Unsure): the model already knows these docs and usually can't open the link inside Cursor. Dropping it saves about 15 words.
- **"Write concise, technical responses with accurate TypeScript examples"** (Unsure): "accurate" adds nothing. The rest is your choice, so I kept it.

I have no suggested additions. The only one the profile names is for loosely specified work across several apps, which doesn't fit a coding-rules file.

## 6. Proposed text
It's all in `trimmed.md`.