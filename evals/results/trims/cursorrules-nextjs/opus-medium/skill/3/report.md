I saved the proposed version as `trimmed.md`. `instructions.md` is unchanged.

**Target model:** `claude-opus-5-5`, as you named it. Its profile says it has been tested.

**Word count:** about 590 before and about 390 after, roughly a third shorter. I had no counting tool in this session, so both figures are estimates.

## Changes
| Original | Change | Reason |
|---|---|---|
| "You are an expert in…" | Became "Stack: …" with the same list | The list of tools and versions (Viem v2, Wagmi v2, Tailwind Aria) is what matters. The "expert" framing adds nothing for this model. |
| Lines 23–25 (three rules about curly braces) | Merged into one line | All three say the same thing. |
| Lines 29–34 (six error-handling bullets) | Merged into one line | "Prioritize error handling", "early returns", "guard clauses", "happy path last" and "avoid else" are one rule. |
| "Use functional components and TypeScript interfaces", "Use declarative JSX" | Cut | Already covered by "functional, declarative programming" and "Prefer interfaces". |
| "Use function, not const, for components" | Merged into the `function` keyword rule | Same rule, now in one place. |
| "Place static content and interfaces at file end" | Cut | Already covered by the file-structure line. |
| Key Conventions item 3 and "Minimize 'use client'…" in React/Next.js | Merged into one bullet | The same rule was stated twice. I kept all of its conditions (Web API access only, small components, never for data fetching or state). |
| Key Conventions items 1–2 | Moved into React/Next.js | This removes a section header. The wording is unchanged. |
| "Refer to Next.js documentation… https://nextjs.org/docs" | Cut | It's a general pointer with no specific instruction. The model already knows the docs. |
| next-safe-action: "type-safe… with proper validation", "Handle errors gracefully" | Cut | They're generic, and the Zod-schema and ActionResponse lines already cover them. |
| next-safe-action: the two ActionResponse bullets | Merged | Same requirement. |
| "accurate" in the first principle | Cut | The model aims for accuracy anyway. |

## Kept
- **Every concrete choice:** the RORO pattern, no semicolons, interfaces over types, maps instead of enums, directory naming, named exports, Zod, react-hook-form with useActionState, the `@/types/actions` import path, the `error.tsx` and `global-error.tsx` files, TanStack Query errors in `services/`, the image rules, Suspense and dynamic loading. The model can't know any of these without being told.
- **The frontmatter**, word for word. Cursor reads it.
- None of the rules cover risky or irreversible actions, so the skill's rule about keeping those exactly as written didn't come into play.

## For you to decide
1. **FID in "Prioritize Web Vitals (LCP, CLS, FID)":** Google replaced FID with INP as a Core Web Vital in 2024. I left it as you wrote it. You may want INP there.
2. **"Consider custom error types or error factories":** I kept this because it records a design choice. If you don't feel strongly about it, dropping it saves 10 words.
3. **"Write concise, technical responses with TypeScript examples":** this is close to what Opus 5.5 does by default. Dropping it saves 7 words, but I kept it because it records your preferred style.
4. **Possible conflict:** expected errors in Server Actions are returned as values through useActionState, while code in `services/` throws for TanStack Query. Both are kept as written, but it may help to say which layer each rule applies to.