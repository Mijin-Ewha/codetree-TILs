arr = list(map(int, input().split()))
arr2 = [i-1 for i in arr if i % 3 == 0]
print(arr2[0])