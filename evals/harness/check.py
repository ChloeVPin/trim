#!/usr/bin/env python3
"""Mechanical checks for contributions. No model calls, no network, no dependencies.

  python3 evals/harness/check.py            check only
  python3 evals/harness/check.py --package  rebuild dist/ from skills/trim, then check

Exits 1 and lists every problem if any rule is broken. The rules are the ones
that are cheap to verify and expensive to get wrong; AGENTS.md covers the rest.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "trim"
MAX_BODY_WORDS = 300  # the body is 290; raising this number is a change a reviewer should see
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SHOUT = re.compile(r"\b(MUST|NEVER|ALWAYS|CRITICAL|IMPORTANT|MANDATORY)\b")
TAG = re.compile(r"\[([AOG]\d+)\]")

problems: list[str] = []


def bad(msg: str) -> None:
    problems.append(msg)


def check_skill() -> str:
    text = (SKILL / "SKILL.md").read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        bad("SKILL.md: no frontmatter block")
        return ""
    front, body = m.group(1), m.group(2)
    keys = re.findall(r"^([A-Za-z][\w-]*):", front, re.M)
    for k in keys:
        if k not in ALLOWED_KEYS:
            bad(f"SKILL.md: frontmatter key '{k}' is not in the open spec; Claude app uploads reject it")
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    name = name.group(1).strip().strip('"') if name else ""
    if name != SKILL.name:
        bad(f"SKILL.md: name '{name}' must equal the folder name '{SKILL.name}'")
    if re.search(r"claude|anthropic", name, re.I):
        bad("SKILL.md: name must not contain 'claude' or 'anthropic'")
    desc = re.search(r'^description:\s*"?(.*?)"?$', front, re.M)
    desc = desc.group(1) if desc else ""
    if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
        bad("SKILL.md: description must be 1 to 1024 characters with no angle brackets")
    words = len(body.split())
    if words > MAX_BODY_WORDS:
        bad(f"SKILL.md: body is {words} words, limit {MAX_BODY_WORDS}. A longer skill needs deletion-test "
            f"evidence (evals/harness/ablate.py); raise MAX_BODY_WORDS in the same change if it has it")
    for hit in SHOUT.findall(body):
        bad(f"SKILL.md: '{hit}' in capitals. State the rule at normal volume with its reason")
    extra = sorted(p.relative_to(SKILL).as_posix() for p in SKILL.rglob("*")
                   if p.is_file() and p.relative_to(SKILL).as_posix() not in ("SKILL.md", "references/profiles.md"))
    if extra:
        bad(f"skills/trim: unexpected files {extra}. The skill is two text files: no scripts, no assets")
    v = re.search(r'version:\s*"?([\d.]+)"?', front)
    return v.group(1) if v else ""


def check_profiles() -> None:
    text = (SKILL / "references" / "profiles.md").read_text()
    if "## Sources" not in text:
        bad("profiles.md: no '## Sources' section")
        return
    claims, sources = text.split("## Sources", 1)
    defined = {}
    for line in sources.splitlines():
        m = re.match(r"- \[([AOG]\d+)\]\s+(.*)", line)
        if m:
            defined[m.group(1)] = m.group(2)
            if "http" not in m.group(2):
                bad(f"profiles.md: source [{m.group(1)}] has no URL")
    for tag in sorted(set(TAG.findall(claims))):
        if tag not in defined:
            bad(f"profiles.md: [{tag}] is cited but not listed under Sources")
    section = None
    for n, line in enumerate(claims.splitlines(), 1):
        if line.startswith("## "):
            section = line[3:].strip()
        if section in ("Anthropic", "OpenAI", "Google"):
            if line.startswith("### ") and not re.search(r"\((tested[^)]*|from documentation, untested)\)", line):
                bad(f"profiles.md:{n}: model heading needs '(tested ...)' or '(from documentation, untested)'")
            if line.startswith("- ") and not TAG.search(line) and "unverified" not in line.lower():
                bad(f"profiles.md:{n}: claim has no source tag and is not marked unverified: {line[:60]}...")
    if not re.search(r"Checked on \d{4}-\d{2}-\d{2}", text):
        bad("profiles.md: the opening line must say 'Checked on YYYY-MM-DD'")


def check_versions(skill_version: str) -> None:
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    top = re.search(r"^## ([\d.]+)", (ROOT / "CHANGELOG.md").read_text(), re.M)
    top = top.group(1) if top else ""
    if not (skill_version == plugin.get("version") == top):
        bad(f"versions differ: SKILL.md {skill_version}, plugin.json {plugin.get('version')}, CHANGELOG {top}")
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    if market["plugins"][0]["name"] != plugin["name"]:
        bad("marketplace.json plugin name differs from plugin.json name")


def check_dist() -> None:
    z = ROOT / "dist" / "trim.zip"
    if not z.exists():
        bad("dist/trim.zip is missing. Rebuild: python3 evals/harness/check.py --package")
        return
    with zipfile.ZipFile(z) as zf:
        packed = {n: zf.read(n) for n in zf.namelist() if not n.endswith("/")}
    current = {f"trim/{p.relative_to(SKILL).as_posix()}": p.read_bytes() for p in SKILL.rglob("*") if p.is_file()}
    if packed != current:
        bad("dist/trim.zip does not match skills/trim. Rebuild: python3 evals/harness/check.py --package")


def check_corpus() -> None:
    for src in sorted((ROOT / "evals" / "corpus").glob("*/source.json")):
        meta = json.loads(src.read_text())
        digest = hashlib.sha256((src.parent / "original.md").read_bytes()).hexdigest()
        if digest != meta["sha256"]:
            bad(f"evals/corpus/{meta['id']}/original.md was edited. Corpus files are pinned to upstream commits")
    for probe in sorted((ROOT / "evals" / "probes").glob("*.json")):
        try:
            json.loads(probe.read_text())
        except json.JSONDecodeError as e:
            bad(f"{probe.relative_to(ROOT)}: invalid JSON ({e})")


def package() -> None:
    """Rebuild dist/trim.zip and dist/trim.skill from skills/trim."""
    (ROOT / "dist").mkdir(exist_ok=True)
    tmp = ROOT / "dist" / "trim.zip.tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file():
                zf.write(f, f"trim/{f.relative_to(SKILL).as_posix()}")
    data = tmp.read_bytes()
    (ROOT / "dist" / "trim.zip").write_bytes(data)
    (ROOT / "dist" / "trim.skill").write_bytes(data)
    tmp.unlink()
    print("rebuilt dist/trim.zip and dist/trim.skill")


def main() -> None:
    if "--package" in sys.argv:
        package()
    version = check_skill()
    check_profiles()
    check_versions(version)
    check_dist()
    check_corpus()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("ok: skill, profiles, versions, package and corpus all pass")


if __name__ == "__main__":
    main()
