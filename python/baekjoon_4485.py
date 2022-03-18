import heapq
import sys


def dijkstra():
    que = []
    heapq.heappush(que, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while que:
        cost, x, y = heapq.heappop(que)

        if x == n-1 and y == n-1:
            print(f"Problem {idx}: {distance[x][y]}")
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            new_cost = graph[nx][ny] + cost

            if new_cost < distance[nx][ny]:
                heapq.heappush(que, (new_cost, nx, ny))
                distance[nx][ny] = new_cost

    return distance[n - 1][n - 1]


idx = 1
while 1:

    n = int(sys.stdin.readline())

    if n == 0:
        exit(0)

    INF = sys.maxsize
    distance = [[INF] * n for i in range(n)]
    graph = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    dijkstra()
    idx += 1
