def is_Prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_Num(n):
    if n >= 10:
        n = n % 10 + n // 10
    if n % 2 == 0:
        return True
    else:
        return False

def fun(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_Prime(i) and sum_Num(i):
            cnt += 1
    print(cnt)

arr = list(map(int, input().split()))
fun(arr[0], arr[1])