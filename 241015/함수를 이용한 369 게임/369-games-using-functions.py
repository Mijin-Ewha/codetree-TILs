def thirdSixNine(a, b):
    cnt = 0
    for i in range(a, b+1):
        j = str(i)
        if i % 3 == 0:
            cnt += 1
        else:
            for k in range(len(j)):
                if j[k] == '3' or j[k] == '6' or j[k] == '9':
                    cnt += 1
                    break
    return cnt

arr = list(map(int, input().split()))
print(thirdSixNine(arr[0], arr[1]))