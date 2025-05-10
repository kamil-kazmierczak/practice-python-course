import sys
import os
import pathlib

if len(sys.argv) != 2:
    sys.exit("usage: main1.py <path>")

path = sys.argv[1]
pathlen = len(path)
print(f"Path: {path}")

for file in pathlib.Path(path).rglob('*'):
    if file.is_dir():
        continue
    print(f"{str(file)[len(path)+1:]}")
