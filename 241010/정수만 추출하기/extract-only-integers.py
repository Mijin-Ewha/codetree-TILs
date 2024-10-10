arr = input().split()
rlt = 0
for i in range(2):
    temp = ''
    for j in range(len(arr[i])):
        if arr[i][j].isdigit():
            temp += arr[i][j]
        else:
            break;
    rlt += int(temp)    

print(rlt)