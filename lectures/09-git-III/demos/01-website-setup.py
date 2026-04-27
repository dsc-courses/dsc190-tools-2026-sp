#!/usr/bin/env python3
"""Create a Git repository for the ChainForge website demo.

Usage:
    python 01-website-setup.py <path>

Initializes a fresh repo at <path> and replays a six-commit history spanning
April 20-24, 2026. The tip of `main` contains three pages under `pages/`,
with a typo in the title of `pages/03.md` left intentionally for the demo.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

AUTHOR_NAME = "Alex Rivera"
AUTHOR_EMAIL = "alex@chainforge.io"

README = """# ChainForge Website

Marketing site for ChainForge.
"""

PAGE_01_V1 = """# Welcome to ChainForge

ChainForge is the next-generation blockchain plaform built for serious builders.
Our high-throughput consensus layer settles transactions in under a second, with
fees so low your users will forget they're on-chain.
"""

PAGE_01_V2 = """# Welcome to ChainForge

ChainForge is the next-generation blockchain plaform built for serious builders.
Our high-throughput consensus layer settles transactions in under a second, with
fees so low your users will forget they're on-chain. Join thousands of
developers shipping the future of decentralized finance.
"""

PAGE_01_V3 = """# Welcome to ChainForge

ChainForge is the next-generation blockchain platform built for serious
builders. Our high-throughput consensus layer settles transactions in under a
second, with fees so low your users will forget they're on-chain. Join thousands
of developers shipping the future of decentralized finance.
"""

PAGE_02 = """# Why ChainForge?

Built from first principles, ChainForge combines battle-tested cryptography with
a developer experience that just works. Deploy smart contracts in minutes, not
days. Our SDK supports every major language, and our docs are written by humans
who actually ship code.
"""

PAGE_03 = """# Get Started Todya

Spinning up a node takes one command, and our testnet is free for everyone.
Whether you're building DeFi, NFTs, or something nobody has imagined yet,
ChainForge gives you the rails. The future is decentralized, and it starts with
you.
"""

COMMITS = [
    ("2026-04-20T09:15:00", "Initial commit",            [("README.md",   README)]),
    ("2026-04-20T14:32:00", "Add landing page",          [("pages/01.md", PAGE_01_V1)]),
    ("2026-04-21T10:08:00", "Tighten landing page copy", [("pages/01.md", PAGE_01_V2)]),
    ("2026-04-22T16:45:00", "Add Why ChainForge page",   [("pages/02.md", PAGE_02)]),
    ("2026-04-23T09:22:00", "Fix typo on landing page",  [("pages/01.md", PAGE_01_V3)]),
    ("2026-04-24T11:30:00", "Add Get Started page",      [("pages/03.md", PAGE_03)]),
]


def git(args, cwd, env=None):
    subprocess.run(["git", *args], cwd=cwd, env=env, check=True)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: 01-website-setup.py <path>")

    repo = Path(sys.argv[1]).expanduser().resolve()
    if repo.exists() and any(repo.iterdir()):
        sys.exit(f"error: {repo} exists and is not empty")
    repo.mkdir(parents=True, exist_ok=True)

    git(["init", "-q", "-b", "main"], cwd=repo)

    for date, message, writes in COMMITS:
        for relpath, content in writes:
            path = repo / relpath
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            git(["add", relpath], cwd=repo)

        env = {
            **os.environ,
            "GIT_AUTHOR_NAME":     AUTHOR_NAME,
            "GIT_AUTHOR_EMAIL":    AUTHOR_EMAIL,
            "GIT_COMMITTER_NAME":  AUTHOR_NAME,
            "GIT_COMMITTER_EMAIL": AUTHOR_EMAIL,
            "GIT_AUTHOR_DATE":     date,
            "GIT_COMMITTER_DATE":  date,
        }
        git(["commit", "-q", "-m", message], cwd=repo, env=env)

    print(f"created repo at {repo}")


if __name__ == "__main__":
    main()
