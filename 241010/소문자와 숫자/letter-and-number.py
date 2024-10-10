arr = input()

arr = arr.lower()

for i in range(len(arr)):
    if arr[i].isalpha() or arr[i].isdigit():
        print(arr[i], end="")