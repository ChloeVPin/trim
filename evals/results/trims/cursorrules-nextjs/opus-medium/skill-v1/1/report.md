I saved the proposed version to `trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-opus-5-5`, as you named it. There's a profile for it, tested at medium effort.

**2. Length:** about 550 words before and about 430 after, roughly 22% shorter. I had no counting tool here, so both figures are estimates.

**3. Changes**
- **Opening line:** I changed "You are an expert in…" to "Stack: …". The list of tools is useful information, but the role framing adds nothing for this model. I also dropped "accurate" from the line about responses, because it's a generic virtue.
- **Curly braces:** three lines (23–25) said the same thing about one-line conditionals without braces. They're now one line, with your example kept.
- **File layout:** "Place static content and interfaces at file end" (line 46) overlapped with the file-structure rule (line 22). I moved it into that rule.
- **Error handling:** seven bullets that overlapped (guard clauses, early returns, happy path last, avoiding else, and so on) are now three. Every point is still there.
- **React/Next.js:** "Use functional components" repeated "Avoid classes", so I cut it. "Responsive design with Tailwind" and "mobile-first" are now one line.
- **Server actions:** seven sub-bullets are now two. The cut lines were generic ("handle errors gracefully", "proper validation") or repeated each other: there were three separate lines about returning ActionResponse. The import path, Zod schemas, the action function and the ActionResponse return type all stay.
- **`'use client'`:** this was stated twice (line 48 and Key Conventions #3). It's now only in Key Conventions #3, with the `useEffect`/`setState` part added there.
- **Docs link:** I removed "Refer to Next.js documentation… https://nextjs.org/docs". The model already knows where the Next.js docs are, and the line didn't ask it to do anything specific.

**4. What I kept and why**
- **Frontmatter:** left exactly as written, because Cursor reads it.
- **Your coding conventions:** I kept every one, even where I'd choose differently. That includes no semicolons, interfaces over types, maps instead of enums, `function` rather than `const` for components, RORO, and named exports. These are your preferences, and the model can't know them unless the file says so.
- **Facts:** all names, paths, libraries and file names are unchanged.

**5. Things for you to decide.** I left all of these in the text as written.
- **"Tailwind Aria":** this doesn't seem to be a real library. Did you mean Tailwind CSS or React Aria? Line 44 already says Tailwind CSS.
- **FID:** Google replaced FID with INP as a Core Web Vital in 2024. You might want "LCP, CLS, INP".
- **"Next.js 14":** this may be out of date if the project has moved to a newer version.
- **Error handling conflicts:** "model expected errors as return values" (Server Actions) and "services/ always throw" (for TanStack Query) pull in opposite directions. It might help to say which layer uses which approach.
- **Form validation:** there are three rules for it (Zod, useActionState with react-hook-form, and next-safe-action's Zod schemas). Using useActionState with react-hook-form together is unusual, so check that this is what you intend.
- **Web3 tools:** Solidity, Viem and Wagmi are in the stack list but no rule covers them. If you want conventions for them, they would need to be added.
- **Frontmatter description:** it doesn't mention the web3 part of the stack. That's only worth changing if you use Cursor's agent-requested mode, which reads the description to decide when to apply the rules.

**6. Proposed text:** it's in full in `/root/trim-sbx/55929d22fed0/trimmed.md`.