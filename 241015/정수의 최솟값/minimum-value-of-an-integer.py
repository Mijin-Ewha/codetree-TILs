def minValue(a, b, c):
    return min(a, b, c)

arr = list(map(int, input().split()))
print(minValue(arr[0], arr[1], arr[2]))