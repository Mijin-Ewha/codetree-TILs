def day_exist(m, d):
    state = "Yes"
    if m == '2':
        if int(d) > 28:
            state = "No"
    else:
        if int(d) > 31:
            state = "No"
        elif (int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11) and int(d) > 30:
            state = "No"
    return state

arr = input().split()
print(day_exist(arr[0], arr[1]))