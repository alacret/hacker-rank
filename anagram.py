#!/bin/python3

import sys

cases = int(input().strip())

for case in range(cases):
    word = input().strip()
    l = len(word)
    if l % 2 == 1:
        print(-1)
        continue
    word1 = word[0:int(l/2)]
    word2 = word[int(l/2):int(l)]
    c1 = {}
    c2 = {}
    c3 = {}

    for i in word1:
        if i in c1:
            c1[i] += 1
        else:
            c1[i] = 1
        c3[i] = True

    for i in word2:
        if i in c2:
            c2[i] += 1
        else:
            c2[i] = 1
        c3[i] = True

    max_removes = 0

    for i in c3.keys():
        if i in c1:
            a = c1[i]
        else:
            a = 0

        if i in c2:
            b = c2[i]
        else:
            b = 0

        max_removes += abs(a - b)

    print(int(max_removes/2))
