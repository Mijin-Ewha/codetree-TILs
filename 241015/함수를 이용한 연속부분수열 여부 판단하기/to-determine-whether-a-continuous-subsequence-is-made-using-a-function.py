arr = list(map(int, input().split()))
n1 = arr[0]
n2 = arr[1]

n1Arr = list(map(int, input().split()))
n2Arr = list(map(int, input().split()))

def arr_Find(n1Arr, n2Arr, n1, n2):
    state = "Yes"
    for i in range(n1):
        for j in range(n2):
            if n1Arr[i] == n2Arr[j]:
                for k in range(n2):
                    if n1Arr[i + k] != n2Arr[j + k]:
                        state = "No"
                        break;
                state = "Yes"
    return state

print(arr_Find(n1Arr, n2Arr, n1, n2))