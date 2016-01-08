t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    k = int(((n-1)/3) + 1)
    x1 = (2*n) - (5*k)
    y1 = (-1*n) + (3*k)
    if x1 < 0:
        print(-1)
        continue
    threes = str('3') * x1
    fives = str('5') * y1
    print(int(str(threes) + str(fives)))