import sys
import heapq


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start)) # cost, node
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for next_cost, next_node in edges[now]:
            cost = dist + next_cost

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, (cost, next_node))


n, m = map(int, sys.stdin.readline().split())
INF_areas = list(map(int, sys.stdin.readline().split()))
edges = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

for i in range(n):
    if INF_areas[i] == 1:
        edges[i] = []

INF = sys.maxsize
distance = [INF] * n

dijkstra(0)
print(-1) if distance[n-1] == INF else print(distance[n-1])


