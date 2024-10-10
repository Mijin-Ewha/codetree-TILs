arr = list(map(int, input().split()))
dot = []
for _ in range(arr[1]):
    temp = list(map(int, input().split()))
    dot.append(temp)

result = [[0]*arr[0] for _ in range(arr[0])]

for i in range(arr[0]):
    for j in range(arr[0]):
        for k in range(arr[1]):
            # print("i = ", i, "j = ", j, "k = ", k)
            # print("dot[",k,"][0] = " , dot[k][0], "dot[",k,"][0] = ", dot[k][1])
            if i + 1 == dot[k][0] and j + 1 == dot[k][1]:
                # print("조건 만족")
                result[i][j] = dot[k][0] * dot[k][1]
                break
            else:
                result[i][j] = 0

for i in range(arr[0]):
    for j in range(arr[0]):
        print(result[i][j], end=" ")
    print()