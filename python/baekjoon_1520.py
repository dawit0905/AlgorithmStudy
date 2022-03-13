import sys


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


m, n = map(int, sys.stdin.readline().split())
graph = []
dp = [[-1] * n for i in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sys.setrecursionlimit(1000000)

for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(dfs(0, 0))

