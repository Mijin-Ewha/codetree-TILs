arr = input().split()

index = arr[0].find(arr[1])

if index == -1:
    print('No')
else:
    print(index)