def pal(a):
    n = int(len(a)/2)
    for i in range(n):
        if a[i] != a[-i-1]:
            return "No"
    return "Yes"

arr = input()
print(pal(arr))