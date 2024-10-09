arr = list(map(int, input().split()))

arr.sort()
minVal = 500
maxVal = 500

for i in arr:
    if i < 500:
        minVal = i
    elif i > 500:
        maxVal = i
        break

print(minVal, maxVal)