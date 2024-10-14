def minVal(n, m):
    rlt = n * m
    for i in range(rlt, 0, -1):
        if i % n == 0 and i % m == 0:
            rlt = i;
    print(rlt)

arr = list(map(int, input().split()))
minVal(arr[0], arr[1])