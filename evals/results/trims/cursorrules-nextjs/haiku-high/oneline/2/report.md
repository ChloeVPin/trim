I saved the shorter version to `/root/trim-sbx/bbfec449c4a2/trimmed.md`. `instructions.md` is unchanged. The file went from 65 non-blank lines to 42, and the frontmatter is kept as-is.

## Audit of instructions.md

- **Stack line lists tools with no rules:** Solidity, Viem, and Wagmi appear, but nothing in the file uses them. Vite also appears alongside Next.js, which conflicts with the rest of the file. I dropped all four from the stack line.
- **TanStack Query is used but not listed:** The services rule depends on it, so I kept it in the rule but it is absent from the stack line.
- **Outdated Web Vital:** FID was replaced by INP as a Core Web Vital in 2024. I changed it to INP.
- **Duplicates:** The `'use client'` and RSC guidance appears three times (React section, Key Conventions 3, and the "minimize" bullets). The curly-brace rule appears twice. "Mobile-first" and "responsive with Tailwind" overlap. I merged each into one bullet.
- **Vague or non-actionable lines:** "Write concise, technical responses" and "Prioritize Web Vitals" are kept but tightened. The Next.js docs URL is removed, since the model cannot browse.
- **Restructuring for a smaller model:** I grouped the rules under short headings and wrote them as imperatives with one example each. Haiku follows direct rules more reliably than long prose lists. I have not measured this against Haiku, so treat it as a judgment call.

## Decisions to confirm

1. **Vite:** I treated it as leftover. If any part of the project still uses Vite, add it back.
2. **Solidity, Viem, Wagmi:** I removed them because there are no rules for them. If you want them, a short rule for each would be needed.
3. **"Tailwind Aria":** I kept the phrase unchanged, but it is ambiguous. I think you may mean `tailwindcss-react-aria-components` or a similar package. Please confirm the exact name.
4. **`useActionState` with react-hook-form:** I kept this pairing as written. Combining them is unusual, so check that it matches how your forms actually work.