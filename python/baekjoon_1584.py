import sys
from collections import deque


def bfs():
    que = deque()
    que.append((0, 0, 0))
    graph[0][0] = 0
    visited[0][0] = True

    while que:
        x, y, cost = que.popleft()

        if x == 500 and y == 500:
            return cost

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= 500 and 0 <= ny <= 500 and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    que.appendleft((nx, ny, cost))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 1:
                    que.append((nx, ny, cost+1))
                    visited[nx][ny] = True
    return -1


n = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = [[0] * 501 for _ in range(501)]
visited = [[False] * 501 for _ in range(501)]

danger = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    danger.append((x1, y1, x2, y2))

death = []
m = int(sys.stdin.readline())
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    death.append((x1, y1, x2, y2))

for i in range(501):
    for j in range(501):
        for a1, b1, a2, b2 in danger:
            if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
                graph[i][j] = 1
        for a1, b1, a2, b2 in death:
            if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
                graph[i][j] = 2

print(bfs())
