I saved the shorter version to `/root/trim-sbx/1143dce03ca0/trimmed.md`. `instructions.md` is unchanged.

## Audit of instructions.md

**Problems**
- **Dangling reference.** Line 216 points to `writing-good-tests.md`, which isn't in the directory. I inlined its four rules into the trimmed file so it doesn't depend on that file. If the file exists elsewhere, I haven't audited it.
- **Redundant diagram.** The graphviz block (lines 49–69) repeats the Red-Green-Refactor section in a form Haiku has to parse. The numbered cycle replaces it.
- **Long rationalization table and red-flag list.** The table has about 15 persuasive-prose rows. The trimmed file keeps the six red flags that describe concrete behavior and drops the rest.
- **Ambiguous wording.** "Ask your human partner" doesn't say who that is in a session with a user. I changed it to "ask the user."
- **JavaScript-specific examples.** `npm test` and the TypeScript examples are the only commands given. The trimmed file names the repo's test command generically and keeps one TypeScript example.
- **Buried key rule.** The full-suite requirement and the reporting requirement are the rules a model is most likely to skip, and they were spread across long paragraphs. They now have their own short sections.

**Kept as written**
- The Iron Law and the delete-and-restart rule.
- Verify RED and Verify GREEN, with the same failure-handling branches.
- The exceptions list.
- The completion checklist.
- The bug-fix rule.

## Changes for Haiku 5.5

- Numbered steps with one action each.
- Short imperative sentences. Idioms such as "spirit not ritual" are removed.
- Each conditional is written as an explicit branch, for example "It passes: … / It errors: …".
- Result: about 67 non-empty lines, down from 256 in the original, with the same rules.

## Decisions for you

- **Delete rule.** The trimmed file keeps "delete it and start over." That's destructive for code a user may already have, so you may want to soften it to "move it aside" or "ask before deleting."
- **Missing reference.** If `writing-good-tests.md` exists and has content you want kept, send it and I'll fold the relevant parts in.