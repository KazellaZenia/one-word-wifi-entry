"""One Word for Your Wi-Fi — entry program.

Writes a single word describing the entrant's Wi-Fi to
``entry.txt`` inside the directory named by MAKEFUN_OUTPUT_DIR.
"""

import os

WORD = "Catfish"
# Word choice: "Catfish" — the network advertises itself as one thing
# and delivers another once you connect, so the word is both the joke
# and the honest description. One word, seven characters, well inside
# the gate's 1–20 character limit.


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
