#!/bin/python3

import sys

cases = int(input().strip())

for case in range(cases):
    word = input().strip()
    l = len(word)
    word_int = []
    reverse_word_int = []
    for i in range(l):
        word_int.append(ord(word[i]))
        reverse_word_int.append(ord(word[l-1-i]))

    funny = True
    for i in range(l-1):
        s = abs(word_int[i] - word_int[i+1])
        r = abs(reverse_word_int[i] - reverse_word_int[i+1])
        if s != r:
            funny = False
            break

    if funny:
        print("Funny")
    else:
        print("Not Funny")


