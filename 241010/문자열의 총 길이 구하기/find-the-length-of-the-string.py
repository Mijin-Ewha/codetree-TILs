arr = input().split()

result = 0

for i in range(len(arr)):
    result += len(arr[i])

print(result)