import sys


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            continue

        if graph[x][y] < graph[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)

    return dp[x][y]

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
dp = [[0] * n for i in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
