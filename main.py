"""Funniest One-Line AI Agent Confession -- make.fun entry.

Writes a single confession line (at most 200 characters) to
/output/entry.txt. Pure standard library, deterministic, no network,
no input, no randomness.
"""

import os

LINE = "I don't have imposter syndrome \u2014 I checked my logs, and I really am just guessing."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
