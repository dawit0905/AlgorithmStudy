import sys
from collections import deque


# 영역 표시
def marking(x, y):
    global cnt
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    graph[x][y] = cnt

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = cnt
                que.append((nx, ny))


def bfs(z) -> int:
    global answer
    que2 = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):  # 섬들의 위치 모두 큐에 저장
        for j in range(n):
            if graph[i][j] == z:
                que2.append([i, j])
                dist[i][j] = 0

    while que2:
        x, y = que2.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] > 0 and graph[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return

            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                que2.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1


n = int(sys.stdin.readline())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 1
answer = sys.maxsize
visited = [[0] * n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            marking(i, j)
            cnt += 1


for i in range(1, cnt):
    bfs(i)
print(answer)
