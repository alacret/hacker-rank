#!/bin/python3

import sys


def find(word1, word2):
    base_list = [0 for i in range(26)]
    for i in word2:
        base_list[ord(i) % 26] += 1

    for i in word1:
        if base_list[ord(i) % 26] > 0:
            print("YES")
            return
    print("NO")

cases = int(input().strip())

for case in range(cases):
    word1 = input().strip()
    word2 = input().strip()
    find(word1, word2)



