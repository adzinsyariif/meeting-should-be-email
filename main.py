#!/usr/bin/env python3
import os

LINE = "Twelve of us met for an hour to watch my boss read his email aloud, then he emailed us the recording."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
