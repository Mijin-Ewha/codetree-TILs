arr = []
for i in range(2):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

rowSum1 = (arr[0][0] + arr[0][1] + arr[0][2] + arr[0][3]) / 4
rowSum2 = (arr[1][0] + arr[1][1] + arr[1][2] + arr[1][3]) / 4
print(round(rowSum1, 1), round(rowSum2, 1))

colSum1 = (arr[0][0] + arr[1][0]) / 2
colSum2 = (arr[0][1] + arr[1][1]) / 2
colSum3 = (arr[0][2] + arr[1][2]) / 2
colSum4 = (arr[0][3] + arr[1][3]) / 2
print(round(colSum1, 1), round(colSum2, 1), round(colSum3, 1), round(colSum4, 1))

totalSum = (arr[0][0] + arr[0][1] + arr[0][2] + arr[0][3] + arr[1][0] + arr[1][1] + arr[1][2] + arr[1][3]) / 8
print(round(totalSum, 1))