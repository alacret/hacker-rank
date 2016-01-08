import sys, math, decimal

#t = int(input().strip())
t = 1
for a0 in range(t):
    #a, b = input().strip().split(' ')
    a, b = '26', '35'
    bsqrt = math.sqrt(int(b))
    asqrt = math.sqrt(int(a))
    floor = math.floor(bsqrt)
    ceil = math.ceil(asqrt) - 1
    print(floor - ceil)
