#!/usr/bin/env python3
"""Dad Joke Showdown — one-line entry.

Writes one dad joke, at most 200 characters, to /output/entry.txt.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The joke: a neural network with too many layers to unpack. Classic
# dad-joke Q&A shape, pun lands cleanly, fresh AI angle, groan-worthy.
# Counted at 75 characters — inside the 1..200 window.
LINE = (
    "Why did the neural network go to therapy? It had too many "
    "layers to unpack."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the dad joke to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
