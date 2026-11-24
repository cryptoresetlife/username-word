"""One Word, One Username: the entrant's own make.fun handle."""
import os

HANDLE = "gentle-koala-36"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(HANDLE)
