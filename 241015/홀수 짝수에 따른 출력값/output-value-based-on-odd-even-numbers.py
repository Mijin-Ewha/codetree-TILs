def cal(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return n + cal(n-2)
    else:
        return n + cal(n-2)

n = int(input())
print(cal(n))