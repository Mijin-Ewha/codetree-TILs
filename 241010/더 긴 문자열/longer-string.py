arr = input().split()

if len(arr[0]) == len(arr[1]):
    print("same")
elif len(arr[0]) > len(arr[1]):
    print(arr[0], len(arr[0]))
else:
    print(arr[1], len(arr[1]))