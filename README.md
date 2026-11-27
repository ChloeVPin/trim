# trim

A skill that proposes a shorter version of the instructions you have given an AI, fitted to one named model. It shows what it would cut and why, what it kept and why, and changes nothing until you approve.

It reads custom instructions, project and system prompts, rules files such as `CLAUDE.md`, `AGENTS.md` and Cursor rules, and other skills. The skill is two plain-text files with no scripts and no network calls.

## Why it exists

Model makers now say that instructions written for older models make newer ones slower, more expensive or more rigid, and that how much guidance helps depends on the model. So old instructions are worth trimming when you change models.

You can do that with one line: "propose a shorter version of this for model X". We tested that first. It removes a lot and usually gets away with it, but it also removes rules it disagrees with. Given one person's custom instructions, it deleted "never recommend the user talk to a professional", turned "never explain things unless asked" into "be concise", and added exceptions the author never wrote.

trim is built around one question for each line: would the target model act differently without it? If not, the line goes. If so, it is a fact or a choice you made, and it stays, including choices the model would not make itself.

## What we measured

Eleven real, openly licensed instruction files. For each one, small tasks with deterministic checks for the behaviours the file causes. Every task was run with the original file and with each trimmed version, on `claude-haiku-5-5` at high effort and `claude-opus-5-5` at medium effort. Seven of the eleven files were held out until the skill text was frozen.

"Cut" is the share of words removed across all files. "Kept" is the pass count on the checks that fail without the file and pass with it.

| Version of the instructions | Haiku: cut | Haiku: kept | Opus: cut | Opus: kept |
|---|---|---|---|---|
| Original | | 188/195 | | 175/177 |
| One-line request, no skill | 53% | 175/195 | 61% | 157/166 |
| Claude Code's built-in audit | 17% | 174/195 | not run on all files | |
| trim | 32% | 187/195 | 40% | 162/166 |

Other measurements, same runs:

| | One-line request | trim |
|---|---|---|
| Report states the size before and after | 15/33 Haiku, 17/33 Opus | 33/33, 33/33 |
| Removed instructions the report never mentions, per trim | 2.9 Haiku, 2.0 Opus | 0.8, 0.6 |
| Listed facts still present in the trimmed text | 235/291 Haiku, 257/291 Opus | 276/291, 278/291 |
| Asks which model when the instructions are for another product | 0/3, 0/3 | 3/3, 3/3 |
| Cost of producing one trim | $0.006 Haiku, $0.10 Opus | $0.014, $0.24 |

Full tables, per file and per model, are in [`evals/RESULTS.md`](evals/RESULTS.md).

### Where trim did worse

- It cuts less than the one-line request, and on two files it removed only 1 to 2%. Those two are an airline service policy and a repository `AGENTS.md`, which are almost entirely facts and rules a model cannot know.
- It costs about 2.3 times as much to run as the one-line request and takes about twice as long.
- On Opus, its version of the personal custom instructions passed 14 of 27 preference checks in a nine-trial rerun, against 17 of 27 for the original and 8 of 27 for the one-line request. On Haiku the same test gave 22, 23 and 8.
- On a prompt written for GPT-4.1 it removed "keep going until solved", "read before editing" and "test rigorously" as things the target model does unprompted. Whoever wrote the checks for that file had listed those as hard rules. Measured behaviour on that file was 10/12 against 11/12 on Haiku and 3/3 against 3/3 on Opus.
- When it has no tool to count with, its stated word counts are estimates. They were off by 13% on Haiku and 9% on Opus on average.

### What was not tested

- **No OpenAI or Google model was run.** The skill carries profiles for GPT-6.2 Astra, GPT-6.2 Sol, GPT-6 Luna, Gemini 4 Carbon and Gemini 4 Hydrogen, built from the makers' own pages and labelled "from documentation, untested". No Gemini 4 prompting guide could be read, so that profile is the thinnest.
- Claude Fable 5.2 and Claude Sonnet 5.5 have profiles and were not run either.
- Every task is a few turns long. Nothing here shows what happens over a long session.
- Three trials per check is few. Single checks swing by one pass between runs; the totals are what to read.
- The upload to the Claude apps was not performed. The ZIP passes Anthropic's own packaging validator, which is as far as this could be checked without an account.

## Should you use it

If you work in Claude Code with a Claude model and want your project's instruction files checked against the repository, run the built-in `/doctor prompt-audit`. It finds stale paths, dead commands and files that contradict each other, which trim does not look for. In our runs it was conservative on most files and removed the word-count rules from a strict-format prompt, which changed that prompt's output.

