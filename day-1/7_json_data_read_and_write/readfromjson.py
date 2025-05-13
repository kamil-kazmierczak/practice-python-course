import json
import sys
from pprint import pprint # only make sense in nested structures


if len(sys.argv) != 2:
    sys.exit(f"usage: main.py <path>")

fname = sys.argv[1]

with open(fname, 'r') as f:
    data = json.load(f)

pprint(data)


