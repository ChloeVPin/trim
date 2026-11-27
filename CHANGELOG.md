# Changelog

Each entry names the models the version was run on. Instructions age with every model release, so a version is only vouched for on the models listed.

## 0.3.0 (2026-11-27)

First public version.

- Run on `claude-haiku-5-5` at high effort and `claude-opus-5-5` at medium effort, inside Claude Code 2.1.332.
- Not run on any OpenAI or Google model. Their profiles are from the makers' documentation only.
- Skill text is v2 of the drafts after a sentence-by-sentence deletion test; see `evals/ITERATIONS.md`.
- Profiles checked against the makers' pages on 2026-11-27.

## Drafts (not released)

- 0.2.0: sorting rule rewritten around one question, "would the target model act differently without this line?"; asks for the model when the instructions are for another product.
- 0.1.0: first draft. Kept every fact and hard rule but cut too little.
