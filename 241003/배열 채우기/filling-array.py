arr = [];
a = list(map(int, input().split()))
for i in range(10):
    if a[i] == 0:
        break
    else:
        arr.append(a[i])

arr.reverse()

for i in range(len(arr)):
    print(arr[i], end=" ")