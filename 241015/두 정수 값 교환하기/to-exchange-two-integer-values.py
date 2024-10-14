def swap(n, m):
    n, m = m, n
    return n, m

arr = list(map(int, input().split()))
n, m = swap(arr[0], arr[1])
print(n, m)