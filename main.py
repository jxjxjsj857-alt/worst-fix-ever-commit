#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message -- a bug fix that made everything worse --
to $MAKEFUN_OUTPUT_DIR/entry.txt. The text is 1-100 UTF-8 characters.
"""
import os

LINE = "fix: infinite loop by adding a second loop to cancel it out"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    # One line, no explanation needed: the fix IS the bug, twice over.
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 100, "entry must be 1-100 characters, got %d" % len(text)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
