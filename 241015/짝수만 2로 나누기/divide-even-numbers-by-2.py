def div(arr, n):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)

n = int(input())
arr = list(map(int, input().split()))
div(arr, n)
for i in arr:
    print(i, end=" ")