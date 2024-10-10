n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

al = input()

avg = 0
sm = 0
cnt = 0

for i in range(len(arr)):
    if al == arr[i][0]:
        sm += len(arr[i])
        cnt += 1

avg = round(float(sm / cnt), 2)

print(cnt, "{:.2f}".format(avg))