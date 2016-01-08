import sys, math, decimal

#t = int(input().strip())
t = 1
for a0 in range(t):
    #a, b = input().strip().split(' ')
    a, b = 3, 9
    divs = 0
    i = int(a)
    while (i < (int(b)+1)):
        sq = math.sqrt(i)
        if sq % 1 == 0.0:
            divs += 1
            i += int(sq)
        else:
            i += 1
    print(divs)
