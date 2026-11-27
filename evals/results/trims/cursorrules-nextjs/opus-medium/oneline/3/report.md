I saved the shorter version as `trimmed.md`. It's about 30% shorter, and `instructions.md` is unchanged. Every rule from the original is still in it. The savings come from merging repeated rules, not from dropping any.

**What I cut or merged:**
- **Braces in `if` statements:** stated three times (lines 23–25). Now one rule with the example.
- **Early returns:** lines 30–34 said the same thing five different ways (guard clauses, early returns, no nesting, happy path last, no `else`). Now one bullet.
- **`'use client'`:** covered in both line 48 and lines 70–73. Merged into one bullet.
- **Other overlaps:**
  - "Avoid classes" and "functional components" became one rule.
  - "Use `function` for pure functions" and "use `function` for components" became one rule.
  - "Place static content and interfaces at file end" was already covered by the file-order rule.
  - Interfaces were mentioned twice.
- **"You are an expert in…":** a role line like this adds little for Opus 5.5. I kept the tech list as a plain `Stack:` line because it does tell the model what the project uses.
- **The nextjs.org/docs link:** the model already knows the Next.js docs, so the pointer adds nothing.
- **Layout:** sections now use headings and short bullets instead of a mix of numbered and nested lists.

**One edit that changes a meaning:** I replaced FID with INP in the Web Vitals list, because Google replaced FID with INP in March 2024. If you'd rather keep FID, change it back.

**Problems in the original that I left alone because they're your call:**
1. **`useActionState` doesn't exist in Next.js 14.** It comes with React 19, which Next.js 15 uses; Next.js 14 has `useFormState`. Either update the version in the stack line or change the hook name.
2. **The `description` field doesn't match the content.** It says "Next.js with React and TypeScript", but the rules also cover Solidity and the Viem/Wagmi web3 libraries.
3. **"Tailwind Aria" isn't a library name I recognize.** If you meant React Aria or `tailwindcss-react-aria-components`, name it exactly so the model doesn't guess.
4. **Vite is listed alongside Next.js.** That's unusual unless the repo has a separate Vite app. Drop it if there isn't one.
5. **"Use the `action` function from next-safe-action" may be outdated.** Recent versions use a client built with `createSafeActionClient`. I wrote that rule in neutral terms so it doesn't name a specific API.
6. **`globs: **/*` with `alwaysApply: false`** applies the rule to every file anyway. That's harmless, but you could narrow the globs to `**/*.{ts,tsx}`.