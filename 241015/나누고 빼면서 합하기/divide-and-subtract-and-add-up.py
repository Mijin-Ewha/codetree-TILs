def div_Mul(a, m):
    sm = 0
    while m >= 1:
        sm += a[m - 1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return sm

arr = list(map(int, input().split()))
a = list(map(int, input().split()))

print(div_Mul(a, arr[1]))