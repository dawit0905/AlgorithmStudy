import sys
from collections import deque


def bfs():
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                que.append((nx, ny))


m, n = map(int, sys.stdin.readline().split())
data = []
visited = [[0] * m for i in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
que = deque()
res = 0

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            que.append((i, j))
bfs()

for i in data:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
