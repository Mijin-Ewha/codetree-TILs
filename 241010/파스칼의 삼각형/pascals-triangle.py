n = int(input())

result = [[1]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j <= i:
            if j != i and j != 0:
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

for i in range(n):
    for j in range(n):
        if j <= i:
            print(result[i][j], end=" ")
    print()