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
    """The entry must be one line of 1 to 200 characters.

    The judge only ever sees this one line, so it has to land on
    its own: no setup, no punchline deferred to a second sentence.
    At 115 characters it fits the cap with room to spare.
    """
    if not excuse or excuse != excuse.strip():
        raise SystemExit("entry must be non-empty text without padding")
    if "\n" in excuse or "\r" in excuse:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(excuse) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(excuse)}")
    return excuse


def run():
    excuse = validate(join_excuse(PARTS))
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(excuse, encoding="utf-8")
    print(f"wrote {len(excuse)}-character entry to {OUT_FILE}")


if __name__ == "__main__":
    run()
