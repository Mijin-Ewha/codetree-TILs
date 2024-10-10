arr = []
cnt = 0
temp = input()
while temp != '0':
    arr.append(temp)
    cnt += 1
    temp = input()

print(cnt)

for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])