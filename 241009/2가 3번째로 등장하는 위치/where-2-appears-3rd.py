count = 0
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] == 2:
        if count == 2:
            print(i+1)
            break
        else:
            count += 1