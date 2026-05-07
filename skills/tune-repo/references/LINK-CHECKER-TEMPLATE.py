#!/usr/bin/env python3
"""Dependency-free local Markdown link checker.

Copy into a repository as scripts/check_markdown_links.py and adjust ignore
patterns if needed. It validates local relative links and simple Markdown
heading anchors, while skipping external URLs and mailto/tel links.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORE_PARTS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
    "vendor",
}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


def iter_markdown() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in IGNORE_PARTS for part in rel.parts):
            continue
        files.append(path)
    return sorted(files)


def slugify(heading: str) -> str:
    """Approximate GitHub-style Markdown heading anchors."""
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = heading.strip().lower()
    heading = re.sub(r"[`*_]", "", heading)
    heading = re.sub(r"[^a-z0-9\s-]", "", heading)
    heading = re.sub(r"\s+", "-", heading)
    return heading.strip("-")


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            anchors.add(slugify(match.group(2)))
    return anchors


def is_external_or_special(raw: str) -> bool:
    parsed = urlsplit(raw)
    if parsed.scheme in EXTERNAL_SCHEMES:
        return True
    return raw.startswith("#")


def resolve_target(source: Path, raw: str) -> tuple[Path, str]:
    parsed = urlsplit(raw)
    target = unquote(parsed.path)
    fragment = unquote(parsed.fragment)
    return (source.parent / target).resolve(), fragment


def main() -> int:
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}

    for md in iter_markdown():
        text = md.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer(text):
            raw = match.group(2).strip()
            if not raw or is_external_or_special(raw):
                continue

            resolved, fragment = resolve_target(md, raw)
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{md.relative_to(ROOT)}: link escapes repo: {raw}")
                continue

            if not resolved.exists():
                errors.append(f"{md.relative_to(ROOT)}: missing link target: {raw}")
                continue

            if fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
                anchors = anchor_cache.setdefault(resolved, anchors_for(resolved))
                if fragment.lower() not in anchors:
                    errors.append(
                        f"{md.relative_to(ROOT)}: missing anchor #{fragment} in "
                        f"{resolved.relative_to(ROOT)}"
                    )

    if errors:
        print("Broken Markdown links:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Markdown local links OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
