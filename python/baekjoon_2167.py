# import sys
#
#
# n, m = map(int, sys.stdin.readline().split())
# arr = []
# sum_arr = [[0] * m for i in range(n)]
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#     sum_arr[i][0] = arr[i][0]
#     for j in range(1, m):
#         sum_arr[i][j] = sum_arr[i][j-1] + arr[i][j]
#
# k = int(sys.stdin.readline())
#
# for i in range(k):
#     i, j, x, y = map(int, sys.stdin.readline().split())
#     answer = 0
#     for a in range(i-1, x):
#         if j == 1:
#             answer += sum_arr[a][y-1]
#         else:
#             answer += sum_arr[a][y-1] - sum_arr[a][j-1-1]
#     print(answer)

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [[0]*(m+1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    a.append(temp)

s = a
for i in range(1, n+1):
    for j in range(2, m+1):
        s[i][j] = a[i][j-1] + a[i][j]
for j in range(1, m+1):
    for i in range(2, n+1):
        s[i][j] += s[i-1][j]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1])