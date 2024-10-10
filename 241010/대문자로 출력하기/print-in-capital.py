arr = input()

arr = arr.upper()

for i in range(len(arr)):
    if ord(arr[i]) >= ord('A') and ord(arr[i]) <= ord('Z'):
        print(arr[i], end='')