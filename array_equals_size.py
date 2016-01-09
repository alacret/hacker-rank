#!/bin/python3

import sys


def solve(arr):
    arr_int = [int(i) for i in arr]
    arr_acc = []
    acc = 0
    for i in arr_int:
        acc += i
        arr_acc.append(acc)

    new_acc = 0
    for i in range(len(arr_int)):
        if new_acc == (acc - arr_acc[i]):
            print("YES")
            return
        new_acc += arr_int[i]
    print("NO")

cases = int(input().strip())

for case in range(cases):
    _ = input().strip()
    arr = input().strip().split()
    solve(arr)
