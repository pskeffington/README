#!/usr/bin/env python3
"""Validate repository policy before running the weekly scanner."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "data" / "repo_policy.json"
LATIN_SAFE_RE = re.compile(r"^[A-Za-z0-9._-]+$")
REQUIRED_KEYS = {
    "owner",
    "public_status_repo",
    "operational_repos",
    "public_scholarly_repos",
    "public_scholarly_purpose",
    "rules",
}


def fail(message: str) -> int:
    print(f"policy validation failed: {message}", file=sys.stderr)
    return 1


def load_policy() -> dict[str, Any]:
    if not POLICY_PATH.exists():
        raise FileNotFoundError(f"missing policy file: {POLICY_PATH}")
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def require_string(policy: dict[str, Any], key: str) -> str:
    value = policy.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a non-empty string")
    return value.strip()


def require_name_list(policy: dict[str, Any], key: str) -> list[str]:
    value = policy.get(key)
    if not isinstance(value, list):
        raise ValueError(f"{key} must be a list")
    names: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"{key} contains an invalid repository name")
        name = item.strip()
        if not LATIN_SAFE_RE.match(name):
            raise ValueError(f"{key} contains a non Latin-safe repository name: {name}")
        names.append(name)
    if len(names) != len(set(name.lower() for name in names)):
        raise ValueError(f"{key} contains duplicate repository names")
    return names


def main() -> int:
    try:
        policy = load_policy()
        missing = REQUIRED_KEYS - set(policy)
        if missing:
            return fail(f"missing required keys: {', '.join(sorted(missing))}")

        owner = require_string(policy, "owner")
        public_status_repo = require_string(policy, "public_status_repo")
        public_scholarly_purpose = require_string(policy, "public_scholarly_purpose")
        operational = require_name_list(policy, "operational_repos")
        scholarly = require_name_list(policy, "public_scholarly_repos")
        rules = policy.get("rules")

        if not LATIN_SAFE_RE.match(owner):
            return fail(f"owner is not Latin-safe: {owner}")
        if not LATIN_SAFE_RE.match(public_status_repo):
            return fail(f"public_status_repo is not Latin-safe: {public_status_repo}")
        if not public_scholarly_purpose:
            return fail("public_scholarly_purpose must not be empty")
        if not isinstance(rules, dict):
            return fail("rules must be an object")

        overlap = {name.lower() for name in operational} & {name.lower() for name in scholarly}
        if overlap:
            return fail(f"repository cannot be both operational and public scholarly: {', '.join(sorted(overlap))}")

    except Exception as exc:  # noqa: BLE001 - command-line validator should report all policy failures plainly.
        return fail(str(exc))

    print("policy validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
