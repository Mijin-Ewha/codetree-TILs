arr = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()
cnt = 0
for i in range(len(arr)):
    for j in range(2, 4):
        if n == arr[i][j]:
            print(arr[i])
            cnt += 1
            break
        

print(cnt)