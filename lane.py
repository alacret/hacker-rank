import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    m = 3
    for i in range(i,j+1):
        m = min(m,with[i])
    print(m)