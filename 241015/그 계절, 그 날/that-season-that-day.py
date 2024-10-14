def leap_year(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 == 0 and y % 400 != 0:
        return False
    elif y % 4 == 0 and y % 100 == 0:
        return False
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

def day_exist(y, m, d):
    if m > 12:
        return False
    if leap_year(y) == True:
        if m == 2 and d > 29:
            return False
    else:
        if m == 2 and d > 28:
            return False
    if d > 31:
        return False
    elif (m == 2 or m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
        return False
    return True

def what_Season(y, m, d):
    if day_exist(y, m, d):
        if m >=3 and m <= 5:
            return "Spring"
        elif m >=6 and m <= 8:
            return "Summer"
        elif m >=9 and m <= 11:
            return "Fall"
        elif m == 12 or (m >= 1 and m <= 2):
            return "Winter"
    else:
        return "-1"

arr = list(map(int, input().split()))
print(what_Season(arr[0], arr[1], arr[2]))