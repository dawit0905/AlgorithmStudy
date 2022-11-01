import sys


def recur(x_start, x_end, y_start, y_end, n):
    if n == 1:
        return
    elif n >= 2:

        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if i == x_start or i == x_end-1 or j == y_start or j == y_end-1:
                    arr[i][j] = '*'

        recur(x_start+2, x_end-2, y_start+2, y_end-2, n-1)


n = int(sys.stdin.readline())
end = 5+(4*(n-2))
arr = [[' '] * end for _ in range(end)]
arr[end//2][end//2] = '*'
recur(0, end, 0, end, n)

for i in arr:
    print(*i, sep='')

