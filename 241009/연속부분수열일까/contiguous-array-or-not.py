length = list(map(int, input().split()))
alength = length[0]
blength = length[1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

state = "Yes"

for i in range(len(a)):
    if a[i] == b[0]:
        for k in range(blength):
            if a[i + k] != b[k]:
                state = "No"

print(state)