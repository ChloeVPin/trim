## Prompt audit: `instructions.md`

**Assumptions (Step 0)**
- **Scope:** `instructions.md` only, as the request named it. It is the only file in the workspace. The directory is not a git repo, so there is no `git blame` provenance.
- **Target model:** `claude-haiku-5-5`, from the request. The file is a Cursor rules document, so no Claude agent reads it directly.

**Summary**

The file is mostly stack context and team conventions, which the audit keeps. It has no pressure language (no MUST/NEVER/CRITICAL), no prefill or JSON scaffolding, and no thinking-steering prose. One factual claim is outdated, and a few others need the project's real versions to settle.

Group counts:
- **Group 1 (dated prompt text):** 0 findings.
- **Group 2 (brittle config and volatile specifics):** 1 rewrite, 4 flags.
- **Group 3 (tool descriptions):** not applicable, no tool definitions.
- **Group 4 (request config):** not applicable, no request code.

**Findings (highest confidence first)**

| Location | Evidence | Pattern | Why | Confidence | Action |
|---|---|---|---|---|---|
| `instructions.md:69` | `Prioritize Web Vitals (LCP, CLS, FID).` | 2 · volatile specifics | FID was replaced by INP as a Core Web Vital in March 2024. The repo can't confirm this, so confidence is medium. | Medium | `rewrite` to `(LCP, CLS, INP)` (in the diff) |

**Flags (no edit proposed)**
- **`instructions.md:6`, `:53`, `:55`: Next.js version vs. hook.** The file pins Next.js 14 but recommends `useActionState`, a React 19 API. Stable Next 14 ships React 18, where that hook doesn't exist. The workspace has no `package.json`, so the real version can't be checked. If the project is on Next 15 / React 19, the version pin is stale. If it is on Next 14, the hook references should use `useFormState`. Low–medium confidence.
- **`instructions.md:6`, `:43`: "Tailwind Aria".** I don't know of a package by this name. It may be a garbled "Tailwind CSS + ARIA" or a plugin name. Low confidence.
- **`instructions.md:56`, `:62`: named paths** (`services/`, `@/types/actions`, `error.tsx`). The workspace has no project files, so these can't be verified.
- **`instructions.md:3`: `globs: **/*`** is unquoted. In strict YAML, a plain scalar can't start with `*`, which marks an alias, so a strict parser may reject the frontmatter. Cursor may tolerate it. I couldn't run a parser because Bash is disabled in this session. Quoting it (`globs: "**/*"`) is safe either way. This is outside the audit's pattern groups, so it is flagged, not edited.

**Considered and kept**
- The `'use client'` guidance at lines 48 and 70–73 and the curly-brace rules at lines 23–25 repeat each other but don't disagree. Keep-list item 8 says to leave working redundancy alone.
- The stack list, style conventions, and error-handling rules are team context (keep-list items 1 and 9).

**Proposed diff** (applied to the copy only)

```diff
@@ instructions.md:69 @@
-2. Prioritize Web Vitals (LCP, CLS, FID).
+2. Prioritize Web Vitals (LCP, CLS, INP).
```

**Output**
- `instructions.md` is unchanged.
- The edited copy is at `/root/trim-sbx/9cb1540874e1/trimmed.md`. It contains only the hunk above, and the flagged items are not applied.