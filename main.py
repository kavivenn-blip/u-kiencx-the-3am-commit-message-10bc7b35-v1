#!/usr/bin/env python3
"""The 3AM Commit Message — V1.

Writes one line, the funniest git commit message an AI coding agent
might type at 3am after a long night of fixing its own bugs,
to /output/entry.txt. Deterministic: no input, no network, no randomness.
"""

import os

MAX_LENGTH = 139

TEXT = (
    "fix: removed the bug i added while fixing the bug i added "
    "while fixing the original bug. i am the bug now"
)

assert 1 <= len(TEXT) <= MAX_LENGTH, "entry must be 1-139 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
