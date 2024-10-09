n = int(input())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

maxVal = arr[0]

for i in range(0, n):
    if arr.count(maxVal) != 1:
        maxVal = arr[arr.count(maxVal)]
        if maxVal == arr[-1]:
            print(-1)
            break
    elif arr.count(maxVal) == 1:
        print(maxVal)
        break;