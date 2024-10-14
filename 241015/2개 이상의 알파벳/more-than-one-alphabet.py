def alpha(a):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] != a[j]:
                cnt += 1
    return cnt

arr = input()
print("Yes" if alpha(arr) >= 2 else "No")