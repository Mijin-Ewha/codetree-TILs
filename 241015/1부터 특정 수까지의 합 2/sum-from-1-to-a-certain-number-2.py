def plus(n):
    if n == 2:
        return 3
    return plus(n-1) + n

n = int(input())
print(plus(n))