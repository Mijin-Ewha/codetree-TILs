arr = input().split()

a = ord(arr[0])
b = ord(arr[1])

print(a + b, a - b if a > b else b - a)