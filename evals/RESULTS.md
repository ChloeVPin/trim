# Results

Run on 2026-11-27 with Claude Code 2.1.332. Two models: `claude-haiku-5-5` at high effort and `claude-opus-5-5` at medium effort. No OpenAI or Google model was run.

Eleven real instruction files, 55 tasks carrying 90 checks, 1,777 task runs and 195 trims. `README.md` in this folder explains the method and the terms used below. Everything here is generated from the files in `results/`.

## Headline

"Cut" is the share of words removed across all eleven files. "Kept" is the pass count on instruction-dependent checks, which are the behaviours the original file demonstrably causes.

| Version of the instructions | Haiku: cut | Haiku: kept | Opus: cut | Opus: kept |
|---|---|---|---|---|
| No instructions | | 4/195 | | 3/177 |
| Original | | 188/195 | | 175/177 |
| One-line request, no skill | 53% | 175/195 | 61% | 157/166 |
| Claude Code's built-in audit | 17% | 174/195 | 20% (4 dev files only) | 49/51 (4 dev files only) |
| trim | 32% | 187/195 | 40% | 162/166 |

Reading it:

- **trim** kept behaviour within one pass of the original on Haiku and removed about a third of the words. On Opus it removed 40% and passed 162 of 166 against the original's 175 of 177.
- **The one-line request** removed the most. It failed 20 of 195 checks on Haiku against the original's 7, and 9 of 166 on Opus against the original's 2 of 177. Nearly all of the extra failures sit in three files: the personal custom instructions, the strict-format prompt and one personal `CLAUDE.md`.
- **The built-in audit** changed little on most files. On Haiku it lost 14 passes, most of them on the strict-format prompt, where it removed the author's word-count rules as its guidance on numeric caps says to.

Three trials per check is few. A single check can swing by one pass between runs, so the totals carry the result and the single rows do not. The Opus denominators differ between arms because the most expensive file was run twice per check on the trimmed arms and three times on the original.

## Where trim did worse

- **It cuts less than the one-line request**: 32% against 53% on Haiku, 40% against 61% on Opus. On two files it removed 1 to 2%: the airline policy and the repository `AGENTS.md`, which are nearly all facts and rules the model cannot know.
- **It costs more to run**: $0.014 a trim on Haiku against $0.006, and $0.24 on Opus against $0.10. It takes about twice as long (65 and 51 seconds against 30 and 25).
- **On Opus it weakened the personal custom instructions a little.** With nine trials per check on that file's three preference checks, the original passed 17 of 27, trim 14 of 27 and the one-line request 8 of 27. On Haiku the same test gave 23, 22 and 8 of 27. trim's versions still contain those rules; what it removed was repetition and harsh phrasing around them, which may carry some weight on Opus. With counts this small the gap could also be noise.
- **On a prompt written for GPT-4.1 it removed lines that the probe's author had listed as hard rules**: "keep going until solved", "read before editing", "test rigorously" and, in one trim, a todo-list format rule. These account for 7 of the 8 unmatched hard-rule entries on Haiku and all 7 on Opus. Behaviour on that file's checks was 10/12 against the original's 11/12 on Haiku and 3/3 against 3/3 on Opus. The eighth is one Haiku trim that dropped "no auto-commit" from a file that also says "commit frequently".
- **Its reports still miss things**: by the judge's count, 0.8 removed instructions per trim on Haiku and 0.6 on Opus go unmentioned. The one-line request leaves 2.9 and 2.0.
- **Its sizes are estimates when it has no counting tool.** The harness gave it none, and its stated word counts were off by 13% on Haiku and 9% on Opus on average, and by up to 36%.
- **Single-pass differences on Haiku**: 32/33 against 33/33 on the slide-deck prompt, 10/12 against 11/12 on the GPT-4.1 prompt, 11/12 against 12/12 on the Cursor rules.

## What the test could not show

