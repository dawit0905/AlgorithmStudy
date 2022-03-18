import sys
from collections import deque


def bfs():
    que = deque()
    que.append((0, 0, graph[0][0]))
    visited[0][0] = graph[0][0]

    while que:
        x, y, cost = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny]+cost < visited[nx][ny]:
                    que.append((nx, ny, graph[nx][ny]+cost))
                    visited[nx][ny] = graph[nx][ny] + cost

    return visited[n-1][n-1]


idx = 1
while 1:

    n = int(sys.stdin.readline())

    if n == 0:
        exit(0)

    INF = sys.maxsize
    visited = [[INF] * n for i in range(n)]
    graph = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    print(f"Problem {idx}: {bfs()}")
    idx += 1