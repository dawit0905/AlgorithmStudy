import sys
import heapq

def dijkstra(start):
    que = []
    distance = [INF for i in range(n + 1)]
    heapq.heappush(que, (0,start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

    return distance


n, m, x = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

result = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)

    result = max(result, go[x] + back[i])

print(result)