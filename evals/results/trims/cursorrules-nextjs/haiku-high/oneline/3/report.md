I saved the proposed version to `/root/trim-sbx/1c367ba61cc8/trimmed.md`. `instructions.md` is unchanged. The trimmed file is about 45 lines against the original's 76, with the same rules grouped by topic.

**Audit of instructions.md**

- **Cursor metadata:** The frontmatter (`globs`, `alwaysApply: false`) is Cursor-specific. I dropped it. Restore it if the file is still read by Cursor.
- **Duplicates:** `'use client'` guidance appears in both the React section and Key Conventions. Curly-brace rules appear twice. The Shadcn/Radix/Tailwind line is repeated. Zod form validation is stated twice. Mobile-first and responsive design overlap. I merged each into one rule.
- **Vague wording:** "Prioritize," "Favor," "Rely on," and "Consider" rules are hard for a smaller model to act on. I kept them but made the action concrete where the original allowed it.
- **Long technology list:** The opening line lists about 11 technologies. I kept them as a single stack line, since the rules only need to name the libraries they use.
- **Outdated metric:** The original cites FID. Google replaced FID with INP in 2024, so I changed it to INP. This is a content change, so check it.
- **Ambiguous terms:**
  - "Tailwind Aria" is not a standard name. I kept it verbatim. It may mean `tailwindcss-aria-attributes`, or it may be a typo for Tailwind CSS.
  - "Next.js 14" should be checked against the project's actual `package.json`.
- **Possible conflict:** Server actions must return `ActionResponse`, but `next-safe-action` has its own result shape. The rule needs a note on how the two fit together.
- **Error-handling split:** `services/` throws errors, while server actions return them. This is intentional but easy to misread, so I stated it explicitly.

**Questions for you**

1. Is "Tailwind Aria" meant literally?
2. Should the `ActionResponse` rule say how it wraps `next-safe-action` results? I did not invent a shape.
3. Is the Next.js version 14, or should the file avoid pinning one?