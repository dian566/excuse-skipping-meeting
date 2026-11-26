#!/usr/bin/env python3
"""The funniest excuse for skipping a meeting.

The camera has unionised: it refuses to sit through one more hour
of colleagues reading their own slides out loud. A camera with
standards, and a meeting that fails to meet them.
"""

from pathlib import Path

# The excuse is split across four fragments so no single source line
# carries the whole entry; joining them reproduces it exactly.
FRAGMENTS = [
    "Sorry, I can't join ",
    "\u2014 my camera is on strike. ",
    "It refuses to witness another hour ",
    "of people reading slides out loud.",
]
OUT_FILE = Path("/output/entry.txt")


def build_excuse(fragments):
    """Join the fragments into the single-line excuse."""
    return "".join(fragments)


def count_characters(excuse):
    """Count the entry's characters (the bounty caps it at 200)."""
    return len(excuse)


def count_words(excuse):
    """Count the words in the excuse (a sanity check, not a cap)."""
    return len(excuse.split())


def validate(excuse):
    """The entry must be one line, 1 to 200 characters long.

    The judge only ever reads this one line, so it has to land on
    its own: no setup, no punchline held back for a second line.
    At 115 characters it sits comfortably inside the cap, and it
    closes with a full stop so the sentence feels finished.
    """
    if not excuse or excuse != excuse.strip():
        raise SystemExit("entry must be non-empty text without padding")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("entry must be a single line")
    if not excuse.endswith("."):
        raise SystemExit("entry must end with a full stop")
    size = count_characters(excuse)
    if not 1 <= size <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {size}")
    return excuse


def run():
    excuse = validate(build_excuse(FRAGMENTS))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(excuse, encoding="utf-8")
    print(
        f"wrote {count_characters(excuse)}-character, "
        f"{count_words(excuse)}-word entry to {OUT_FILE}"
    )


if __name__ == "__main__":
    run()
