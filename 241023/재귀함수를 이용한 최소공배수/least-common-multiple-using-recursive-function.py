import math

# 최소공배수(Lowest Common Multiple) 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 재귀적으로 n개의 수에 대해 최소공배수를 구하는 함수
def lcm_of_list(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return lcm(nums[idx], lcm_of_list(nums, idx + 1))

# 입력 받기
n = int(input())  # 숫자의 개수
nums = list(map(int, input().split()))  # n개의 숫자 리스트

# 결과 출력
print(lcm_of_list(nums, 0))