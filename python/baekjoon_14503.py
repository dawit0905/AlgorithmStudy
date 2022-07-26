import sys


n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
# 위 오른 아래 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[0] * m for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


cnt = 1
visited[x][y] = 1

while True:
    flag = 0

    for _ in range(4):
        nx = x + dx[(d+3)%4]
        ny = y + dy[(d+3)%4]
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x = nx
                y = ny
                flag = 1
                break

    if flag == 0:
        if graph[x-dx[d]][y-dy[d]] == 1:
            print(cnt)
            break
        else:
            x = x-dx[d]
            y = y-dy[d]


