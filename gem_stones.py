#!/bin/python3

import sys

n = int(input().strip())
c = {}

for i in range(n):
    word = input().strip()
    t = {}
    for w in word:
        t[w] = True

    for w in t.keys():
        if w in c:
            c[w] += 1
        else:
            c[w] = 1

gem_element = 0

for j in c.keys():
    if c[j] == n:
        gem_element += 1

print(gem_element)
