I saved the shorter version as `trimmed.md` and left `instructions.md` unchanged. It drops from 75 lines to about 34, and the frontmatter is identical so Cursor will treat it the same way.

**What I cut or merged:**
- **Repeated rules.** The curly-brace rule appeared three times and the `'use client'` rule twice. "Function keyword" was split across the TypeScript and React sections, and "functional components / TS interfaces" and "static content at file end" repeated other lines. Each now appears once.
- **Error-handling list.** Seven bullets on early returns, guard clauses, happy path last and avoiding `else` all said the same thing, so they're now one bullet.
- **next-safe-action list.** Seven sub-bullets ("handle errors gracefully", "proper validation", and so on) became the two rules that actually matter: use a Zod schema, and always return `ActionResponse`.
- **Generic filler.** I removed the "You are an expert…" persona, "write concise, technical responses", and the link to the Next.js docs. Opus 5.5 doesn't need these to follow the rules.
- **Structure.** Related rules are grouped under headings, and the numbered "Key Conventions" list is folded into the React section.

**Things I changed because they looked wrong:**
- I read **"Tailwind Aria"** as Tailwind CSS. No library by that name exists, and line 44 of the original already says Tailwind CSS. Change it back if you meant something else, such as React Aria.
- I replaced **FID** with **INP**, since Google retired FID as a Core Web Vital in 2024.

**Things I kept but you should check:**
- **Next.js 14 vs `useActionState`.** `useActionState` needs React 19, which comes with Next.js 15. On Next.js 14 the equivalent is `useFormState`. Either the version or the hook name is out of date.
- **Unused parts of the stack.** Solidity, Vite, Viem and Wagmi are listed but no rule mentions them. I kept them as a one-line stack summary. Drop them if this project doesn't use them, or add rules if it does.
- **"`action` function from next-safe-action".** Current versions of the library use `createSafeActionClient()`, so I left out the function name and just said to use next-safe-action.
- **Two error patterns.** Server actions return errors as values, while code in `services/` throws for TanStack Query. Those don't actually conflict, so I kept both, written so it's clear which applies where.