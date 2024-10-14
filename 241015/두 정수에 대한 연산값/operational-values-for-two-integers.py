def mul(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a, b

n = list(map(int, input().split()))
n[0], n[1] = mul(n[0], n[1])
print(n[0], n[1], end=" ")