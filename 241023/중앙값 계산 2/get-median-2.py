n = int(input())
arr = list(map(int, input().split()))
brr = sorted(arr)

for i in range(len(arr)):
    if i % 2 == 0:
        print(brr[i // 2], end=" ")