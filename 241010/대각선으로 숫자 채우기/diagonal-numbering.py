arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

result = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

cnt = 1;
for i in range(m):
    row = 0; column = i
    while(row<n and column>=0):
        result[row][column] = cnt
        cnt+=1
        row+=1
        column-=1

for i in range(1,n):
    row = i; column = m-1
    while(row<n and column >=0):
        result[row][column] = cnt
        cnt+=1
        row+=1
        column-=1

for i in range(n):
    for j in range(m):
        print(result[i][j], end = " ")
    print()