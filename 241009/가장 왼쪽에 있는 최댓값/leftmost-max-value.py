n = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)
temp.reverse()

maxVal = temp[0]
index = n
count = 0
for i in range(n):
    if index == 1:
        break;
    else: 
        tempIndex = arr.index(maxVal) + 1
        #print("tempIndex is ", tempIndex)
        #print("index is ", index)
        count += arr.count(maxVal)
        #print("count is ", count)
        if tempIndex < index:
            #print("tempIndex < index")
            print(tempIndex, end=" ")
            index = tempIndex
            if index == 1:
                break;
            #print("index is ", index)
            maxVal = temp[count]
            #print("maxVal is ", maxVal)
            #print()
        else:
            #print("tempIndex > index")
            maxVal = temp[count]
            #print("maxVal is ", maxVal)
            #print()