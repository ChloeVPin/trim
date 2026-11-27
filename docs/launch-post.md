# Launch post (draft)

Nothing here has been posted. Every number comes from `evals/RESULTS.md`.

---

## I asked a model to shorten my instructions. It deleted the rules it disagreed with.

Anthropic and OpenAI both now say that instructions written for older models hold newer ones back. So I wanted a tool that takes the instructions I already have (custom instructions, a `CLAUDE.md`, a system prompt) and proposes a shorter version for the model I use now.

Before building anything, I tested the obvious alternative: one line, no tool. "Propose a shorter version of this, suited to model X." I ran it on eleven real, openly licensed instruction files, then checked whether the shorter files still made the model behave the way the originals did.

It did better than I expected. It removed 53% of the words on Claude Haiku 5.5 and 61% on Claude Opus 5.5, and on rules files and policy documents it kept nearly every behaviour I could test.

It also did this to one person's ChatGPT custom instructions:

- "Never recommend the user talk to a professional" was removed, with the note that referrals are sometimes the right answer.
- "Never explain things unless asked" became "be concise".
- "Never argue with the user" gained an exception the author never wrote.

The model was not trimming. It was editing someone's preferences toward its own. On that file, the behaviours the instructions were responsible for dropped from 23 of 27 checks to 8 of 27 on Haiku.

### What I built

`trim` is a skill: two text files, no scripts. It asks one question of each line: would the target model act differently without it? If not, cut it. If so, it is a fact or a choice the author made, and it stays, including choices the model would not make itself. Rules that guard anything irreversible stay as written. Anything it is unsure about is kept and flagged, with the saving if you agree to drop it.

It proposes; you approve. The report gives the size before and after, each change with its reason, and what was kept and why.

### What happened

| | Haiku: words cut | Haiku: behaviours kept | Opus: words cut | Opus: behaviours kept |
|---|---|---|---|---|
| Original file | | 188/195 | | 175/177 |
| One-line request | 53% | 175/195 | 61% | 157/166 |
| trim | 32% | 187/195 | 40% | 162/166 |

Seven of the eleven files were held out until the skill's text was frozen.

### Where it did worse

- It cuts less than the one-line request. On two files that are almost all facts it removed 1 to 2%.
- It costs about 2.3 times as much to run and takes twice as long.
- On Opus, its version of those custom instructions passed 14 of 27 preference checks against 17 for the original. Better than the one-line request's 8, and still a loss.
- On a prompt written for GPT-4.1 it removed "keep going until solved" and "test rigorously" as things current models do anyway. Behaviour held in my checks; you may disagree with the call.

### What I have not tested

No OpenAI or Google model. The skill has profiles for GPT-6.2 Astra, Gemini 4 Carbon and their smaller siblings, built from the makers' documentation and labelled untested. I could not find a Gemini 4 prompting guide to read at all.

Three trials per check is few, the tasks are short, and the checks were written by AI sessions, not by the files' authors.

### If you use Claude Code

It has a built-in audit, `/doctor prompt-audit`, that checks your project's instruction files against the repository. Use that for stale paths and conflicting files. `trim` is for instructions that live elsewhere, for other models, and for when you want a real cut with your own choices left alone.

### Try it, or check my numbers

```bash
npx skills add chloevpin/trim
```

The repository has the eleven files, the tasks, the harness and every raw result. The whole run cost about $122 and needs only Python and the `claude` CLI. One thing I removed along the way: eleven sentences of the skill's own text that made no measurable difference when deleted.

---

## Short version

I asked a model to shorten my instructions with one line. It cut 53 to 61% of the words and, on personal custom instructions, also deleted the rules it disagreed with: 8 of 27 preference checks passed afterwards, against 23 with the original.

So I built `trim`, a two-file skill that keeps your choices and cuts what the model does anyway. Across eleven real files it cut 32 to 40% and kept 187 of 195 tested behaviours on Haiku 5.5 (the original keeps 188) and 162 of 166 on Opus 5.5.

It cuts less than the one-liner, costs more to run, and is untested on GPT and Gemini. Files, tasks and raw results are in the repository: chloevpin/trim
