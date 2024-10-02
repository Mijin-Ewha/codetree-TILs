arr = input().split()

sum = 0
cnt = 0;

for i in range(0, len(arr)):
    if int(arr[i]) >= 250:
        break;
    else:
        sum += int(arr[i])
    cnt += 1
avg = sum / cnt
print(sum, avg)