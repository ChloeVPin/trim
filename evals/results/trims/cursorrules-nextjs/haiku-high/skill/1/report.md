I wrote the proposed version to `/root/trim-sbx/ccc98a68ea6c/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, as you named it. It has a profile, tested at high effort. Haiku needs more explicit detail than the larger models, so I kept every procedure and every example.

**2. Length:** I have no word-count tool here, so these are my hand counts. The body went from about 535 words to about 395, roughly 26% shorter. The frontmatter (about 17 words) is unchanged in both.

**3. Changes**
- **Merged three curly-brace lines** into one line with the example. They said the same thing three times.
- **Merged the error-handling bullets** (edge cases first, early returns, no `else`, guard clauses, happy path last) into two bullets. Each rule is still there.
- **Removed "Prefer iteration and modularization over duplication."** It is a generic virtue the model already follows.
- **Removed "accurate"** from the first bullet. It is a generic virtue.
- **Removed "Implement type-safe server actions with proper validation" and "Handle errors gracefully and return appropriate responses."** Both are covered by the Zod-schema and `ActionResponse` lines.
- **Folded "consistent error handling and success responses using ActionResponse"** into the `ActionResponse` bullet.
- **Removed "Place static content and interfaces at file end."** The file-structure line already gives the order.
- **Merged the two responsive-design lines** and the two form-validation lines.
- **Removed "Minimize 'use client'" from the React section.** It duplicated Key Conventions 3. The `useEffect`/`setState` part stays.
- **Shortened the error-boundary line** and the error-logging line without dropping their rules.

**4. Kept, and flagged as unsure:** These could go if you agree, and the trimmed file still contains them.
- "Consider custom error types or error factories…" The hedge may do little. Dropping it saves about 12 words.
- "Rely on Next.js App Router for state changes." It is vague. Dropping it saves about 8 words.
- "Prioritize Web Vitals (LCP, CLS, FID)." FID was replaced by INP as a Core Web Vital in March 2024, so you may want INP here. I did not change it in the file. Dropping the line saves about 5 words.
- The Next.js docs link. It only helps if the model can fetch the page. Dropping it saves about 14 words.

**Kept as written:** the stack and version list, the naming and formatting rules, RORO, file structure, the server-action procedure and its import line, the error-boundary files, the `services/` rule, and the `'use client'` rules. I did not change the frontmatter.

**Possible typo to check:** "Tailwind Aria" appears on lines 6 and 43. I left it alone. Did you mean something else, such as the ARIA plugin?

**Suggestions, not added to the file:** the profile suggests two lines for Haiku. Add them only if they fit how the file is used.
- For a coding agent: "Before reporting a change done, run the type check and the tests that cover it."
- Only if the model stops early on long tasks: "Keep working until the task is done."