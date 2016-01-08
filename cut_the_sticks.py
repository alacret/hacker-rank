n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while len(arr) > 0:
    print(len(arr))
    min_l = min(arr)
    new_arr = []
    for i in arr:
        if i > min_l:
            new_arr.append(i-min_l)
    arr = new_arr