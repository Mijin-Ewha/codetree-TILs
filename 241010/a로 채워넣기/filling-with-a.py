arr = input()

for i in range(len(arr)):
    if i == 1 or i == len(arr)-2:
        print('a', end='')
    else:
        print(arr[i], end='')