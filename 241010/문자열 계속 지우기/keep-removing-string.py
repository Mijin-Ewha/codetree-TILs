a = input()
b = input()

while a.count(b) != 0:
    temp = ''
    index = a.find(b)
    tmIndex = index
    if index == -1:
        break
    for i in range(len(a)):
        if i == tmIndex:
            if tmIndex < index + len(b) - 1:
                tmIndex += 1
        else:
            temp += a[i]
    a = temp

print(a)