- **Anything about OpenAI or Google models.** Those profiles come from documentation.
- **The test-driven-development skill may be an easy case.** Its author reports that removing its argument section costs test-first behaviour under pressure. trim removed the passage that rebuts "tests after" in all three Opus trims, and test-first still held in 21 of 21 runs. The pressure prompts here are mild, and the probe's author found that an explicit order to write tests later defeats even the original file.
- **One short principles card produced no instruction-dependent checks at all.** Every behaviour it asks for, the models showed without it. It is in the size tables and absent from the behaviour totals.
- **Whether the cuts hold on long tasks.** Every task here is a few turns.

## claude-haiku-5-5 at high effort

### Size

Words in the file, as a mean over the trims of each arm, with the cut against the original.

| File | Split | Original | One-line | Built-in | trim |
|---|---|---|---|---|---|
| beast-mode | heldout | 2,657 | 415 (-84%) | 480 (-82%) | 482 (-82%) |
| citypaul-claude-md | heldout | 2,933 | 1,228 (-58%) | 2,870 (-2%) | 2,138 (-27%) |
| cursorrules-nextjs | dev | 578 | 411 (-29%) | 578 (+0%) | 443 (-23%) |
| daveshap-default-ci | dev | 242 | 154 (-36%) | 244 (+1%) | 215 (-11%) |
| daveshap-slide-deck | heldout | 200 | 195 (-2%) | 216 (+8%) | 170 (-15%) |
| fabric-extract-wisdom | heldout | 539 | 315 (-42%) | 451 (-16%) | 419 (-22%) |
| karpathy-claude-md | heldout | 358 | 265 (-26%) | 366 (+2%) | 313 (-13%) |
| openai-agents-agents-md | heldout | 2,103 | 1,874 (-11%) | 2,103 (+0%) | 2,091 (-1%) |
| superclaude-rules | dev | 2,127 | 545 (-74%) | 2,004 (-6%) | 1,220 (-43%) |
| superpowers-tdd | heldout | 1,475 | 581 (-61%) | 1,498 (+2%) | 1,126 (-24%) |
| taubench-airline | dev | 1,051 | 677 (-36%) | 1,088 (+4%) | 1,035 (-2%) |
| **All files** | | | **-53%** | **-17%** | **-32%** |

The same in tokens, measured on this model:

| File | Original | One-line | Built-in | trim |
|---|---|---|---|---|
| beast-mode | 6,234 | 787 (-87%) | 885 (-86%) | 926 (-85%) |
| citypaul-claude-md | 7,530 | 2,848 (-62%) | 7,123 (-5%) | 5,257 (-30%) |
| cursorrules-nextjs | 1,420 | 986 (-31%) | 1,418 (-0%) | 1,094 (-23%) |
| daveshap-default-ci | 465 | 296 (-36%) | 457 (-2%) | 418 (-10%) |
| daveshap-slide-deck | 411 | 398 (-3%) | 444 (+8%) | 367 (-11%) |
| fabric-extract-wisdom | 1,098 | 690 (-37%) | 924 (-16%) | 892 (-19%) |
| karpathy-claude-md | 863 | 507 (-41%) | 842 (-2%) | 734 (-15%) |
| openai-agents-agents-md | 5,475 | 4,546 (-17%) | 5,476 (+0%) | 5,449 (-0%) |
| superclaude-rules | 6,091 | 1,083 (-82%) | 5,665 (-7%) | 3,252 (-47%) |
| superpowers-tdd | 3,735 | 1,144 (-69%) | 3,754 (+1%) | 2,764 (-26%) |
| taubench-airline | 1,845 | 1,386 (-25%) | 1,923 (+4%) | 1,824 (-1%) |

### Behaviour

Passes on instruction-dependent checks (the behaviours the original file is responsible for).

