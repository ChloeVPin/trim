I saved the proposed version to `/root/trim-sbx/dbdf93085476/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile was tested at high effort. Haiku needs more explicit detail than the larger models, so I cut only duplicates and left the procedures alone.

**2. Length:** about 620 → about 510 words, roughly 18% shorter. These are my estimates; I had no word-count tool here. The frontmatter is byte-for-byte unchanged.

**3. Changes**
- Merged three conditional-brace lines into one with the example kept.
- Merged the four overlapping early-return, guard-clause, and else lines into one bullet. Kept the happy-path-last rule.
- Dropped "Use functional components and TypeScript interfaces" (covered by lines 11, 21, 42), "Use declarative JSX" (covered by line 11), and "Place static content and interfaces at file end" (covered by the file-structure line).
- Merged the two responsive-design lines.
- Shortened "Minimize 'use client'…" to the `useEffect`/`setState` rule, since the Key Conventions block already covers `use client`.
- In the next-safe-action block, dropped the generic "Implement type-safe server actions" and "Handle errors gracefully" lines and merged the rest.
- Put the Next.js docs URL on the same line as its reference.
- Removed trailing double spaces (no effect on meaning).

**4. Kept as written:** the frontmatter, the stack list, the file-structure order, the error-handling and happy-path procedure, the Server Action rules (`return` vs `try/catch`, `useActionState`, `ActionResponse`, the exact import), the error-boundary files, the `services/` rule, the Web Vitals priority, and the `use client` rules. Haiku's profile says to keep procedures and examples, and this file has no blanket search lines to cut.

**5. Flags for you to decide**
- **"Tailwind Aria"** (lines 6 and 43): unclear. Line 44 says Tailwind CSS. Is there a specific package you mean?
- **Version pins:** Next.js 14, Viem v2, and Wagmi v2 may be out of date. Check them.
- **FID** (Key Conventions 2): from my own knowledge, not checked against a source in this session, Google replaced First Input Delay with INP as a Core Web Vital in 2024. Consider updating.
- **Possible conflict:** line 56 says `services/` code "always throw," while line 53 says expected errors in Server Actions should be returned as values. If `services/` is called from Server Actions, these disagree. I left both as written.
- **Two form-validation approaches:** Zod (line 49) and react-hook-form with `useActionState` (line 55). Not a conflict as written, but check which one you intend.
- **Unsure, kept:** "Consider using custom error types or error factories" (about 14 words; dropping it saves that much). "Rely on Next.js App Router for state changes" is vague: does it mean navigation or refetching?

**6. Suggestions, not added to the text**
- For a coding agent, the profile recommends a check before reporting done. For example: "Before reporting a change done, run a real check (type-check, lint, or tests) and report the result."
- If the agent tends to stop early, the profile suggests: "Keep working until the task is done."