import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] == 0:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                que.append((nx, ny))
    return array[n-1][m-1]

n, m = map(int, sys.stdin.readline().split())
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(bfs(0, 0))
# for i in array:
#     for j in range(m):
#         print(i[j], end=" ")
#     print()
