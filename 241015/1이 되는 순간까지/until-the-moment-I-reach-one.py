n = int(input())
def div(n):
    cnt = 0
    if n == 1:
        return cnt
    elif n % 2 == 0:
        n /= 2
        cnt+= 1
        return div(n) + cnt
    else:
        n //= 3
        cnt += 1
        return div(n) + cnt

print(div(n))