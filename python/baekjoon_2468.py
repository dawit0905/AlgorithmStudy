import sys
from collections import deque

def bfs(x,y,safe_area):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] >= safe_area and visited[nx][ny] == 0:
                que.append((nx,ny))
                visited[nx][ny] = 1


n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

graph_min = min(map(min, graph))
graph_max = max(map(max, graph))

max_safe_area = graph_min
for safe_area in range(graph_min, graph_max+1):
    visited = [[0] * n for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= safe_area and visited[i][j] == 0:
                bfs(i,j, safe_area)
                cnt += 1

    if cnt > max_safe_area:
        max_safe_area = cnt

print(max_safe_area)


