#!/usr/bin/env python3
"""Refresh the "Top 10 repositories" table inside README.md.

Reads public repositories from the GitHub REST API, ranks them, and rewrites
the block between the TOP-REPOS markers. Standard library only, so it runs
anywhere Python 3.9+ does.

Usage:
    python .github/scripts/update_top_repos.py            # rewrite README.md
    PROFILE_USER=someone python .../update_top_repos.py   # preview another user

Environment:
    GITHUB_TOKEN  optional; raises the API rate limit from 60 to 5,000 req/h.
    PROFILE_USER  optional; defaults to the repo's own owner.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

README_PATH = "README.md"
START = "<!-- TOP-REPOS:START -->"
END = "<!-- TOP-REPOS:END -->"
LIMIT = 10
API = "https://api.github.com"

DEFAULT_USER = os.environ.get("GITHUB_REPOSITORY", "").split("/")[0] or "kamalbhue547"
USER = os.environ.get("PROFILE_USER") or DEFAULT_USER

EMPTY_STATE = """\
_Projects are on the way — nothing public to rank yet._

_This table rebuilds itself from my public repositories as soon as they exist._

> **Populate it now:** **Actions** → **Update top repositories** → **Run workflow**.
"""


def api_get(url: str) -> list[dict]:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", f"{USER}-profile-readme")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_repos(user: str) -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        url = f"{API}/users/{user}/repos?per_page=100&page={page}&sort=pushed&type=owner"
        batch = api_get(url)
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def candidates(repos: list[dict]) -> list[dict]:
    """Own repositories only: no profile repo, forks only as a last resort."""
    own = [r for r in repos if r["name"].lower() != USER.lower()]
    originals = [r for r in own if not r.get("fork")]
    return originals or own


def rank(pool: list[dict]) -> list[dict]:
    """Order by stars, then forks, then most recent push; keep the top 10."""

    def key(repo: dict) -> tuple:
        pushed = repo.get("pushed_at") or repo.get("updated_at") or ""
        return (repo.get("stargazers_count", 0), repo.get("forks_count", 0), pushed)

    return sorted(pool, key=key, reverse=True)[:LIMIT]


def cell(text: str | None, limit: int) -> str:
    """Make a string safe for a Markdown table cell."""
    if not text:
        return "—"
    flat = " ".join(text.split()).replace("|", "\\|")
    return flat if len(flat) <= limit else flat[: limit - 1].rstrip() + "…"


def render(repos: list[dict]) -> str:
    pool = candidates(repos)
    ranked = rank(pool)
    if not ranked:
        return EMPTY_STATE

    stars = sum(r.get("stargazers_count", 0) for r in pool)
    forks = sum(r.get("forks_count", 0) for r in pool)
    today = datetime.now(timezone.utc).strftime("%d %b %Y")

    lines = [
        f"**{len(pool)}** public repositories · **{stars:,}** stars · **{forks:,}** forks"
        f"  \n<sub>Ranked by stars, then forks, then most recent push · refreshed {today}</sub>",
        "",
        "| # | Repository | Description | Stack | ★ | Last push |",
        "|:--:|---|---|---|:--:|:--:|",
    ]

    for i, repo in enumerate(ranked, start=1):
        name = cell(repo["name"], 40)
        pushed = (repo.get("pushed_at") or "")[:10]
        lines.append(
            f"| {i} "
            f"| [**{name}**]({repo['html_url']}) "
            f"| {cell(repo.get('description'), 72)} "
            f"| {cell(repo.get('language'), 20)} "
            f"| {repo.get('stargazers_count', 0):,} "
            f"| {pushed} |"
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    try:
        repos = fetch_repos(USER)
    except urllib.error.HTTPError as err:
        print(f"error: GitHub API returned {err.code} for {USER}", file=sys.stderr)
        return 1
    except urllib.error.URLError as err:
        print(f"error: cannot reach GitHub API ({err.reason})", file=sys.stderr)
        return 1

    with open(README_PATH, encoding="utf-8") as fh:
        readme = fh.read()

    if START not in readme or END not in readme:
        print(f"error: markers {START} / {END} not found in {README_PATH}", file=sys.stderr)
        return 1

    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = f"{head}{START}\n\n{render(repos)}\n{END}{tail}"

    if updated == readme:
        print("README already up to date.")
        return 0

    with open(README_PATH, "w", encoding="utf-8") as fh:
        fh.write(updated)
    print(f"README updated: {len(rank(candidates(repos)))} repositories listed for {USER}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
