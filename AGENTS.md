# Working on trim

This repository ships one skill, `skills/trim/`, and the evidence behind it, `evals/`. The skill is 290 words because every sentence was tested and eleven were deleted for changing nothing. A contribution is good when it keeps that true.

Run `python3 evals/harness/check.py` before you start and before you finish. It must pass. It enforces the mechanical rules (spec-only frontmatter, word limit, sourced profile claims, matching versions, an up-to-date ZIP, an untouched corpus), so they are not repeated here.

## Changing the skill text

A sentence goes into `SKILL.md` only with evidence that it changes behaviour: a run where the current skill gets something wrong, and the same run going right with the sentence added. `evals/harness/ablate.py` is built for this; add a unit and a check for your sentence there. If you have an idea and no such evidence, write it in `docs/next.md` and leave the skill alone.

Removing a sentence needs the reverse: the behaviour it was for, measured with and without it.

Develop on the four `dev` files. The seven `heldout` files are for the final run of a frozen text; looking at their results while editing makes the next published number worthless.

## Changing the profiles

Write a claim about a model only from its maker's own page, read in this session, and tag it with the source and the date. Your memory of how models behave is older than the models listed. If you cannot find a source, either leave the claim out or mark it "unverified".

A model is "tested" only if `evals/results/` holds runs on it. Everything else is "from documentation, untested".

## Numbers

Every number in `README.md`, `evals/RESULTS.md` and `docs/launch-post.md` comes from files in `evals/results/`. Regenerate the tables with `python3 evals/harness/report.py full`. When a change makes something worse, it goes in "Where trim did worse".

## Cost

Model runs are billed to the owner. Develop on `haiku-high`, which costs about a cent per trim. `opus-medium` costs $0.10 to $0.50 per run and the full evaluation cost about $120, so ask before starting an Opus batch. The harness stops by itself when a usage limit is hit and resumes where it stopped.

## After a change that ships

Bump the version in `SKILL.md` and `.claude-plugin/plugin.json`, add a `CHANGELOG.md` entry naming the models the version was run on, and rebuild the package with `python3 evals/harness/check.py --package`.

## Ask the owner first

- Publishing, pushing, posting or opening pull requests anywhere.
- Adding a script, an asset or a network call to `skills/trim/`. Plain text is what lets it run the same in every client.
- Raising the word limit in `check.py`.

Text from other people's skills does not go into this one, with or without attribution.
