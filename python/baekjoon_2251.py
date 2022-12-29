import sys
from collections import deque


def bfs():
    while que:
        x, y, z = que.popleft()
        if visited[x][y] == 1:
            continue

        visited[x][y] = 1
        if x == 0:
            answer.append(z)

        if x + y > b:
            que.append([x + y - b, b, z])
        else:
            que.append([0, x + y, z])
        if x + z > c:
            que.append([x + z - c, y, c])
        else:
            que.append([0, y, x + z])
        if y + x > a:
            que.append([a, y + x - a, z])
        else:
            que.append([y + x, 0, z])
        if y + z > c:
            que.append([x, y + z - c, c])
        else:
            que.append([x, 0, y + z])
        if z + x > a:
            que.append([a, y, z + x - a])
        else:
            que.append([z + x, y, 0])
        if z + y > b:
            que.append([x, b, z + y - b])
        else:
            que.append([x, z + y, 0])


a, b, c = map(int, sys.stdin.readline().split())
answer = []
visited = [[0] * 201 for _ in range(201)]
que = deque()
que.append((0, 0, c))
bfs()

answer.sort()
print(*answer)
