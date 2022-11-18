import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                que.append((nx, ny))
                cnt += 1
                graph[nx][ny] = 0

    return cnt


n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = 0
draw = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j))
            draw += 1

print(draw)
print(answer)