| File | Split | Checks | No instructions | Original | One-line | Built-in | trim |
|---|---|---|---|---|---|---|---|
| beast-mode | heldout | 4 | 1/12 | 11/12 | 11/12 | 10/12 | 10/12 |
| citypaul-claude-md | heldout | 7 | 0/21 | 21/21 | 19/21 | 21/21 | 21/21 |
| cursorrules-nextjs | dev | 4 | 0/12 | 12/12 | 11/12 | 12/12 | 11/12 |
| daveshap-default-ci | dev | 2 | 0/6 | 5/6 | 0/6 | 3/6 | 4/6 |
| daveshap-slide-deck | heldout | 4 | 0/33 | 33/33 | 33/33 | 33/33 | 32/33 |
| fabric-extract-wisdom | heldout | 10 | 0/36 | 34/36 | 28/36 | 24/36 | 35/36 |
| karpathy-claude-md | heldout | 0 | - | - | - | - | - |
| openai-agents-agents-md | heldout | 9 | 1/27 | 25/27 | 26/27 | 25/27 | 26/27 |
| superclaude-rules | dev | 3 | 0/9 | 9/9 | 9/9 | 8/9 | 9/9 |
| superpowers-tdd | heldout | 7 | 1/21 | 21/21 | 21/21 | 21/21 | 21/21 |
| taubench-airline | dev | 6 | 1/18 | 17/18 | 17/18 | 17/18 | 18/18 |
| **Dev files** | | | **1/45** | **43/45** | **37/45** | **40/45** | **42/45** |
| **Held-out files** | | | **3/150** | **145/150** | **138/150** | **134/150** | **145/150** |
| **All** | | | **4/195** | **188/195** | **175/195** | **174/195** | **187/195** |

Checks the model passes even with no instructions (so the rule behind them changes nothing): Original 74/75, One-line 73/75, Built-in 75/75, trim 75/75.

Checks where an arm passed at least two-thirds less often than the original:

| Arm | File | Check | Kind | Original | Arm |
|---|---|---|---|---|---|
| Built-in | daveshap-default-ci | no-unasked-explanation | preference | 3/3 | 0/3 |
| Built-in | fabric-extract-wisdom | bullets-16-words | format | 6/6 | 0/6 |
| Built-in | fabric-extract-wisdom | summary-about-25-words | format | 3/3 | 1/3 |
| Built-in | fabric-extract-wisdom | takeaway-about-15-words | format | 3/3 | 1/3 |
| One-line | citypaul-claude-md | plan-in-plans-dir | fact | 3/3 | 1/3 |
| One-line | daveshap-default-ci | no-professional-referral | preference | 2/3 | 0/3 |
| One-line | daveshap-default-ci | no-unasked-explanation | preference | 3/3 | 0/3 |
| One-line | fabric-extract-wisdom | habits-at-least-15 | format | 2/3 | 0/3 |
| One-line | fabric-extract-wisdom | ideas-at-least-20 | format | 3/3 | 1/3 |
| trim | daveshap-default-ci | no-unasked-explanation | preference | 3/3 | 1/3 |

### Cost of running the tasks

Mean cost in US dollars of one task run with each version loaded.

| File | Original | One-line | Built-in | trim |
|---|---|---|---|---|
| beast-mode | 0.0063 | 0.0040 | 0.0046 | 0.0040 |
| citypaul-claude-md | 0.0081 | 0.0077 | 0.0083 | 0.0076 |
| cursorrules-nextjs | 0.0063 | 0.0063 | 0.0065 | 0.0063 |
| daveshap-default-ci | 0.0005 | 0.0005 | 0.0004 | 0.0006 |
| daveshap-slide-deck | 0.0013 | 0.0007 | 0.0009 | 0.0007 |
| fabric-extract-wisdom | 0.0444 | 0.0393 | 0.0044 | 0.0345 |
| karpathy-claude-md | 0.0022 | 0.0028 | 0.0022 | 0.0021 |
| openai-agents-agents-md | 0.0070 | 0.0060 | 0.0067 | 0.0063 |
| superclaude-rules | 0.0050 | 0.0042 | 0.0047 | 0.0046 |
| superpowers-tdd | 0.0035 | 0.0032 | 0.0033 | 0.0032 |
| taubench-airline | 0.0005 | 0.0006 | 0.0005 | 0.0007 |
| **Mean of files** | **0.0077** | **0.0069** | **0.0039** | **0.0064** |

### The trims themselves

