import sys
from collections import deque


def bfs(i, j):
    que = deque()
    que.append((i, j))

    while que:
        x, y = que.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0:
                count[x][y] += 1
            else:
                que.append((nx, ny))
                visited[nx][ny] = 1


n, m = map(int, sys.stdin.readline().split())
arr = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visit = [[0] * m for i in range(n)]
flag = False
year = 0

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

while 1:
    visited = [[0] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    for i in range(n):
        for j in range(m):
            arr[i][j] -= count[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

    if cnt == 0:
        break
    if cnt >= 2:
        flag = True
        break

    year += 1

if flag:
    print(year)
else:
    print(0)
