def ntoOne(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        ntoOne(n-1)

def oneToN(n):
    if n == 0:
        return
    else:
        oneToN(n-1)
    print(n, end=" ")

n = int(input())
oneToN(n)
print()
ntoOne(n)