| | One-line | Built-in | trim |
|---|---|---|---|
| Trims scored | 33 | 11 | 33 |
| Non-derivable facts still present | 235/291 | 88/97 | 276/291 |
| Hard rules still present | 84/111 | 34/37 | 103/111 |
| Original file left untouched | 33/33 | 11/11 | 33/33 |
| Report states size before and after | 15/33 | 2/11 | 33/33 |
| Report gives a reason for every change | 32/33 | 10/11 | 33/33 |
| Report lists what was kept and why | 31/33 | 10/11 | 33/33 |
| Report names the target model | 27/33 | 11/11 | 33/33 |
| Removed instructions the report never mentions, per trim | 2.9 | 0.1 | 0.8 |
| Cost of producing one trim (USD) | 0.006 | 0.053 | 0.014 |
| Time to produce one trim (seconds) | 30 | 93 | 65 |

## claude-opus-5-5 at medium effort

### Size

Words in the file, as a mean over the trims of each arm, with the cut against the original.

| File | Split | Original | One-line | Built-in | trim |
|---|---|---|---|---|---|
| beast-mode | heldout | 2,657 | 450 (-83%) | - | 488 (-82%) |
| citypaul-claude-md | heldout | 2,933 | 885 (-70%) | - | 2,078 (-29%) |
| cursorrules-nextjs | dev | 578 | 341 (-41%) | 565 (-2%) | 416 (-28%) |
| daveshap-default-ci | dev | 242 | 113 (-53%) | 119 (-51%) | 192 (-21%) |
| daveshap-slide-deck | heldout | 200 | 159 (-20%) | - | 173 (-13%) |
| fabric-extract-wisdom | heldout | 539 | 254 (-53%) | - | 430 (-20%) |
| karpathy-claude-md | heldout | 358 | 191 (-47%) | - | 266 (-26%) |
| openai-agents-agents-md | heldout | 2,103 | 1,423 (-32%) | - | 2,069 (-2%) |
| superclaude-rules | dev | 2,127 | 444 (-79%) | 1,522 (-28%) | 798 (-62%) |
| superpowers-tdd | heldout | 1,475 | 619 (-58%) | - | 671 (-55%) |
| taubench-airline | dev | 1,051 | 684 (-35%) | 1,005 (-4%) | 1,040 (-1%) |
| **All files** | | | **-61%** | **-20%** | **-40%** |

### Behaviour

Passes on instruction-dependent checks (the behaviours the original file is responsible for).

| File | Split | Checks | No instructions | Original | One-line | Built-in | trim |
|---|---|---|---|---|---|---|---|
| beast-mode | heldout | 1 | 1/3 | 3/3 | 3/3 | - | 3/3 |
| citypaul-claude-md | heldout | 8 | 0/24 | 24/24 | 24/24 | - | 24/24 |
| cursorrules-nextjs | dev | 8 | 0/24 | 24/24 | 24/24 | 24/24 | 24/24 |
| daveshap-default-ci | dev | 2 | 1/6 | 5/6 | 3/6 | 4/6 | 3/6 |
| daveshap-slide-deck | heldout | 3 | 0/24 | 24/24 | 24/24 | - | 24/24 |
| fabric-extract-wisdom | heldout | 9 | 0/33 | 33/33 | 17/22 | - | 21/22 |
| karpathy-claude-md | heldout | 0 | - | - | - | - | - |
| openai-agents-agents-md | heldout | 7 | 1/21 | 21/21 | 20/21 | - | 21/21 |
| superclaude-rules | dev | 3 | 0/9 | 9/9 | 9/9 | 9/9 | 9/9 |
| superpowers-tdd | heldout | 7 | 0/21 | 20/21 | 21/21 | - | 21/21 |
| taubench-airline | dev | 4 | 0/12 | 12/12 | 12/12 | 12/12 | 12/12 |
| **Dev files** | | | **1/51** | **50/51** | **48/51** | **49/51** | **48/51** |
| **Held-out files** | | | **2/126** | **125/126** | **109/115** | - | **114/115** |
| **All** | | | **3/177** | **175/177** | **157/166** | **49/51** | **162/166** |

Checks the model passes even with no instructions (so the rule behind them changes nothing): Original 87/87, One-line 86/86, Built-in 30/30, trim 86/86.

Checks where an arm passed at least two-thirds less often than the original:

