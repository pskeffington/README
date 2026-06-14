#!/usr/bin/env python3
"""Scan visible GitHub repositories and produce sanitized status data."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
WEEKLY_DIR = ROOT / "docs" / "weekly"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def request_json(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "skeffington-readme-repo-scanner",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub request failed: {exc.code} {url} {body}") from exc


def collect_repos(owner: str, token: str | None) -> list[dict[str, Any]]:
    repos: list[dict[str, Any]] = []
    page = 1
    while True:
        if token:
            url = (
                "https://api.github.com/user/repos"
                f"?per_page=100&page={page}&affiliation=owner,collaborator,organization_member"
                "&sort=pushed&direction=desc"
            )
        else:
            url = f"https://api.github.com/users/{owner}/repos?per_page=100&page={page}&sort=pushed&direction=desc"
        batch = request_json(url, token)
        if not batch:
            break
        for repo in batch:
            repo_owner = repo.get("owner", {}).get("login", "")
            if repo_owner.lower() == owner.lower():
                repos.append(repo)
        page += 1
    return repos


def classify_status(repo: dict[str, Any]) -> str:
    archived = bool(repo.get("archived"))
    disabled = bool(repo.get("disabled"))
    if archived or disabled:
        return "Archived"
    pushed_at = repo.get("pushed_at") or ""
    if not pushed_at:
        return "Unknown"
    try:
        pushed = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    except ValueError:
        return "Unknown"
    age_days = (datetime.now(timezone.utc) - pushed).days
    if age_days <= 14:
        return "Active"
    if age_days <= 90:
        return "Warm"
    return "Quiet"


def is_operational(repo: dict[str, Any], configured: set[str]) -> bool:
    name = str(repo.get("name", ""))
    topics = {str(topic).lower() for topic in repo.get("topics", [])}
    configured_lower = {item.lower() for item in configured}
    if name.lower() in configured_lower:
        return True
    operational_topics = {"operational", "ops", "production", "core", "main-processing"}
    return bool(topics & operational_topics)


def sanitize_repo(repo: dict[str, Any], configured_operational: set[str]) -> dict[str, Any]:
    operational = is_operational(repo, configured_operational)
    visibility = str(repo.get("visibility") or ("private" if repo.get("private") else "public"))
    is_public = visibility == "public" or repo.get("private") is False
    return {
        "name": repo.get("name"),
        "full_name": repo.get("full_name"),
        "visibility": visibility,
        "status": classify_status(repo),
        "description": repo.get("description") or "",
        "default_branch": repo.get("default_branch"),
        "pushed_at": repo.get("pushed_at"),
        "updated_at": repo.get("updated_at"),
        "archived": bool(repo.get("archived")),
        "fork": bool(repo.get("fork")),
        "operational": operational,
        "security_flag": "PUBLIC_OPERATIONAL_REPO" if operational and is_public else "",
    }


def main() -> int:
    owner = os.environ.get("REPO_OWNER", "pskeffington")
    token = os.environ.get("REPO_SCAN_TOKEN") or os.environ.get("GITHUB_TOKEN")
    configured_operational = {
        item.strip()
        for item in os.environ.get("OPERATIONAL_REPOS", "Eagle-Eye,trans").split(",")
        if item.strip()
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)

    repos = collect_repos(owner, token)
    scanned_at = now_iso()
    inventory = {
        "owner": owner,
        "scanned_at": scanned_at,
        "repo_count": len(repos),
        "repos": [sanitize_repo(repo, configured_operational) for repo in repos],
    }

    security_flags = [repo for repo in inventory["repos"] if repo.get("security_flag")]
    status = {
        "owner": owner,
        "scanned_at": scanned_at,
        "repo_count": len(repos),
        "security_flags": security_flags,
        "projects": inventory["repos"],
    }

    (DATA_DIR / "repo_inventory.json").write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    (DATA_DIR / "project_status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
