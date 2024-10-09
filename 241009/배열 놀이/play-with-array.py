inputNQ = input().split()
n = int(inputNQ[0])
q = int(inputNQ[1])

index = -1
arrN = list(map(int, input().split()))
for i in range(q):
    arrQ = list(map(int, input().split()))
    if arrQ[0] == 1:
        print(arrN[arrQ[1] - 1])
    elif arrQ[0] == 2:
        for i in range(len(arrN)):
            if arrN[i] == arrQ[1]:
                index = i
                print(index + 1)
                break
        if index == -1:
            print(0)
        index = -1
    else:
        for j in range(arrQ[1] - 1, arrQ[2]):
            print(arrN[j], end=" ")
        print()