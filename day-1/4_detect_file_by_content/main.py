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

def check_line(value):
    # todo

with open(fname, 'r') as f:
    for line in f.readlines():
       # check_line(str(line)) 
