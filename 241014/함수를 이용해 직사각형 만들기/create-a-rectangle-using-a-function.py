def print_rect(n, m):
    for _ in range(n):
        print("1" * m)

arr = list(map(int, input().split()))
print_rect(arr[0], arr[1])