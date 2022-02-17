import sys
from collections import deque

dx = [-1, 0, 0, 1, -1, -1, 1, 1]
dy = [0, -1, 1, 0, -1, 1, -1, 1]


def bfs(i, j, visited, graph):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1

    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= height or ny < 0 or ny >= weight:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1


while 1:

    weight, height = map(int, sys.stdin.readline().split())
    if weight == 0 and height == 0:
        exit(0)

    graph = []
    visited = [[0] * weight for i in range(height)]
    cnt = 0
    for i in range(height):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(height):
        for j in range(weight):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, visited, graph)
                cnt += 1
    print(cnt)
