arr = input()

temp = ''
rlt = ''
cnt = 1
for i in range(len(arr)):
    if temp != arr[i] and i > 0:
        rlt += str(cnt)
        rlt += arr[i]
        cnt = 1
        temp = arr[i]
    elif temp != arr[i] and i == 0:
        rlt += arr[i]
        temp = arr[i]
    else:
        cnt += 1

rlt += str(cnt)
print(len(rlt))
print(rlt)