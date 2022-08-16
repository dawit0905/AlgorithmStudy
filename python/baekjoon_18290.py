import sys


def sol(x, y, depth, s):
    global answer
    if depth == k:
        answer = max(answer, s)
        return

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if [i, j] not in que:
                if ([i + 1, j] not in que) and ([i - 1, j] not in que) and ([i, j + 1] not in que) and ([i, j - 1] not in que):
                    que.append([i, j])
                    sol(i, j, depth + 1, s + arr[i][j])
                    que.pop()


n, m, k = map(int, sys.stdin.readline().split())
arr = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = -10001
que = []
sol(0, 0, 0, 0)

print(answer)