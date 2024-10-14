def cal(a, o, c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '/':
        return a / c
    else:
        return a * c

arr = input().split()
print(int(arr[0]),arr[1], int(arr[2]), '=', cal(int(arr[0]), arr[1], int(arr[2])))