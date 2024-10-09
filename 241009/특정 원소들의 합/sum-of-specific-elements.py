arr = []
for i in range(4):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

result = 0

for i in range(4):
    for j in range(4):
        if i >= j:
            result += arr[i][j]

print(result)