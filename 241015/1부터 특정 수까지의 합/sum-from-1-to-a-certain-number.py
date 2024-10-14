def left(n):
    val = 0
    for i in range(n+1):
        val += i
    return val // 10

N = int(input())
print(left(N))