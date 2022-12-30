import sys
import heapq


def dijkstra(start):
    distance[start] = 0
    que = []
    heapq.heappush(que, [0,1]) # dist, now
    # que = [[0, 1]]
    # heapq.heapify(que)

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for next_node, next_cost in edges[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, [cost, next_node])


n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
edges = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

dijkstra(1)
print(distance[n])