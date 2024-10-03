n = int(input())
arr = [1, n]
i = 0

while arr[-1] <= 100:
    arr.append(arr[i] + arr[i+1])
    i += 1

for i in arr:
    print(i, end=" ")