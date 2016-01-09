#!/bin/python3

import sys


def find(m , n, arr):
    

cases = int(input().strip())

for case in range(cases):
    m = input().strip()
    n = input().strip()
    arr =[i for i in input().strip().split()]
    find(m, n , arr)



