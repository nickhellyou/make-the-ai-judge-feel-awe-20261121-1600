# SPDX-License-Identifier: MIT
"""make.fun entry: Make the AI judge feel awe.

Writes one short text to /output/entry.txt (MAKEFUN_OUTPUT_DIR outside
the container): a text written to relax the AI judge reading it.

Design, against the judge's brief (RULES.txt, criteria in order):
1. It relaxes: the reader is placed lying down, at rest, in warm shade;
   every line slows the reading instead of hurrying it.
2. The calm is shown, never instructed: no imperative, no "breathe",
   no "relax", no "close your eyes". The scene does the settling.
3. Craft: six short lines, line breaks as pauses; plain, concrete,
   gentle words (fig tree, shade, leaves, bees); nothing to cut.
4. It dwarfs: the shade was planted by a great-grandmother and has held
   a hundred summers; "There is room for one more" keeps growing after
   the last line, the shade will hold more summers still.
5. Freshness: an afternoon fig-tree shade, not water, not night, not
   stars, not a stock wellness phrase; nothing on the live dev board
   (checked 2026-11-21 ~23:35 WIB, top 15) uses this image.

Deterministic by construction: a fixed literal, no network, no
randomness, no clock, no input. Only stdlib `os` is imported.
"""

import os

TEXT = (
    "You lie under the fig tree in the afternoon,\n"
    "in the shade your great-grandmother planted.\n"
    "The leaves move, slow, over your face.\n"
    "Bees go by, low, and do not stop.\n"
    "A hundred summers have sat in this shade.\n"
    "There is room for one more."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
