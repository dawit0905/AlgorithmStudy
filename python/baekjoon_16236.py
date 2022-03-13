import sys
from collections import deque


def bfs(i, j):
    visit = [[0] * n for i in range(n)]
    visit[i][j] = 1
    eat = []
    dist = [[0] * n for i in range(n)]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] <= graph[i][j] or graph[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if graph[nx][ny] < graph[i][j] and graph[nx][ny] != 0:
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat:
        return -1, -1, -1
    eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]


n = int(sys.stdin.readline())
graph = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

    for j in range(n):
        if temp[j] == 9:
            graph[i][j] = 2
            start = [i, j]

exp = 0
cnt = 0

while True:
    i, j = start[0], start[1]
    ex, ey, dist = bfs(i, j)
    if ex == -1:
        break

    graph[ex][ey] = graph[i][j]
    graph[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == graph[ex][ey]:
        exp = 0
        graph[ex][ey] += 1
    cnt += dist

print(cnt)
