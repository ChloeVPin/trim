I've saved the proposed version to `trimmed.md` and left `instructions.md` unchanged.

**Target model:** claude-opus-5-5, which you named. Its profile was tested at medium effort.

**Word count:** about 530 before and 415 after, roughly 22% shorter. I had no shell to run a counter, so both figures are hand estimates.

## Changes
| Original | Change | Reason |
|---|---|---|
| Three curly-brace lines (23–25) | Merged into one | All three say the same thing. |
| Seven error-handling bullets (29–35) | "Prioritize…", early returns, guard clauses, happy path last and if-return combined into one line | Five bullets describe one pattern. |
| "Use functional components and TypeScript interfaces" | Cut | Already covered by "functional, declarative… avoid classes" and "prefer interfaces". |
| "Use declarative JSX" | Cut | Repeats "functional, declarative programming". |
| Responsive design + mobile-first | Merged | Same rule. |
| "Place static content and interfaces at file end" | Cut | The file-structure line already puts static content and types last. |
| "Minimize 'use client', 'useEffect', 'setState'. Favor RSC" | Merged into Key Conventions #3 | The 'use client' rule appeared twice. |
| next-safe-action sub-bullets (7 → 2) | "Type-safe with proper validation" and "handle errors gracefully" cut; the three ActionResponse lines merged into one | The cut lines are generic and covered by the Zod and ActionResponse rules. The import path and return type are kept word for word. |
| "You are an expert in…" | Changed to "Stack: …" | Every tool name is kept, since those are facts the model can't guess. The persona framing doesn't change how Opus 5.5 behaves. |

## Kept as written
- **Frontmatter:** Cursor uses the `globs` and `alwaysApply` settings.
- **Every specific fact:** library versions, `@/types/actions`, `error.tsx` and `global-error.tsx`, `services/` and TanStack Query, the RORO pattern, naming formats, no semicolons, function components, Web Vitals.
- **Your style choices:** concise replies, maps instead of enums, named exports, custom error types.

## Please check these
1. **The two form-validation rules seem to conflict.** One says "Use Zod for form validation" and another says "Use useActionState with react-hook-form for form validation." I kept both. If you mean react-hook-form plus a Zod schema, you could write that as one line.
2. **"Tailwind Aria" may be a typo.** I don't know of a library by that name. If you meant Tailwind CSS, fix it in both places it appears. A wrong library name could lead the model to invent imports.
3. **The FID metric is out of date.** Google replaced FID with INP as a Core Web Vital in 2024. Consider changing it to "LCP, CLS, INP".
4. **"Refer to Next.js documentation…" and its link:** I kept this but flagged it. Opus 5.5 already knows those docs, so the line adds little, and it could prompt needless fetching. Dropping it saves about 13 more words.
5. **"Write concise, technical responses":** Opus 5.5 is fairly concise by default, but I kept the line as your choice. Dropping it saves 7 words.