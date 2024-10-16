def div(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (div(n-1) * div(n-2)) % 100

n = int(input())
print(div(n))