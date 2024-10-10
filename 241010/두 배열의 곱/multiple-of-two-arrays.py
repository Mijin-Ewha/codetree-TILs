n = 3
arr = []
arr2 = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

temp = input()

for i in range(n):
    temp = list(map(int, input().split()))
    arr2.append(temp)

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(n):
    for j in range(n):
        result[i][j] = arr[i][j] * arr2[i][j]

for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
    print()