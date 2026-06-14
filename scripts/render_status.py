#!/usr/bin/env python3
"""Render sanitized repository status outputs for the public README repo."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
WEEKLY_DIR = DOCS_DIR / "weekly"
README = ROOT / "README.md"
STORYBOARD = DOCS_DIR / "storyboard.md"


def load_status() -> dict[str, Any]:
    path = DATA_DIR / "project_status.json"
    if not path.exists():
        return {"owner": "pskeffington", "scanned_at": "pending", "repo_count": 0, "security_flags": [], "projects": []}
    return json.loads(path.read_text(encoding="utf-8"))


def clean(value: Any) -> str:
    text = str(value or "")
    text = text.replace("|", "-").replace("\n", " ").strip()
    return text


def build_project_table(projects: list[dict[str, Any]], limit: int = 25) -> str:
    rows = ["| Project | Visibility | Status | Last Activity | Notes |", "|---|---:|---:|---:|---|"]
    for repo in projects[:limit]:
        name = clean(repo.get("name"))
        visibility = clean(repo.get("visibility"))
        status = clean(repo.get("status"))
        last_activity = clean(repo.get("pushed_at"))[:10]
        note = clean(repo.get("description")) or "No public note."
        if repo.get("security_flag"):
            note = "Security flag: operational repository is public."
        rows.append(f"| {name} | {visibility} | {status} | {last_activity} | {note} |")
    if len(projects) > limit:
        rows.append(f"| ... | ... | ... | ... | {len(projects) - limit} additional repositories in data/project_status.json. |")
    return "\n".join(rows)


def build_security_section(flags: list[dict[str, Any]]) -> str:
    if not flags:
        return "No public operational repository flags were detected in the latest visible scan."
    rows = ["| Repository | Flag | Action |", "|---|---:|---|"]
    for repo in flags:
        rows.append(f"| {clean(repo.get('name'))} | {clean(repo.get('security_flag'))} | Review visibility immediately. |")
    return "\n".join(rows)


def write_storyboard(status: dict[str, Any]) -> None:
    STORYBOARD.parent.mkdir(parents=True, exist_ok=True)
    if STORYBOARD.exists():
        return
    STORYBOARD.write_text(
        "# Storyboard\n\n"
        "This file tracks public-facing project narrative, milestones, and weekly direction.\n\n"
        "## Current Frame\n\n"
        "- Establish the README repository as the public status surface.\n"
        "- Keep operational detail out of public text.\n"
        "- Use weekly scans to maintain a concise project map.\n\n"
        "## Next Frame\n\n"
        "- Add human-edited project summaries after the first automated scan.\n"
        "- Split public research, support, and operational categories.\n"
        "- Keep security flags visible without exposing sensitive implementation detail.\n",
        encoding="utf-8",
    )


def render_readme(status: dict[str, Any]) -> str:
    scanned_at = clean(status.get("scanned_at"))
    projects = status.get("projects", [])
    flags = status.get("security_flags", [])
    repo_count = clean(status.get("repo_count"))
    return f"""# Skeffington Repository Status

This repository is public by design. It provides a sanitized weekly status surface for project coordination, storyboard tracking, and repository governance.

## Status

Last automated update: {scanned_at}

| Area | Current State |
|---|---|
| Repository scan | {repo_count} visible repositories scanned |
| Project status | Updated from `data/project_status.json` |
| Storyboard | Maintained in `docs/storyboard.md` |
| Security review | {len(flags)} public operational flags |

## Active Workstreams

{build_project_table(projects)}

## Security Review

{build_security_section(flags)}

## Storyboard

Storyboard notes are maintained in [`docs/storyboard.md`](docs/storyboard.md). Weekly snapshots are written under [`docs/weekly/`](docs/weekly/).

## Repository Governance

Operational repositories should remain private. Public repositories should contain only sanitized documentation, demonstrations, research material, or public-facing coordination notes. If a repository is classified as operational and is found public, the weekly scanner flags it in this README and in the weekly snapshot.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

To scan private repositories, add a repository secret named `REPO_SCAN_TOKEN` with permission to read the target repositories and write contents to this repository. Without that secret, the workflow can only report on repositories visible to the default token.
"""


def write_weekly(status: dict[str, Any]) -> None:
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    date_name = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = WEEKLY_DIR / f"{date_name}.md"
    flags = status.get("security_flags", [])
    content = (
        f"# Weekly Repository Snapshot - {date_name}\n\n"
        f"Scanned at: {clean(status.get('scanned_at'))}\n\n"
        f"Visible repositories scanned: {clean(status.get('repo_count'))}\n\n"
        "## Security Flags\n\n"
        f"{build_security_section(flags)}\n\n"
        "## Project Table\n\n"
        f"{build_project_table(status.get('projects', []), limit=100)}\n"
    )
    path.write_text(content, encoding="utf-8")


def main() -> int:
    status = load_status()
    write_storyboard(status)
    README.write_text(render_readme(status), encoding="utf-8")
    write_weekly(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
