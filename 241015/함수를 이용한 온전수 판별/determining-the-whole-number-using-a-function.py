def comNum(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 2 == 1 and i % 10 != 5 and not (i % 3 == 0 and i % 9 != 0):
            cnt += 1
    return cnt

arr = list(map(int, input().split()))
print(comNum(arr[0], arr[1]))