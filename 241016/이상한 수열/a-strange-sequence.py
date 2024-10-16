def odd(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return odd(n//3) + odd(n-1)

n = int(input())
print(odd(n))