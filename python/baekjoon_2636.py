import sys
from collections import deque


def find(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 2
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 2
                    que.append((nx, ny))


def index(x):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == x:
                return [i, j]


def bfs(x, y):
    cheeze_index = []
    cnt_temp = 0
    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 2:
                cnt_temp += 1
    if cnt_temp >= 1:
        cheeze_index.append((x, y))
    for x, y in cheeze_index:
        graph[x][y] = 0


n, m = map(int, sys.stdin.readline().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
last_cheeze = 0
while True:
    visited = [[0] * m for _ in range(n)]
    temp = 0
    for i in range(n):
        temp += graph[i].count(1)

    if temp == 0:
        break
    else:
        last_cheeze = temp

    # 외부 치즈들 공기
    x, y = index(0)
    find(x, y)
    # 치즈 녹이기~
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
    cnt += 1

print(cnt)
print(last_cheeze)

