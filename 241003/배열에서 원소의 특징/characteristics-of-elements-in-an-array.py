arr = list(map(int, input().split()))
arr2 = [i-1 for i in arr if i % 3 == 0]
if arr2[0] != None:
    print(arr2[0])