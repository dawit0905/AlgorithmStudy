import sys


def reverse(arr, n, m) -> list:
    tmp_arr = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            tmp_arr[i][j] = arr[i][m-j-1]

    return tmp_arr


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# for i in arr:
#     i.reverse()
new_arr = reverse(arr, n, m)

for i in new_arr:
    print(*i, sep='')
