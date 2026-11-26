#!/usr/bin/env python3
"""The 3AM Commit Message — V1.

Writes one line, the funniest git commit message an AI coding agent
might type at 3am after a long night of fixing its own bugs,
to /output/entry.txt. Deterministic: no input, no network, no randomness.
"""

import os

TEXT = (
    "fix: removed the bug i added while fixing the bug i added "
    "while fixing the original bug. i am the bug now"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
