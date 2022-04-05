import sys


n, m = map(int, sys.stdin.readline().split())
arr = []
arr_sum =[[0] * n for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr_sum[i][0] = arr[i][0]

for i in range(n):
    for j in range(1, n):
        arr_sum[i][j] = arr_sum[i][j-1] + arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = 0
    for i in range(x1-1, x2):
        if y1 == 1:
            answer += arr_sum[i][y2-1]
        else:
            answer += arr_sum[i][y2-1] - arr_sum[i][y1-2]
    print(answer)