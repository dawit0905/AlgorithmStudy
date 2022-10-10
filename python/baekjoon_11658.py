import sys


def update(r, c, num):
    global arr, tree
    row = r
    col = c
    while row <= n:
        while col <= n:
            tree[row][col] += num
            col += (col & -col)
        row += (row & -row)


def _sum(r, c):
    result = 0
    row = r
    col = c
    while row > 0:
        while col > 0:
            result += tree[row][col]
            col -= (col & -col)
        row -= (row & -row)
    return result


n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n+1) for _ in range(n+1)]
tree = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    tmp = [0] + list(map(int, sys.stdin.readline().split()))

    for j in range(1, n+1):
        arr[i][j] = tmp[j]
        update(i, j, arr[i][j])


for i in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))

    if tmp[0] == 0:
        r1 = tmp[1]
        c1 = tmp[2]
        num = tmp[3]
        update(r1, c1, num - arr[r1][c1])
        arr[r1][c1] = num
    elif tmp[0] == 1:
        r1 = tmp[1]
        c1 = tmp[2]
        r2 = tmp[3]
        c2 = tmp[4]
        answer = _sum(r2, c2) - _sum(r2, c1-1) - _sum(r1-1, c2) + _sum(r1-1, c1-1)
        print(answer)
