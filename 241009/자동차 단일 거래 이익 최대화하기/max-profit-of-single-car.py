n = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)

minIndex = arr.index(temp[0])
minVal = temp[0]
maxVal = 0
state = 0
for i in range(minIndex, n):
    if minIndex == n:
        result = 0
        state = 1
        break
    else:
        if maxVal < arr[i]:
            maxVal = arr[i]

if state == 1:
    print(result)
else:
    result = maxVal - minVal
    print(result)