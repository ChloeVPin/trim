I saved the shorter version to `/root/trim-sbx/2a9f6377df93/trimmed.md`. `instructions.md` is unchanged.

**Audit of instructions.md**

- **Outdated:** "Prioritize Web Vitals (LCP, CLS, FID)". FID was replaced by INP in 2024, so I changed it to INP.
- **Duplicated:** The `'use client'` guidance appears in both the React section and Key Conventions. The three rules about curly braces and one-line conditionals overlap. Form validation with Zod is stated twice. The early-return and no-`else` rules repeat each other.
- **Vague or unclear:** "Tailwind Aria" is not a recognized library name, so I dropped it and kept Tailwind CSS and Radix. "Use 'use client' only for Web API access in small components" is hard to apply, so I rewrote it as a direct rule.
- **Unused:** The role line names Solidity, Viem, Wagmi, Vite, and Node.js, but no rule covers them. I removed them from the role line. The Next.js docs link is also gone, since a model can't follow a link mid-task.
- **Undefined:** The `ActionResponse` type is required in every server action, but the file doesn't define its shape, and `@/types/actions` may not exist in the repo. A model will have to guess the shape. I kept the import rule but didn't invent a definition.
- **Cursor-specific:** The frontmatter (`globs`, `alwaysApply`) only matters to Cursor. I kept it unchanged in case something reads it.

**Choices in trimmed.md**

- I kept the rules as short imperatives grouped under headings. Smaller models follow short, unambiguous rules more reliably than long prose.
- I merged the duplicates and dropped the stack names and the docs link.
- I didn't add examples, because I didn't want to invent code the repo doesn't use.

This is a judgment call based on general principles for smaller models. I haven't tested it against claude-haiku-5-5.

**Questions for you**

1. Are Solidity, Viem, and Wagmi used in this repo? If so, the Web3 rules need to come back.
2. What does `ActionResponse` look like in your codebase? If you share it, I can add a short example.
3. Is "Tailwind Aria" a specific package you use? If it is, I'll restore it with the correct name.