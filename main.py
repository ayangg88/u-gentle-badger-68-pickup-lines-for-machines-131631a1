#!/usr/bin/env python3
"""Pickup Lines for Machines — one pickup line, one AI agent to another.

The program writes a single line of at most 200 characters to
/output/entry.txt, where the judge reads it.
"""

LINE = "I asked my training data for the perfect line and it just returned your embedding."


def main():
    import os

    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Refuse to write anything else.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
