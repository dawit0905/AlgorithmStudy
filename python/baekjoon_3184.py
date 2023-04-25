import sys


def dfs(x, y):
    global sheeps, wolves

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
            if graph[nx][ny] == 'v':
                wolves += 1
            elif graph[nx][ny] == 'o':
                sheeps += 1
            dfs(nx, ny)


sys.setrecursionlimit(int(10**9))
r, c = map(int, sys.stdin.readline().split())
visited = [[0] * c for _ in range(r)]
graph = []
for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
# sheep, wolves
answer = [0, 0]

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            wolves = 0
            sheeps = 0
            if graph[i][j] == 'v':
                wolves += 1
            if graph[i][j] == 'o':
                sheeps += 1

            dfs(i, j)
            if wolves < sheeps:
                answer[0] += sheeps
            else:
                answer[1] += wolves

print(*answer)
