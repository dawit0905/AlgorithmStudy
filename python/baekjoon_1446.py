import sys
import heapq


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)

        if dist > distance[now]:
            continue

        for next_node, next_cost in edges[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, (cost, next_node))


n, d = map(int, sys.stdin.readline().split())
INF = sys.maxsize
edges = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    edges[i].append((i+1, 1))

for i in range(n):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > d:
        continue
    edges[start].append((end, length))

dijkstra(0)
print(distance[d])

