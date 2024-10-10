arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

if n == 1:
    for i in range(m):
        print(i+1, end = " ")

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
            elif j == 0 and i > 0 and n == 2:
                result[i][j] = result[i-1][j] + 2
            if result[i][j] == 0:
                if j - 1 >= 0:
                    result[i][j] = result[i][j - 1] + arr3[i][j-1]

    for i in range(n):
        for j in range(m):
            print(result[i][j], end=" ")
        print()