import sys
import heapq

def dijkstra(start):
    distance = [INFINITE] * (n + 1)
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for graph_node, graph_cost in graph[now]:
            cost = dist + graph_cost

            if cost < distance[graph_node]:
                distance[graph_node] = cost
                heapq.heappush(que, (cost, graph_node))

    return distance


n, e = map(int, sys.stdin.readline().split())
INFINITE = int(1e9)
graph = [[] for i in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

one = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)
cnt = min(one[v1]+v1_dist[v2]+v2_dist[n], one[v2]+v2_dist[v1]+v1_dist[n])

if cnt < INFINITE:
    print(cnt)
else:
    print(-1)


