import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    cnt = 1

    while que:
        x, y = que.popleft()
        area_group[x][y] = group
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


def move_count(x, y):
    data = set()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not area_group[nx][ny]:
            continue
        data.add(area_group[nx][ny])

    cnt = 1

    for d in data:
        cnt += area_dict[d]
        cnt %= 10

    return cnt


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited = [[0] * m for _ in range(n)]
area_group = [[0] * m for _ in range(n)]
area_dict = {}

group = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            cnt = bfs(i, j)
            area_dict[group] = cnt
            group += 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = move_count(i, j)


for i in graph:
    print(*i, sep='')


