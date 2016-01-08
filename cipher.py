n = int(input().strip())
s = input().strip()
k = int(input().strip())

c = ''
for i in s:
    if i.isalpha():
        code = ord(i)
        l = k
        while l > 0:
            if code == 122:
                code = 96
            elif code == 90:
                code = 64
            code += 1
            l -= 1
        c += chr(code)
    else:
        c += i
print(c)