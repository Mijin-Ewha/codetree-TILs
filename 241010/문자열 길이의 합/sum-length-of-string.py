n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

result = 0
cnt = 0
for i in range(len(arr)):
    result += len(arr[i])
    if arr[i][0] == 'a':
        cnt += 1

print(result, cnt)