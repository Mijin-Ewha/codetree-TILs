arr = list(map(int, input().split()))
for i in range(8):
    arr.append((2 * arr[i]) + arr[i + 1])

for i in arr:
    print(i, end=" ")