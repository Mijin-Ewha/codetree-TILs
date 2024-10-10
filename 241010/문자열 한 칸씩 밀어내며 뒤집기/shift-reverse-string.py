arr = input().split()
a = arr[0]
n = int(arr[1])

for i in range(n):
    tmp = int(input())
    temp = ''
    if tmp == 1:
        for i in range(1, len(a)):
            temp += a[i]
        temp += a[0]
        print(temp)
        a = temp
    elif tmp == 2:
        temp += a[-1]
        for i in range(0, len(a) - 1):
            temp += a[i]
        print(temp)
        a = temp
    else:
        for i in range(len(a) -1, -1, -1):
            temp += a[i]
        print(temp)
        a = temp