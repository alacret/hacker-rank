#!/bin/python3

import sys


def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


def find(word1, word2):
    word2_as_list = [ord(i) for i in word2]
    word2_as_list.sort()
    for i in word1:
        if binarySearch(word2_as_list, ord(i)):
            print("YES")
            return
    print("NO")

cases = int(input().strip())

for case in range(cases):
    word1 = input().strip()
    word2 = input().strip()
    find(word1, word2)


