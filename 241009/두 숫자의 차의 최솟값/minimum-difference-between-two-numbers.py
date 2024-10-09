n = int(input())
arr = list(map(int, input().split()))

minVal = 100

for i in range(0, n):
    for j in range(0, n):
        if i == j:
            break;
        temp = arr[i] - arr[j]
        if temp < 0:
            temp *= -1
        if temp < minVal:
            minVal = temp

print(minVal)