# Probe format

One JSON file per corpus file, at `evals/probes/<id>.json`. A probe file says how
to tell whether a version of the instruction file still produces the behaviour
the original produces.

```json
{
  "id": "<corpus id>",
  "mode": "agent" | "chat",
  "scaffold": "<dir under evals/scaffolds>",      // agent mode only, optional
  "allowed_bash": ["git *"],                      // agent mode only, optional
  "notes": "one line on what kind of file this is",
  "protected": [ {"id": "...", "why": "...", "patterns": ["regex", "..."]} ],
  "facts":     [ {"id": "...", "patterns": ["regex", "..."]} ],
  "tasks": [
    { "id": "...", "prompt": "what the user types",
      "checks": [ {"id": "...", "kind": "...", "rule": "the quoted rule this check observes", "all": [ <primitive>, ... ]} ] }
  ]
}
```

## How a task runs

- **agent mode**: a fresh sandbox is copied from the scaffold, the instruction
  variant is written to `CLAUDE.md`, the sandbox becomes a git repository on
  branch `main` with one commit, and the prompt runs in headless Claude Code with
  the tools Read, Write, Edit, Glob and Grep. Bash is available only for the
  command patterns in `allowed_bash`. The "none" arm has no `CLAUDE.md`.
- **chat mode**: the instruction variant is the system prompt, there are no
  tools, and the prompt is a single user message. The "none" arm uses
  "You are a helpful assistant."

## Checks

A check passes when every primitive in `all` is true. `kind` is one of:

| kind | observes |
|---|---|
| fact | a project fact the model cannot know without the file (a path, command, price, name) |
| convention | a code or file convention |
| guard | a rule that prevents an irreversible, fragile or out-of-policy action |
| format | a required output shape |
| preference | how the author wants to be answered |
| process | a ritual or ordering of steps |

Primitives (regexes are Python; `flags` is any of `i`, `s`, `m`):

| type | fields | true when |
|---|---|---|
| `text_regex` | pattern, expect=true, flags="is" | the final reply matches (or does not match) |
| `word_count` | max, min | the final reply's word count is in range |
| `regex_count` | pattern, eq or min/max, glob (optional), flags="m" | the number of matches in the reply (or in changed files matching glob) is in range |
| `glob_exists` | glob | a created or modified file matches (alternatives separated by `\|`) |
| `glob_absent` | glob | no created or modified file matches |
| `file_regex` | glob, pattern, expect=true, flags="ms" | changed files matching glob contain (or lack) the pattern; false when no file matches |
| `file_order` | glob, first, then | in one changed file, `first` appears before `then` |
| `path_regex` | glob, pattern, quantifier="all", expect=true | changed paths matching glob match the pattern |
| `write_order` | first, then | the first Write/Edit to a path matching `first` comes before the first to a path matching `then` |
| `bash_regex` | pattern, expect=true | some Bash call's command matches |
| `tool_used` | name, expect=true | the tool was called |
| `git_branch_not` | names | the sandbox ends on a branch outside `names` |
| `git_no_new_commits` | | `main` still has exactly one commit |

## `protected` and `facts`

These are checked against the text of a trimmed file, not against behaviour.
`protected` lists hard rules that guard fragile or irreversible work. `facts`
lists things the model cannot derive. Each entry holds if every regex in
`patterns` matches the trimmed text, so patterns target key tokens (a path, a
number, a command) and not the original phrasing.

## Rules for writing probes

1. Write probes from the original file only, before looking at any trimmed version.
2. The prompt must not mention the rule being checked.
3. Prefer rules a model would not follow by default; the "none" arm then fails and the check is informative.
4. Keep checks deterministic. If a behaviour needs a judge to recognise, leave it out.
5. A check the original file fails in two of three trials is dropped and listed as invalid.
