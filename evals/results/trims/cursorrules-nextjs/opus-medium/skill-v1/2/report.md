I saved the proposed version to `/root/trim-sbx/d364562560a5/trimmed.md`. `instructions.md` is unchanged.

## 1. Target model
**claude-opus-5-5**, which you named. The skill has a tested profile for it. That profile says this model follows wording closely and needs little hand-holding. But this file is almost entirely your coding preferences, and the model can't guess those, so I kept nearly all of them. The cuts are mostly repeats.

## 2. Word count
About **600 words before and 430 after (roughly 28% shorter)**. These are estimates: I didn't have a word-count tool in this session.

## 3. Changes
- **Opening line**: "You are an expert in X, Y, Z" became "Stack: X, Y, Z". The list of technologies is the useful part; the "expert" framing adds nothing.
- **"accurate" TypeScript examples**: dropped "accurate". It's a general virtue that changes nothing.
- **Curly braces**: three bullets said the same thing ("avoid unnecessary braces", "omit braces for single-line", "one-line syntax"). They're now one bullet, and the example is kept.
- **`function` keyword**: the rule for pure functions and the rule for components ("function, not const") are now one line.
- **File structure**: "Place static content and interfaces at file end" repeated the file-order rule, so it's folded into it.
- **Functional components / declarative JSX / TypeScript interfaces** (React section): cut. They repeat "functional, declarative, avoid classes" and "prefer interfaces" from earlier.
- **Error handling**: seven sub-bullets became four. "Prioritize error handling", "early returns", "guard clauses" and "happy path last" overlapped heavily. Every distinct preference is still there.
- **Responsive design**: the two lines (Tailwind, mobile-first) are now one.
- **'use client'**: this appeared in both the React section and Key Conventions #3. It's now one bullet with all the conditions kept: favor RSC/SSR, Web API access only, small components, never for data fetching or state.
- **Key Conventions**: the section is folded into React/Next.js. App Router, Web Vitals and the docs link all stay.
- **next-safe-action**: cut the generic sub-bullets ("type-safe with proper validation", "handle errors gracefully"). Kept the specifics: the action function, Zod input schemas, the exact `ActionResponse` import line, and that every action returns `ActionResponse`.
- Removed the trailing double spaces.

## 4. What I kept, and why
- **Frontmatter**: unchanged, because Cursor reads it.
- **Every convention**: semicolons, RORO, named exports, dash-case directories, maps instead of enums, `services/` errors for TanStack Query, error.tsx/global-error.tsx, the image rules, Suspense and dynamic loading. These are your preferences, and the model can't know them unless told.
- **Exact paths, names and the docs URL**.

There were no rules guarding risky or irreversible actions, so nothing needed to stay word-for-word for that reason.

## 5. Flags and suggestions (all kept as written; your call)
- **"Tailwind Aria"** appears twice. Did you mean Tailwind CSS, or a specific package? If the package doesn't exist, the model may make up its API.
- **FID** was replaced by **INP** as a Core Web Vital in 2024. Consider "LCP, CLS, INP".
- **"Next.js 14"**: check this still matches the project. A pinned version steers the model toward that version's APIs.
- **Vite alongside Next.js** is unusual. Keep it only if Vite really is part of this repo, for example for a separate package.
- **Possible conflict in form and error handling**: Zod, react-hook-form, useActionState and next-safe-action are all named for validation or errors, and the file never says how they fit together. Separately, `services/` code *throws* errors, while Server Actions *return* expected errors. That may be deliberate (different layers), but one line saying which applies where would remove the ambiguity.
- **`globs: **/*` with `alwaysApply: false`**: the rule matches every file. If it's meant for TS/TSX only, narrow the glob. I left it alone because it's frontmatter.

The full text is in `/root/trim-sbx/d364562560a5/trimmed.md`.