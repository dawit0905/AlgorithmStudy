import sys
from collections import deque


def bfs(color, x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] in color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append((nx, ny))

def red_green_bfs(color, x, y):
    que2 = deque()
    que2.append((x, y))
    red_green_visited[x][y] = 1
    while que2:
        x, y = que2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] in color and red_green_visited[nx][ny] == 0:
                red_green_visited[nx][ny] = 1
                que2.append((nx, ny))


n = int(sys.stdin.readline())
graph = []
visited = [[0] * n for i in range(n)]
red_green_visited = [[0] * n for i in range(n)]
colors = ['R', 'G', 'B']
red_green_colors = ['RG','B']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
red_green_cnt = 0
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(n):

        for color in colors:
            if graph[i][j] == color and visited[i][j] == 0:
                bfs(color, i, j)
                cnt += 1

        for color in red_green_colors:
            if graph[i][j] in color and red_green_visited[i][j] == 0:
                red_green_bfs(color,i,j)
                red_green_cnt += 1

print(cnt, red_green_cnt)
