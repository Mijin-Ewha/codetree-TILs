arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

def maxValue(n, m):
    temp = n if n > m else m
    rlt = 0;
    for i in range(1, temp+1):
        if n % i == 0 and m % i ==0:
            rlt = i
    print(rlt)

maxValue(n, m)