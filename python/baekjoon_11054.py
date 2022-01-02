# num = int(input(''))
# array = list(map(int, input().split(' ')))
# dp = [0 for _ in range(num)]
# rever_dp = [0 for _ in range(num)]
# '''
# 1 5 2 1 4 3 4 5 2 1
# 1 2 2 1 3 3 4 5 2 1
# LIS를 구한다음에..
# 끝에서부터 LIS의 가장 끝값(큰값)까지
# 순증가를 구한다.
# '''
#
# for i in range(0, num, 1):
#     dp[i] = 1
#     for j in range(0,i,1):
#         if(array[i] > array[j]):
#             if dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#
#
# for i in range(num - 1, -1, -1):
#     rever_dp[i] = 1
#     for j in range(num - 1, 0, -1):
#         if(array[i] > array[j]):
#             if rever_dp[i] < rever_dp[j] + 1:
#                 rever_dp[i] = rever_dp[j] + 1
#
# total_list= [0 for i in range(num)]
# for i in range(num):
#     total_list[i] = dp[i] + rever_dp[i]
#
# print(dp)
# print(rever_dp)
# print(max(total_list)-1)
num = int(input(''))
array = list(map(int, input().split(' ')))
dp = [0 for _ in range(num)]
rever_dp = [0 for _ in range(num)]

for i in range(0, num, 1):
    dp[i] = 1
    for j in range(0,i,1):
        if(array[i] > array[j]):
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
dp1 = max(dp)



for i in range(num - 1, -1, -1):
    rever_dp[i] = 1
    for j in range(num - 1, 0, -1):
        if(array[i] > array[j]):
            if rever_dp[i] < rever_dp[j] + 1:
                rever_dp[i] = rever_dp[j] + 1

print(dp)
print(rever_dp)
print(dp1 + rever_dp[dp.index(max(dp))]-1)





