#!/usr/bin/env python3
"""Entry point for the 20 November 2026 news-image bounty.

Copies the pre-drawn front page (entry.png, in this repository) to the
grader's output directory, refusing to run if the image is over the
competition's 1 MiB limit. Standard library only, no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
LIMIT_BYTES = 1_048_576


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    size = os.path.getsize(SOURCE)
    if size > LIMIT_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print(f"copied entry.png ({size} bytes) to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
