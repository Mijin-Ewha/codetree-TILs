arr = input()
arr2 = input()

sumArr = arr + arr2

for i in range(len(sumArr)):
    if sumArr[i] != " ":
        print(sumArr[i], end="")