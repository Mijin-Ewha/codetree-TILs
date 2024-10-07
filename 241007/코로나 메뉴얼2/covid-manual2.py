arr = [0, 0, 0, 0]

std1 = input().split()
std1[1] = int(std1[1])
std2 = input().split()
std2[1] = int(std2[1])
std3 = input().split()
std3[1] = int(std3[1])

std = [std1, std2, std3]

for i in range(3):
    if std[i][0] =='Y' and std[i][1] >= 37:
        arr[0] += 1
    elif std[i][0] =='N' and std[i][1] >= 37:
        arr[1] += 1
    elif std[i][0] =='Y' and std[i][1] <= 37:
        arr[2] += 1
    else:
        arr[3] += 1

if arr[0] == 2:
    arr.append('E')

for i in arr:
    print(i, end=" ")