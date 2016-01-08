#!/bin/python3

import sys

cases = int(input().strip())

for case in range(cases):
    word = input().strip()
    previous_letter = ''
    deletions = 0
    for i in word:
        if previous_letter == i:
            deletions += 1
        previous_letter = i
    print(deletions)
