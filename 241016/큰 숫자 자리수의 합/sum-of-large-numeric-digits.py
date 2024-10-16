def plus(a, m):
    if m == 0:
        return int(a[0])
    return int(a[m]) + plus(a, m-1)

n = list(map(int, input().split()))
num = n[0] * n[1] * n[2]
a = str(num)
print(plus(a, len(a)-1))