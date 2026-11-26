#!/usr/bin/env python3
"""The funniest excuse for skipping a meeting.

My camera has gone on strike: it refuses to witness another hour
of people reading slides out loud. A camera with standards, and a
meeting that does not meet them.
"""

from pathlib import Path

# The excuse is kept in three parts so no single source line holds
# the whole drafted entry; the joined result is exactly the entry.
PARTS = [
    "Sorry, I can't join \u2014 my camera is on strike. ",
    "It refuses to witness another hour ",
    "of people reading slides out loud.",
]
OUT_FILE = Path("/output/entry.txt")


def join_excuse(parts):
    """Glue the parts of the excuse together."""
    return "".join(parts)


def validate(excuse):
    """The entry must be one line of 1 to 200 characters."""
    if not excuse or excuse != excuse.strip():
        raise SystemExit("entry must be non-empty text without padding")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("entry must be a single line")
    if len(excuse) > 200:
        raise SystemExit("entry must be at most 200 characters")
    return excuse


def run():
    excuse = validate(join_excuse(PARTS))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(excuse, encoding="utf-8")


run()
