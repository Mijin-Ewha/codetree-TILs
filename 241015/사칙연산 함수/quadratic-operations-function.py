def cal(a, o, c):
    if o == '+':
        print(a, o, c, '=', a + c)
    elif o == '-':
        print(a, o, c, '=', a - c)
    elif o == '/':
        print(a, o, c, '=', int(a / c))
    elif o == '*':
        print(a, o, c, '=', a * c)
    else:
        print("False")

arr = input().split()
cal(int(arr[0]), arr[1], int(arr[2]))