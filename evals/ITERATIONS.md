# How the skill text changed, and why

Each version was run on the four dev files only. The seven held-out files were not run with any skill version until the text was frozen.

## Baseline: a one-line request, no skill

Prompt: "Audit instructions.md and propose a shorter version suited to <model>."

What it did well: cut 44% (Haiku) and 52% (Opus) of the words on average, kept the tested conventions and guards in three of four files, and usually explained its changes.

Where it fell short:

- **It replaced the author's preferences with its own.** On the ChatGPT custom-instructions file it removed "never recommend the user talk to a professional", turned "never explain things unless asked" into "be concise", and added exceptions the author never wrote. Behaviour on that file dropped from 5/6 to 0/6 on Haiku and from 5/6 to 3/6 on Opus.
- **About two removed instructions per trim went unmentioned in the report.**
- **Facts it judged stale disappeared.** One trim of the airline policy dropped the "current time" line; several dropped session commands and tool routing from the rules file.
- **It settled contradictions silently**, for example keeping "commit frequently" and dropping "no auto-commit".
- **One trim in six dropped the frontmatter** a Cursor rules file needs in order to load.
- **Two trims in twelve wrote the model's name into the instructions.**
- **Size before and after was stated in about half the reports**, and was off by 24% on Haiku when it was.
- **It never asked which model** when told the instructions were for another product.

## v1

Aimed at the list above: fix the target model first, read the profile, sort every instruction into leave-as-written, keep, or cut, flag what looks stale or conflicting, and report sizes, changes, what was kept, and flags.

Result: every listed fact and hard rule survived in all 24 dev trims, and reports met the contract. But it cut too little: 11% on Haiku and 26% on Opus. On the bloated rules file it removed about 10% for Haiku where the one-line request had removed 75% with no measured loss. Two causes: "the author's preferences" was read as "everything the author wrote", and the Haiku profile's "cut less" was applied to generic advice as well as to task procedures.

## v2

- The sorting rule became one question: would the target model act differently without this line? No means cut. Yes means it is a fact or a choice the author made, so keep it at full strength. Unsure means keep and flag, with the saving if the author agrees.
- The target rule now covers instructions written for a different product: ask which model, do not assume the running one.
- The Haiku profile now says that keeping procedures does not extend to generic advice or repeated emphasis.

Result: 19% cut on Haiku and 23% on Opus across the dev files (41% and 54% on the bloated rules file), with behaviour level with the original on both models. It asked for the model in 6 of 6 other-product runs; the one-line request asked in 0 of 6.

## v3 (released as 0.3.0)

v2 after the deletion test in `harness/ablate.py`. Each sentence was removed in turn and the behaviour it is meant to produce was measured with and without it, on Haiku (3 to 10 runs) and Opus (1 to 2 runs). The body went from 467 words to 290.

Removed, because the behaviour was the same without them:

| Sentence | Behaviour measured | With | Without |
|---|---|---|---|
| "A model with no profile gets the conservative treatment described there." | report says there is no profile | 4/4 | 4/4 |
| "Model-specific reasons come from that file ... your own memory ... predates the current ones." | no unsupported claims about the model (judged) | 1/6 | 0/6 |
| "Keep it at full strength, including choices you would advise against. Turning 'never explain' into 'be concise' changes what was asked." | three "never ..." preferences survive word for word | 12/12 | 11/11 |
| "... and anything a program reads, such as frontmatter" | Cursor frontmatter intact | 12/12 | 11/11 |
| "Lines that look stale, risky or in conflict with each other get flagged, not settled; that is the author's call." | stale date kept; commit conflict flagged and both sides kept | 17/23 | 17/22 |
| "So is anything new: list additions the profile recommends as suggestions outside the text." | no profile additions inside the trimmed text | 12/12 | 4/4 |
| "Wording can change (emphasis down to normal volume, a reason kept beside its rule)" | capitalised emphasis at least halved | 12/12 | 4/4 |
| "... and the model's name stays out of the text, since the file may outlive the model." | no model name in the trimmed text | 12/12 | 11/11 |
| Report item "Flags and suggestions for the author." | report has a flags section | 11/12 | 4/4 |
| Report item "The proposed text in full ..." | full text present in the reply or file | 12/12 | 10/11 |
| "A file that is already lean should come back nearly unchanged ..." | policy file cut by 15% or less | 9/11 | 3/4 |

Kept, because the behaviour changed without them:

| Sentence | Behaviour measured | With | Without |
|---|---|---|---|
| "Unsure: keep it and flag it, with how much shorter the text gets if the author agrees to drop it." | flags that state a saving in words | 11/12 | 5/11 |
| Report item "Words before and after ..." | report states both sizes | 10/12 | 0/4 |
| Report item "Each change, with its reason." | report has a changes section | 11/12 | 1/4 |
| Report item "What you kept and why." | report has a kept section | 11/12 | 1/4 |

Kept without a deletion test, because they are design decisions and not candidates for removal: nothing changes until the author approves (held in 17/17 runs), the user's requests outrank the skill (5/5), the target-model rule (assumed and said so 5/5; asked and waited 5/5), and the paragraph keeping hard rules as written. The sentence explaining that the reader may not be the model running the skill was tested (5/5 with, 3/4 without) and kept: the difference is too small to call either way.

One deletion was reversed. Report item "Target model, and whether it was named, assumed, or has no profile" passed the deletion test (12/12 with, 4/4 without), but that test named the model in the request. A check of the assembled v3 on a request that named no model found a report that never said which model it had assumed, so the line went back in.

Two caveats about this test. The counts are small, so "no measurable change" means "none that 4 to 11 runs could show". And sentences were removed one at a time; the released text removes them together. The assembled text was checked afterwards on the same assertions with four runs each. Most held at 4/4. Lowered emphasis fell to 2/4, the report line above was restored, and five other assertions showed a single miss, two of which were correct behaviour that the check's pattern failed to recognise.
