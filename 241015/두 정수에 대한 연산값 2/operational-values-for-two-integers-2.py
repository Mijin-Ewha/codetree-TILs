def cal(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        a +=10
        b *= 2
    return a, b

arr = list(map(int, input().split()))
arr[0], arr[1] = cal(arr[0], arr[1])
print(arr[0], arr[1], end=" ")