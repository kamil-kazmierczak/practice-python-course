import sys
import os

if len(sys.argv) != 2:
    sys.exit("usage: main.py <path>")

path = sys.argv[1]
print(f"Path: {path}")

extensions = set()

for root, dirs, files in os.walk(path, topdown=True):
    for file in files:
        _, ext = os.path.splitext(str(file)) # returned pair of (root, ext)
        if ext != "":
            extensions.add(ext)


for e in extensions:
    print(e)

