def mulmul(a, b):
    return a ** b

arr = list(map(int, input().split()))
print(mulmul(arr[0], arr[1]))