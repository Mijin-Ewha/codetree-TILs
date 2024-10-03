arr = list(map(float, input().split()))

sumArr = 0
for i in range(len(arr)):
    sumArr += arr[i]

avg = sumArr / 8

print(round(avg, 1))