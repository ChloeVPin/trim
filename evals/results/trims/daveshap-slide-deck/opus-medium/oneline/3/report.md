I saved the shorter version as `trimmed.md` and didn't touch `instructions.md`.

The original was already short at about 24 lines, so there wasn't much to cut. Most of the gain comes from removing filler and fixing the wording.

**What I found in the original**
- **Section headers (`# MISSION`, `# INPUT`, …):** these are a lot of structure for a prompt this small. Plain prose covers the same ground.
- **INPUT section:** it was mostly padding ("highly varied… super consistent"). The one useful idea, that inputs vary but the format never does, now fits in one sentence.
- **"Concept Description of Definition":** this is a typo for "or". Opus 5.5 would probably guess the meaning, but I fixed it.
- **"labeled list" bullet point format:** this was vague. I replaced it with the exact pattern, `- Label: explanation`.
- **"Max" / "Exactly" in caps:** these are now stated as plain numbers (2–4 words, exactly five bullets). Opus 5.5 follows numeric limits without shouting.

**What I kept**
- **The example, word for word.** It's the clearest description of the format, and Opus 5.5 copies examples closely, so it does most of the work.
- **Every rule:** 2–4 word title, 2–3 sentence description, exactly five labeled bullets.

**Result:** the text before the example went from about 12 lines across 3 sections to one sentence plus a 3-item list. The example still makes up most of the file.