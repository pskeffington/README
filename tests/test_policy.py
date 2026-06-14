#!/usr/bin/env python3
"""Simple tests for repository policy structure."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "data" / "repo_policy.json"
LATIN_SAFE_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def load_policy() -> dict:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def test_policy_exists() -> None:
    assert POLICY_PATH.exists()


def test_operational_and_scholarly_do_not_overlap() -> None:
    policy = load_policy()
    operational = {name.lower() for name in policy["operational_repos"]}
    scholarly = {name.lower() for name in policy["public_scholarly_repos"]}
    assert not operational & scholarly


def test_policy_names_are_latin_safe() -> None:
    policy = load_policy()
    names = [policy["owner"], policy["public_status_repo"]]
    names.extend(policy["operational_repos"])
    names.extend(policy["public_scholarly_repos"])
    for name in names:
        assert LATIN_SAFE_RE.match(name)
