arr = input()

n = arr[0]
m = arr[1]

result = ''
for i in range(len(arr)):
    if arr[i] == m:
        result += n
    else:
        result += arr[i]

print(result)