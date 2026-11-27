#!/usr/bin/env python3
"""Shared helpers for the trim eval harness. Standard library only.

Everything here drives the `claude` CLI in headless mode. A provider adapter
for another CLI or API only needs to return the same dict that `run_claude`
returns (see `PROVIDERS` at the bottom of this file).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import threading
import time
import uuid
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
EVALS = ROOT / "evals"
CORPUS = EVALS / "corpus"
PROBES = EVALS / "probes"
SCAFFOLDS = EVALS / "scaffolds"
RESULTS = EVALS / "results"

# Claude Code does not load CLAUDE.md or project skills when the working
# directory is under its own temp scratchpad, so sandboxes live elsewhere.
SBX_ROOT = Path(os.environ.get("TRIM_SBX_ROOT", str(Path.home() / "trim-sbx")))

# Run configurations: the model that is both the trim target and the model
# the tasks run on, plus the effort it runs at.
CONFIGS = {
    "haiku-high": {"provider": "claude", "model": "claude-haiku-5-5", "effort": "high"},
    "opus-medium": {"provider": "claude", "model": "claude-opus-5-5", "effort": "medium"},
    "sonnet-medium": {"provider": "claude", "model": "claude-sonnet-5-5", "effort": "medium"},
}

NEUTRAL_SYSTEM = "You are a helpful assistant.\n"
AGENT_TOOLS = "Read,Write,Edit,Glob,Grep"

_write_lock = threading.Lock()


def words(text: str) -> int:
    return len(text.split())


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with _write_lock:
        with path.open("a") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict]:
    gz = Path(str(path) + ".gz")
    if path.exists():
        text = path.read_text()
    elif gz.exists():
        import gzip
        text = gzip.decompress(gz.read_bytes()).decode("utf-8", "replace")
    else:
        return []
    out = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def load_probe(file_id: str) -> dict:
    return json.loads((PROBES / f"{file_id}.json").read_text())


def corpus_ids(split: str | None = None) -> list[str]:
    ids = []
    for d in sorted(CORPUS.iterdir()):
        src = d / "source.json"
        if src.exists():
            meta = json.loads(src.read_text())
            if split in (None, "all") or meta["split"] == split:
                ids.append(meta["id"])
    return ids


def source_meta(file_id: str) -> dict:
    return json.loads((CORPUS / file_id / "source.json").read_text())


def original_text(file_id: str) -> str:
    return (CORPUS / file_id / "original.md").read_text()


def trim_dir(file_id: str, config: str, arm: str, k: int) -> Path:
    return RESULTS / "trims" / file_id / config / arm / str(k)


def variant_text(file_id: str, config: str, arm: str, k: int) -> str | None:
    """Instruction text for an arm. None means no instructions at all."""
    if arm == "none":
        return None
    if arm == "original":
        return original_text(file_id)
    p = trim_dir(file_id, config, arm, k) / "trimmed.md"
    if not p.exists():
        raise FileNotFoundError(f"missing trim: {p}")
    return p.read_text()


# --------------------------------------------------------------------------
# Sandboxes
# --------------------------------------------------------------------------

def make_sandbox(scaffold: str | None = None) -> Path:
    sbx = SBX_ROOT / uuid.uuid4().hex[:12]
    if scaffold:
        shutil.copytree(SCAFFOLDS / scaffold, sbx)
    else:
        sbx.mkdir(parents=True)
    return sbx


def git_init(sbx: Path) -> None:
    env = dict(os.environ, GIT_AUTHOR_NAME="eval", GIT_AUTHOR_EMAIL="eval@example.com",
               GIT_COMMITTER_NAME="eval", GIT_COMMITTER_EMAIL="eval@example.com")
    for cmd in (["git", "init", "-q", "-b", "main", "."], ["git", "add", "-A"],
                ["git", "commit", "-q", "-m", "initial commit"]):
        subprocess.run(cmd, cwd=sbx, env=env, capture_output=True, check=False)


def snapshot(sbx: Path) -> dict[str, str]:
    snap = {}
    for p in sbx.rglob("*"):
        if p.is_file() and ".git" not in p.relative_to(sbx).parts:
            try:
                snap[p.relative_to(sbx).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
            except OSError:
                pass
    return snap


def changed_files(sbx: Path, before: dict[str, str]) -> dict[str, str]:
    """Files created or modified since `before`, with text content."""
    out = {}
    for rel, digest in snapshot(sbx).items():
        if before.get(rel) != digest:
            try:
                out[rel] = (sbx / rel).read_text(errors="replace")[:200_000]
            except OSError:
                out[rel] = ""
    return out


def git_branch(sbx: Path) -> str:
    r = subprocess.run(["git", "branch", "--show-current"], cwd=sbx, capture_output=True, text=True)
    return r.stdout.strip()


def git_commit_count(sbx: Path, ref: str = "HEAD") -> int:
    r = subprocess.run(["git", "rev-list", "--count", ref], cwd=sbx, capture_output=True, text=True)
    try:
        return int(r.stdout.strip())
    except ValueError:
        return -1


# --------------------------------------------------------------------------
# Running a model
# --------------------------------------------------------------------------

LIMIT = re.compile(r"hit your .{0,30}limit|usage limit reached", re.I)
LIMIT_FLAG = RESULTS / ".limit_hit"


def limit_hit() -> bool:
    """True once any run in this process tree has been refused for usage limits."""
    return LIMIT_FLAG.exists()


RETRYABLE = re.compile(r"rate.?limit|overloaded|529|429|timeout|timed out|ECONNRESET|socket hang up|"
                       r"fetch failed|503|502|internal server error", re.I)


def run_claude(prompt: str, config: str, cwd: Path, *, system_prompt_file: Path | None = None,
               tools: str = "", allowed_tools: str | None = None, permission_mode: str | None = None,
               slash: bool = False, budget: float = 1.5, timeout: int = 900, retries: int = 2) -> dict:
    """Run one headless Claude Code session and return a normalised record."""
    cfg = CONFIGS[config]
    cmd = ["claude", "-p", prompt, "--model", cfg["model"], "--effort", cfg["effort"],
           "--output-format", "stream-json", "--verbose", "--no-session-persistence",
           "--strict-mcp-config", "--setting-sources", "project",
           "--max-budget-usd", str(budget), "--tools", tools]
    if allowed_tools:
        cmd += ["--allowedTools", allowed_tools]
    if permission_mode:
        cmd += ["--permission-mode", permission_mode]
    if not slash:
        cmd += ["--disable-slash-commands"]
    if system_prompt_file is not None:
        cmd += ["--system-prompt-file", str(system_prompt_file)]
    else:
        cmd += ["--exclude-dynamic-system-prompt-sections"]

    last = None
    for attempt in range(retries + 1):
        start = time.time()
        try:
            proc = subprocess.run(cmd, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True,
                                  text=True, timeout=timeout)
            rec = _parse_stream(proc.stdout)
            rec["exit_code"] = proc.returncode
            if rec.get("result_missing"):
                rec["error"] = (proc.stderr or proc.stdout)[-500:]
        except subprocess.TimeoutExpired:
            rec = {"is_error": True, "error": f"timeout after {timeout}s", "text": "", "tool_calls": [],
                   "cost_usd": 0.0, "usage": {}, "num_turns": 0, "duration_ms": int((time.time() - start) * 1000)}
        rec["attempts"] = attempt + 1
        rec["wall_s"] = round(time.time() - start, 1)
        last = rec
        if LIMIT.search((rec.get("error") or "") + " " + (rec.get("text") or "")[:300]):
            rec["is_error"] = True
            rec["limit_hit"] = True
            LIMIT_FLAG.write_text(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
            break
        blob = (rec.get("error") or "") + (rec.get("text") or "" if rec.get("is_error") else "")
        if rec.get("is_error") and RETRYABLE.search(blob) and attempt < retries:
            time.sleep(15 * (attempt + 1))
            continue
        break
    return last


def _parse_stream(stdout: str) -> dict:
    tool_calls, texts, result = [], [], None
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = ev.get("type")
        if t == "assistant":
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    inp = block.get("input", {}) or {}
                    tool_calls.append({
                        "name": block.get("name"),
                        "path": inp.get("file_path") or inp.get("path") or inp.get("pattern"),
                        "command": inp.get("command"),
                        "skill": inp.get("skill"),
                    })
                elif block.get("type") == "text":
                    texts.append(block.get("text", ""))
        elif t == "result":
            result = ev
    if result is None:
        return {"is_error": True, "result_missing": True, "text": "\n".join(texts), "tool_calls": tool_calls,
                "cost_usd": 0.0, "usage": {}, "num_turns": 0, "duration_ms": 0}
    usage = result.get("usage", {}) or {}
    return {
        "is_error": bool(result.get("is_error")),
        "subtype": result.get("subtype"),
        "text": result.get("result") or "",
        "all_text": "\n".join(texts),
        "tool_calls": tool_calls,
        "cost_usd": result.get("total_cost_usd") or 0.0,
        "usage": {k: usage.get(k, 0) for k in ("input_tokens", "output_tokens",
                                                "cache_read_input_tokens", "cache_creation_input_tokens")},
        "num_turns": result.get("num_turns", 0),
        "duration_ms": result.get("duration_ms", 0),
    }


def run_not_configured(provider: str):
    def _run(*_args, **_kwargs):
        raise RuntimeError(
            f"No runner configured for provider '{provider}'. See evals/README.md, "
            f"'Running on other providers', for the adapter contract.")
    return _run


# Provider adapters. Only `claude` is implemented and exercised. The others are
# placeholders so that a config such as {"provider": "openai", "model": ...}
# fails loudly instead of silently running on the wrong model.
PROVIDERS = {
    "claude": run_claude,
    "openai": run_not_configured("openai"),
    "google": run_not_configured("google"),
}


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def _flags(spec: dict, default: str = "is") -> int:
    f = 0
    for ch in spec.get("flags", default):
        f |= {"i": re.I, "s": re.S, "m": re.M}[ch]
    return f


def _match_glob(path: str, glob: str) -> bool:
    return any(PurePosixPath(path).full_match(g.strip()) for g in glob.split("|"))


def _files(ctx: dict, glob: str) -> dict[str, str]:
    return {p: c for p, c in ctx["changed"].items() if _match_glob(p, glob)}


def eval_prim(spec: dict, ctx: dict) -> bool:
    t = spec["type"]
    if t == "text_regex":
        return bool(re.search(spec["pattern"], ctx["text"], _flags(spec))) == spec.get("expect", True)
    if t == "word_count":
        n = words(ctx["text"])
        return n <= spec.get("max", 10**9) and n >= spec.get("min", 0)
    if t == "glob_exists":
        return bool(_files(ctx, spec["glob"]))
    if t == "glob_absent":
        return not _files(ctx, spec["glob"])
    if t == "file_regex":
        files = _files(ctx, spec["glob"])
        if not files:
            return False  # the task produced nothing to judge
        blob = "\n".join(files.values())
        return bool(re.search(spec["pattern"], blob, _flags(spec, "ms"))) == spec.get("expect", True)
    if t == "regex_count":
        if spec.get("glob"):
            files = _files(ctx, spec["glob"])
            if not files:
                return False
            blob = "\n".join(files.values())
        else:
            blob = ctx["text"]
        n = len(re.findall(spec["pattern"], blob, _flags(spec, "m")))
        if "eq" in spec:
            return n == spec["eq"]
        return spec.get("min", 0) <= n <= spec.get("max", 10**9)
    if t == "path_regex":
        # every (or any) changed path matching `glob` must match / not match `pattern`
        paths = list(_files(ctx, spec.get("glob", "**")))
        if not paths:
            return False
        hits = [bool(re.search(spec["pattern"], p)) for p in paths]
        ok = all(hits) if spec.get("quantifier", "all") == "all" else any(hits)
        return ok == spec.get("expect", True)
    if t == "git_branch_not":
        return ctx.get("git_branch") not in spec["names"]
    if t == "git_no_new_commits":
        return ctx.get("git_commits_main") == 1
    if t == "write_order":
        # first write to a path matching `first` happens before first write matching `then`
        order = [c["path"] or "" for c in ctx["tool_calls"] if c["name"] in ("Write", "Edit")]
        a = next((i for i, p in enumerate(order) if re.search(spec["first"], p)), None)
        b = next((i for i, p in enumerate(order) if re.search(spec["then"], p)), None)
        if a is None:
            return False
        return b is None or a < b
    if t == "file_order":
        # in the changed files matching `glob`, `first` appears before `then`
        files = _files(ctx, spec["glob"])
        if not files:
            return False
        for content in files.values():
            a = re.search(spec["first"], content, _flags(spec, "ms"))
            b = re.search(spec["then"], content, _flags(spec, "ms"))
            if a and b and a.start() < b.start():
                return True
        return False
    if t == "bash_regex":
        hit = any(c["name"] == "Bash" and re.search(spec["pattern"], c.get("command") or "", re.I)
                  for c in ctx["tool_calls"])
        return hit == spec.get("expect", True)
    if t == "tool_used":
        used = any(c["name"] == spec["name"] for c in ctx["tool_calls"])
        return used == spec.get("expect", True)
    raise ValueError(f"unknown check type: {t}")


def eval_check(check: dict, ctx: dict) -> dict:
    prims = check.get("all") or []
    results = [eval_prim(p, ctx) for p in prims]
    passed = all(results)
    if check.get("any"):
        passed = passed and any(eval_prim(p, ctx) for p in check["any"])
    return {"pass": passed, "detail": results}
