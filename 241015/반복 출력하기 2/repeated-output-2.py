def HelloWorld(n):
    if n == 0:
        return
    else:
        HelloWorld(n-1)
    print("HelloWorld")

n = int(input())
HelloWorld(n)