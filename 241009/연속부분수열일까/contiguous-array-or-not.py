length = list(map(int, input().split()))
alength = length[0]
blength = length[1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

state = "Yes"

for i in range(0, alength):
    if a[i] == b[0]:
        state = "Yes"
        for k in range(0, blength):
            if i + k >= alength:
                state = "No"
                break
            if a[i + k] != b[k]:
                state = "No"
                break
        if state == "Yes":
            break  # 외부 루프를 종료
    else:
        state = "No"
print(state)