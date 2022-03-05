import sys
from collections import deque

def bfs(x,y,w):
    que = deque()
    que.append((x, y, w))
    visited[x][y][w] = 1
    while que:
        x, y, w = que.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and w == 1:
                visited[nx][ny][0] = visited[x][y][1] + 1
                que.append((nx, ny, 0))
            elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w]+1
                que.append((nx, ny, w))
    return -1


n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[[0] * 2 for _i in range(m)] for __ in range(n)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(0, 0, 1))
print(visited)

for i in visited:
    print(*i)