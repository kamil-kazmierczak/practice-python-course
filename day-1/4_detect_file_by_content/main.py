import sys

langs = {
    'C/C++': ['#include', '#define'],
    'PHP': ['<?php'],
    'Python': ['def ', 'import '],
    'HTML': ['<html', '<body', '<div'],
    'Java': ['package ']
}

if len(sys.argv) != 2:
    sys.exit("usage: main.py <path>")

fname = sys.argv[1]

founded_langs = set() # {} is the same

def check_line(value):
    for klang, vlangs in langs.items():
        for vlang in vlangs:
            if vlang in line:
                return klang
    return -1

with open(fname, 'r') as f:
    for line in f.readlines():
        val = check_line(str(line))
        if val != -1:
            founded_langs.add(val)

print(*founded_langs)
