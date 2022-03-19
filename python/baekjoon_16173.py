import sys
from collections import deque


def bfs():
    que = deque()
    que.append((0, 0))
    visited[0][0] = 1

    while que:
        x, y = que.popleft()

        if x == n-1 and y == n-1:
            return 'HaruHaru'

        for i in range(2):
            nx = x + dx[i]*graph[x][y]
            ny = y + dy[i]*graph[x][y]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1
    return 'Hing'


dx = [1, 0]
dy = [0, 1]

n = int(sys.stdin.readline())
graph = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(bfs())