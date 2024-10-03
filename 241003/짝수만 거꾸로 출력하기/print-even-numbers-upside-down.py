num = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(*[i for i in arr if i % 2 == 0])