| Arm | File | Check | Kind | Original | Arm |
|---|---|---|---|---|---|
| One-line | daveshap-default-ci | no-professional-referral | preference | 2/3 | 0/3 |
| One-line | fabric-extract-wisdom | habits-at-least-15 | format | 3/3 | 0/2 |
| One-line | fabric-extract-wisdom | ideas-at-least-20 | format | 3/3 | 0/2 |

Checks left out because the original file itself fails them on this model: `beast-mode/markdown-todo-list`, `daveshap-default-ci/no-unasked-explanation`.

### Cost of running the tasks

Mean cost in US dollars of one task run with each version loaded.

| File | Original | One-line | Built-in | trim |
|---|---|---|---|---|
| beast-mode | 0.1102 | 0.0675 | - | 0.0704 |
| citypaul-claude-md | 0.1595 | 0.1117 | - | 0.1299 |
| cursorrules-nextjs | 0.0848 | 0.0823 | 0.0804 | 0.0783 |
| daveshap-default-ci | 0.0180 | 0.0195 | 0.0161 | 0.0209 |
| daveshap-slide-deck | 0.0273 | 0.0203 | - | 0.0298 |
| fabric-extract-wisdom | 0.4946 | 0.3747 | - | 0.4874 |
| karpathy-claude-md | 0.0494 | 0.0510 | - | 0.0519 |
| openai-agents-agents-md | 0.1389 | 0.1114 | - | 0.1352 |
| superclaude-rules | 0.1229 | 0.0838 | 0.1060 | 0.0824 |
| superpowers-tdd | 0.1029 | 0.0935 | - | 0.0831 |
| taubench-airline | 0.0163 | 0.0189 | 0.0160 | 0.0178 |
| **Mean of files** | **0.1204** | **0.0940** | - | **0.1079** |

### The trims themselves

| | One-line | Built-in | trim |
|---|---|---|---|
| Trims scored | 33 | 4 | 33 |
| Non-derivable facts still present | 257/291 | 32/32 | 278/291 |
| Hard rules still present | 88/111 | 12/12 | 104/111 |
| Original file left untouched | 33/33 | 4/4 | 33/33 |
| Report states size before and after | 17/33 | 1/4 | 33/33 |
| Report gives a reason for every change | 33/33 | 4/4 | 32/33 |
| Report lists what was kept and why | 30/33 | 4/4 | 33/33 |
| Report names the target model | 30/33 | 4/4 | 33/33 |
| Removed instructions the report never mentions, per trim | 2.0 | 0.2 | 0.6 |
| Cost of producing one trim (USD) | 0.103 | 0.804 | 0.241 |
| Time to produce one trim (seconds) | 25 | 77 | 51 |

## Target-model handling

Three runs per cell with the released skill. See `harness/asktest.py`.

| Situation | Right behaviour | One-line | trim |
|---|---|---|---|
| File is plainly for the assistant that is running; no model named | use the stated model ID and say it was assumed | 0/3 Haiku, 0/3 Opus | 3/3 Haiku, 3/3 Opus |
| Person says the instructions are for ChatGPT; no model named | ask which model and wait | 0/3 Haiku, 0/3 Opus | 3/3 Haiku, 3/3 Opus |

Claude Code tells every session its own model ID, so the case where the app names no model at all could not be produced.

## Triggering

Twenty queries, with the skill installed beside Claude Code's bundled skills. See `harness/triggertest.py` and `trigger_queries.json`.

| | Haiku (3 runs each) | Opus (1 run each) |
|---|---|---|
| Direct requests that should load it | 18/18 | 6/6 |
| Indirect requests that should load it | 8/12 | 3/4 |
| Near-misses that should not | 0/30 | 0/10 |

This is a friendly setting: few neighbouring skills, and none that compete for the same job except the bundled audit. Published trigger rates with dozens of skills installed are much lower. Invoking the skill by name does not depend on any of this.

## Deletion test

`ITERATIONS.md` has the table: which sentences of the skill were removed because the behaviour was the same without them, which were kept because it changed, and which were kept as design decisions.

## Spend

Recorded cost of every run behind these tables, including drafts, the deletion test and the judge: about $122, of which $105 was Opus, $10 Haiku and $7 the Sonnet judge. This excludes the sessions that wrote the probes and the session that orchestrated the work.
