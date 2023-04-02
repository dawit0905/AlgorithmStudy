import sys
from collections import deque


def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    que = deque()
    que.append((x, y, 0))

    while que:
        x, y, cost = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    que.append((nx, ny, cost+1))
                    visited[nx][ny] = 1
                if graph[nx][ny] == 1:
                    return cost+1


dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            num = bfs(i, j)
            answer = max(answer, num)


print(answer)
