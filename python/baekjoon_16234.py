from collections import deque
import sys


def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
cnt = 0
while True:
    visit = [[0] * n for i in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    flag = True
                    num = sum([graph[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        graph[x][y] = num
    if not flag:
        break
    cnt += 1

print(cnt)
