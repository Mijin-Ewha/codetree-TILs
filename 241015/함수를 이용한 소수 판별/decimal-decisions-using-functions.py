def primeSum(a, b):
    rlt = 0
    for i in range(a, b+1):
        if is_prime(i) == True:
            rlt += i
    return rlt

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


arr = list(map(int, input().split()))
print(primeSum(arr[0], arr[1]))