import sys
from collections import deque


def bfs(x, y, k):
    que = deque()
    que.append((x, y, k))
    while que:
        x, y, z = que.popleft()

        if x == h - 1 and y == w - 1:
            return visited[h - 1][w - 1][z]

        if 1 <= z:
            for dx, dy in house_direction:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][z - 1] and not arr[nx][ny]:
                    que.append((nx, ny, z - 1))
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
        for dx, dy, in four_direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][z] and not arr[nx][ny]:
                que.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1

    return -1


four_direction = [(0, 1), (1, 0), (-1, 0,), (0, -1)]
house_direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
arr = []
visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]
for i in range(h):
    arr.append(list(map(int, sys.stdin.readline().split())))

ans = bfs(0, 0, k)

print(ans)
