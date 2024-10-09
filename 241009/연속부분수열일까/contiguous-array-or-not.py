length = list(map(int, input().split()))
alength = length[0]
blength = length[1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

state = "Yes"

for i in range(0, alength):
        for k in range(0, blength):
            if i + k > alength:
                state = "No"
            if a[i + k] != b[k]:
                state = "No"
                break
            else:
                state = "Yes"
print(state)