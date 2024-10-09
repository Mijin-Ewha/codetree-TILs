length = list(map(int, input().split()))
alength = length[0]
blength = length[1]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

state = "Yes"

for i in range(alength):
        for k in range(blength):
            if i + k > alength:
                state = "No"
                break;
            if a[i + k] != b[k]:
                state = "No"
                break
print(state)