## Prompt audit: `instructions.md` (target: `claude-haiku-5-5`)

**Assumptions (Step 0):**
- **Scope:** `instructions.md` only, since the request names it. It is the only file in the working directory, and the one link it contains (`writing-good-tests.md`) is not present here.
- **Target:** `claude-haiku-5-5`, as you named it.
- **Provenance:** not available. The directory is not a git repository, so there is no blame history.

**Headline:** The file is mostly sound. Its rules are concrete and its reasons are stated. The only dated pattern I could tie to a documented Haiku 5.5 behavior is emphasis with no reason attached, in two places. I changed only those. The one real question for you is whether `writing-good-tests.md` ships alongside this skill.

**Counts:** Group 1 has 2 edits and 3 flags. Group 2 has 1 flag. Group 3 and Group 4 are not applicable (no tool descriptions, no request-building code). Nothing is high confidence.

### Findings

| Location | Evidence | Pattern | Why it's obsolete | Confidence | Action |
|---|---|---|---|---|---|
| `instructions.md:115` | `**MANDATORY. Never skip.**` | 1a: emphasis with no adjacent "because" | The reason ("a test you never watched fail proves nothing") is already stated in Core principle. Haiku 5.5 follows instructions literally, so the caps add nothing. | Medium | **Rewrite** → `Run it and watch it fail. A test that never failed doesn't show it can catch the bug.` (applied in `trimmed.md`) |
| `instructions.md:170` | `**MANDATORY.**` | 1a, same | Same register problem. | Medium | **Rewrite** → `Run it and confirm the result before moving on.` (applied in `trimmed.md`) |
| `instructions.md:216` | `read [writing-good-tests.md](writing-good-tests.md)` | 2: named path | The file is not in this directory. If it ships with the skill, the link is fine. If not, the four bullets beneath it are self-contained and the link should go. I can't tell from the scope I was given. | Low | Flag |
| `instructions.md:185-193` | "Other tests" paragraph, ending "a report falsified by omission" | 1a / 1c: overwrought register | The requirement is correct and matches Haiku 5.5's documented verification guidance (`shared/model-migration.md`, "Verification on coding tasks"). Kept. The tone could be plainer, but the wording carries the requirement. | Low | Flag only |
| `instructions.md:222-254` | Rationalizations table plus Red Flags list | 1c: repetition | About 10 of the 13 Red Flags repeat a table row. This is working redundancy with no contradiction and no evidence of failure, so the keep-list (item 8) protects it. | Low | Flag only |
| `instructions.md:256-291` | "Example: Bug Fix" | 1c: example over-indexing | A full gold trace of the cycle the prose already covers. Possibly removable, but the keep-list (item 8) covers worked examples that aren't causing errors. | Low | Flag only |
| `instructions.md:24, 312, 330` | "ask your human partner" | Not a listed pattern | Assumes an interactive human. If the skill runs unattended, those branches have no path. Depends on the harness. | Low | Flag only |

**Kept on purpose:** the Iron Law and its "Delete means delete" prohibitions (each has a stated reason), the Verification Checklist and Final Rule (a deliberate recap), the Good/Bad contrast pairs, and the dot diagram.

### Proposed diff (in `/root/trim-sbx/28066b3bc0aa/trimmed.md`)

- **Hunk 1, line 115:** `**MANDATORY. Never skip.**` → `Run it and watch it fail. A test that never failed doesn't show it can catch the bug.`
- **Hunk 2, line 170:** `**MANDATORY.**` → `Run it and confirm the result before moving on.`

`instructions.md` is unchanged.

### Verification

- I did **not** run a behavioral probe (Step 7). There is no eval here, and the edits are unverified against Haiku 5.5.
- Bash is disabled in this session, so I couldn't `cp`. I wrote `trimmed.md` by reproducing `instructions.md` and then applied the two edits. Both files have 330 lines, and a grep confirms the two changed lines. I did not byte-diff them. Running `diff instructions.md trimmed.md` should show exactly those two hunks.