import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    h = 1
    for i in range(n):
        if i % 2 == 0:
            h = h * 2
        else:
            h += 1
    print(h)