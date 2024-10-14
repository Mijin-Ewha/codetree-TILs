n = int(input())

def posNum(arr, n):
    for i in range(n):
        if arr[i] < 0:
            arr[i] *= -1

arr = list(map(int, input().split()))
posNum(arr, n)
for i in arr:
    print(i, end=" ")