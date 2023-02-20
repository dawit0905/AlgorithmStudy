import sys
from collections import deque


def bfs(start_x, start_y):
    que = deque()
    que.append((start_x, start_y))
    visited[start_x][start_y] = 0
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x
            ny = y
            while 1:
                nx += dx[i]
                ny += dy[i]

                if 0 > nx or nx >= h or 0 > ny or ny >= w:
                    break

                if graph[nx][ny] == '*':
                    break

                if visited[nx][ny] <= visited[x][y] + 1:
                    continue

                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


w, h = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
visited = [[sys.maxsize] * w for _ in range(h)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
result = 0

point = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            point.append((i, j))

(start_x, start_y), (end_x, end_y) = point
bfs(start_x, start_y)

print(visited[end_x][end_y]-1)
