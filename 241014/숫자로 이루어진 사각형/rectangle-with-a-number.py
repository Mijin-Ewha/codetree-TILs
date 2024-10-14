def printSquare(n):
    count = 1
    for i in range(n):
        for j in range(n):
            if count % 10 == 0:
                count = 1
            print(count % 10, end=" ")
            count += 1
        print()

n = int(input())
printSquare(n)