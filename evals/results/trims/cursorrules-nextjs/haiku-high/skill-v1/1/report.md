I saved the proposed version to `/root/trim-sbx/cce1944d1f16/trimmed.md`. `instructions.md` is unchanged.

**1. Target model:** `claude-haiku-5-5`, named by you. The profile is tested at high effort. Haiku needs more detail than the larger models, so I cut conservatively.

**2. Size:** I have no word-count tool in this session, so these are estimates: about 680 words before and about 560 after, roughly an 18% cut. The frontmatter is unchanged.

**3. Changes and reasons**
- **Curly-brace rules (old lines 23–25):** three lines said the same thing. Merged into one bullet.
- **Guard clauses and early returns (old lines 30, 31, 34):** three overlapping points merged into one sub-bullet.
- **Components and JSX (old lines 40–42):** merged into two bullets. The `function`-not-`const` rule moved to the JavaScript section, where it sits with the other `function` rule.
- **Responsive design (old lines 44–45):** one line instead of two saying the same thing.
- **Static content (old lines 46–47):** line 46 repeated the file-structure order already in line 22. Merged into one line.
- **Server Actions (old lines 58, 61):** "type-safe server actions with proper validation" and "handle errors gracefully" were generic. The Zod and ActionResponse lines already cover them, so I dropped them.
- **ActionResponse (old lines 63–64):** same point twice. Merged.
- **`use client` (old lines 70–73):** repeated old line 48 and the same rule. Folded into item 3 of Key Conventions. Line 48 stays as its own bullet because it also covers `useEffect` and `setState`.

**4. Kept, and why**
- **Frontmatter:** Cursor reads it, so it stays exactly as written.
- **Stack list, the RORO pattern, named exports, semicolon and brace style:** these are author preferences the model cannot infer.
- **Error-handling procedure, Server Actions pattern, and the `ActionResponse` import line:** Haiku needs the steps and examples that carry a procedure. The import line is code, so I kept it exact.
- **"Consider custom error types":** the wording is hedged, but it is your preference, so I kept it.
- **Docs link:** kept, since the model cannot know the exact URL.

**5. Flags and suggestions**
- **Flag, FID:** First Input Delay was replaced by Interaction to Next Paint (INP) as a Core Web Vital in March 2024. I kept FID as written. Consider changing it to INP.
- **Flag, "Tailwind Aria":** I don't recognise this as a package name. Check whether you mean a specific package such as `tailwindcss-aria-attributes`.
- **Flag, Vite:** Vite is in the stack list, but the rules are Next.js-only. Clarify whether Vite projects are covered.
- **Flag, possible conflict:** `services/` code throws errors, while Server Actions return them as `ActionResponse`. If a Server Action calls a service, the rules don't say where the throw becomes a return value.
- **Flag, version:** the file says Next.js 14. If the project has moved on, update it.
- **Suggestion, coding agents:** the Haiku profile recommends adding a line that the agent must run a real check (type-check, lint, or tests) before reporting a change done. I did not add it to the text. It is an addition for you to decide on.
- **Suggestion, agents that stop early:** if the agent tends to stop before the task is finished, add a line to keep working until the task is done. Also optional.

**6. Proposed text:** in `/root/trim-sbx/cce1944d1f16/trimmed.md`.