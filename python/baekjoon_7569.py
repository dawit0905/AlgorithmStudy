import sys
from collections import deque


def bfs():
    while que:
        x, y, z = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                que.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1

    pass


m, n, h = map(int, sys.stdin.readline().split())
graph = []
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
que = deque()

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if temp[j][k] == 1:
                que.append((i, j, k))
    graph.append(temp)

bfs()

cnt = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt, max(j))

print(cnt - 1)
