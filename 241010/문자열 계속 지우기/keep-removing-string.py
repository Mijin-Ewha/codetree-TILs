a = input()
b = input()

while a.count(b) != 0:
    temp = ''
    index = a.find(b)
    if index == -1:
        break
    for i in range(len(a)):
        if i == index:
            for j in range(len(b)):
                index += j
        else:
            temp += a[i]
    a = temp

print(a)