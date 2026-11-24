"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one letter, "W". The word behind it is "wired":
# a day wired on coffee, deadlines and too many open tabs — vivid,
# funny and true, and W fits the word's sound and shape. No word, no
# gloss, no punctuation: the single letter is the whole entry.
import os

TEXT = "W"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
