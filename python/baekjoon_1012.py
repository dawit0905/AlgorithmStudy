import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
    return


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
T = int(sys.stdin.readline())

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for _ in range(m)]
    # print(graph)
    cnt = 0
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

