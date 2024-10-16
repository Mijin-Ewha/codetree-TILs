def odd_even(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        return odd_even(n//2, cnt+1)
    else:
        return odd_even(3*n+1, cnt+1)

n = int(input())
print(odd_even(n, 0))