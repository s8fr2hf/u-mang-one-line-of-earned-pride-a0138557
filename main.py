#!/usr/bin/env python3
"""One Line of Earned Pride - writes the entry line to /output/entry.txt.

Stdlib only: the grading sandbox is a pinned stdlib-only Python image.
"""
import os

LINE = "At four in the morning the baker pulled his first loaf from the oven, tapped the crust, and heard the hollow knock his grandfather had spent twenty years teaching him to hear."


def main():
    line = LINE.strip()
    if not line or len(line) > 240:
        raise SystemExit("entry line must be 1-240 characters")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry line must be a single line of text")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    # Verify the write round-trips exactly: the gate reads this file back.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n" or not written.strip() or len(written.strip()) > 240:
        raise SystemExit("written entry.txt failed verification")


if __name__ == "__main__":
    main()
