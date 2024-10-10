arr = input().split()

st = arr[0]
n = int(arr[1])

for i in range(n):
    temp = input().split()
    tempStr = ''
    if temp[0] == '1':
        a = st[int(temp[1]) - 1]
        b = st[int(temp[2] ) - 1]
        for i in range(len(st)):
            if i == int(temp[1]) - 1:
                tempStr += b
            elif i == int(temp[2] ) - 1:
                tempStr += a;
            else:
                tempStr += st[i]
        st = tempStr
    elif temp[0] == '2':
        a = temp[1]
        b = temp[2]
        for j in range(len(st)):
            if st[j] == a:
                tempStr += b
            else:
                tempStr += st[j]
        st = tempStr
    print(st)