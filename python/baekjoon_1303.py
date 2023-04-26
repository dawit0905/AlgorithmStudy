import sys


def dfs(x, y, color):
    global cnt
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == color:
            visited[x][y] = 1
            cnt += 1
            dfs(nx, ny, color)


sys.setrecursionlimit(10**9)
m, n = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[0] * m for _ in range(n)]
white = 0
blue = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt = 1
            dfs(i, j, graph[i][j])
            if graph[i][j] == 'W':
                white += cnt ** 2
            else:
                blue += cnt ** 2

print(white, blue)