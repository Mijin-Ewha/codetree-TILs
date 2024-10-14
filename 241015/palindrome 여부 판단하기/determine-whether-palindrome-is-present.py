def pal(a):
    n = int(len(a)/2)
    for i in range(n):
        if a[i] != a[-i]:
            return "No"
    return "Yes"

arr = input()
print(pal(arr))