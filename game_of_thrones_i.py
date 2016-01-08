#!/bin/python3

import sys

word = input().strip()
c = {}

for i in word:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

word_is_par = True if len(word) % 2 == 0 else False

even = 0

for i in c.keys():
    if c[i] % 2 == 1:
        even += 1

if word_is_par:
    if even == 0:
        print("YES")
    else:
        print("NO")
else:
    if even == 1:
        print("YES")
    else:
        print("NO")
