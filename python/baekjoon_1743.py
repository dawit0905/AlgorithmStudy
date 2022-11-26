import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while que:
        x, y = que.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                que.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


n, m, k = map(int, sys.stdin.readline().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    arr[x][y] = 1

ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            ans = max(ans, bfs(i, j))

print(ans)
