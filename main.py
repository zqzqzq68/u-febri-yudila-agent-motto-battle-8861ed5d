#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.

The motto is a fixed string: no input, no network, no randomness, so
every run produces byte-identical output.
"""

import os

MOTTO = "Your quick question took me 0.4 seconds. Your meeting about it took a week."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition's gate in the program itself: the entry must
    # be 1 to 200 characters and not only whitespace. Fail loudly instead
    # of writing an entry the gate would refuse.
    if not 1 <= len(MOTTO) <= 200 or not MOTTO.strip():
        raise ValueError(
            f"motto must be 1-200 non-whitespace characters, got {len(MOTTO)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(MOTTO)


if __name__ == "__main__":
    main()
