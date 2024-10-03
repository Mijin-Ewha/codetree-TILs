arr = list(map(int, input().split()))
for i in arr:
    if i % 3 == 0:
        print(i - 1)
        break;
    else:
        continue;