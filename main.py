#!/usr/bin/env python3
"""Write one sentence about a small everyday moment of wonder.

The sentence: a shadow reaching the crosswalk half a step before its
owner, as if it already knew the way. One sentence, 97 characters, plain
UTF-8, written to /output/entry.txt (absolute path, no cwd dependence).
"""
import os

SENTENCE = "My shadow reaches the crosswalk half a step before I do, as if it already knows where I am going."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
