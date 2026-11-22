#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

A quiet text written to relax the reader: evening light, a cooling
kettle, and nothing waiting to be finished.
"""

import os
import shutil

TEXT = (
    "The evening light comes in low across the floor and stays there, "
    "in no hurry at all. Somewhere a kettle ticks as it cools. "
    "Nothing is waiting for you to finish. You can sit here a while, "
    "in the warm quiet, and let the day set down beside you, "
    "like a coat hung up by the door."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir(path):
    """Remove the contents of the output directory, never the directory."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        item = os.path.join(path, name)
        if os.path.isdir(item) and not os.path.islink(item):
            shutil.rmtree(item)
        else:
            os.unlink(item)


def main():
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
