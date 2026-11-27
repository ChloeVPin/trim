The audit is done on `instructions.md`, which is unchanged. The proposed edit is applied to a copy at `/root/trim-sbx/2a018a511c0b/trimmed.md`. The surface is mostly clean: one medium-confidence finding.

**Step 0 assumptions**
- **Scope:** `instructions.md` only, as named in the request. It is the whole prompt surface (one file, a system prompt for a slide-deck builder). No tool definitions, request code, skills, or config files were in scope.
- **Target model:** `claude-haiku-5-5`, as named in the request.
- **Provider markers:** none found.
- **Provenance:** not a git repository, so there is no blame history.

**Inventory:** four sections, `MISSION`, `INPUT`, `OUTPUT FORMAT`, `EXAMPLE OUTPUT`.

**Audit report**

| Location | Evidence | Pattern | Why obsolete | Confidence | Action |
|---|---|---|---|---|---|
| `instructions.md:13-23` | `# EXAMPLE OUTPUT` followed by one gold output ("Speed Chess"), while the input is described as "highly varied" | 1c, example over-indexing | Current models match a single gold example's content, length, and wording. Here the example is chess, and the input may be any topic. | Medium | `rewrite` the heading to mark the example as format-only |
| `instructions.md:9-11` | "Two to Four Words Max", "2 or 3 complete sentences", "Exactly five points" | 1f / keep-list 7 | Word caps look like the numeric ceilings in 1f, but these are the layout and format spec of a slide deck. | n/a | Kept |
| `instructions.md:10` | "Concept Description of Definition" | Not a dated pattern | The label reads as garbled, and the model may echo it as a heading. | Low | `flag`, not edited. Please confirm the intended label. |
| `instructions.md:1,7,13` | `MISSION` / `INPUT` / `OUTPUT FORMAT` / `EXAMPLE OUTPUT` headers | 2, idiom-dating only | Generic template scaffolding, but nothing in it misleads the model. | Low | `flag` only |

Group counts: Group 1 has one medium finding and one low flag. Groups 2, 3, and 4 are not applicable (no skill or config files, no tool definitions, no request-building code in scope). I found no pressure language, prefills, "think step by step" scaffolds, or forced-JSON machinery. The role line is fine.

**Proposed diff (applied to `trimmed.md`)**

```diff
-# EXAMPLE OUTPUT
+# EXAMPLE OUTPUT (illustrative only: it shows the format; the topic, title wording, and content come from the input)
```

This is the only hunk. The example stays because it is a format-sensitive output (keep-list 7), and the label is the documented fix.

**Verification:** I checked this by reading only. I did not call the model, so no budget was spent. The change needs a behavioral check before you rely on it. Run 3–5 varied topics through Haiku 5.5 with the original and the trimmed prompt, and check whether the output still pulls in chess content or copies the example's wording. If chess still leaks, the stronger fix is to add a second example in a different domain, also labeled illustrative. I can draft that if you want it.