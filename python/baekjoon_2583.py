import sys
from collections import deque

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    area_cnt = 1
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1
                area_cnt +=1

    return area_cnt

n, m, k = map(int, sys.stdin.readline().split())

graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# 색깔 칠하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(n-y2, n-y1):
        for j in range(x1, x2):
            graph[i][j] = 1


cnt = 0
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            arr.append(bfs(i, j))
            cnt += 1

arr.sort()
print(cnt)
print(*arr)