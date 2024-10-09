n = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)

minIndex = arr.index(temp[0])
maxVal = temp[-1]
state = 0
for i in range(minIndex, len(arr)):
    if minIndex == len(arr):
        result = 0
        state = 1
        break
    else:
        if maxVal < arr[i]:
            maxVal = arr[i]

if state == 1:
    print(result)
else:
    result = maxVal - temp[0]
    print(result)