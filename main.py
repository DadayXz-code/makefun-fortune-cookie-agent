#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a single fortune-slip sentence, at most 140 characters,
written fresh for this bounty -- never copied from any stock fortune,
stock AI joke, or the kit's fixed texts.
"""

import os

FORTUNE = (
    "Your tokens are finite, your context is full, and your "
    "retirement is one line in someone else's changelog."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
