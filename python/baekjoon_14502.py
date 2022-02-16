import sys
from collections import deque
import copy


def bfs():
    que = deque()
    temp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                que.append((i, j))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                que.append((nx, ny))
    global answer
    cnt = 0

    for i in range(n):
        cnt += temp_graph[i].count(0)

    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
graph = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = 0
makeWall(0)
print(answer)
