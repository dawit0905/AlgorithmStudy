# import sys
#
#
# n, m = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
#
# prefix_sum = [0] * n
# prefix_sum[0] = 1
#
# pre_sum = 0
# for i in range(n):
#     pre_sum += arr[i]
#     prefix_sum[pre_sum%m] += 1
#
# print(prefix_sum)
#
# ans=0
# for i in prefix_sum:
#     ans += i*(i-1)//2
#
# print(ans)

import sys


n, m = map(int, sys.stdin.readline().split())
prefix_sum = [0] * (n+1)
cnt = [0] * (m)

arr = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, n+1):
    prefix_sum[i] = (prefix_sum[i-1] + arr[i]) % m
    cnt[prefix_sum[i]] += 1

answer = 0
for i in range(1, n+1):
    answer += cnt[prefix_sum[i-1]]
    cnt[prefix_sum[i]] -= 1


print(answer)
