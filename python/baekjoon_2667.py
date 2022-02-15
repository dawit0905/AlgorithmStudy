import sys
from collections import deque


def bfs(x, y):
    que = deque()
    que.append((x, y))
    arr[x][y] = 0
    cnt = 1
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == 1:
                que.append((nx, ny))
                arr[nx][ny] = 0
                cnt += 1
    return cnt


n = int(sys.stdin.readline())
arr = []

answer = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
