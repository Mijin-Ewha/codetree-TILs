arr = []
for i in range(3):
    temp = input()
    arr.append(temp)

lenArr = []
for i in range(3):
    tempLen = len(arr[i])
    lenArr.append(tempLen)

maxVAl = 0
minVal = 100
for i in range(3):
    if maxVAl < lenArr[i]:
        maxVAl = lenArr[i]
    if minVal > lenArr[i]:
        minVal = lenArr[i]

result = maxVAl - minVal

print(result)