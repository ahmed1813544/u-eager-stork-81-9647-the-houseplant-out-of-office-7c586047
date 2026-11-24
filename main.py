"""Houseplant Out-of-Office entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Deterministic: the same bytes every run.
"""

import os

ENTRY = "Out of office: this plant is on strike. No water since March, no sunlight, and HR still calls me 'low maintenance'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1-120 characters,
    # not only whitespace. Fail loudly here rather than ship an invalid entry.
    if not ENTRY.strip() or len(ENTRY) > 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(ENTRY)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
