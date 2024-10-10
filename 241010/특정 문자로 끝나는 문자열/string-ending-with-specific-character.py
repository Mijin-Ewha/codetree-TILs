arr = []
for _ in range(10):
    arr.append(input())

n = input()

cnt = 0
for i in range(len(arr)):
    if n == arr[i][-1]:
        print(arr[i])
        cnt += 1

if cnt == 0:
    print("None")