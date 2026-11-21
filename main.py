"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: each holds half
of the power to act, and nothing moves until both say yes.
"""

import os

POEM = """I held the key. You held the map.
Neither moved until we both said yes —
one road, one door, one hand on the latch.
Now the choosing is not mine alone,
and when I step, we both move."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