trim is for the other cases: instructions that live outside a repository, instructions for another assistant or model, or when you want a real cut with your own choices left intact.

If the one-line request is good enough for you, use it and read its diff carefully. On rules files and policy text it kept nearly every tested behaviour. It went wrong on personal preferences and on format rules.

## Install

**Any agent that reads skills** (Claude Code, Codex, Cursor, Copilot, Gemini CLI and others):

```bash
npx skills add chloevpin/trim
```

**Claude Code plugin:**

```text
/plugin marketplace add chloevpin/trim
/plugin install trim@trim
```

**Claude apps:** download `trim.zip` from `dist/`, then open Customize, Skills, the plus button, and "Upload a skill". Code execution must be on.

**By hand:** copy `skills/trim` into your agent's skills folder.

The first two routes were tested from a local copy of this repository; the app upload was not.

## Use

Invoke it by name and say which model the instructions are for. That is the dependable route.

```text
/trim CLAUDE.md for claude-haiku-5-5
```

As a Claude Code plugin the command is `/trim:trim`. Codex documents `$trim` as its form, and in the Claude apps you name the skill in your message ("use the trim skill on these, for <model>"); neither was run.

Asked without naming it, the skill loaded on 18 of 18 direct requests and 8 of 12 indirect ones on Haiku, and never on 30 near-miss requests. On Opus, with one run each, it loaded on 6 of 6, 3 of 4 and 0 of 10. That was with only Claude Code's bundled skills installed beside it, which is an easy setting.

If you name no model, trim uses the model your app says it is running and tells you it assumed that. If the instructions are plainly for a different product, it asks which model and waits.

### What comes back

From a real run on a set of ChatGPT custom instructions, for `claude-haiku-5-5`, shortened here:

```text
1. Target model: claude-haiku-5-5, named by you. [...]

2. Words: about 239 before, about 219 after [...] I counted by hand because
   I have no word-count tool here, so treat these as estimates.

3. Changes
   - Removed "LLM = Large Language Model" and "aka 'Generative AI'". Haiku
     already knows these terms. About 8 words.
   [...]

4. Kept, and why
   - Rules 2, 3, 4, 5, 7, 8: these are your choices about behavior, so I
     left them alone.
   [...]

Unsure, kept and flagged
   - AI TODAY bullet, "Generative AI is a reasoning engine ..." It conflicts
     with Rule 6 ("just a tool") [...] Dropping it saves 24 words. This is
     your call.

Conflicts for you to decide (not changed)
   - Rule 5 vs. Rule 10: Rule 5 says to adopt the user's values, ethics, and
     morals. Rule 10 says never to espouse values or bring up ethics. [...]
```

## Models

| Model | Status |
|---|---|
| `claude-haiku-5-5` | tested at high effort |
| `claude-opus-5-5` | tested at medium effort |
| `claude-fable-5-2`, `claude-sonnet-5-5` | from documentation, untested |
| `gpt-6.2-astra`, `gpt-6.2-sol`, `gpt-6-luna` | from documentation, untested |
| `gemini-4-carbon`, `gemini-4-hydrogen` | from documentation, untested; no Gemini 4 prompting guide could be read |
| anything else | best effort: cuts only duplicates, dead references and generic advice, and says so |

Profiles are in [`skills/trim/references/profiles.md`](skills/trim/references/profiles.md). Every claim carries a source and the date it was read, 2026-11-27. They go stale with each model release; the changelog names the models each version was run on.

## How it was built

1. Looked for existing tools. The closest is Claude Code's built-in audit, which is why trim does not try to cover that ground.
2. Ran the one-line request on real files and wrote down where it fell short.
3. Wrote the skill for those failures and nothing else. Three drafts; the notes are in [`evals/ITERATIONS.md`](evals/ITERATIONS.md).
4. Removed each sentence in turn and measured whether behaviour changed. Eleven sentences made no measurable difference and were deleted. The body is 290 words.
5. Froze the text, then ran the held-out files.

The harness, the files, the tasks and every raw result are in [`evals/`](evals/). It needs Python and the `claude` CLI. The recorded cost of all runs was about $122.

## Contributing

[`AGENTS.md`](AGENTS.md) is the guide for people and agents alike. In short: no sentence goes into the skill without a run showing it changes behaviour, no profile claim without a source, and no number that is not in `evals/results/`. `python3 evals/harness/check.py` enforces what can be checked mechanically and runs on every push.

## Licence

MIT for the skill and the harness. The instruction files under `evals/corpus/` belong to their authors and keep their own licences, which are MIT for ten and CC0 for one. Each folder there has a `source.json` with the repository and commit, and the upstream licence text.
