<img src="assets/trim-og.png" width="360" height="180" alt="Five instructions; the three a current model does not need are struck out, and 'Use pnpm.' and 'Never push to main.' remain." />

# trim

A skill that proposes a shorter version of the instructions you have given an AI, fitted to one named model. It shows what it would cut and why, what it kept and why, and changes nothing until you approve.

It reads custom instructions, project and system prompts, rules files such as `CLAUDE.md` and `AGENTS.md`, and other skills. It asks one question of each line: would the target model act differently without it? If not, the line goes. If so, it is a fact or a choice you made, and it stays.

## Install

```bash
npx skills add chloevpin/trim
```

Claude Code plugin:

```text
/plugin marketplace add chloevpin/trim
/plugin install trim@trim
```

Claude apps: upload [`dist/trim.zip`](dist/trim.zip) under Customize, Skills. This route was not tested.

## Use

```text
/trim CLAUDE.md for claude-haiku-5-5
```

As a plugin the command is `/trim:trim`. If you name no model, trim uses the one your app says it is running and tells you so. If the instructions are plainly for another product, it asks.

## What we measured

Eleven real instruction files, with tasks that check the behaviours each file causes, run on `claude-haiku-5-5` and `claude-opus-5-5`. "Kept" counts the checks that fail without the file and pass with it.

| Version of the instructions | Haiku: cut | Haiku: kept | Opus: cut | Opus: kept |
|---|---|---|---|---|
| Original | | 188/195 | | 175/177 |
| One-line request, no skill | 53% | 175/195 | 61% | 157/166 |
| trim | 32% | 187/195 | 40% | 162/166 |

The one-line request cuts more, and on personal custom instructions it also removed rules it disagreed with: 8 of 27 preference checks passed afterwards on Haiku, against 23 for the original and 22 for trim.

Where trim did worse:

- It cuts less, and only 1 to 2% on two files that are almost all facts.
- It costs about 2.3 times as much to run as the one-line request.
- On Opus, its version of those custom instructions passed 14 of 27 preference checks, against 17 for the original.

No OpenAI or Google model was run. Their profiles, and those for Claude Fable 5.2 and Sonnet 5.5, come from the makers' documentation and are labelled untested. Full tables, the remaining weak spots and every raw result are in [`evals/RESULTS.md`](evals/RESULTS.md).

If you work in Claude Code and want your project's instruction files checked against the repository, use its built-in `/doctor prompt-audit`. trim is for instructions that live elsewhere, for other models, or when you want a real cut with your own choices left intact.

## Contributing

[`AGENTS.md`](AGENTS.md) is the guide for people and agents. No sentence goes into the skill without a run showing it changes behaviour. How the skill was built is in [`evals/ITERATIONS.md`](evals/ITERATIONS.md).

## Licence

MIT. The instruction files under `evals/corpus/` belong to their authors and keep their own licences.
