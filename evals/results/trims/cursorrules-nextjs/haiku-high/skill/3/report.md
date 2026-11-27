I saved the proposed version to `/root/trim-sbx/b90da3b8f26f/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. It has a profile, tested at high effort.

**2. Words:** about 555 before and about 445 after, a cut of roughly 20%. I have no word-count tool here, so these are hand counts.

**3. Changes**

- **Merged three conditional-brace lines into one** with the example kept. The three said the same thing.
- **Merged the three early-return and guard-clause lines into one.** They overlapped.
- **Dropped "Place static content and interfaces at file end."** The file-structure line already says this.
- **Dropped "Use declarative JSX" and "Use functional components and TypeScript interfaces."** Both repeat the principles and the TypeScript section.
- **Merged the mobile-first line into the responsive-design line.**
- **Merged the three `'use client'` lines.** The React section and Key Conventions gave the same rule three times. The merged line keeps every specific rule: server components first, `'use client'` only for Web API access in small components, and never for data fetching or state management.
- **Dropped the vague or duplicated server-action lines:** "Implement type-safe server actions with proper validation", "Handle errors gracefully and return appropriate responses", and "Implement consistent error handling and success responses using ActionResponse". The `ActionResponse` rule itself is kept.
- **Shortened the Zod line** to "Define action input schemas with Zod." The Zod form-validation line is kept.
- **Removed generic virtues:** "accurate" and "proper".
- **Replaced the Next.js docs sentence** with the URL and a short pointer.

**Kept as written:** the stack list, the naming and file-structure rules, the `function` keyword and semicolon rules, the RORO pattern, the `useActionState` and `react-hook-form` rules, the expected-error rule for Server Actions, the error-boundary rule, the `services/` error rule, the `ActionResponse` import and return rules, and the `globs` and `alwaysApply` front matter. None of them guard fragile or irreversible work, but the Server Action and `services/` rules define how errors flow through the code, so I left them unchanged.

**4. Not cut, and why**

- **"Consider custom error types or error factories…"** is optional wording. It may be the only line that changes what the model does, so I kept it. Dropping it saves 12 words if you agree.
- **"Rely on Next.js App Router for state changes"** is vague, but it is your choice and short. Kept.

**Suggested additions (not applied):**

- **Add a done check for coding work.** Haiku 5.5's profile says coding agents need an instruction to run a real check before reporting done, for example: "Before reporting a change as done, run the relevant typecheck, build, or tests and report the result."
- **Add one RORO example** if you want Haiku to apply the pattern reliably. The profile says Haiku benefits from more concrete detail than the larger models.

**Things for you to check:**

- **"Tailwind Aria"** appears in the stack list and in the styling rule. I don't recognise it as a library. You may mean Tailwind CSS, or a different Aria-related package. I left it as written.
- **"FID"** in Web Vitals: Google replaced First Input Delay with Interaction to Next Paint as a Core Web Vital in 2024. I left it as written.