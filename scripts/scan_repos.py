#!/usr/bin/env python3
"""Scan visible GitHub repositories and produce sanitized status data."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
WEEKLY_DIR = ROOT / "docs" / "weekly"
LATIN_SAFE_RE = re.compile(r"^[A-Za-z0-9._-]+$")


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


def flag_repo(repo: dict[str, Any], operational: bool, public_status_repo: str) -> str:
    name = str(repo.get("name", ""))
    visibility = str(repo.get("visibility") or ("private" if repo.get("private") else "public"))
    is_public = visibility == "public" or repo.get("private") is False
    if operational and is_public:
        return "PUBLIC_OPERATIONAL_REPO"
    if operational and not LATIN_SAFE_RE.match(name):
        return "NON_LATIN_OPERATIONAL_NAME"
    if name.lower() == public_status_repo.lower() and visibility != "public":
        return "STATUS_REPO_NOT_PUBLIC"
    return ""


def sanitize_repo(repo: dict[str, Any], configured_operational: set[str], public_status_repo: str) -> dict[str, Any]:
    operational = is_operational(repo, configured_operational)
    visibility = str(repo.get("visibility") or ("private" if repo.get("private") else "public"))
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
        "security_flag": flag_repo(repo, operational, public_status_repo),
    }


def main() -> int:
    owner = os.environ.get("REPO_OWNER", "pskeffington")
    token = os.environ.get("REPO_SCAN_TOKEN") or os.environ.get("GITHUB_TOKEN")
    public_status_repo = os.environ.get("PUBLIC_STATUS_REPO", "README")
    configured_operational = {
        item.strip()
        for item in os.environ.get("OPERATIONAL_REPOS", "Eagle-Eye,trans,trans-latin").split(",")
        if item.strip()
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)

    repos = collect_repos(owner, token)
    scanned_at = now_iso()
    sanitized = [sanitize_repo(repo, configured_operational, public_status_repo) for repo in repos]
    inventory = {
        "owner": owner,
        "scanned_at": scanned_at,
        "repo_count": len(repos),
        "repos": sanitized,
    }

    security_flags = [repo for repo in sanitized if repo.get("security_flag")]
    status = {
        "owner": owner,
        "scanned_at": scanned_at,
        "repo_count": len(repos),
        "security_flags": security_flags,
        "projects": sanitized,
    }

    (DATA_DIR / "repo_inventory.json").write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    (DATA_DIR / "project_status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
