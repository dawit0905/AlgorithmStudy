import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1

    while que:
        x, y, = que.popleft()

        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx < 0 or xx >= I or yy < 0 or yy >= I:
                continue

            if visited[xx][yy] == 0:
                graph[xx][yy] += graph[x][y] + 1
                que.append((xx, yy))
                visited[xx][yy] = 1


T = int(sys.stdin.readline())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(T):
    I = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    graph = [[0] * I for _ in range(I)]
    visited = [[0] * I for _ in range(I)]

    bfs(start_x, start_y)
    print(graph[end_x][end_y])
