arr = input()
n = input()

cnt = 0
for i in range(len(arr)):
    if arr[i] == n[0]:
        if arr[i+1] == n[1]:
            cnt += 1

print(cnt)