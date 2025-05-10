import sys
import os

if len(sys.argv) != 2:
    sys.exit("usage: main.py <path>")

path = sys.argv[1]
print(f"Path: {path}")


for root, dirs, files in os.walk(path, topdown=True):
    for file in files:
        if root == path:
            print(f"{file}")
        else:
            print(f"{root[len(path)+1:]}/{file}")


