n = int(input())
std = []
cnt = 0
sumScore = 0
for i in range(n):
    std = list(map(int,input().split()))
    for j in range(len(std)):
        sumScore += std[j]
    avg = sumScore / len(std)
    if avg >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
    sumScore = 0
print(cnt)