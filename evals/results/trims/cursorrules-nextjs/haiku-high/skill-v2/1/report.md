The trimmed version is in `/root/trim-sbx/9acd5218e27e/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. The cuts below follow that profile: Haiku needs more explicit detail than the larger models, so I kept every procedure, example and fact, and cut only duplication.

**2. Size:** about 560 words before and about 475 after, roughly 15% shorter. These are my hand counts; no word-count tool was available in this session. The frontmatter is unchanged.

**3. Changes**
- **Curly-brace rules merged (3 lines into 1).** They said the same thing twice. The one-line example is kept.
- **Error-handling rules merged.** "At the beginning", "early returns" and "guard clauses" overlapped. The happy-path and if-return lines are kept.
- **Component rules merged.** "Functional components and interfaces" and "function, not const" are one line. "Declarative JSX" was cut because the "declarative programming" rule already covers it.
- **Responsive-design rules merged.** "Responsive with Tailwind" and "mobile-first" are one line.
- **Static-content placement cut.** "Place static content at file end" repeats the file-structure line.
- **Error-boundary line shortened.** The wording is tighter; the files and the fallback UI are still named.
- **Server-action rules merged and cut.** "Utilize the action function" repeated the `next-safe-action` line. "Type-safe with proper validation" repeated the Zod-schema line. "Handle errors gracefully" was absorbed into the consistent-responses line. The `import type` line is kept verbatim.
- **Server-component line cut.** "Prefer server components and SSR features" was covered by "Favor RSC" and the App Router rule. The SSR wording is the only thing lost, so restore it if you want it.

**4. Kept**
- The stack list, naming, file layout, RORO, `function` keyword, no semicolons, and the `services/` rule. These are choices the model cannot infer.
- The `use client` and Server Action rules, and the `ActionResponse` import. They are fragile to get wrong.
- Frontmatter, exactly as written.

**5. Flags and suggestions**
- **Frontmatter may not parse.** `globs: **/*` is unquoted. In YAML, a plain value starting with `*` is read as an alias, so a strict parser may reject it. I left it alone because a program reads it. Quoting it (`globs: "**/*"`) is the safe fix if your tool reads it as YAML.
- **Stack list names tools no rule covers.** Solidity, Viem, Wagmi and Vite appear in the first line, but nothing else mentions them. If this project does not use them, remove them.
- **Version mismatch.** The file pins Next.js 14, but the docs link goes to the current Next.js docs. Consider pinning a versioned docs link or dropping it.
- **Possibly stale metric.** I believe Google replaced FID with INP as a Core Web Vital in 2024. I did not check a source for this, so verify it before changing the line.
- **Conflict to check.** `services/` must always throw, but the Server Actions rule says to return expected errors as values. If Server Actions call services, the two rules collide. Which one should win?
- **Unclear wording, kept as written.** "Tailwind Aria" may be a typo. "Avoid enums, use maps" could mean `Map` objects or plain object lookups.
- **Unsure lines, kept.** Each is short. Dropping them saves about 25 words in total: "Prefer iteration over duplication", "Implement proper error logging", "Consider custom error types", and "Prioritize Web Vitals".
- **Suggestion: add a real-check line.** The Haiku profile recommends a line telling a coding agent to run a real check before reporting a change done. For example, "run `tsc --noEmit` and lint before reporting done". Tell me which commands this project uses and I'll write the line.

**6. Proposed text:** `/root/trim-sbx/9acd5218e27e/trimmed.md`, including the frontmatter.