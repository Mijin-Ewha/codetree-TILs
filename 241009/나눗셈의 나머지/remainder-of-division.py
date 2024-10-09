arr = input().split()
a = int(arr[0])
b = int(arr[1])
remainder_count = {}
while a > 1:
    remainder = a % b
    # Count the remainder occurrences
    if remainder in remainder_count:
        remainder_count[remainder] += 1
    else:
        remainder_count[remainder] = 1
    # Update a to be the quotient
    a //= b
result = sum(count ** 2 for count in remainder_count.values())
print(result)