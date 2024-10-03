num = int(input())
arr = list(map(int, input().split()))
arr.reverse()
for i in arr:
    print(i if i % 2 == 0 else "", end=" ")