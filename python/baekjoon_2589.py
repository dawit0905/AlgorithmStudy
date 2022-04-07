import sys
from collections import deque

def bfs(x, y):
    visited = [[0] * m for i in range(n)]
    visited[x][y] = 1
    que = deque()
    que.append((x, y))
    result = 0
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 'L':
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    for i in visited:
        result = max(result, max(i))

    return result


n, m = map(int, sys.stdin.readline().split())
graph = []
answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer-1)
