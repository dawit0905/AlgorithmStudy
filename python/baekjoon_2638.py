import sys
from collections import deque

# graph 에서 x(공기 or 치즈) 을 찾는 함수
def temp(x):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == x:
                return (i, j)

# 1. 외부공기 판별. 0,0에서 bfs을 돌렸을 때, 접촉가능한 graph[x][y]만 2(외부공기)로 표시
def air(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 2

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    que.append((nx, ny))
                    visited[nx][ny] = 2


# 배열을 돌면서 이번 시간에 녹을 치즈들을 확인한다.
def bfs(x, y):
    # 이번에 사라질 치즈들
    cheeze_index = []

    cnt = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 2:
                cnt += 1
    if cnt >= 2:
        cheeze_index.append((x, y))

    for x, y in cheeze_index:
        graph[x][y] = 0


n, m = map(int, sys.stdin.readline().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))



total = 0
while True:
    visited = [[0] * m for i in range(n)]
    temp_num = 0
    for i in graph:
        temp_num += i.count(0)
    if temp_num == n*m:
        break

    x, y = temp(0)
    air(x, y)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)

    total += 1

print(total)

        

