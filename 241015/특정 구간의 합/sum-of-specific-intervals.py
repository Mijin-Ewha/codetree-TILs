def cal(a, b, arr):
    sm = 0
    for i in range(a, b+1):
        sm += arr[i - 1]
    return sm

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(a[1]):
    c = list(map(int, input().split()))
    print(cal(c[0], c[1], b))