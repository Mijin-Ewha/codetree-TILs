n = int(input())
arr = input().split()

total = ''
for i in range(len(arr)):
    total += arr[i]

cnt = 0

for i in range(len(total)):
    if cnt != 5:
        print(total[i], end='')
        cnt += 1
    else:
        print()
        print(total[i], end='')
        cnt = 1