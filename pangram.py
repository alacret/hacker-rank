#!/bin/python3

import sys

word = input().strip().lower()
all_dict = dict()
for l in word:
    a = ord(l)
    if 122 >= a >= 97:
        all_dict[l] = True

if len(all_dict) == 26:
    print("pangram")
else:
    print("not pangram")