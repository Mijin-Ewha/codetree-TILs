arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

if n == 1:
    for i in range(m):
        print(i+1, end = " ")
elif m == 1:
    for i in range(n):
        print(i+1)
elif n == 2:
    result = [
        [0 for _ in range(n)]
        for _ in range(m)
    ]
    result[0][0] = 1
    result[1][0] = 3
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                print(result[0][0], end = " ")
            elif i == 0 and j > 0:
                print((2 * j), end=" ")
            elif i == 1 and j < m - 1:
                print(result[1][0] + (2 * j), end=" ")
            else:
                print(n * m)
        print()
elif m == 2:
    result = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    result[0][0] = 1
    result[0][1] = 2
    for i in range(n):
        for j in range(m):
            if j == 0:
                print(2*(j+1), end=" ")
            else:
                print(result[0][1] + 2*(j + 1), end=" ")
        print()
else:
    result = [
        [0 for _ in range(n)]
        for _ in range(m)
    ]
    result[0][0] = 1

    arr2 = []
    for j in range(1, n):
        arr2.append(j)
    for k in range(n-1,0, -1):
        arr2.append(k)

    arr3 = []
    arr4 = []
    for i in range(n):
        for j in range(m-1):
            arr4.append(arr2[j + i])
        arr3.append(arr4)
        arr4 = []

    '''
    for i in range(n):
        for j in range(m-1):
            print(arr3[i][j], end=" ")
        print()
    '''

    for i in range(n):
        for j in range(m):
            if j == 0 and i > 0 and n > 2:
                result[i][j] = result[i-1][j] + i + 1
            if result[i][j] == 0:
                if j - 1 >= 0:
                    result[i][j] = result[i][j - 1] + arr3[i][j-1]

    for i in range(n):
        for j in range(m):
            print(result[i][j], end=" ")
        print()

result = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]






# cnt = 1;
# for i in range(m):
#     row = 0; column = i
#     while(row<n and column>=0):
#         result[row][column] = cnt
#         cnt+=1
#         row+=1
#         column-=1

# for i in range(1,n):
#     row = i; column = m-1
#     while(row<n and column >=0):
#         result[row][column] = cnt
#         cnt+=1
#         row+=1
#         column-=1

# for i in range(n):
#     for j in range(m):
#         print(result[i][j], end = " ")
#     print()