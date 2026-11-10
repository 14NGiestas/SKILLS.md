#!/usr/bin/env python3
"""Lint the YAML frontmatter of every skill in this repository.

A skill is a folder containing a SKILL.md file. The folder name must match the
frontmatter `name` field so that opencode/Claude-style discovery works.

Usage:
    python3 scripts/lint_skills.py

Requires PyYAML:
    pip install pyyaml
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("error: PyYAML is required. Install it with: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".github", ".opencode"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_KEYS = ("name", "description")


def skill_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(ROOT.rglob("SKILL.md")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS:
            continue
        files.append(path)
    return files


def stray_markdown() -> list[Path]:
    strays: list[Path] = []
    for language in ("en", "pt-br"):
        for path in sorted((ROOT / language).rglob("*.md")):
            if path.name in {"SKILL.md", "README.md"}:
                continue
            if "references" in path.relative_to(ROOT / language).parts:
                continue
            strays.append(path)
    return strays


def split_frontmatter(text: str) -> str | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[1:index])
    return None


def main() -> int:
    errors: list[str] = []
    seen: dict[str, Path] = {}

    for path in stray_markdown():
        rel = path.relative_to(ROOT)
        errors.append(
            f"{rel}: unexpected Markdown file; use <skill-name>/SKILL.md or README.md"
        )

    files = skill_files()
    if not files:
        print("No SKILL.md files found. Nothing to lint.")
        return 1

    for path in files:
        rel = path.relative_to(ROOT)
        raw = split_frontmatter(path.read_text(encoding="utf-8"))
        if raw is None:
            errors.append(f"{rel}: missing YAML frontmatter (--- ... ---)")
            continue

        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML\n    {exc}")
            if "mapping values are not allowed" in str(exc):
                errors.append(
                    f"{rel}: hint: a description containing ': ' must be wrapped in quotes"
                )
            continue

        if not isinstance(data, dict):
            errors.append(f"{rel}: frontmatter must be a YAML mapping")
            continue

        for key in REQUIRED_KEYS:
            value = data.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{rel}: missing or empty '{key}'")

        name = data.get("name")
        if isinstance(name, str):
            expected = path.parent.name
            if not NAME_RE.match(name):
                errors.append(
                    f"{rel}: name '{name}' must be kebab-case (e.g. bardin-coding)"
                )
            if name != expected:
                errors.append(
                    f"{rel}: name '{name}' must match the folder name '{expected}'"
                )
            if name in seen:
                errors.append(
                    f"{rel}: duplicate name '{name}' (already used in {seen[name]})"
                )
            else:
                seen[name] = rel

        description = data.get("description")
        if isinstance(description, str) and len(description) > 1024:
            errors.append(
                f"{rel}: description is {len(description)} chars (keep it under 1024)"
            )

    manifest = ROOT / "llms.txt"
    if not manifest.exists():
        errors.append("llms.txt: missing agent discovery manifest")
    else:
        manifest_text = manifest.read_text(encoding="utf-8")
        for name in sorted(seen):
            if name not in manifest_text:
                errors.append(f"llms.txt: missing entry for skill '{name}'")

    if errors:
        print(f"Found {len(errors)} problem(s) in {len(files)} skill file(s):\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(files)} skill file(s) validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
